"""Generate the SVG graphics used in the profile README.

Every graphic is written in Spanish, once per GitHub theme:
    assets/<name>-light.svg, assets/<name>-dark.svg

The theme button in the top bar is written as assets/theme-<light|dark>.svg

Graphics are drawn at 880 px, the width of the README column on a GitHub
profile, so SVG font sizes match rendered pixels (minimum 12 px).

Run:  python3 scripts/build_charts.py
"""
import base64
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"
# Square portrait embedded in the header (SVGs shown as images cannot load
# external files, so the photo is inlined as base64).
PHOTO = ASSETS / "profile-photo.jpg"
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
    "es": {
        "title": "Desarrollador Full Stack y Analista de Datos",
        "tagline": "Plataformas de logística, ventas y BI en producción",
        "facts": [
            ("EXPERIENCIA", "5+ años · software y datos"),
            ("UBICACIÓN", "Lima, Perú (GMT-5) · remoto"),
            ("CARGO ACTUAL", "Full Stack Developer · BI"),
        ],
        "impact": [
            ("Rechazo de pedidos", "7% → 1%", "RutaLiquidador · logística"),
            ("Conversión de ventas", "+15%", "Analítica predictiva · UBYCALL"),
            ("Pérdidas por impago", "−18%", "Scoring · Alfin Banco"),
            ("Reportes automatizados", "80%", "Python y SQL · UBYCALL"),
        ],
        "approach": ["Métrica", "Diseño", "Desarrollo", "Pruebas", "Despliegue", "Medición"],
        "journey": ("DE LOS DATOS AL SOFTWARE", [
            ("2021 – 2022", "Asistente Adm.", "Inmobiliaria · SQL, Power BI"),
            ("2022", "Analista Financiero", "Alfin Banco · riesgo"),
            ("2023 – 2024", "Analista de Datos", "UBYCALL · analítica, BI"),
            ("2025 – HOY", "Full Stack Dev", "Consumo masivo · logística, BI"),
        ]),
        "cv": ("Descargar CV", "PDF"),
        "a11y": ("Italo Fabio Sinisi Quintana, Desarrollador Full Stack y Analista de Datos",
                 "Resultados destacados", "Cómo trabajo", "Trayectoria"),
    },
}

# Connectors marked class="flow" show a slow moving dash, disabled for
# viewers who prefer reduced motion.
FLOW_STYLE = (
    "<style>.flow{stroke-dasharray:5 5;animation:flow 1.4s linear infinite}"
    "@keyframes flow{to{stroke-dashoffset:-20}}"
    "@media (prefers-reduced-motion:reduce){.flow{animation:none;stroke-dasharray:none}}</style>"
)


def svg(height, body, title, width=W):
    style = FLOW_STYLE if 'class="flow"' in body else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}" '
        f'font-family="{SANS}">\n<title>{title}</title>\n{style}{body}\n</svg>\n'
    )


def arrow_marker(t):
    return (
        f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{t["accent"]}"/></marker></defs>'
    )


