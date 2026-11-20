"""Profil görsellerini üretir: başlık (açık/koyu) ve proje kartları.

Metinleri ya da renkleri değiştirmek için bu dosyayı düzenleyip çalıştır:
    python scripts/build_assets.py
Çıktılar: assets/header-dark.svg, assets/header-light.svg, assets/featured.svg, assets/cards/*.svg
"""
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'

DARK = {"t": "#e6edf3", "m": "#7d8590", "a": "#2dd4bf", "r": "#30363d", "ink": "#0d1117", "bg": "#0d1117", "s": "#161b22"}
LIGHT = {"t": "#1f2328", "m": "#656d76", "a": "#0f766e", "r": "#d0d7de", "ink": "#ffffff", "bg": "#ffffff", "s": "#f6f8fa"}

# Kartlar tek dosyada iki temayı da taşır (prefers-color-scheme ile).
VARS = (
    ":root { "
    + " ".join(f"--{k}: {v};" for k, v in LIGHT.items())
    + " }\n  @media (prefers-color-scheme: dark) { :root { "
    + " ".join(f"--{k}: {v};" for k, v in DARK.items())
    + " } }"
)

ANIM = """
  .draw { stroke-dasharray: 400; stroke-dashoffset: 400; animation: draw 1.2s .3s cubic-bezier(.6,0,.2,1) forwards; }
  .pop { opacity: 0; animation: fade .4s 1.2s forwards; }
  .flow { stroke-dasharray: 4 6; animation: dash 1.2s linear infinite; }
  .pulse { animation: pulse 2.4s ease-in-out infinite; }
  .grow { transform-box: fill-box; transform-origin: bottom; animation: grow 1s .4s cubic-bezier(.2,.8,.2,1) both; }
  .growx { transform-box: fill-box; transform-origin: left; animation: growx .9s .4s cubic-bezier(.2,.8,.2,1) both; }
  .scan { animation: scan 2.6s ease-in-out infinite alternate; }
  .b1, .b2, .b3, .b4, .b5 { opacity: .2; animation: blink 2.4s infinite; }
  .b2 { animation-delay: .3s; } .b3 { animation-delay: .6s; } .b4 { animation-delay: .9s; } .b5 { animation-delay: 1.2s; }
  .d1 { animation-delay: .5s; } .d2 { animation-delay: .65s; } .d3 { animation-delay: .8s; } .d4 { animation-delay: .95s; } .d5 { animation-delay: 1.1s; } .d6 { animation-delay: 1.25s; }
  @keyframes draw { to { stroke-dashoffset: 0; } }
  @keyframes fade { to { opacity: 1; } }
  @keyframes dash { to { stroke-dashoffset: -20; } }
  @keyframes pulse { 50% { opacity: .3; } }
  @keyframes grow { from { transform: scaleY(0); } }
  @keyframes growx { from { transform: scaleX(0); } }
  @keyframes scan { to { transform: translateY(var(--scan, 90px)); } }
  @keyframes blink { 0%, 60%, 100% { opacity: .2; } 30% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) {
    .draw { animation: none; stroke-dashoffset: 0; }
    .pop { animation: none; opacity: 1; }
    .flow, .pulse, .grow, .growx, .scan, .b1, .b2, .b3, .b4, .b5 { animation: none; opacity: 1; }
  }"""


# ---------------------------------------------------------------- başlık

HEADER_ROWS = [
    ("rol", "Full-Stack &amp; AI Developer · LLM · RAG · SaaS"),
    ("durum", "Bilgisayar Mühendisliği · KTO Karatay Üniversitesi"),
    ("stack", "Python · TypeScript · FastAPI · Next.js · PostgreSQL"),
]


