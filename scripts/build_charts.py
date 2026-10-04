"""Generate the SVG graphics used in the profile README.

Each graphic is written twice, once per GitHub theme:
    assets/<name>-light.svg and assets/<name>-dark.svg

Run:  python3 scripts/build_charts.py
"""
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"

THEMES = {
    "light": {
        "card": "#ffffff", "panel": "#f6f8fa", "border": "#d0d7de",
        "text": "#1f2328", "text2": "#59636e", "muted": "#6e7781",
        "accent": "#2a78d6", "accent_soft": "#cde2fb",
    },
    "dark": {
        "card": "#0d1117", "panel": "#151b23", "border": "#3d444d",
        "text": "#f0f6fc", "text2": "#9198a1", "muted": "#7d8590",
        "accent": "#3987e5", "accent_soft": "#184f95",
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
    ("Order rejection rate", "7% → 1%", "RutaLiquidador · Auren"),
    ("Sales conversion", "+15%", "Predictive analytics · UBYCALL"),
    ("Credit default losses", "−18%", "ML credit scoring · Alfin Banco"),
    ("Manual reporting automated", "80%", "Python and SQL · UBYCALL"),
]

CASE_METRICS = [
    ("REST API endpoints", "207", "FastAPI · JWT · rate limiting"),
    ("Automated tests", "7,700+", "pytest · Jest · Vitest · Playwright"),
    ("Data model", "47 tables", "PostgreSQL 16 · 60 migrations"),
    ("Field rollout", "43 devices", "Driver app in daily production use"),
]

SOURCES = [
    ("ERP · SQL Server", "Dispatch, invoices, promotions", "Read-only synchronization"),
    ("Fleet GPS tracker", "Live truck positions", "Isolated, token-hiding proxy"),
    ("OSRM and map tiles", "Road routing for Lima", "Self-hosted tile server"),
]

CORE_MODULES = [
    "Promotion identification engine · 14 cases",
    "Route settlement and multi-user delivery log",
    "Offline conflict resolution and audit trail",
    "Scheduler · 12 background jobs and alerts",
]

CLIENTS = [
    ("Driver app", "Expo · React Native", "Offline-first · GPS · AES-256"),
    ("Control tower", "React · TypeScript · Vite", "27 views · live fleet map"),
    ("WhatsApp gateway", "Operational alerts", "Rejections and partial deliveries"),
]

HEADER_FACTS = [
    ("EXPERIENCE", "5+ years in software and data"),
    ("LOCATION", "Lima, Peru · open to remote"),
    ("CURRENTLY", "Lead developer, BI area · Auren"),
]


def svg(width, height, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}" '
        f'font-family="{SANS}">\n<title>{title}</title>\n{body}\n</svg>\n'
    )


def frame(t, w, h):
    return f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="{t["panel"]}" stroke="{t["border"]}"/>'


def header(t):
    w, h = 1200, 280
    facts = "".join(
        f'<text x="880" y="{82 + i * 62}" font-size="11" letter-spacing="1.6" fill="{t["muted"]}">{label}</text>'
        f'<text x="880" y="{104 + i * 62}" font-size="16" fill="{t["text"]}">{value}</text>'
        for i, (label, value) in enumerate(HEADER_FACTS)
    )
    body = f"""{frame(t, w, h)}
<rect x="0.5" y="0.5" width="6" height="{h - 1}" fill="{t["accent"]}"/>
<text x="64" y="112" font-family="{SERIF}" font-size="48" fill="{t["text"]}">Italo Fabio Sinisi Quintana</text>
<rect x="64" y="134" width="64" height="3" fill="{t["accent"]}"/>
<text x="64" y="180" font-size="23" font-weight="600" fill="{t["text"]}">Full Stack Developer  |  Data Analyst</text>
<text x="64" y="216" font-size="15" fill="{t["text2"]}">Logistics platforms · Business Intelligence · Data engineering</text>
<text x="64" y="242" font-size="14" fill="{t["muted"]}">Python · FastAPI · PostgreSQL · TypeScript · React · React Native · Docker · CI/CD · Rust</text>
<line x1="840" y1="58" x2="840" y2="{h - 50}" stroke="{t["border"]}"/>
{facts}"""
    return svg(w, h, body, "Italo Fabio Sinisi Quintana, Full Stack Developer and Data Analyst")


