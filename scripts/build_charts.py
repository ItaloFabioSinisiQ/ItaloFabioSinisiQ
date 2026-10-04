"""Generate the SVG graphics used in the profile README.

Each graphic is written twice, once per GitHub theme:
    assets/<name>-light.svg and assets/<name>-dark.svg

Run:  python3 scripts/build_charts.py
"""
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "light": {
        "card": "#f6f8fa", "border": "#d0d7de", "grid": "#e4e8ec",
        "text": "#1f2328", "text2": "#59636e", "muted": "#6e7781",
        "accent": "#2a78d6",
    },
    "dark": {
        "card": "#151b23", "border": "#3d444d", "grid": "#262c36",
        "text": "#f0f6fc", "text2": "#9198a1", "muted": "#7d8590",
        "accent": "#3987e5",
    },
}

# Non-blank lines of code per language, measured with `git ls-files` over the
# 15 private production repositories (dependencies, builds, migrations and
# docs excluded; duplicated forks counted once).
LANGUAGES = [
    ("TypeScript", 216_725),
    ("Python", 196_806),
    ("HTML / CSS", 26_715),
    ("JavaScript", 25_700),
    ("Shell", 14_268),
    ("SQL", 3_515),
]

IMPACT = [
    ("ORDER REJECTION RATE", "7% → 1%", "Delivery platform · Auren"),
    ("SALES CONVERSION", "+15%", "Predictive analytics · UBYCALL"),
    ("CREDIT DEFAULT LOSSES", "−18%", "ML credit scoring · Alfin Banco"),
    ("MANUAL REPORTS AUTOMATED", "80%", "Python + SQL · UBYCALL"),
]


def svg(width, height, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}" '
        f'font-family="{FONT}">\n<title>{title}</title>\n{body}\n</svg>\n'
    )


