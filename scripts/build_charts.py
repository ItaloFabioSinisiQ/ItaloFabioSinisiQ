"""Generate the SVG graphics used in the profile README.

Every graphic is written per language and per GitHub theme:
    assets/<name>-light.svg, assets/<name>-dark.svg        (English)
    assets/<name>-es-light.svg, assets/<name>-es-dark.svg  (Spanish)

The language switcher buttons are written as:
    assets/lang-<en|es>[-active]-<light|dark>.svg

Graphics are drawn at 880 px, the width of the README column on a GitHub
profile, so SVG font sizes match rendered pixels (minimum 12 px).

Run:  python3 scripts/build_charts.py
"""
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"
W = 880

# Accent matches GitHub's own link color in each theme.
THEMES = {
    "light": {
        "panel": "#f6f8fa", "card": "#ffffff", "border": "#d0d7de",
        "text": "#1f2328", "text2": "#59636e", "accent": "#0969da", "on_accent": "#ffffff",
    },
    "dark": {
        "panel": "#151b23", "card": "#0d1117", "border": "#3d444d",
        "text": "#f0f6fc", "text2": "#9198a1", "accent": "#4493f8", "on_accent": "#0d1117",
    },
}

COPY = {
    "en": {
        "title": "Full Stack Developer &amp; Data Analyst",
        "tagline": "Logistics, sales and BI platforms in production",
        "facts": [
            ("EXPERIENCE", "5+ years · software and data"),
            ("LOCATION", "Lima, Peru (GMT-5) · remote"),
            ("CURRENT ROLE", "Full Stack Developer · Auren"),
        ],
        "impact": [
            ("Order rejection rate", "7% → 1%", "RutaLiquidador · Auren"),
            ("Sales conversion", "+15%", "Predictive analytics · UBYCALL"),
            ("Credit default losses", "−18%", "Credit scoring · Alfin Banco"),
            ("Reports automated", "80%", "Python and SQL · UBYCALL"),
        ],
        "case": [
            ("207", "REST API endpoints"),
            ("7,700+", "automated tests"),
            ("47", "database tables"),
            ("43", "devices in production"),
        ],
        "columns": ("DATA SOURCES", "PLATFORM CORE", "CLIENTS"),
        "sources": [
            ("ERP (SQL Server)", "Orders and promotions"),
            ("Fleet GPS tracker", "Live truck positions"),
            ("OSRM routing", "Self-hosted Lima maps"),
        ],
        "core": ("FastAPI backend", "Python · SQLAlchemy · APScheduler"),
        "modules": [
            "Promotion engine · 14 promotion types",
            "Route settlement and delivery log",
            "Offline conflict resolution, audit trail",
            "Scheduler · 12 background jobs",
        ],
        "db": ("PostgreSQL 16", "47 tables · 60 migrations"),
        "clients": [
            ("Driver app", "React Native · offline-first"),
            ("Control tower", "React · 27 views"),
            ("WhatsApp gateway", "Operational alerts"),
        ],
        "delivery": (
            "DELIVERY",
            "Docker Compose · Nginx · 6 GitHub Actions workflows · images on GHCR",
            "Scripted releases with backup, smoke test and automatic rollback",
        ),
        "a11y": ("Italo Fabio Sinisi Quintana, Full Stack Developer and Data Analyst",
                 "Selected results", "RutaLiquidador at a glance", "RutaLiquidador system architecture"),
    },
    "es": {
        "title": "Desarrollador Full Stack y Analista de Datos",
        "tagline": "Plataformas de logística, ventas y BI en producción",
        "facts": [
            ("EXPERIENCIA", "5+ años · software y datos"),
            ("UBICACIÓN", "Lima, Perú (GMT-5) · remoto"),
            ("CARGO ACTUAL", "Full Stack Developer · Auren"),
        ],
        "impact": [
            ("Rechazo de pedidos", "7% → 1%", "RutaLiquidador · Auren"),
            ("Conversión de ventas", "+15%", "Analítica predictiva · UBYCALL"),
            ("Pérdidas por impago", "−18%", "Scoring · Alfin Banco"),
            ("Reportes automatizados", "80%", "Python y SQL · UBYCALL"),
        ],
        "case": [
            ("207", "endpoints de API REST"),
            ("7,700+", "tests automatizados"),
            ("47", "tablas de base de datos"),
            ("43", "dispositivos en producción"),
        ],
        "columns": ("FUENTES DE DATOS", "NÚCLEO DE LA PLATAFORMA", "CLIENTES"),
        "sources": [
            ("ERP (SQL Server)", "Pedidos y promociones"),
            ("Rastreador GPS", "Posición de los camiones"),
            ("Ruteo OSRM", "Mapas de Lima propios"),
        ],
        "core": ("Backend FastAPI", "Python · SQLAlchemy · APScheduler"),
        "modules": [
            "Motor de promociones · 14 tipos",
            "Liquidación de rutas y bitácora",
            "Conflictos offline y auditoría",
            "Scheduler · 12 tareas programadas",
        ],
        "db": ("PostgreSQL 16", "47 tablas · 60 migraciones"),
        "clients": [
            ("App del chofer", "React Native · offline-first"),
            ("Torre de control", "React · 27 vistas"),
            ("Gateway WhatsApp", "Alertas operativas"),
        ],
        "delivery": (
            "DESPLIEGUE",
            "Docker Compose · Nginx · 6 workflows de GitHub Actions · imágenes en GHCR",
            "Releases automatizados con backup, smoke test y rollback automático",
        ),
        "a11y": ("Italo Fabio Sinisi Quintana, Desarrollador Full Stack y Analista de Datos",
                 "Resultados destacados", "RutaLiquidador en cifras", "Arquitectura de RutaLiquidador"),
    },
}