def tiles(t, items, title):
    w, h, gap = 1200, 150, 16
    tile_w = (w - gap * (len(items) - 1)) / len(items)
    parts = []
    for i, (label, value, source) in enumerate(items):
        x = i * (tile_w + gap)
        parts.append(f"""<g transform="translate({x:.1f},0)">
{frame(t, tile_w, h)}
<text x="24" y="38" font-size="13" fill="{t["text2"]}">{label}</text>
<text x="24" y="92" font-size="38" font-weight="700" fill="{t["text"]}">{value}</text>
<rect x="24" y="108" width="28" height="2" fill="{t["accent"]}"/>
<text x="24" y="130" font-size="12" fill="{t["muted"]}">{source}</text>
</g>""")
    return svg(w, h, "\n".join(parts), title)


def impact(t):
    return tiles(t, IMPACT, "Measured business impact")


def case_metrics(t):
    return tiles(t, CASE_METRICS, "RutaLiquidador at a glance")


def architecture(t):
    w, h = 1200, 540
    col = {"src": (40, 260), "core": (380, 440), "cli": (900, 260)}
    box_h, gap, top = 100, 22, 84

    def node(x, y, bw, title, line1, line2):
        return (
            f'<rect x="{x}" y="{y}" width="{bw}" height="{box_h}" rx="6" fill="{t["card"]}" stroke="{t["border"]}"/>'
            f'<text x="{x + 18}" y="{y + 32}" font-size="16" font-weight="600" fill="{t["text"]}">{title}</text>'
            f'<text x="{x + 18}" y="{y + 58}" font-size="13" fill="{t["text2"]}">{line1}</text>'
            f'<text x="{x + 18}" y="{y + 80}" font-size="13" fill="{t["muted"]}">{line2}</text>'
        )

    def arrow(x1, x2, y):
        return f'<line x1="{x1}" y1="{y}" x2="{x2 - 4}" y2="{y}" stroke="{t["accent"]}" stroke-width="1.6" marker-end="url(#arrow)"/>'

    parts = [frame(t, w, h)]
    parts.append(
        f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{t["accent"]}"/></marker></defs>'
    )
    for key, label in (("src", "DATA SOURCES"), ("core", "PLATFORM CORE"), ("cli", "CLIENTS")):
        parts.append(f'<text x="{col[key][0]}" y="58" font-size="11" letter-spacing="1.6" fill="{t["muted"]}">{label}</text>')

    core_x, core_w = col["core"]
    core_h = 3 * box_h + 2 * gap
    for i, (a, b, c) in enumerate(SOURCES):
        y = top + i * (box_h + gap)
        parts.append(node(col["src"][0], y, col["src"][1], a, b, c))
        parts.append(arrow(col["src"][0] + col["src"][1], core_x, y + box_h / 2))
    for i, (a, b, c) in enumerate(CLIENTS):
        y = top + i * (box_h + gap)
        parts.append(node(col["cli"][0], y, col["cli"][1], a, b, c))
        parts.append(arrow(core_x + core_w, col["cli"][0], y + box_h / 2))

    parts.append(
        f'<rect x="{core_x}" y="{top}" width="{core_w}" height="{core_h}" rx="6" fill="{t["card"]}" stroke="{t["accent"]}" stroke-width="1.5"/>'
        f'<text x="{core_x + 22}" y="{top + 36}" font-size="18" font-weight="600" fill="{t["text"]}">FastAPI backend</text>'
        f'<text x="{core_x + 22}" y="{top + 60}" font-size="13" fill="{t["text2"]}">Python · SQLAlchemy async · Alembic · APScheduler</text>'
    )
    for i, label in enumerate(CORE_MODULES):
        y = top + 80 + i * 44
        parts.append(
            f'<rect x="{core_x + 22}" y="{y}" width="{core_w - 44}" height="34" rx="4" fill="{t["panel"]}" stroke="{t["border"]}"/>'
            f'<text x="{core_x + 38}" y="{y + 22}" font-size="13" fill="{t["text"]}">{label}</text>'
        )
    db_y = top + 80 + len(CORE_MODULES) * 44 + 6
    parts.append(
        f'<rect x="{core_x + 22}" y="{db_y}" width="{core_w - 44}" height="40" rx="4" fill="{t["accent_soft"]}" fill-opacity="0.45" stroke="{t["accent"]}"/>'
        f'<text x="{core_x + 38}" y="{db_y + 26}" font-size="14" font-weight="600" fill="{t["text"]}">PostgreSQL 16</text>'
        f'<text x="{core_x + 160}" y="{db_y + 26}" font-size="13" fill="{t["text2"]}">47 tables · 60 migrations · 13 GB</text>'
    )

    band_y = top + core_h + 26
    parts.append(
        f'<line x1="40" y1="{band_y}" x2="{w - 40}" y2="{band_y}" stroke="{t["border"]}"/>'
        f'<text x="40" y="{band_y + 34}" font-size="11" letter-spacing="1.6" fill="{t["muted"]}">DELIVERY</text>'
        f'<text x="140" y="{band_y + 34}" font-size="13" fill="{t["text2"]}">Docker Compose · Nginx · 6 GitHub Actions workflows · '
        f'container images on GHCR · scripted deploy with backup, smoke test and rollback</text>'
    )
    return svg(w, h, "\n".join(parts), "RutaLiquidador system architecture")


