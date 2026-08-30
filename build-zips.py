#!/usr/bin/env python3
"""
build-zips.py
Generate readme.html + install.cmd + install.ps1 for each pack, then zip.

Run: python build-zips.py
Output: D:\\SimpliGen-Backups\\zips\\community-<slug>.zip
"""

import os, re, json, zipfile

BASE    = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packs')
OUT_DIR = r'D:\SimpliGen-Backups\zips'

# ── Custom node registry ──────────────────────────────────────────────────────
CUSTOM_NODES = {
    'Power Lora Loader (rgthree)': {
        'name': 'Power Lora Loader (rgthree)',
        'url':  'https://github.com/rgthree/rgthree-comfy',
        'note': 'Enables user LoRA support. Usually pre-installed by SimpliGen.',
    },
    'UnetLoaderGGUF': {
        'name': 'ComfyUI-GGUF',
        'url':  'https://github.com/city96/ComfyUI-GGUF',
        'note': 'Required for GGUF quantised models. Usually pre-installed by SimpliGen.',
    },
    'ConditioningKrea2Rebalance': {
        'name': 'ComfyUI-ConditioningKrea2Rebalance',
        'url':  'https://github.com/Jonseed/ComfyUI-ConditioningKrea2Rebalance',
        'note': 'Required for the Krea 2 Turbo + Rebalance preset. Usually pre-installed by SimpliGen.',
    },
    'MiniMaxH3TurboLoRA': {
        'name': 'ComfyUI-MiniMax-H3-Turbo',
        'url':  'https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo',
        'note': 'Turbo LoRA loader + 4-step dual-schedule sampler for MiniMax H3. NOT pre-installed by SimpliGen - clone into ComfyUI/custom_nodes manually before using this preset.',
    },
    'MiniMaxH3TurboSampler': {
        'name': 'ComfyUI-MiniMax-H3-Turbo',
        'url':  'https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo',
        'note': 'Turbo LoRA loader + 4-step dual-schedule sampler for MiniMax H3. NOT pre-installed by SimpliGen - clone into ComfyUI/custom_nodes manually before using this preset.',
    },
    'RebelsSeFiLoader': {
        'name': 'ComfyUI_Rebels_SeFi',
        'url':  'https://github.com/RealRebelAI/ComfyUI_Rebels_SeFi',
        'note': 'SeFi-Image 5B Turbo loader + sampler. NOT pre-installed by SimpliGen. The repo nests the package - clone it, then move the INNER ComfyUI_Rebels_SeFi/ folder into ComfyUI/custom_nodes (a plain clone of the outer repo will not load).',
    },
    'RebelsSeFiSampler': {
        'name': 'ComfyUI_Rebels_SeFi',
        'url':  'https://github.com/RealRebelAI/ComfyUI_Rebels_SeFi',
        'note': 'SeFi-Image 5B Turbo loader + sampler. NOT pre-installed by SimpliGen. The repo nests the package - clone it, then move the INNER ComfyUI_Rebels_SeFi/ folder into ComfyUI/custom_nodes (a plain clone of the outer repo will not load).',
    },
    'SolAttnPatch': {
        'name': 'ComfyUI-SolAttn_triton',
        'url':  'https://github.com/kijai/ComfyUI-SolAttn_triton',
        'note': 'Sol-Attn sparse-attention node (Triton kernels) for MiniMax H3. NOT pre-installed by SimpliGen - clone into ComfyUI/custom_nodes manually before using this preset. Requires Triton JIT compiler support (Python.h/python3XX.lib in the engine\'s Python - present from SimpliGen 1.43.x onward).',
    },
    # NOTE: the "Pathch" spelling is the real registered class name upstream, not a typo here.
    'PathchSageAttentionKJ': {
        'name': 'ComfyUI-KJNodes',
        'url':  'https://github.com/kijai/ComfyUI-KJNodes',
        'note': 'Global SageAttention patch. The workflow applies SageAttention itself through this node, so do NOT also run ComfyUI with --use-sage-attention or let a host app patch the model - two model-level attention patches together can make Turbo output numerically invalid (black or garbage frames). SimpliGen handles this automatically by withholding its own per-preset patch.',
    },
    'SpectrumApplyMiniMaxH3': {
        'name': 'ComfyUI-Spectrum-MiniMax-H3',
        'url':  'https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3',
        'note': 'Spectral-feature-forecasting accelerator for MiniMax H3 - skips transformer evaluations and predicts them instead (~30-40% fewer). NOT pre-installed by SimpliGen - clone into ComfyUI/custom_nodes manually. Approximate by design: output is not bit-identical to unaccelerated MiniMax H3.',
    },
}

