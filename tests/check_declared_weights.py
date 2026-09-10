"""Every weight filename hardcoded in a pack workflow must be declared in the pack manifest.

The app downloads only what the manifest declares (checkpoint/unet/vae/clip/clips/unets/loras).
A workflow that hardcodes a filename the manifest does not mention works on the author's PC
and fails with "Value not in list" on every fresh install (krea-csg-foundation, 2026-09-10).

Run:  uv run python tests/check_declared_weights.py   (exit 1 on any finding)
"""
import glob, io, json, os, re, sys

WEIGHT = re.compile(r'"([^"{}]+\.(?:safetensors|gguf|pth|pt|ckpt|bin))"')
bad = []
for mf in sorted(glob.glob("packs/*/*.json")):
    if "workflows" in mf.replace("\\", "/").split("/"):
        continue
    try:
        d = json.load(io.open(mf, encoding="utf8"))
    except Exception:
        continue
    if not isinstance(d, dict) or "presets" not in d:
        continue
    mtxt = io.open(mf, encoding="utf8").read()
    for p in d["presets"]:
        for media in ("image", "video"):
            c = p.get(media) or {}
            wf = c.get("workflow")
            if not wf:
                continue
            wp = os.path.join(os.path.dirname(mf), wf)
            if not os.path.exists(wp):
                bad.append((mf, p["id"], "MISSING WORKFLOW " + wf))
                continue
            wtxt = io.open(wp, encoding="utf8").read()
            for name in sorted(set(WEIGHT.findall(wtxt))):
                if name not in mtxt:
                    bad.append((mf, p["id"], name))
for mf, pid, name in bad:
    print(f"{mf}: preset {pid}: undeclared {name}")
print(f"undeclared hardcoded weights: {len(bad)}")
sys.exit(1 if bad else 0)