def connector(t, d):
    return (
        f'<path d="{d}" fill="none" stroke="{t["accent"]}" stroke-width="1.5" '
        f'class="flow" marker-end="url(#arrow)"/>'
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
    photo = base64.b64encode(PHOTO.read_bytes()).decode()
    cx, cy, r = 100, h / 2, 62
    facts = "".join(
        caps(652, 52 + i * 52, label, t)
        + f'<text x="652" y="{73 + i * 52}" font-size="14" fill="{t["text"]}">{value}</text>'
        for i, (label, value) in enumerate(c["facts"])
    )
    body = f"""<defs>
<clipPath id="card"><rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="6"/></clipPath>
<clipPath id="avatar"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
</defs>
{frame(t, W, h)}
<rect x="0" y="0" width="5" height="{h}" fill="{t["accent"]}" clip-path="url(#card)"/>
<image href="data:image/jpeg;base64,{photo}" x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" clip-path="url(#avatar)" preserveAspectRatio="xMidYMid slice"/>
<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="{t["accent"]}" stroke-width="2"/>
<text x="190" y="82" font-family="{SERIF}" font-size="33" fill="{t["text"]}">Italo Fabio Sinisi Quintana</text>
<rect x="190" y="98" width="44" height="3" rx="1.5" fill="{t["accent"]}"/>
<text x="190" y="134" font-size="18" font-weight="600" fill="{t["text"]}">{c["title"]}</text>
<text x="190" y="160" font-size="14" fill="{t["text2"]}">{c["tagline"]}</text>
<line x1="630" y1="32" x2="630" y2="{h - 32}" stroke="{t["border"]}"/>
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


def approach(t, c):
    steps = c["approach"]
    h, pill_w, pill_h, gap, x0, y0 = 104, 118, 38, 24, 26, 20
    parts = [arrow_marker(t)]
    for i, label in enumerate(steps):
        x = x0 + i * (pill_w + gap)
        last = i == len(steps) - 1
        parts.append(
            f'<rect x="{x}" y="{y0}" width="{pill_w}" height="{pill_h}" rx="{pill_h / 2}" '
            f'fill="{t["accent"] if last else t["panel"]}" stroke="{t["accent"] if last else t["border"]}"/>'
            f'<text x="{x + pill_w / 2}" y="{y0 + 24}" font-size="14" font-weight="600" text-anchor="middle" '
            f'fill="{t["on_accent"] if last else t["text"]}">{label}</text>'
        )
        if not last:
            parts.append(connector(t, f"M{x + pill_w + 3},{y0 + pill_h / 2} H{x + pill_w + gap - 3}"))
    first_c = x0 + pill_w / 2
    last_c = x0 + (len(steps) - 1) * (pill_w + gap) + pill_w / 2
    bottom = y0 + pill_h
    parts.append(connector(
        t, f"M{last_c},{bottom + 4} C{last_c},{bottom + 42} {first_c},{bottom + 42} {first_c},{bottom + 7}"))
    return svg(h, "\n".join(parts), c["a11y"][2])


def journey(t, c):
    caption, stages = c["journey"]
    h, gap, top, node_h = 150, 24, 46, 88
    node_w = (W - 48 - gap * (len(stages) - 1)) / len(stages)
    parts = [arrow_marker(t), caps(24, 26, caption, t)]
    for i, (period, role, place) in enumerate(stages):
        x = 24 + i * (node_w + gap)
        current = i == len(stages) - 1
        parts.append(
            f'<rect x="{x}" y="{top}" width="{node_w}" height="{node_h}" rx="6" fill="{t["panel"]}" '
            f'stroke="{t["accent"] if current else t["border"]}" stroke-width="{1.5 if current else 1}"/>'
            + caps(x + 16, top + 26, period, t)
            + f'<text x="{x + 16}" y="{top + 52}" font-size="15" font-weight="600" fill="{t["text"]}">{role}</text>'
            f'<text x="{x + 16}" y="{top + 74}" font-size="13" fill="{t["text2"]}">{place}</text>'
        )
        if not current:
            mid = top + node_h / 2
            parts.append(connector(t, f"M{x + node_w + 3},{mid} H{x + node_w + gap - 3}"))
    return svg(h, "\n".join(parts), c["a11y"][3])


def cv_button(t, c):
    """Compact outlined pill with a download icon, sized to sit in the top bar."""
    label, _ = c["cv"]
    h = 30
    w = 46 + round(len(label) * 7.6)
    ix, iy = 17, h / 2
    icon = (
        f'<path d="M{ix},{iy - 6} V{iy + 2} M{ix - 3.5},{iy - 1.5} L{ix},{iy + 2} L{ix + 3.5},{iy - 1.5} '
        f'M{ix - 5.5},{iy + 6} H{ix + 5.5}" fill="none" stroke="{t["accent"]}" stroke-width="1.7" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    body = (
        f'<rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="{h / 2}" fill="none" '
        f'stroke="{t["accent"]}" stroke-width="1.5"/>{icon}'
        f'<text x="31" y="20" font-size="13" font-weight="600" fill="{t["accent"]}">{label}</text>'
    )
    return svg(h, body, label, width=w)


def theme_button(t, mode):
    """Round button showing the current theme: a sun in light mode, a moon in dark mode."""
    size, c = 30, 15
    frame_ = f'<circle cx="{c}" cy="{c}" r="{c - 0.75}" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>'
    if mode == "light":
        rays = "".join(
            f'<line x1="{c}" y1="{c - 9}" x2="{c}" y2="{c - 7}" transform="rotate({a} {c} {c})"/>'
            for a in range(0, 360, 45)
        )
        icon = (
            f'<circle cx="{c}" cy="{c}" r="4" fill="none" stroke="{t["text"]}" stroke-width="1.6"/>'
            f'<g stroke="{t["text"]}" stroke-width="1.6" stroke-linecap="round">{rays}</g>'
        )
    else:
        icon = (
            f'<path d="M{c + 2.5},{c - 7.5} A7.5,7.5 0 1 0 {c + 7.5},{c + 2.5} A6,6 0 0 1 {c + 2.5},{c - 7.5} Z" '
            f'fill="none" stroke="{t["text"]}" stroke-width="1.6" stroke-linejoin="round"/>'
        )
    title = "Tema claro" if mode == "light" else "Tema oscuro"
    return svg(size, frame_ + icon, title, width=size)


GRAPHICS = {
    "header": header,
    "impact": impact,
    "approach": approach,
    "journey": journey,
    "cv-button": cv_button,
}


def main():
    ASSETS.mkdir(exist_ok=True)
    count = 0
    copy = COPY["es"]
    for mode, theme in THEMES.items():
        for name, build in GRAPHICS.items():
            (ASSETS / f"{name}-{mode}.svg").write_text(build(theme, copy), encoding="utf-8")
            count += 1
        (ASSETS / f"theme-{mode}.svg").write_text(theme_button(theme, mode), encoding="utf-8")
        count += 1
    print(f"wrote {count} files to {ASSETS}")


if __name__ == "__main__":
    main()
