"""Check (or fill) the `sizes` map of one or more pack manifests.

SimpliGen 1.95.0+ judges a model file on disk against the byte size the preset
declares in `image.sizes` / `video.sizes` ({download url: bytes}). A file shorter
than that is not ready and is downloaded again; with no declared size the app only
checks that the file exists. New packs declare `sizes` (see AGENTS.md step 4 and
the guide §6.1).

The URL list mirrors the app's declaredModelFiles (electron/services/presetModels.js,
app 1.96.0): checkpoint, vae, clip, clipVision, upscaler, spatialUpscaler, unet,
unets[], clips[], loras[], embeddings[], refiner_checkpoint, sam_model,
controlnet_models[], extraModels[].

Usage, from the repo root:
  uv run --no-project python tests/check_declared_sizes.py packs/<slug>/<file>.json [...]
  uv run --no-project python tests/check_declared_sizes.py --write packs/<slug>/<file>.json

Sizes come from the download host: Hugging Face's X-Linked-Size header, else the
final Content-Length, else a one-byte ranged GET. A Civitai URL uses the token in
CIVITAI_API_TOKEN when set. Exit 0 = every declared file has a size that matches the
host; 1 = missing or mismatched sizes (or a host that would not answer).
"""
import json
import os
import sys
import urllib.error
import urllib.request
from urllib.parse import urljoin, urlparse

sys.stdout.reconfigure(encoding="utf-8")
UA = "simpligen-presets-size-check/1.0"


def declared_urls(c):
    out = []

    def add(filename, url):
        if url and filename:
            out.append(url)

    for f in ("checkpoint", "vae", "clip", "clipVision", "upscaler", "spatialUpscaler", "unet", "refiner_checkpoint"):
        add(c.get(f), c.get(f + "Url"))
    for key in ("unets", "clips", "embeddings"):
        for m in c.get(key) or []:
            add(m.get("filename"), m.get("url"))
    for lora in c.get("loras") or []:
        add(lora.get("filename") or lora.get("localPath"), lora.get("url") or lora.get("downloadUrl"))
    sam = c.get("sam_model")
    if sam:
        sam = {"filename": sam, "url": c.get("sam_modelUrl")} if isinstance(sam, str) else sam
        add(sam.get("filename"), sam.get("url"))
    for cn in c.get("controlnet_models") or []:
        if isinstance(cn, dict):
            add(cn.get("filename"), cn.get("url"))
    for m in c.get("extraModels") or []:
        if m and m.get("url") and m.get("filename"):
            out.append(m["url"])
    return list(dict.fromkeys(out))


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


opener = urllib.request.build_opener(NoRedirect)


def headers_for(url):
    h = {"User-Agent": UA}
    token = os.environ.get("CIVITAI_API_TOKEN")
    if token and urlparse(url).hostname and urlparse(url).hostname.endswith("civitai.com"):
        h["Authorization"] = f"Bearer {token}"
    return h


def request(url, method, extra=None):
    req = urllib.request.Request(url, method=method, headers={**headers_for(url), **(extra or {})})
    try:
        return opener.open(req, timeout=60)
    except urllib.error.HTTPError as e:
        return e  # 3xx (redirects are not followed) and errors carry headers too


def remote_size(url):
    cur = url
    for _ in range(8):
        r = request(cur, "HEAD")
        linked = r.headers.get("X-Linked-Size")
        if linked and linked.isdigit():
            return int(linked)
        if r.status in (301, 302, 303, 307, 308) and r.headers.get("Location"):
            cur = urljoin(cur, r.headers["Location"])
            continue
        if r.status == 200 and (r.headers.get("Content-Length") or "").isdigit():
            return int(r.headers["Content-Length"])
        break
    r = request(cur, "GET", {"Range": "bytes=0-0"})
    cr = r.headers.get("Content-Range") or ""
    if r.status == 206 and "/" in cr and cr.rsplit("/", 1)[1].isdigit():
        return int(cr.rsplit("/", 1)[1])
    raise RuntimeError(f"no size from host (HTTP {r.status})")


def main(argv):
    write = "--write" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    bad = 0
    cache = {}
    for path in paths:
        raw = open(path, "rb").read()
        if raw.startswith(b"\xef\xbb\xbf"):
            print(f"{path}: starts with a UTF-8 BOM, fix that first")
            bad += 1
            continue
        text = raw.decode("utf-8")
        manifest = json.loads(text)
        changed = False
        for p in manifest.get("presets", []):
            kind = "video" if "video" in p else "image" if "image" in p else None
            if not kind:
                continue
            c = p[kind]
            have = c.get("sizes") or {}
            want = {}
            for url in declared_urls(c):
                if url not in cache:
                    try:
                        cache[url] = remote_size(url)
                    except Exception as e:  # noqa: BLE001 - report and keep going
                        cache[url] = None
                        print(f"  {p['id']}: {url}\n    could not size: {e}")
                size = cache[url]
                if size is None:
                    bad += 1
                    continue
                want[url] = size
                if have.get(url) != size:
                    state = "missing" if url not in have else f"declared {have[url]}"
                    print(f"  {p['id']}: {url.rsplit('/', 1)[-1]} {state}, host says {size}")
                    if not write:
                        bad += 1
            # Extra entries are harmless (the app looks sizes up by url; the official
            # core pack repeats one pack-wide map in every preset), so they are kept.
            merged = {**have, **want}
            if write and want and merged != have:
                c["sizes"] = merged
                changed = True
        if changed:
            indent = len(text.split("\n", 1)[1]) - len(text.split("\n", 1)[1].lstrip(" ")) or 2
            out = json.dumps(manifest, indent=indent, ensure_ascii=False)
            nl = "\r\n" if "\r\n" in text else "\n"
            out = out.replace("\n", nl) + (nl if text.endswith(("\n", "\r\n")) else "")
            with open(path, "wb") as f:
                f.write(out.encode("utf-8"))
            print(f"{path}: wrote sizes")
        else:
            print(f"{path}: {'no change' if write else 'checked'}")
    print("problems:", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