LANG_LABELS = {"en": "English", "es": "Español"}


def svg(height, body, title, width=W):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}" '
        f'font-family="{SANS}">\n<title>{title}</title>\n{body}\n</svg>\n'
    )


def frame(t, w, h, fill="panel"):
    return (
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" '
        f'fill="{t[fill]}" stroke="{t["border"]}"/>'
    )


def caps(x, y, label, t):
    return (
        f'<text x="{x}" y="{y}" font-size="12" font-weight="600" letter-spacing="0.8" '
        f'fill="{t["text2"]}">{label}</text>'
    )


def header(t, c):
    h = 200
    facts = "".join(
        caps(612, 52 + i * 52, label, t)
        + f'<text x="612" y="{73 + i * 52}" font-size="15" fill="{t["text"]}">{value}</text>'
        for i, (label, value) in enumerate(c["facts"])
    )
    body = f"""<defs><clipPath id="card"><rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="6"/></clipPath></defs>
{frame(t, W, h)}
<rect x="0" y="0" width="5" height="{h}" fill="{t["accent"]}" clip-path="url(#card)"/>
<text x="40" y="78" font-family="{SERIF}" font-size="38" fill="{t["text"]}">Italo Fabio Sinisi Quintana</text>
<rect x="40" y="96" width="48" height="3" rx="1.5" fill="{t["accent"]}"/>
<text x="40" y="134" font-size="20" font-weight="600" fill="{t["text"]}">{c["title"]}</text>
<text x="40" y="162" font-size="15" fill="{t["text2"]}">{c["tagline"]}</text>
<line x1="588" y1="32" x2="588" y2="{h - 32}" stroke="{t["border"]}"/>
{facts}"""
    return svg(h, body, c["a11y"][0])


def impact(t, c):
    h, gap = 120, 12
    items = c["impact"]
    tile_w = (W - gap * (len(items) - 1)) / len(items)
    parts = []
    for i, (label, value, source) in enumerate(items):
        x = i * (tile_w + gap)
        parts.append(f"""<g transform="translate({x:.1f},0)">
{frame(t, tile_w, h)}
<text x="18" y="32" font-size="13" font-weight="600" fill="{t["text2"]}">{label}</text>
<text x="18" y="74" font-size="30" font-weight="700" fill="{t["text"]}">{value}</text>
<text x="18" y="100" font-size="12" fill="{t["text2"]}">{source}</text>
</g>""")
    return svg(h, "\n".join(parts), c["a11y"][1])


def case_metrics(t, c):
    h = 92
    items = c["case"]
    col_w = W / len(items)
    parts = [frame(t, W, h)]
    for i, (value, label) in enumerate(items):
        x = i * col_w
        if i:
            parts.append(f'<line x1="{x:.1f}" y1="20" x2="{x:.1f}" y2="{h - 20}" stroke="{t["border"]}"/>')
        parts.append(
            f'<text x="{x + 24:.1f}" y="46" font-size="26" font-weight="700" fill="{t["text"]}">{value}</text>'
            f'<text x="{x + 24:.1f}" y="70" font-size="13" fill="{t["text2"]}">{label}</text>'
        )
    return svg(h, "\n".join(parts), c["a11y"][2])