HF_GATED_REPOS = [
    'Comfy-Org/Krea-2',
    'circlestone-labs/Anima',
    'Comfy-Org/z_image_turbo',
    'Comfy-Org/flux2',
    'Comfy-Org/flux2-klein',
    'hakurei/waifu-diffusion',
]

MODEL_FIELDS = ['checkpoint', 'unet', 'vae', 'clip']
URL_FIELDS   = {'checkpoint': 'checkpointUrl', 'unet': 'unetUrl', 'vae': 'vaeUrl', 'clip': 'clipUrl'}
DEST_FOLDER  = {'checkpoint': 'checkpoints', 'unet': 'diffusion_models', 'vae': 'vae', 'clip': 'clip'}

# Array-shaped model lists seen in some video packs (e.g. Wan's dual high/low-noise
# experts): each item is {filename, url, ...}, dest folder is fixed per array name.
ARRAY_MODEL_FIELDS = {'unets': 'diffusion_models', 'loras': 'loras'}

MEDIA_TYPES = ('image', 'video')


def media_key(p):
    """Which media block this preset uses ('image' or 'video'), or None if neither."""
    for k in MEDIA_TYPES:
        if k in p:
            return k
    return None


def media_block(p):
    k = media_key(p)
    return p[k] if k else {}


def preset_model_filenames(p):
    """All model filenames a single preset needs: core fields + extraModels + array fields."""
    blk = media_block(p)
    names = [blk[f] for f in MODEL_FIELDS if blk.get(f)]
    names += [e['filename'] for e in blk.get('extraModels', []) if e.get('filename')]
    for arr_field in ARRAY_MODEL_FIELDS:
        names += [e['filename'] for e in blk.get(arr_field, []) if e.get('filename')]
    return names


# ── Helpers ───────────────────────────────────────────────────────────────────

def is_hf_gated(url):
    return bool(url and any(r in url for r in HF_GATED_REPOS))

def is_hf(url):
    return bool(url and 'huggingface.co' in url)

def h(text):
    return (str(text)
            .replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))

PLACEHOLDER_RE = re.compile(r'\{\{[^}]+\}\}')

def norm_repo(url):
    """Same repo whether written with .git, a trailing slash, or neither."""
    return (url or '').strip().rstrip('/').removesuffix('.git').lower()

def collect_custom_nodes(data, pack_dir):
    """Prerequisites come from TWO sources, and both are needed.

    Workflow class_types catch the nodes a graph names. Declared extensions
    catch the ones it does not: SimpliGen INJECTS PathchSageAttentionKJ at
    render time when a preset sets supportsSage, so that node never appears
    in any workflow yet must still be installed. Reading only the graph
    silently dropped ComfyUI-KJNodes from the accelerated pack's readme.

    Bare {{PLACEHOLDER}} tokens are substituted before parsing, exactly as the
    engine does. Skipping unparseable workflows meant a pack could emit NO
    prerequisites at all and look like a pack that simply needed none - the
    Wan 2.2 readme shipped that way until the workflow was hand-quoted.
    """
    by_repo = {}
    known_by_name = {e['name']: e for e in CUSTOM_NODES.values()}

    def add(name, url, note, commit=None):
        key = norm_repo(url)
        if not key:
            return
        if key in by_repo:
            # A workflow class_type is seen before the declared extension, and
            # only the declaration carries the pin. Let the later entry fill
            # the gap instead of the first writer silently winning.
            if commit and not by_repo[key].get('commit'):
                by_repo[key]['commit'] = commit
            return
        by_repo[key] = {'name': name, 'url': url, 'note': note,
                        'commit': commit}

    wf_dir = os.path.join(pack_dir, 'workflows')
    if os.path.isdir(wf_dir):
        for fn in sorted(os.listdir(wf_dir)):
            if not fn.endswith('.json'):
                continue
            raw = open(os.path.join(wf_dir, fn), encoding='utf-8').read()
            try:
                wf = json.loads(PLACEHOLDER_RE.sub('0', raw))
            except json.JSONDecodeError as e:
                print(f'  WARN  {fn}: unparseable even after placeholder '
                      f'substitution ({e.msg}) - its nodes are not listed')
                continue
            for node in wf.values():
                if isinstance(node, dict) and node.get('class_type') in CUSTOM_NODES:
                    n = CUSTOM_NODES[node['class_type']]
                    add(n['name'], n['url'], n['note'])

    for preset in data.get('presets', []):
        for media in ('video', 'image'):
            for ext in ((preset.get(media) or {}).get('extensions') or []):
                name = ext.get('name') or ''
                # prefer the curated note; fall back to the pack's own text
                known = known_by_name.get(name)
                add(name,
                    ext.get('url') or (known or {}).get('url'),
                    (known or {}).get('note') or ext.get('description') or '',
                    ext.get('pinnedCommit'))

    return sorted(by_repo.values(), key=lambda n: n['name'].lower())

