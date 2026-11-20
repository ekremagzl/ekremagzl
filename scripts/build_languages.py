"""Profil için dil dağılımı kartını (assets/languages.svg) üretir.

Veri: GitHub API'deki repo dil istatistikleri (bayt). GH_TOKEN `repo` izinli bir
kişisel token ise gizli repolar da sayılır; token yoksa yalnızca açık repolar.
İşaretleme/yapılandırma dilleri (HTML, CSS, Dockerfile...) dışarıda bırakılır.

Çalıştırma:  GH_TOKEN=... python scripts/build_languages.py
"""
import json
import math
import os
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "languages.svg"
USER = os.environ.get("GH_USER", "ekremagzl")
SKIPPED_REPOS = {USER}  # profil reposunun kendisi
IGNORED = {"HTML", "CSS", "SCSS", "Dockerfile", "Procfile", "Shell", "PowerShell", "Batchfile", "Makefile", "Mako"}
ALIASES = {"PLpgSQL": "SQL", "TSQL": "SQL", "Jupyter Notebook": "Notebook"}
TOP = 5

LIGHT = {"t": "#1f2328", "m": "#656d76", "r": "#d0d7de", "bg": "#ffffff",
         "c0": "#0f766e", "c1": "#14b8a6", "c2": "#115e59", "c3": "#5eead4", "c4": "#134e4a", "c5": "#8c959f"}
DARK = {"t": "#e6edf3", "m": "#7d8590", "r": "#30363d", "bg": "#0d1117",
        "c0": "#2dd4bf", "c1": "#14937f", "c2": "#99f6e4", "c3": "#0f766e", "c4": "#5eead4", "c5": "#6e7681"}
MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'


def api(path, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-languages"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect(token):
    totals = {}
    base = "/user/repos?affiliation=owner" if token else f"/users/{USER}/repos?type=owner"
    page = 1
    while True:
        try:
            repos = api(f"{base}&per_page=100&page={page}", token)
        except urllib.error.HTTPError:
            if base.startswith("/user/"):  # GITHUB_TOKEN /user/repos'a erişemez → açık repolara düş
                base, page = f"/users/{USER}/repos?type=owner", 1
                continue
            raise
        if not repos:
            break
        for repo in repos:
            if repo["fork"] or repo["name"] in SKIPPED_REPOS:
                continue
            for lang, size in api(f"/repos/{repo['full_name']}/languages", token).items():
                if lang in IGNORED:
                    continue
                name = ALIASES.get(lang, lang)
                totals[name] = totals.get(name, 0) + size
        page += 1
    return totals


def fmt(p):
    return "&lt;0.1%" if p < 0.1 else f"{p:.1f}%"


def render(totals):
    total = sum(totals.values()) or 1
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    rows = ranked[:TOP]
    rest = sum(v for _, v in ranked[TOP:])
    if rest:
        rows.append(("Diğer", rest))

    cx, cy, r = 130, 118, 70
    circ = 2 * math.pi * r
    arcs, offset = [], 0.0
    for i, (_, v) in enumerate(rows):
        length = circ * v / total
        seg = max(length - 2, 0.5)
        color = f"c{i}" if i < TOP else "c5"
        arcs.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" style="stroke:var(--{color})" stroke-width="22" '
            f'stroke-dasharray="{seg:.2f} {circ:.2f}" stroke-dashoffset="{-offset:.2f}" transform="rotate(-90 {cx} {cy})" class="arc" />'
        )
        offset += length

    lines = []
    for i, (name, v) in enumerate(rows):
        y = 49 + i * 28
        p = 100 * v / total
        color = f"c{i}" if i < TOP else "c5"
        lines.append(
            f'<g class="row" style="animation-delay:{0.3 + i * 0.1:.1f}s">'
            f'<rect x="270" y="{y}" width="10" height="10" style="fill:var(--{color})"/>'
            f'<text x="290" y="{y + 9}" font-size="13" style="fill:var(--t)">{name}</text>'
            f'<rect x="420" y="{y + 2}" width="300" height="6" style="fill:var(--r)"/>'
            f'<rect x="420" y="{y + 2}" width="{max(300 * p / 100, 1):.1f}" height="6" style="fill:var(--{color})" class="bar"/>'
            f'<text x="840" y="{y + 9}" font-size="12" text-anchor="end" style="fill:var(--m)">{fmt(p)}</text></g>'
        )

    v = lambda d: " ".join(f"--{k}: {val};" for k, val in d.items())
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="230" viewBox="0 0 880 230" role="img" aria-label="En çok kullandığım diller">
<style>
  :root {{ {v(LIGHT)} }}
  @media (prefers-color-scheme: dark) {{ :root {{ {v(DARK)} }} }}
  text {{ font-family: {MONO}; }}
  .arc {{ opacity: 0; animation: fade .6s .1s forwards; }}
  .row {{ opacity: 0; animation: fade .4s forwards; }}
  .bar {{ transform-box: fill-box; transform-origin: left; animation: grow .9s .4s cubic-bezier(.2,.8,.2,1) both; }}
  @keyframes fade {{ to {{ opacity: 1; }} }}
  @keyframes grow {{ from {{ transform: scaleX(0); }} }}
  @media (prefers-reduced-motion: reduce) {{ .arc, .row {{ animation: none; opacity: 1; }} .bar {{ animation: none; }} }}
</style>
<rect x=".5" y=".5" width="879" height="229" style="fill:var(--bg);stroke:var(--r)"/>
<text x="40" y="28" font-size="11" style="fill:var(--m)">diller · kendi repolarımdaki koda göre</text>
{''.join(arcs)}
<text x="{cx}" y="{cy - 2}" font-size="12" text-anchor="middle" style="fill:var(--m)">kod</text>
<text x="{cx}" y="{cy + 16}" font-size="14" font-weight="700" text-anchor="middle" style="fill:var(--t)">{len(totals)} dil</text>
{''.join(lines)}
</svg>
"""


if __name__ == "__main__":
    totals = collect(os.environ.get("GH_TOKEN", "").strip())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(totals), encoding="utf-8")
    print(f"{OUT.name}: {len(totals)} dil yazıldı")
