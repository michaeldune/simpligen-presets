# Reply draft — YuE2 Song card fails with "CUDA driver version is insufficient" (RTX 4090 Laptop, driver 576.52, 2026-09-24) (SENT by Michael 2026-09-24)

Thanks for the logs. This one is your graphics driver, and the fix is a driver update.

**What happens.** All four runs of the Song + Album Art card fail a few seconds in with:

> RuntimeError: CUDA error: CUDA driver version is insufficient for CUDA runtime version

It comes from the fast attention kernel SimpliGen's engine uses while YuE2 writes the song, and it means the engine's
CUDA code is newer than your driver can run. Your driver is **576.52**; SimpliGen noticed and installed its CUDA 12.8
build for you (`CUDA target: cu128 (driver 576.52)`), but that kernel still needs a newer driver than you have.

**The fix:** update your NVIDIA driver from nvidia.com (or GeForce Experience / NVIDIA App) and restart. Either Game
Ready or Studio is fine. Current drivers are in the 617.x range, so yours is a long way back. Nothing in the pack or
your settings needs to change, and none of the other settings will work around it: this kernel is chosen automatically.

**How to check what you have:** press Win+R, type `cmd`, then run `nvidia-smi`. The top line shows the driver version,
and the "CUDA Version" on the right is the newest CUDA that driver supports. After updating, that number should go up.

For what it's worth, nothing else on your machine is at fault: 16 GB of VRAM, 32 GB of RAM and free space were all
fine in the logs, and the job died in the first seconds, not from running out of anything.

I've also passed this to the SimpliGen dev, because the engine should notice a driver this old and fall back to the
slower path by itself instead of failing the job.