def collect_models(data):
    seen = {}

    def add(fname, url, dest, preset_name):
        if not fname:
            return
        if fname not in seen:
            seen[fname] = {
                'filename': fname,
                'url':      url,
                'dest':     dest,
                'gated':    is_hf_gated(url),
                'hf':       is_hf(url),
                'presets':  [],
            }
        if preset_name not in seen[fname]['presets']:
            seen[fname]['presets'].append(preset_name)

    for p in data['presets']:
        blk = media_block(p)
        for field in MODEL_FIELDS:
            fname = blk.get(field)
            if fname:
                add(fname, blk.get(URL_FIELDS.get(field, '')), DEST_FOLDER.get(field, 'models'), p['name'])
        for extra in blk.get('extraModels', []):
            add(extra.get('filename'), extra.get('url'), extra.get('dir', 'models'), p['name'])
        for arr_field, dest in ARRAY_MODEL_FIELDS.items():
            for entry in blk.get(arr_field, []):
                add(entry.get('filename'), entry.get('url'), dest, p['name'])

    return list(seen.values())


# ── readme.html ───────────────────────────────────────────────────────────────

CSS = """
:root {
    --bg: #0f1117; --surface: #1a1d27; --border: #2d3147;
    --accent: #7c6ef7; --accent-dim: #4a3fb5;
    --text: #e2e4f0; --muted: #8b90ab;
    --warn: #f0a045; --gated: #e05c6a; --shared: #4db87a;
    --radius: 8px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; line-height: 1.6; padding: 32px 24px; max-width: 900px; margin: 0 auto; }
h1 { font-size: 26px; font-weight: 700; color: #fff; margin-bottom: 6px; }
h2 { font-size: 15px; font-weight: 600; color: var(--accent); text-transform: uppercase; letter-spacing: .05em; margin: 32px 0 12px; }
p  { color: var(--muted); margin-bottom: 10px; }
a  { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.version { font-size: 12px; color: var(--muted); margin-bottom: 16px; }
.tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.tag { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 2px 8px; font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
.section { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; margin-bottom: 20px; }
.prereq-item { display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-bottom: 1px solid var(--border); }
.prereq-item:last-child { border-bottom: none; padding-bottom: 0; }
.prereq-name { font-weight: 600; color: #fff; }
.prereq-note { color: var(--muted); font-size: 13px; }
.preset-card { display: flex; gap: 16px; border-bottom: 1px solid var(--border); padding: 18px 0; }
.preset-card:first-child { padding-top: 0; }
.preset-card:last-child { border-bottom: none; padding-bottom: 0; }
.preset-thumb { width: 90px; height: 90px; object-fit: cover; border-radius: 6px; flex-shrink: 0; background: var(--border); }
.preset-info { flex: 1; }
.preset-title { font-weight: 600; color: #fff; font-size: 15px; }
.preset-tagline { color: var(--muted); font-size: 13px; margin-bottom: 10px; }
.model-row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; padding: 6px 0; border-top: 1px solid var(--border); font-size: 13px; }
.model-file { font-family: monospace; font-size: 12px; background: var(--bg); padding: 2px 6px; border-radius: 4px; color: #b0c4f8; }
.model-dest { color: var(--muted); font-size: 12px; }
.badge { font-size: 11px; padding: 1px 6px; border-radius: 10px; font-weight: 600; }
.badge-gated  { background: #3d1720; color: var(--gated);  border: 1px solid var(--gated); }
.badge-shared { background: #1a3329; color: var(--shared); border: 1px solid var(--shared); }
.badge-hf     { background: #2a2010; color: var(--warn);   border: 1px solid var(--warn); }
.dl-link { font-size: 12px; }
.vram-row { display: flex; gap: 8px; align-items: center; color: var(--muted); font-size: 12px; margin-top: 6px; }
.vram-val { color: #fff; font-weight: 600; }
.install-box { background: #0a0c14; border: 1px solid var(--accent-dim); border-radius: var(--radius); padding: 16px 20px; }
.install-step { display: flex; gap: 10px; padding: 8px 0; }
.step-num { width: 22px; height: 22px; min-width: 22px; background: var(--accent-dim); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; margin-top: 1px; }
.step-text { color: var(--text); }
code { font-family: monospace; background: var(--border); padding: 1px 5px; border-radius: 3px; font-size: 12px; }
.alert { border-radius: var(--radius); padding: 12px 16px; margin-bottom: 14px; font-size: 13px; }
.alert-warn   { background: #2a2010; border: 1px solid var(--warn);   color: var(--warn); }
.alert-shared { background: #1a2a1a; border: 1px solid var(--shared); color: var(--shared); }
"""