def header(c):
    rows = "\n".join(
        f'    <g class="row r{i + 1}"><text x="40" y="{180 + i * 28}" class="a">›</text>'
        f'<text x="58" y="{180 + i * 28}" class="m">{k}</text>'
        f'<text x="150" y="{180 + i * 28}" class="t">{v}</text></g>'
        for i, (k, v) in enumerate(HEADER_ROWS)
    )
    # Sağda küçük bir PR incelemesi: diff satırları taranır, sonra onay düşer.
    diff = [("-", 70), ("-", 110), ("+", 96), ("+", 132), (" ", 84), ("+", 118)]
    lines = []
    for i, (sign, w) in enumerate(diff):
        y = 108 + i * 17
        cls = "a" if sign == "+" else "m"
        op = "1" if sign == "+" else ".55"
        lines.append(
            f'<g class="dl d{i + 1}"><text x="604" y="{y + 7}" font-size="11" class="{cls}">{sign if sign != " " else "·"}</text>'
            f'<rect x="620" y="{y}" width="{w}" height="8" rx="1" class="{cls}" opacity="{op}"/></g>'
        )
    lines = "\n    ".join(lines)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="270" viewBox="0 0 860 270" role="img" aria-label="Ekrem Ağzıgüzel: full-stack ve yapay zekâ geliştirici">
  <style>
    text {{ font-family: {MONO}; }}
    .t {{ fill: {c['t']}; }}
    .m {{ fill: {c['m']}; }}
    .a {{ fill: {c['a']}; }}
    .ink {{ fill: {c['ink']}; }}
    .rule {{ stroke: {c['r']}; stroke-width: 1; }}
    .panel {{ fill: {c['s']}; stroke: {c['r']}; }}
    .box {{ fill: none; stroke: {c['a']}; stroke-width: 2; stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 1.1s .2s cubic-bezier(.6,0,.2,1) forwards; }}
    .tag {{ opacity: 0; animation: fade .3s 1.2s forwards; }}
    .row {{ opacity: 0; animation: fade .4s forwards; }}
    .r1 {{ animation-delay: 1.4s; }} .r2 {{ animation-delay: 1.55s; }} .r3 {{ animation-delay: 1.7s; }}
    .dl {{ opacity: 0; animation: fade .3s forwards; }}
    .d1 {{ animation-delay: 1.5s; }} .d2 {{ animation-delay: 1.65s; }} .d3 {{ animation-delay: 1.8s; }} .d4 {{ animation-delay: 1.95s; }} .d5 {{ animation-delay: 2.1s; }} .d6 {{ animation-delay: 2.25s; }}
    .scan {{ opacity: 0; animation: fade .2s 2.4s forwards, scan 1.4s 2.4s ease-in-out forwards; }}
    .ok {{ opacity: 0; animation: fade .3s 3.9s forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes fade {{ to {{ opacity: 1; }} }}
    @keyframes scan {{ from {{ transform: translateY(0); }} to {{ transform: translateY(100px); }} }}
    @media (prefers-reduced-motion: reduce) {{
      .box {{ animation: none; stroke-dashoffset: 0; }}
      .tag, .row, .dl, .ok {{ animation: none; opacity: 1; }}
      .scan {{ display: none; }}
    }}
  </style>

  <!-- üst bilgi satırı -->
  <text x="40" y="26" font-size="12" class="m">ekremagzl / profile.diff</text>
  <text x="820" y="26" font-size="12" class="m" text-anchor="end">rev. 2026.11</text>
  <line x1="40" y1="38" x2="820" y2="38" class="rule"/>

  <!-- isim: incelenmiş bir değişiklik gibi -->
  <g class="tag">
    <rect x="40" y="58" width="146" height="20" class="a"/>
    <text x="48" y="72" font-size="12" font-weight="700" class="ink" textLength="130" lengthAdjust="spacingAndGlyphs">+ full-stack · ai</text>
  </g>
  <rect x="40" y="78" width="416" height="58" class="box"/>
  <text x="56" y="120" font-size="38" font-weight="700" class="t" textLength="384" lengthAdjust="spacingAndGlyphs">EKREM AĞZIGÜZEL</text>

  <!-- spesifikasyon satırları -->
  <g font-size="14">
{rows}
  </g>

  <!-- sağda mini PR incelemesi -->
  <rect x="592" y="70" width="228" height="166" class="panel"/>
  <text x="604" y="90" font-size="11" class="m">pr #42 · review</text>
  <circle cx="808" cy="86" r="3" class="a"/>
  <line x1="592" y1="98" x2="820" y2="98" class="rule"/>
  <g>
    {lines}
  </g>
  <rect x="593" y="104" width="226" height="2" class="a scan" opacity=".7"/>
  <g class="ok">
    <line x1="592" y1="214" x2="820" y2="214" class="rule"/>
    <text x="604" y="229" font-size="11" class="a">✓ approved</text>
    <text x="812" y="229" font-size="11" class="m" text-anchor="end">0 kritik</text>
  </g>
</svg>
"""


# ---------------------------------------------------------------- kartlar

def card_shell(num, title, tag, desc, footer, art, link_label, w=440, h=200, wrap=34, art_note=""):
    lines = textwrap.wrap(desc, wrap)
    body = "".join(
        f'<text x="20" y="{72 + i * 18}" font-size="12" style="fill:var(--t)">{escape(l)}</text>' for i, l in enumerate(lines)
    )
    note = f'<text x="{w - 20}" y="{h - 34}" font-size="10" text-anchor="end" style="fill:var(--m)">{art_note}</text>' if art_note else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
<style>
  {VARS}
  text {{ font-family: {MONO}; }}{ANIM}
</style>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" style="fill:var(--bg);stroke:var(--r)"/><path d="M0 12 V0 H12 M{w - 12} 0 H{w} V12 M{w} {h - 12} V{h} H{w - 12} M12 {h} H0 V{h - 12}" fill="none" stroke-width="2" style="stroke:var(--a)"/>
<text x="20" y="34" font-size="12" font-weight="700" style="fill:var(--a)">{num}</text>
<text x="44" y="34" font-size="15" font-weight="700" style="fill:var(--t)">{escape(title)}</text>
<text x="{w - 20}" y="34" font-size="10" text-anchor="end" style="fill:var(--m)">{escape(tag)}</text>
<line x1="20" y1="46" x2="{w - 20}" y2="46" style="stroke:var(--r)"/>
{body}
{art}
{note}
<line x1="20" y1="{h - 28}" x2="{w - 20}" y2="{h - 28}" style="stroke:var(--r)"/>
<text x="20" y="{h - 10}" font-size="10" style="fill:var(--m)">{escape(footer)}</text>
<text x="{w - 20}" y="{h - 10}" font-size="10" text-anchor="end" style="fill:var(--{'a' if link_label == 'repo →' else 'm'})">{link_label}</text>
</svg>
"""


# Kart sağ tarafındaki küçük çizimler (yaklaşık x 290-420, y 58-160 alanı).

ART_QR = (lambda: "\n".join(
    f'<rect x="{300 + (i % 9) * 12}" y="{60 + (i // 9) * 12}" width="10" height="10" class="b{(i * 7) % 5 + 1}" style="fill:var(--a)"/>'
    for i in range(81)
    if (i * 37 + i // 9 * 11) % 3 != 0
    and not ((i % 9) < 3 and (i // 9) < 3) and not ((i % 9) > 5 and (i // 9) < 3) and not ((i % 9) < 3 and (i // 9) > 5)
) + "".join(
    f'<rect x="{x}" y="{y}" width="34" height="34" fill="none" stroke-width="3" style="stroke:var(--a)"/>'
    f'<rect x="{x + 10}" y="{y + 10}" width="14" height="14" style="fill:var(--a)"/>'
    for x, y in [(300, 60), (372, 60), (300, 132)]
))()

ART_CAMPUS = """
<g stroke-width="1" stroke-dasharray="3 3" style="stroke:var(--r)">
  <line x1="355" y1="108" x2="306" y2="72"/><line x1="355" y1="108" x2="410" y2="70"/>
  <line x1="355" y1="108" x2="404" y2="150"/><line x1="355" y1="108" x2="300" y2="146"/>
  <line x1="306" y1="72" x2="410" y2="70"/>
</g>
<g style="fill:var(--m)"><circle cx="306" cy="72" r="5"/><circle cx="410" cy="70" r="5"/><circle cx="404" cy="150" r="5"/><circle cx="300" cy="146" r="5"/></g>
<g style="stroke:var(--a)" fill="none" stroke-width="1.5"><line x1="355" y1="108" x2="306" y2="72" class="flow"/><line x1="355" y1="108" x2="404" y2="150" class="flow"/></g>
<circle cx="355" cy="108" r="12" fill="none" stroke-width="2" style="stroke:var(--a)"/>
<path d="M349 108 l4 4 l8 -8" fill="none" stroke-width="2" style="stroke:var(--a)" class="pop"/>
"""

ART_EARTH = """
<line x1="292" y1="60" x2="292" y2="150" style="stroke:var(--r)"/><line x1="292" y1="150" x2="420" y2="150" style="stroke:var(--r)"/>
<polyline points="294,128 310,122 326,126 342,114 358,110 374,102 390,96 406,86 418,80" fill="none" stroke-width="1.8" style="stroke:var(--a)" class="draw"/>
<polyline points="294,84 310,90 326,86 342,98 358,104 374,110 390,118 406,124 418,130" fill="none" stroke-width="1.4" stroke-dasharray="3 3" style="stroke:var(--m)"/>
<circle cx="418" cy="80" r="3" style="fill:var(--a)" class="pop"/>
<text x="296" y="70" font-size="10" style="fill:var(--m)" class="pop">bölge a ↑</text>
<text x="418" y="146" font-size="10" text-anchor="end" style="fill:var(--m)" class="pop">bölge b ↓</text>
"""

ART_NOTES = """
<rect x="306" y="60" width="96" height="96" fill="none" style="stroke:var(--r)"/>
<rect x="316" y="74" width="60" height="5" class="growx d1" style="fill:var(--a)"/>
<rect x="316" y="88" width="76" height="5" class="growx d2" style="fill:var(--m)"/>
<rect x="316" y="100" width="68" height="5" class="growx d3" style="fill:var(--m)"/>
<rect x="316" y="112" width="48" height="5" class="growx d4" style="fill:var(--m)"/>
<g class="pop"><rect x="378" y="124" width="34" height="26" rx="2" style="fill:var(--a)"/>
<path d="M386 124 v-6 a9 9 0 0 1 18 0 v6" fill="none" stroke-width="2.5" style="stroke:var(--a)"/>
<circle cx="395" cy="137" r="3" style="fill:var(--bg)"/></g>
"""

ART_BOOKS = "\n".join(
    f'<rect x="{298 + i * 16}" y="{150 - h}" width="12" height="{h}" class="grow d{i % 6 + 1}" style="fill:var({c})"/>'
    for i, (h, c) in enumerate([(70, "--a"), (84, "--m"), (60, "--a"), (92, "--m"), (76, "--a"), (66, "--m"), (88, "--a"), (72, "--m")])
) + '<line x1="292" y1="150" x2="426" y2="150" stroke-width="2" style="stroke:var(--r)"/>'

ART_FX = """
<g font-size="11">
  <text x="296" y="74" style="fill:var(--m)">USD</text><text x="420" y="74" text-anchor="end" style="fill:var(--a)" class="b1">▲</text>
  <text x="296" y="94" style="fill:var(--m)">EUR</text><text x="420" y="94" text-anchor="end" style="fill:var(--a)" class="b3">▲</text>
  <text x="296" y="114" style="fill:var(--m)">GBP</text><text x="420" y="114" text-anchor="end" style="fill:var(--m)" class="b5">▼</text>
</g>
<polyline points="328,70 342,66 356,72 370,62 384,64 398,58" fill="none" stroke-width="1.4" style="stroke:var(--a)" class="draw"/>
<polyline points="328,90 342,92 356,84 370,88 384,80 398,82" fill="none" stroke-width="1.4" style="stroke:var(--a)" class="draw"/>
<polyline points="328,104 342,108 356,106 370,112 384,110 398,116" fill="none" stroke-width="1.4" style="stroke:var(--m)" class="draw"/>
<rect x="296" y="128" width="124" height="22" fill="none" style="stroke:var(--r)"/>
<text x="304" y="143" font-size="11" style="fill:var(--t)">1 USD →</text><text x="414" y="143" font-size="11" text-anchor="end" style="fill:var(--a)" class="pulse">TRY ···</text>
"""

CARDS = [
    {
        "file": "menum", "num": "01", "title": "MENÜM", "tag": "saas · multi-tenant", "private": True,
        "desc": "Restoranlar için çok kiracılı dijital menü SaaS'ı: QR ile uygulamasız menü, 14 alerjen ve besin bilgisi, tema editörü, ekip rolleri, analitik.",
        "footer": "fastapi · next.js · postgresql · docker · caddy", "art": ART_QR, "note": "",
    },
    {
        "file": "kampusum", "num": "02", "title": "KAMPÜSÜM", "tag": "sprint 4 · beta", "private": True,
        "desc": "Doğrulanmış üniversite öğrencilerine özel kampüs topluluğu: admin onaylı kayıt, akış, takip, engelleme, moderasyon kuyruğu; tüm tablolarda RLS.",
        "footer": "next.js · typescript · supabase · rls · playwright", "art": ART_CAMPUS, "note": "",
    },
    {
        "file": "earth-trend", "num": "03", "title": "EARTH TREND DETECTIVE", "tag": "nasa verisi", "private": True,
        "desc": "NASA Giovanni verisiyle (GPM yağış, GLDAS toprak nemi, MERRA-2 sıcaklık) bölgelerin 25 yıllık iklim trendlerini yan yana koyan panel.",
        "footer": "python · pandas · streamlit · nasa giovanni", "art": ART_EARTH, "note": "", "label": "takım projesi",
    },
    {
        "file": "not-defteri", "num": "04", "title": "NOT DEFTERİ", "tag": "staj bitirme", "private": True,
        "desc": "Kayıt, giriş ve kullanıcıya özel not CRUD'u olan full-stack uygulama; JWT + bcrypt kimlik doğrulama, Jest + Supertest ile API testleri.",
        "footer": "react · express · mysql · sequelize · jwt", "art": ART_NOTES, "note": "",
    },
    {
        "file": "bookstore", "num": "05", "title": "BOOKSTORE", "tag": "react · staj", "private": False,
        "desc": "Kitap vitrini: Context API ile açık/koyu tema, Open Library'den canlı kapaklar, aynı veriden galeri ve tablo görünümü.",
        "footer": "react 19 · vite · context api · oxlint", "art": ART_BOOKS, "note": "",
    },
    {
        "file": "canli-doviz", "num": "06", "title": "CANLI DÖVİZ", "tag": "masaüstü", "private": False,
        "desc": "Kurları API'den canlı çekip 7 para birimi arasında anında çeviren, 30 saniyede bir yenilenen Tkinter uygulaması.",
        "footer": "python · tkinter · rest api", "art": ART_FX, "note": "",
    },
]


# ---------------------------------------------------------------- öne çıkan proje

def featured():
    w, h = 880, 240
    steps = [("webhook", "imza ✓"), ("diff", "satır no."), ("llm", "gemini"), ("rag", "pgvector"), ("pr yorumu", "önem sırası")]
    boxes = []
    x0, bw, gap = 40, 128, 32
    for i, (name, sub) in enumerate(steps):
        x = x0 + i * (bw + gap)
        dashed = ' stroke-dasharray="4 4"' if name == "rag" else ""
        boxes.append(
            f'<g class="pop" style="animation-delay:{0.3 + i * 0.25:.2f}s">'
            f'<rect x="{x}" y="92" width="{bw}" height="52"{dashed} style="fill:var(--s);stroke:var(--{"a" if i in (2, 4) else "r"})"/>'
            f'<text x="{x + 12}" y="114" font-size="13" font-weight="700" style="fill:var(--t)">{name}</text>'
            f'<text x="{x + 12}" y="132" font-size="10" style="fill:var(--m)">{sub}</text></g>'
        )
        if i < len(steps) - 1:
            ax = x + bw
            boxes.append(
                f'<line x1="{ax + 4}" y1="118" x2="{ax + gap - 6}" y2="118" stroke-width="1.6" style="stroke:var(--a)" class="flow"/>'
                f'<path d="M{ax + gap - 10} 114 l5 4 l-5 4" fill="none" stroke-width="1.6" style="stroke:var(--a)"/>'
            )
    cats = ["hata riski", "güvenlik", "performans", "okunabilirlik"]
    chips = []
    cx = 40
    for i, c in enumerate(cats):
        cw = len(c) * 7 + 20
        chips.append(
            f'<g class="b{i + 1}"><rect x="{cx}" y="166" width="{cw}" height="20" fill="none" style="stroke:var(--a)"/>'
            f'<text x="{cx + 10}" y="180" font-size="11" style="fill:var(--a)">{c}</text></g>'
        )
        cx += cw + 10
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="PR Review Assistant: RAG tabanlı yapay zekâ kod inceleme asistanı">
<style>
  {VARS}
  text {{ font-family: {MONO}; }}{ANIM}
</style>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" style="fill:var(--bg);stroke:var(--r)"/><path d="M0 14 V0 H14 M{w - 14} 0 H{w} V14 M{w} {h - 14} V{h} H{w - 14} M14 {h} H0 V{h - 14}" fill="none" stroke-width="2" style="stroke:var(--a)"/>
<text x="40" y="38" font-size="12" font-weight="700" style="fill:var(--a)">★</text>
<text x="62" y="38" font-size="17" font-weight="700" style="fill:var(--t)">PR REVIEW ASSISTANT</text>
<text x="{w - 40}" y="38" font-size="11" text-anchor="end" style="fill:var(--m)">bitirme projesi · github app</text>
<line x1="40" y1="52" x2="{w - 40}" y2="52" style="stroke:var(--r)"/>
<text x="40" y="76" font-size="12" style="fill:var(--m)">pull request açılır → asistan diff'i okur, bulguları satırına yorum olarak yazar</text>
{''.join(boxes)}
{''.join(chips)}
<text x="{w - 40}" y="180" font-size="11" text-anchor="end" style="fill:var(--m)">- - - planlanan (İP2)</text>
<line x1="40" y1="{h - 30}" x2="{w - 40}" y2="{h - 30}" style="stroke:var(--r)"/>
<text x="40" y="{h - 12}" font-size="10" style="fill:var(--m)">python · fastapi · github apps · gemini · pgvector · tree-sitter · pytest</text>
<text x="{w - 40}" y="{h - 12}" font-size="10" text-anchor="end" style="fill:var(--m)">KTO Karatay Üniversitesi</text>
</svg>
"""


def main():
    (ASSETS / "cards").mkdir(parents=True, exist_ok=True)
    (ASSETS / "header-dark.svg").write_text(header(DARK), encoding="utf-8")
    (ASSETS / "header-light.svg").write_text(header(LIGHT), encoding="utf-8")
    (ASSETS / "featured.svg").write_text(featured(), encoding="utf-8")
    for c in CARDS:
        label = c.get("label") or ("private" if c["private"] else "repo →")
        svg = card_shell(c["num"], c["title"], c["tag"], c["desc"], c["footer"], c["art"], label, art_note=c["note"])
        (ASSETS / "cards" / f"{c['file']}.svg").write_text(svg, encoding="utf-8")
    print("başlık, öne çıkan proje ve", len(CARDS), "kart üretildi")


if __name__ == "__main__":
    main()