def banner(t):
    w, h = 1200, 290
    route_x0, route_x1 = 870, 1150
    rows = [85, 150, 215]
    cols = [890, 970, 1060, 1130]
    grid = "".join(
        f'<line x1="{route_x0}" y1="{y}" x2="{route_x1}" y2="{y}" stroke="{t["grid"]}" stroke-width="1.5"/>'
        for y in rows
    ) + "".join(
        f'<line x1="{x}" y1="55" x2="{x}" y2="245" stroke="{t["grid"]}" stroke-width="1.5"/>'
        for x in cols
    )
    route = (
        f'<path d="M890,215 H970 V150 H1060 V85 H1130" fill="none" stroke="{t["accent"]}" '
        f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    stop = lambda x, y: (
        f'<circle cx="{x}" cy="{y}" r="7" fill="{t["card"]}" stroke="{t["accent"]}" stroke-width="2.5"/>'
    )
    stops = (
        stop(890, 215) + stop(970, 150) + stop(1060, 150)
        + f'<circle cx="1130" cy="85" r="11" fill="{t["accent"]}" fill-opacity="0.18"/>'
        + f'<circle cx="1130" cy="85" r="7" fill="{t["accent"]}"/>'
    )
    label = lambda x, y, s, anchor="middle": (
        f'<text x="{x}" y="{y}" font-size="12" fill="{t["text2"]}" text-anchor="{anchor}">{s}</text>'
    )
    labels = (
        label(890, 240, "Data") + label(956, 155, "API", "end")
        + label(1060, 176, "Web") + label(1130, 64, "Mobile")
    )
    body = f"""<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t["card"]}" stroke="{t["border"]}"/>
<text x="56" y="74" font-size="13" letter-spacing="2" fill="{t["muted"]}">LIMA, PERU  ·  OPEN TO REMOTE</text>
<text x="56" y="128" font-size="42" font-weight="700" fill="{t["text"]}">Italo Fabio Sinisi Quintana</text>
<text x="56" y="170" font-size="24" font-weight="600" fill="{t["accent"]}">Full Stack Developer  ·  Data Analyst</text>
<text x="56" y="208" font-size="15" fill="{t["text2"]}">Python · FastAPI · PostgreSQL · TypeScript · React · React Native · Node.js · Docker · CI/CD · Rust</text>
<text x="56" y="246" font-size="14" fill="{t["muted"]}">5+ years shipping logistics, sales and BI platforms to production</text>
{grid}{route}{stops}{labels}"""
    return svg(w, h, body, "Italo Fabio Sinisi Quintana, Full Stack Developer and Data Analyst")


def impact(t):
    w, h, gap = 1200, 170, 16
    tile_w = (w - gap * (len(IMPACT) - 1)) / len(IMPACT)
    parts = []
    for i, (label, value, source) in enumerate(IMPACT):
        x = i * (tile_w + gap)
        parts.append(f"""<g transform="translate({x:.1f},0)">
<rect x="1" y="1" width="{tile_w - 2:.1f}" height="{h - 2}" rx="12" fill="{t["card"]}" stroke="{t["border"]}"/>
<rect x="24" y="28" width="4" height="16" rx="2" fill="{t["accent"]}"/>
<text x="38" y="41" font-size="12" font-weight="600" letter-spacing="1" fill="{t["text2"]}">{label}</text>
<text x="24" y="102" font-size="42" font-weight="700" fill="{t["text"]}">{value}</text>
<text x="24" y="138" font-size="13" fill="{t["muted"]}">{source}</text>
</g>""")
    return svg(w, h, "\n".join(parts), "Measured business impact")


def languages(t):
    w = 1200
    total = sum(v for _, v in LANGUAGES)
    top_two = (LANGUAGES[0][1] + LANGUAGES[1][1]) / total
    label_w, bar_x, bar_max = 150, 190, 820
    row_h, first_row = 38, 112
    h = first_row + row_h * (len(LANGUAGES) - 1) + 66
    peak = LANGUAGES[0][1]
    rows = []
    for i, (name, lines) in enumerate(LANGUAGES):
        y = first_row + i * row_h
        bw = max(4, bar_max * lines / peak)
        share = 100 * lines / total
        rows.append(
            f'<text x="{label_w}" y="{y + 5}" font-size="14" fill="{t["text"]}" text-anchor="end">{name}</text>'
            f'<rect x="{bar_x}" y="{y - 10}" width="{bw:.1f}" height="20" rx="4" fill="{t["accent"]}"/>'
            f'<text x="{bar_x + bw + 12:.1f}" y="{y + 5}" font-size="13" fill="{t["text2"]}">'
            f'<tspan font-weight="600" fill="{t["text"]}">{share:.1f}%</tspan>  ·  {lines / 1000:.0f}K lines</text>'
        )
    body = f"""<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t["card"]}" stroke="{t["border"]}"/>
<text x="40" y="48" font-size="19" font-weight="700" fill="{t["text"]}">Code shipped across 15 production repositories</text>
<text x="40" y="74" font-size="13" fill="{t["text2"]}">{total / 1000:.0f}K non-blank lines by language · TypeScript and Python account for {100 * top_two:.0f}%</text>
<line x1="{bar_x}" y1="{first_row - 22}" x2="{bar_x}" y2="{first_row + row_h * (len(LANGUAGES) - 1) + 14}" stroke="{t["border"]}"/>
{"".join(rows)}
<text x="40" y="{h - 18}" font-size="11" fill="{t["muted"]}">Measured from private repositories with git ls-files · dependencies, builds and docs excluded</text>"""
    return svg(w, h, body, "Lines of code by language across production repositories")


def main():
    ASSETS.mkdir(exist_ok=True)
    for name, build in (("banner", banner), ("impact", impact), ("languages", languages)):
        for mode, theme in THEMES.items():
            (ASSETS / f"{name}-{mode}.svg").write_text(build(theme), encoding="utf-8")
    print(f"wrote {len(THEMES) * 3} files to {ASSETS}")


if __name__ == "__main__":
    main()