def make_readme(data, pack_dir):
    custom_nodes_used = collect_custom_nodes(data, pack_dir)
    models            = collect_models(data)
    shared_set        = {m['filename'] for m in models if len(m['presets']) > 1}
    model_by_fname    = {m['filename']: m for m in models}
    pack_name         = data['name']

    # Prerequisites (dedup by node package, since one package can register
    # multiple class_types - e.g. a loader + a sampler from the same repo)
    prereq_html = ''
    if custom_nodes_used:
        unique_nodes = custom_nodes_used  # already deduped by repo, name-sorted

        def pin_html(node):
            """A pinned extension is pinned for a reason - the pack was tested
            against that commit. SimpliGen checks it out itself, but the zip is
            also read by people cloning by hand, and a plain clone lands on
            HEAD. Emit the checkout line so both routes end up at the same node.
            """
            sha = node.get('commit')
            if not sha:
                return ''
            folder = node['url'].rstrip('/').split('/')[-1]
            if folder.endswith('.git'):
                folder = folder[:-4]
            return (f'<div class="prereq-note">Tested at <code>{h(sha[:7])}</code>. '
                    f'SimpliGen checks this out for you; if you clone it by hand, '
                    f'run <code>git -C {h(folder)} checkout {h(sha)}</code> '
                    f'afterwards.</div>')

        items = ''.join(
            f'<div class="prereq-item"><div>'
            f'<div class="prereq-name"><a href="{h(node["url"])}" target="_blank">{h(node["name"])}</a></div>'
            f'<div class="prereq-note">{h(node["note"])}</div>'
            f'{pin_html(node)}'
            f'</div></div>'
            for node in unique_nodes
        )
        prereq_html = f'<h2>Custom Node Prerequisites</h2><div class="section">{items}</div>'

    # HF gated alert
    gated_alert = ''
    if any(m['gated'] for m in models):
        gated_alert = '<div class="alert alert-warn">&#9888; Some models require a free HuggingFace account. Sign in at huggingface.co and accept the model licence before downloading.</div>'

    # Civitai token alert
    civitai_alert = ''
    if any(m['url'] and 'civitai.com' in m['url'] for m in models):
        civitai_alert = ('<div class="alert alert-warn">&#9888; Some models are hosted on Civitai, which requires a free API token to download. '
                         'Create one at <a href="https://civitai.com/user/account" target="_blank">civitai.com/user/account</a> (API Keys section). '
                         'The installer will prompt you to paste it.</div>')

    # Shared models alert
    shared_alert = ''
    shared_models = [m for m in models if m['filename'] in shared_set]
    if shared_models:
        rows = ''.join(
            f'<li><span class="model-file">{h(m["filename"])}</span> &mdash; used by {h(", ".join(m["presets"]))}</li>'
            for m in shared_models
        )
        shared_alert = (
            f'<div class="alert alert-shared">&#9432; These models are shared by multiple presets &mdash; download once:'
            f'<ul style="margin:8px 0 0 18px">{rows}</ul></div>'
        )

    # Preset cards
    def model_row(fname, entry):
        url    = entry['url']
        dl     = (f'<a class="dl-link" href="{h(url)}" target="_blank">Download</a>'
                  if url else '<span style="color:var(--muted);font-size:12px">Find on Civitai or HuggingFace</span>')
        badges = ''
        if entry['gated']:
            badges += ' <span class="badge badge-gated">HF login required</span>'
        elif entry['hf']:
            badges += ' <span class="badge badge-hf">HuggingFace</span>'
        if fname in shared_set:
            badges += ' <span class="badge badge-shared">shared</span>'
        return (
            f'<div class="model-row">'
            f'<span class="model-file">{h(fname)}</span>'
            f'<span class="model-dest">&rarr; <code>{h(entry["dest"])}</code></span>'
            f'{dl}{badges}</div>'
        )

    cards = ''
    for p in data['presets']:
        blk      = media_block(p)
        req      = blk.get('requirements', {})
        thumb    = p.get('previewImage', '')
        thumb_el = (f'<img class="preset-thumb" src="{h(thumb)}" alt="{h(p["name"])}">'
                    if thumb else '<div class="preset-thumb"></div>')
        rows = ''.join(
            model_row(fn, model_by_fname[fn])
            for fn in preset_model_filenames(p) if fn in model_by_fname
        )
        cards += (
            f'<div class="preset-card">{thumb_el}'
            f'<div class="preset-info">'
            f'<div class="preset-title">{h(p["name"])}</div>'
            f'<div class="preset-tagline">{h(p.get("tagline",""))}</div>'
            f'{rows}'
            f'<div class="vram-row">VRAM: <span class="vram-val">{req.get("minVramGB","?")} GB min</span>'
            f' / <span class="vram-val">{req.get("recommendedVramGB","?")} GB recommended</span>'
            f'&nbsp;&nbsp;&middot;&nbsp;&nbsp;Model size: <span class="vram-val">{req.get("sizeGB","?")} GB</span>'
            f'</div></div></div>'
        )

    # Install steps
    install_html = (
        '<div class="install-box">'
        '<div class="install-step"><div class="step-num">1</div>'
        '<div class="step-text">Download all required model files (links above) and place each file in the correct subfolder inside SimpliGen\'s engine models directory:<br>'
        '<code>%APPDATA%\\simpligen\\engine\\models\\</code><br>'
        'Subfolders: <code>checkpoints</code> for checkpoint models &bull; '
        '<code>diffusion_models</code> for UNet / GGUF &bull; '
        '<code>clip</code> for CLIP / text encoders &bull; '
        '<code>vae</code> for VAE files</div></div>'
        '<div class="install-step"><div class="step-num">2</div>'
        '<div class="step-text">Double-click <code>install.cmd</code>. '
        'Choose <strong>[0]</strong> to install all presets, or a number to install a single preset.</div></div>'
        '<div class="install-step"><div class="step-num">3</div>'
        '<div class="step-text">Restart SimpliGen. Your preset(s) will appear in the Local section of the model picker.</div></div>'
        '</div>'
    )

    tags_html = ''.join(f'<span class="tag">{h(t)}</span>' for t in data.get('tags', []))

    return (
        f'<!DOCTYPE html><html lang="en"><head>'
        f'<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{h(pack_name)}</title>'
        f'<style>{CSS}</style></head><body>'
        f'<h1>{h(pack_name)}</h1>'
        f'<div class="version">v{h(data.get("version","1.0.0"))} &nbsp;&middot;&nbsp; '
        f'{len(data["presets"])} preset{"s" if len(data["presets"])!=1 else ""} '
        f'&nbsp;&middot;&nbsp; by {h(data.get("author","Community"))}</div>'
        f'<div class="tags">{tags_html}</div>'
        f'<p>{h(data.get("description",""))}</p>'
        f'{prereq_html}'
        f'<h2>Model Downloads</h2>'
        f'{gated_alert}{civitai_alert}{shared_alert}'
        f'<div class="section">{cards}</div>'
        f'<h2>Installation</h2>{install_html}'
        f'</body></html>'
    )


