"""Needs SimpliGen's engine running on 127.0.0.1:8199. For every preset block with a workflow: custom-node classes it uses
versus the extensions that block declares. Prints only gaps."""
import json, glob, os, re, urllib.request
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "packs") + os.sep
info = json.load(urllib.request.urlopen("http://127.0.0.1:8199/object_info"))
mod = {k: v.get("python_module", "") for k, v in info.items()}
def repo(u): return u.rstrip("/").removesuffix(".git").split("/")[-1].lower()
unknown = set(); gaps = 0
for f in sorted(glob.glob(R + "*/*-pack.json")):
    d = json.load(open(f, encoding="utf-8")); pdir = os.path.dirname(f)
    for p in d.get("presets", []):
        for bk, b in p.items():
            if not isinstance(b, dict) or "workflow" not in b: continue
            wf = os.path.join(pdir, "workflows", os.path.basename(b["workflow"]))
            if not os.path.exists(wf): wf = os.path.join(pdir, b["workflow"])
            s = open(wf, encoding="utf-8").read()
            classes = set(re.findall(r'"class_type":\s*"([^"]+)"', s))
            declared = {repo(e.get("url", e.get("name", ""))) for e in b.get("extensions", []) or []} | {e.get("name", "").lower() for e in b.get("extensions", []) or []}
            need = {}
            for c in classes:
                m = mod.get(c)
                if m is None: unknown.add((d["id"], c)); continue
                if m.startswith("custom_nodes."):
                    need.setdefault(m.split(".", 1)[1].split(".")[0].lower().removesuffix(".git"), set()).add(c)
            missing = {k: v for k, v in need.items() if not any(x == k or x.startswith(k + ".") for x in declared)}
            if missing:
                gaps += 1; print(f"{d['id']} {d.get('version')} :: {p['id']} [{bk}] missing -> {missing}")
print("gaps:", gaps)
print("classes the engine does not know:", sorted(unknown))