def architecture(t, c):
    src_x, core_x, cli_x = 24, 290, 656
    node_w, core_w = 200, 300
    top, box_h, gap = 56, 72, 16
    span = 3 * box_h + 2 * gap
    h = top + span + 100

    def node(x, y, title, line):
        return (
            f'<rect x="{x}" y="{y}" width="{node_w}" height="{box_h}" rx="6" fill="{t["card"]}" stroke="{t["border"]}"/>'
            f'<text x="{x + 16}" y="{y + 30}" font-size="15" font-weight="600" fill="{t["text"]}">{title}</text>'
            f'<text x="{x + 16}" y="{y + 52}" font-size="13" fill="{t["text2"]}">{line}</text>'
        )

    def arrow(x1, x2, y):
        return f'<line x1="{x1}" y1="{y}" x2="{x2 - 3}" y2="{y}" stroke="{t["accent"]}" stroke-width="1.5" marker-end="url(#arrow)"/>'

    col_src, col_core, col_cli = c["columns"]
    parts = [
        frame(t, W, h),
        f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{t["accent"]}"/></marker></defs>',
        caps(src_x, 36, col_src, t),
        caps(core_x, 36, col_core, t),
        caps(cli_x, 36, col_cli, t),
    ]
    for i, ((s_title, s_line), (c_title, c_line)) in enumerate(zip(c["sources"], c["clients"])):
        y = top + i * (box_h + gap)
        parts += [
            node(src_x, y, s_title, s_line), arrow(src_x + node_w, core_x, y + box_h / 2),
            node(cli_x, y, c_title, c_line), arrow(core_x + core_w, cli_x, y + box_h / 2),
        ]

    core_title, core_sub = c["core"]
    parts.append(
        f'<rect x="{core_x}" y="{top}" width="{core_w}" height="{span}" rx="6" fill="{t["card"]}" stroke="{t["accent"]}" stroke-width="1.5"/>'
        f'<text x="{core_x + 20}" y="{top + 32}" font-size="16" font-weight="600" fill="{t["text"]}">{core_title}</text>'
        f'<text x="{core_x + 20}" y="{top + 54}" font-size="13" fill="{t["text2"]}">{core_sub}</text>'
        f'<line x1="{core_x + 20}" y1="{top + 72}" x2="{core_x + core_w - 20}" y2="{top + 72}" stroke="{t["border"]}"/>'
    )
    for i, label in enumerate(c["modules"]):
        y = top + 98 + i * 26
        parts.append(
            f'<rect x="{core_x + 20}" y="{y - 9}" width="6" height="6" rx="1" fill="{t["accent"]}"/>'
            f'<text x="{core_x + 34}" y="{y}" font-size="13" fill="{t["text"]}">{label}</text>'
        )
    db_y = top + span - 40
    db_title, db_sub = c["db"]
    parts.append(
        f'<line x1="{core_x + 20}" y1="{db_y}" x2="{core_x + core_w - 20}" y2="{db_y}" stroke="{t["border"]}"/>'
        f'<text x="{core_x + 20}" y="{db_y + 26}" font-size="14" font-weight="600" fill="{t["text"]}">{db_title}</text>'
        f'<text x="{core_x + 128}" y="{db_y + 26}" font-size="13" fill="{t["text2"]}">{db_sub}</text>'
    )

    band_label, band_line1, band_line2 = c["delivery"]
    band_y = top + span + 28
    parts.append(
        f'<line x1="24" y1="{band_y}" x2="{W - 24}" y2="{band_y}" stroke="{t["border"]}"/>'
        + caps(24, band_y + 30, band_label, t)
        + f'<text x="134" y="{band_y + 30}" font-size="13" fill="{t["text"]}">{band_line1}</text>'
        f'<text x="134" y="{band_y + 52}" font-size="13" fill="{t["text2"]}">{band_line2}</text>'
    )
    return svg(h, "\n".join(parts), c["a11y"][3])


def lang_button(t, lang, active):
    """One half of the English | Español switcher."""
    w, h = 92, 30
    label = LANG_LABELS[lang]
    if active:
        shape = f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="15" fill="{t["accent"]}"/>'
        color = t["on_accent"]
    else:
        shape = f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="15" fill="none" stroke="{t["border"]}"/>'
        color = t["text"]
    body = f'{shape}<text x="{w / 2}" y="20" font-size="13" font-weight="600" fill="{color}" text-anchor="middle">{label}</text>'
    return svg(h, body, label, width=w)


GRAPHICS = {
    "header": header,
    "impact": impact,
    "case-metrics": case_metrics,
    "architecture": architecture,
}


def main():
    ASSETS.mkdir(exist_ok=True)
    count = 0
    for mode, theme in THEMES.items():
        for lang, copy in COPY.items():
            suffix = "" if lang == "en" else f"-{lang}"
            for name, build in GRAPHICS.items():
                (ASSETS / f"{name}{suffix}-{mode}.svg").write_text(build(theme, copy), encoding="utf-8")
                count += 1
            for active in (False, True):
                state = "-active" if active else ""
                (ASSETS / f"lang-{lang}{state}-{mode}.svg").write_text(
                    lang_button(theme, lang, active), encoding="utf-8")
                count += 1
    print(f"wrote {count} files to {ASSETS}")


if __name__ == "__main__":
    main()