# ── install.ps1 + install.cmd ─────────────────────────────────────────────────

def make_install(data, slug):
    presets = data['presets']

    media_keys = {media_key(p) for p in presets}
    if not all(media_keys) or len(media_keys) > 1:
        raise ValueError(f'{slug}: presets must all share one media type (image or video), got {media_keys}')
    mkey = media_keys.pop()

    def wf_file(p):
        return media_block(p)['workflow'].replace('workflows/', '').replace('workflows\\', '')

    def prev_file(p):
        return os.path.basename(p.get('previewImage', ''))

    # Individual-preset switch cases
    cases = ''
    for i, p in enumerate(presets, 1):
        wf  = wf_file(p)
        prv = prev_file(p)
        cases += (
            f'    {i} {{\n'
            f'        Copy-Item "$src\\workflows\\{wf}" "$presetsDir\\workflows\\{wf}" -Force\n'
            f'        if (Test-Path "$src\\previews\\{prv}") {{\n'
            f'            Copy-Item "$src\\previews\\{prv}" "$presetsDir\\previews\\{prv}" -Force\n'
            f'        }}\n'
            f'        $installList = @($allPresets[{i-1}])\n'
            f'    }}\n'
        )

    menu_lines = '    Write-Host "  [0]  Install ALL presets"\n'
    for i, p in enumerate(presets, 1):
        menu_lines += f'    Write-Host ("  [{i}]  " + $allPresets[{i-1}].name)\n'

    ps1 = (
        'param([string]$src)\n'
        '$enc        = New-Object System.Text.UTF8Encoding($false)\n'
        '$presetsDir = [Environment]::GetFolderPath(\'ApplicationData\') + \'\\simpligen\\presets\'\n'
        '$modelsDir  = [Environment]::GetFolderPath(\'ApplicationData\') + \'\\simpligen\\engine\\models\'\n'
        '\n'
        '# Model field -> subfolder mapping\n'
        '$destMap = @{ checkpoint=\'checkpoints\'; unet=\'diffusion_models\'; vae=\'vae\'; clip=\'clip\' }\n'
        '\n'
        '# Collect unique models needed by a list of preset objects\n'
        f'function Get-Models($presetList) {{\n'
        '    $seen = @{}; $out = @()\n'
        '    foreach ($p in $presetList) {\n'
        f'        $blk = $p.{mkey}\n'
        '        foreach ($field in \'checkpoint\',\'unet\',\'vae\',\'clip\') {\n'
        '            $fname = $blk.$field\n'
        '            if (-not $fname -or $seen[$fname]) { continue }\n'
        '            $seen[$fname] = $true\n'
        '            $out += [PSCustomObject]@{\n'
        '                filename = $fname\n'
        '                url      = $blk.($field + \'Url\')\n'
        '                dest     = $destMap[$field]\n'
        '            }\n'
        '        }\n'
        '        foreach ($e in $blk.extraModels) {\n'
        '            if (-not $e.filename -or $seen[$e.filename]) { continue }\n'
        '            $seen[$e.filename] = $true\n'
        '            $out += [PSCustomObject]@{ filename = $e.filename; url = $e.url; dest = $e.dir }\n'
        '        }\n'
        '        foreach ($arrField in \'unets\',\'loras\') {\n'
        '            $arrDest = if ($arrField -eq \'unets\') { \'diffusion_models\' } else { \'loras\' }\n'
        '            foreach ($e in $blk.$arrField) {\n'
        '                if (-not $e.filename -or $seen[$e.filename]) { continue }\n'
        '                $seen[$e.filename] = $true\n'
        '                $out += [PSCustomObject]@{ filename = $e.filename; url = $e.url; dest = $arrDest }\n'
        '            }\n'
        '        }\n'
        '    }\n'
        '    return $out\n'
        '}\n'
        '\n'
        'function Download-Models($presetList) {\n'
        '    $models = Get-Models $presetList\n'
        '    $failed = @()\n'
        '    $hfToken = $null\n'
        '    $civitaiToken = $null\n'
        '    if ($models | Where-Object { $_.url -like \'*huggingface.co*\' }) {\n'
        '        Write-Host ""\n'
        '        Write-Host "  Some models are hosted on HuggingFace." -ForegroundColor Yellow\n'
        '        Write-Host "  Enter your HF access token to download them automatically,"\n'
        '        Write-Host "  or press Enter to skip HuggingFace downloads (manual install)."\n'
        '        $hfToken = (Read-Host "  HuggingFace token").Trim()\n'
        '    }\n'
        '    if ($models | Where-Object { $_.url -like \'*civitai.com*\' }) {\n'
        '        Write-Host ""\n'
        '        Write-Host "  Some models are hosted on Civitai." -ForegroundColor Yellow\n'
        '        Write-Host "  Civitai requires a free API token to download."\n'
        '        Write-Host "  Create one at: https://civitai.com/user/account (API Keys)"\n'
        '        Write-Host "  Paste your token, or press Enter to skip Civitai downloads."\n'
        '        $civitaiToken = (Read-Host "  Civitai token").Trim()\n'
        '    }\n'
        '    Write-Host ""\n'
        '    foreach ($m in $models) {\n'
        '        $destDir  = "$modelsDir\\$($m.dest)"\n'
        '        $destPath = "$destDir\\$($m.filename)"\n'
        '        if (Test-Path $destPath) {\n'
        '            Write-Host ("  [exists]   " + $m.filename) -ForegroundColor DarkGray\n'
        '            continue\n'
        '        }\n'
        '        if (-not $m.url) {\n'
        '            Write-Host ("  [manual]   " + $m.filename + " - no URL, place manually in $($m.dest)\\") -ForegroundColor Yellow\n'
        '            $failed += ($m.filename + " (no URL - manual)")\n'
        '            continue\n'
        '        }\n'
        '        $isHF = $m.url -like \'*huggingface.co*\'\n'
        '        $isCivitai = $m.url -like \'*civitai.com*\'\n'
        '        if ($isHF -and -not $hfToken) {\n'
        '            Write-Host ("  [skip]     " + $m.filename + " - HuggingFace token not provided") -ForegroundColor Yellow\n'
        '            $failed += ($m.filename + " (skipped - no HF token)")\n'
        '            continue\n'
        '        }\n'
        '        if ($isCivitai -and -not $civitaiToken) {\n'
        '            Write-Host ("  [skip]     " + $m.filename + " - Civitai token not provided") -ForegroundColor Yellow\n'
        '            $failed += ($m.filename + " (skipped - no Civitai token)")\n'
        '            continue\n'
        '        }\n'
        '        if (-not (Test-Path $destDir)) { New-Item -ItemType Directory $destDir -Force | Out-Null }\n'
        '        Write-Host ("  [download] " + $m.filename + "...") -ForegroundColor Cyan\n'
        '        try {\n'
        '            # curl.exe (built into Win10/11): follows redirects, no HEAD probe (BITS 400s on Civitai)\n'
        '            if ($isHF) {\n'
        '                & curl.exe -L --fail --retry 3 -H "Authorization: Bearer $hfToken" -o $destPath $m.url\n'
        '            } elseif ($isCivitai) {\n'
        '                $sep = if ($m.url -like \'*?*\') { \'&\' } else { \'?\' }\n'
        '                $u = $m.url + $sep + \'token=\' + $civitaiToken\n'
        '                & curl.exe -L --fail --retry 3 -o $destPath $u\n'
        '            } else {\n'
        '                & curl.exe -L --fail --retry 3 -o $destPath $m.url\n'
        '            }\n'
        '            if ($LASTEXITCODE -ne 0) { throw "curl exit code $LASTEXITCODE (HTTP error or network failure)" }\n'
        '            if (-not (Test-Path $destPath) -or (Get-Item $destPath).Length -eq 0) {\n'
        '                throw "downloaded file missing or empty"\n'
        '            }\n'
        '            Write-Host ("  [done]     " + $m.filename) -ForegroundColor Green\n'
        '        } catch {\n'
        '            Write-Host ("  [error]    " + $m.filename + ": " + $_) -ForegroundColor Red\n'
        '            if (Test-Path $destPath) { Remove-Item $destPath -Force }\n'
        '            $failed += ($m.filename + " (download failed)")\n'
        '        }\n'
        '    }\n'
        '    return ,$failed\n'
        '}\n'
        '\n'
        'foreach ($sub in \'workflows\',\'previews\') {\n'
        '    $d = "$presetsDir\\$sub"\n'
        '    if (-not (Test-Path $d)) { New-Item -ItemType Directory $d -Force | Out-Null }\n'
        '}\n'
        '\n'
        '$packFile   = (Get-ChildItem $src -Filter \'*-pack.json\')[0].FullName\n'
        '$pack       = [IO.File]::ReadAllText($packFile, $enc) | ConvertFrom-Json\n'
        '$allPresets = @($pack.presets)\n'
        '\n'
        'Write-Host ""\n'
        'Write-Host ("  " + $pack.name + " Installer") -ForegroundColor Cyan\n'
        'Write-Host ("  " + ("=" * ($pack.name.Length + 11)))\n'
        + menu_lines +
        'Write-Host ""\n'
        '$choice = Read-Host "  Choose"\n'
        '\n'
        '$installList = $null\n'
        'switch ([int]$choice) {\n'
        '    0 {\n'
        '        Copy-Item "$src\\workflows\\*" "$presetsDir\\workflows\\" -Force\n'
        '        Copy-Item "$src\\previews\\*"  "$presetsDir\\previews\\"  -Force\n'
        '        $installList = $allPresets\n'
        '    }\n'
        + cases +
        '    default { Write-Host "Invalid choice." -ForegroundColor Red; exit 1 }\n'
        '}\n'
        '\n'
        '$failedDownloads = Download-Models $installList\n'
        '\n'
        'foreach ($p in $installList) {\n'
        '    $leaf = [IO.Path]::GetFileName($p.previewImage)\n'
        '    $p.previewImage = \'local-file:///\' + (Join-Path "$presetsDir\\previews" $leaf).Replace(\'\\\\\',\'/\')\n'
        '}\n'
        '\n'
        '$out = [PSCustomObject]@{\n'
        '    id          = $pack.id\n'
        '    name        = $pack.name\n'
        '    version     = $pack.version\n'
        '    author      = $pack.author\n'
        '    description = $pack.description\n'
        '    tags        = $pack.tags\n'
        '    presets     = $installList\n'
        '}\n'
        '\n'
        '$destJson = "$presetsDir\\$([IO.Path]::GetFileName($packFile))"\n'
        '[IO.File]::WriteAllText($destJson, ($out | ConvertTo-Json -Depth 30), $enc)\n'
        '\n'
        'Write-Host ""\n'
        'if ($failedDownloads -and $failedDownloads.Count -gt 0) {\n'
        '    Write-Host "  Preset(s) installed, BUT some models did not download:" -ForegroundColor Yellow\n'
        '    foreach ($f in $failedDownloads) { Write-Host ("    - " + $f) -ForegroundColor Yellow }\n'
        '    Write-Host ""\n'
        '    Write-Host "  Download these manually (see readme.html for links and folders)" -ForegroundColor Yellow\n'
        '    Write-Host "  before generating, then restart SimpliGen." -ForegroundColor Yellow\n'
        '} else {\n'
        '    Write-Host "  Installed. Restart SimpliGen to see your preset(s)." -ForegroundColor Green\n'
        '}\n'
        'Write-Host ""\n'
    )

    cmd = (
        '@echo off\n'
        'setlocal\n'
        'set "SRC=%~dp0"\n'
        'if "%SRC:~-1%"=="\\" set "SRC=%SRC:~0,-1%"\n'
        'powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" -src "%SRC%"\n'
        'pause\n'
    )

    return cmd, ps1