def languages(t):
    w = 1200
    total = sum(v for _, v in LANGUAGES)
    top_two = (LANGUAGES[0][1] + LANGUAGES[1][1]) / total
    label_w, bar_x, bar_max = 150, 180, 820
    row_h, first_row = 36, 112
    h = first_row + row_h * (len(LANGUAGES) - 1) + 66
    peak = LANGUAGES[0][1]
    rows = []
    for i, (name, lines) in enumerate(LANGUAGES):
        y = first_row + i * row_h
        bw = max(4, bar_max * lines / peak)
        share = 100 * lines / total
        rows.append(
            f'<text x="{label_w}" y="{y + 5}" font-size="14" fill="{t["text"]}" text-anchor="end">{name}</text>'
            f'<rect x="{bar_x}" y="{y - 9}" width="{bw:.1f}" height="18" rx="3" fill="{t["accent"]}"/>'
            f'<text x="{bar_x + bw + 12:.1f}" y="{y + 5}" font-size="13" fill="{t["text2"]}">'
            f'<tspan font-weight="600" fill="{t["text"]}">{share:.1f}%</tspan>  ·  {lines / 1000:.0f}K lines</text>'
        )
    body = f"""{frame(t, w, h)}
<text x="40" y="50" font-family="{SERIF}" font-size="21" fill="{t["text"]}">Code shipped across 15 production repositories</text>
<text x="40" y="76" font-size="13" fill="{t["text2"]}">{total / 1000:.0f}K non-blank lines by language · TypeScript and Python account for {100 * top_two:.0f}%</text>
<line x1="{bar_x}" y1="{first_row - 20}" x2="{bar_x}" y2="{first_row + row_h * (len(LANGUAGES) - 1) + 14}" stroke="{t["border"]}"/>
{"".join(rows)}
<text x="40" y="{h - 18}" font-size="11" fill="{t["muted"]}">Measured from private repositories with git ls-files · dependencies, builds and docs excluded</text>"""
    return svg(w, h, body, "Lines of code by language across production repositories")


BUILDERS = {
    "header": header,
    "impact": impact,
    "case-metrics": case_metrics,
    "architecture": architecture,
    "languages": languages,
}


def main():
    ASSETS.mkdir(exist_ok=True)
    for name, build in BUILDERS.items():
        for mode, theme in THEMES.items():
            (ASSETS / f"{name}-{mode}.svg").write_text(build(theme), encoding="utf-8")
    print(f"wrote {len(THEMES) * len(BUILDERS)} files to {ASSETS}")


if __name__ == "__main__":
    main()
