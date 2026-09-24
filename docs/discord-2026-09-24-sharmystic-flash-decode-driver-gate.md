# Note draft — flash_attention_decode ignores an old driver (and the registry's own "disabled") (to Sharmystic, 2026-09-24) (SENT by Michael 2026-09-24)

Hi Sharmystic, a user diagnostics bundle from today (RTX 4090 Laptop 16 GB, driver **576.52**, app 1.65.0, engine
v0.37.0) fails every YuE2 run a few seconds in:

```
File "ComfyUI\comfy\text_encoders\yue2.py", line 235, in generate
File "ComfyUI\comfy\text_encoders\llama.py", line 657, in forward
File "site-packages\comfy_kitchen\flash_attention.py", line 106, in flash_attention_decode
RuntimeError: CUDA error: CUDA driver version is insufficient for CUDA runtime version
```

The engine picked the right torch for them (`CUDA target: cu128 (driver 576.52)`, torch 2.11.0+cu128), so this is the
comfy_kitchen extension's own kernel, not torch.

Two things look off from the outside:

1. **`flash_attention.is_available()` never asks whether the driver can launch the kernel.** It checks `_EXT_AVAILABLE`,
   `_C`, `hasattr(..., "flash_attention_decode")`, then `get_device_capability() >= _MINIMUM_CAPABILITY`. A 4090 laptop
   is 8.9, so the gate passes and `llama.py:881` takes the FixedKV/flash path. The `else` branch right there is a working
   fallback, so a driver check (or a guarded trial launch once per process) would turn a failed job into a slower one.
2. **That path uses the CUDA backend even though the registry reports it disabled.** Their startup line says
   `Found comfy_kitchen backend cuda: {'available': True, 'disabled': True, ...}` (mine on 617.14 says `disabled: False`).
   `flash_attention.py` imports `from .backends import cuda as _cuda_backend` directly and calls
   `_cuda_backend._C.flash_attention_decode(...)`, so whatever disabled the backend isn't consulted on this path. If that
   disable is your old-driver gate, this is the hole in it.

Telling the user to update the driver, which I expect to fix it. Flagging it because the failure names neither the
driver nor a minimum, and a user on an old driver with an otherwise healthy machine has nothing to go on.

---

**Sharmystic's reply (2026-09-24):** "good one, ill ship it in the next hotfix" — so the old-driver case will fall back
to the non-flash KV path instead of failing the job. Watch for it in the next app/engine hotfix; until then, a
pre-Turing-era driver on YuE2 still needs the user to update their NVIDIA driver.