# ── Build one pack ────────────────────────────────────────────────────────────

def build_pack(slug, pack_dir):
    jsons = [f for f in os.listdir(pack_dir) if f.endswith('-pack.json')]
    if not jsons:
        print(f'  SKIP {slug}: no pack JSON')
        return False
    wf_dir   = os.path.join(pack_dir, 'workflows')
    prev_dir = os.path.join(pack_dir, 'previews')
    if not os.path.isdir(wf_dir) or not os.listdir(wf_dir):
        print(f'  SKIP {slug}: missing workflows/')
        return False
    if not os.path.isdir(prev_dir) or not os.listdir(prev_dir):
        print(f'  SKIP {slug}: missing previews/')
        return False

    pack_json_path = os.path.join(pack_dir, jsons[0])
    data = json.load(open(pack_json_path, encoding='utf-8'))

    media_keys = {media_key(p) for p in data['presets']}
    if not all(media_keys):
        print(f'  SKIP {slug}: preset(s) missing both image and video block')
        return False
    if len(media_keys) > 1:
        print(f'  SKIP {slug}: mixed image/video presets in one pack (not supported)')
        return False

    readme_html      = make_readme(data, pack_dir)
    install_cmd, ps1 = make_install(data, slug)

    zip_path = os.path.join(OUT_DIR, f'community-{slug}.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('readme.html', readme_html.encode('utf-8'))
        zf.writestr('install.cmd', install_cmd.encode('utf-8'))
        zf.writestr('install.ps1', ps1.encode('utf-8'))
        zf.write(pack_json_path, jsons[0])
        for fn in os.listdir(wf_dir):
            zf.write(os.path.join(wf_dir, fn), f'workflows/{fn}')
        for fn in os.listdir(prev_dir):
            zf.write(os.path.join(prev_dir, fn), f'previews/{fn}')

    size_kb = os.path.getsize(zip_path) // 1024
    print(f'  OK  community-{slug}.zip  ({size_kb} KB, {len(data["presets"])} preset{"s" if len(data["presets"])!=1 else ""})')
    return True


# ── Main ──────────────────────────────────────────────────────────────────────

SKIP = {'pony'}   # stale pre-split folder

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ok = fail = 0
    for slug in sorted(os.listdir(BASE)):
        pack_dir = os.path.join(BASE, slug)
        if not os.path.isdir(pack_dir):
            continue
        if slug in SKIP:
            print(f'  SKIP {slug}: excluded (stale)')
            continue
        if build_pack(slug, pack_dir):
            ok += 1
        else:
            fail += 1
    print(f'\n{ok} zip(s) built, {fail} skipped.')
    print(f'Output: {OUT_DIR}')

if __name__ == '__main__':
    main()
