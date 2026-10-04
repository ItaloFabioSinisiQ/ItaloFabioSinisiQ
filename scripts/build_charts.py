"""Generate the SVG graphics used in the profile README.

Every graphic is written per language and per GitHub theme:
    assets/<name>-light.svg, assets/<name>-dark.svg        (English)
    assets/<name>-es-light.svg, assets/<name>-es-dark.svg  (Spanish)

The top bar buttons are written as:
    assets/lang-<en|es>[-active]-<light|dark>.svg and assets/theme-<light|dark>.svg

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
        "approach": ["Metric", "Design", "Build", "Test", "Ship", "Measure"],
        "journey": ("FROM DATA TO SOFTWARE", [
            ("2021 – 2022", "Admin Assistant", "Real estate · SQL, Power BI"),
            ("2022", "Financial Analyst", "Alfin Banco · credit risk"),
            ("2023 – 2024", "Data Analyst", "UBYCALL · analytics, BI"),
            ("2025 – PRESENT", "Full Stack Dev", "Auren · logistics, BI"),
        ]),
        "cv": ("Download CV", "PDF"),
        "lanes": ("END-TO-END FLOW · WHO DOES WHAT",
                  ["1 · Morning sync", "2 · On the route", "3 · At the stop", "4 · Validation", "5 · Close"],
                  ["ERP", "Backend", "Driver app", "Control tower", "Alerts"],
                  ["SQL Server", "FastAPI", "React Native", "React", "WhatsApp, email"],
                  {
                      (0, 0): ["Orders, invoices", "and promotions"],
                      (1, 0): ["06:00 sync, hourly", "retry until noon"],
                      (2, 0): ["Route and crew", "on each phone"],
                      (2, 1): ["Offline maps,", "encrypted queue"],
                      (3, 1): ["Live fleet map,", "route status"],
                      (2, 2): ["Delivered, partial", "or rejected", "photo · GPS · lines"],
                      (1, 3): ["Promotion engine,", "conflict check"],
                      (3, 3): ["Fraud signals,", "rejection follow-up"],
                      (4, 3): ["Over PEN 1,000", "left uncollected"],
                      (1, 4): ["Settlement per", "crew member"],
                      (3, 4): ["Office corrections,", "audit trail"],
                      (4, 4): ["Closing reports by", "email and WhatsApp"],
                  },
                  "syncs when signal returns", "GPS",
                  "Signal covers about 64% of the shift, so every field step works offline and syncs later."),
        "flow": ("A DAY ON THE ROUTE", [
            ("ERP sync", ["Orders, routes and", "promotions load", "at 06:00"]),
            ("Dispatch", ["Each crew gets", "its route on the", "driver app"]),
            ("Delivery", ["Delivered, partial", "or rejected, with", "photo and GPS"]),
            ("Validation", ["Promotions and", "amounts are", "recalculated"]),
            ("Settlement", ["Money owed per", "crew member and", "closing reports"]),
        ], "LIVE", "Fleet map · alerts for uncollected amounts over PEN 1,000 · stalled-route detection"),
        "engine": ("PROMOTION ENGINE · DECISION ORDER",
                   ("Free-goods line", "from the ERP invoice"),
                   [("Progressive", "N + M"), ("Tiered", "by range"), ("Combo", "all triggers"), ("Discount", "as free goods")],
                   ("Manual review", "never guessed"),
                   "no", "match",
                   "Promotion identified · bonus recalculated on partial rejection",
                   "Validated on 2,000 cases: 2,000 correct (previous method: about 4% errors)"),
        "a11y": ("Italo Fabio Sinisi Quintana, Full Stack Developer and Data Analyst",
                 "Selected results", "RutaLiquidador at a glance", "RutaLiquidador system architecture",
                 "How I work", "Career path", "A day on the route", "Promotion engine decision order",
                 "RutaLiquidador end-to-end flow by actor"),
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
            "Despliegues automatizados con backup, smoke test y rollback",
        ),
        "approach": ["Métrica", "Diseño", "Desarrollo", "Pruebas", "Despliegue", "Medición"],
        "journey": ("DE LOS DATOS AL SOFTWARE", [
            ("2021 – 2022", "Asistente Adm.", "Inmobiliaria · SQL, Power BI"),
            ("2022", "Analista Financiero", "Alfin Banco · riesgo"),
            ("2023 – 2024", "Analista de Datos", "UBYCALL · analítica, BI"),
            ("2025 – HOY", "Full Stack Dev", "Auren · logística, BI"),
        ]),
        "cv": ("Descargar CV", "PDF"),
        "lanes": ("FLUJO DE PUNTA A PUNTA · QUIÉN HACE QUÉ",
                  ["1 · Sync matutino", "2 · En ruta", "3 · En la parada", "4 · Validación", "5 · Cierre"],
                  ["ERP", "Backend", "App del chofer", "Torre de control", "Alertas"],
                  ["SQL Server", "FastAPI", "React Native", "React", "WhatsApp, correo"],
                  {
                      (0, 0): ["Pedidos, boletas", "y promociones"],
                      (1, 0): ["Sync a las 06:00 y", "reintentos por hora"],
                      (2, 0): ["Ruta y tripulación", "en cada celular"],
                      (2, 1): ["Mapas offline,", "cola cifrada"],
                      (3, 1): ["Flota en vivo,", "estado de rutas"],
                      (2, 2): ["Entregado, parcial", "o rechazado", "foto · GPS · líneas"],
                      (1, 3): ["Motor de promos,", "control de choques"],
                      (3, 3): ["Señales de fraude,", "seguimiento"],
                      (4, 3): ["Más de S/ 1,000", "sin cobrar"],
                      (1, 4): ["Liquidación por", "tripulante"],
                      (3, 4): ["Correcciones de", "oficina, auditoría"],
                      (4, 4): ["Reportes de cierre", "correo y WhatsApp"],
                  },
                  "sincroniza al volver la señal", "GPS",
                  "La señal cubre cerca del 64% del turno: cada paso en campo funciona offline y sincroniza después."),
        "flow": ("UN DÍA DE RUTA", [
            ("Sync del ERP", ["Pedidos, rutas y", "promociones a", "las 06:00"]),
            ("Despacho", ["Cada tripulación", "recibe su ruta", "en la app"]),
            ("Entrega", ["Entregado, parcial", "o rechazado, con", "foto y GPS"]),
            ("Validación", ["Se recalculan", "promociones", "y montos"]),
            ("Liquidación", ["Monto por", "tripulante y", "reportes de cierre"]),
        ], "EN VIVO", "Mapa de la flota · alertas por montos sin cobrar sobre S/ 1,000 · rutas detenidas"),
        "engine": ("MOTOR DE PROMOCIONES · ORDEN DE DECISIÓN",
                   ("Línea de regalo", "de la boleta del ERP"),
                   [("Progresiva", "N + M"), ("Por rango", "por escalas"), ("Combo", "combo completo"), ("Descuento", "como regalo")],
                   ("Revisión manual", "nunca se adivina"),
                   "no", "coincide",
                   "Promoción identificada · regalo recalculado ante rechazo parcial",
                   "Validado en 2,000 casos: 2,000 correctos (método anterior: alrededor de 4% de error)"),
        "a11y": ("Italo Fabio Sinisi Quintana, Desarrollador Full Stack y Analista de Datos",
                 "Resultados destacados", "RutaLiquidador en cifras", "Arquitectura de RutaLiquidador",
                 "Cómo trabajo", "Trayectoria", "Un día de ruta", "Orden de decisión del motor de promociones",
                 "Flujo de punta a punta de RutaLiquidador por actor"),
    },
}

LANG_LABELS = {"en": "English", "es": "Español"}


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
        return connector(t, f"M{x1},{y} H{x2 - 3}")

    col_src, col_core, col_cli = c["columns"]
    parts = [
        frame(t, W, h),
        arrow_marker(t),
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
    return svg(h, "\n".join(parts), c["a11y"][4])


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
    return svg(h, "\n".join(parts), c["a11y"][5])


def delivery_flow(t, c):
    caption, steps, live_label, live_text = c["flow"]
    h, node_w, gap, top, node_h = 232, 144, 28, 52, 108
    parts = [frame(t, W, h), arrow_marker(t), caps(24, 34, caption, t)]
    for i, (title, lines) in enumerate(steps):
        x = 24 + i * (node_w + gap)
        parts.append(
            f'<rect x="{x}" y="{top}" width="{node_w}" height="{node_h}" rx="6" fill="{t["card"]}" stroke="{t["border"]}"/>'
            f'<circle cx="{x + 24}" cy="{top + 26}" r="11" fill="{t["accent"]}"/>'
            f'<text x="{x + 24}" y="{top + 30.5}" font-size="12" font-weight="700" text-anchor="middle" fill="{t["on_accent"]}">{i + 1}</text>'
            f'<text x="{x + 42}" y="{top + 31}" font-size="14" font-weight="600" fill="{t["text"]}">{title}</text>'
        )
        for j, line in enumerate(lines):
            parts.append(f'<text x="{x + 14}" y="{top + 60 + j * 18}" font-size="13" fill="{t["text2"]}">{line}</text>')
        if i < len(steps) - 1:
            mid = top + node_h / 2
            parts.append(connector(t, f"M{x + node_w + 3},{mid} H{x + node_w + gap - 3}"))
    band_y = top + node_h + 24
    parts.append(
        f'<line x1="24" y1="{band_y}" x2="{W - 24}" y2="{band_y}" stroke="{t["border"]}"/>'
        f'<circle cx="30" cy="{band_y + 25}" r="4" fill="{t["accent"]}"/>'
        + caps(42, band_y + 29, live_label, t)
        + f'<text x="{42 + 14 + 9 * len(live_label)}" y="{band_y + 29}" font-size="13" fill="{t["text"]}">{live_text}</text>'
    )
    return svg(h, "\n".join(parts), c["a11y"][6])


def engine_flow(t, c):
    caption, source, checks, review, no_label, yes_label, result, footnote = c["engine"]
    h, top, node_h = 262, 52, 64
    src_x, src_w = 24, 150
    chk_x, chk_w, gap = 200, 106, 20
    rev_x = chk_x + 4 * chk_w + 3 * gap + 30
    rev_w = W - 24 - rev_x
    mid = top + node_h / 2
    parts = [frame(t, W, h), arrow_marker(t), caps(24, 34, caption, t)]

    def box(x, w, title, sub, stroke):
        return (
            f'<rect x="{x}" y="{top}" width="{w}" height="{node_h}" rx="10" fill="{t["card"]}" stroke="{stroke}"/>'
            f'<text x="{x + 14}" y="{top + 28}" font-size="14" font-weight="600" fill="{t["text"]}">{title}</text>'
            f'<text x="{x + 14}" y="{top + 48}" font-size="12" fill="{t["text2"]}">{sub}</text>'
        )

    parts.append(box(src_x, src_w, *source, t["border"]))
    parts.append(connector(t, f"M{src_x + src_w + 3},{mid} H{chk_x - 3}"))
    result_y = top + node_h + 46
    for i, (title, sub) in enumerate(checks):
        x = chk_x + i * (chk_w + gap)
        parts.append(box(x, chk_w, title, sub, t["accent"]))
        nxt = rev_x if i == len(checks) - 1 else x + chk_w + gap
        parts.append(connector(t, f"M{x + chk_w + 3},{mid} H{nxt - 3}"))
        cx = x + chk_w / 2
        parts.append(connector(t, f"M{cx},{top + node_h + 3} V{result_y - 3}"))
    last_x = chk_x + 3 * (chk_w + gap) + chk_w
    parts.append(f'<text x="{(last_x + rev_x) / 2}" y="{mid - 8}" font-size="12" fill="{t["text2"]}" text-anchor="middle">{no_label}</text>')
    parts.append(f'<text x="{chk_x + chk_w / 2 + 8}" y="{top + node_h + 26}" font-size="12" fill="{t["text2"]}">{yes_label}</text>')
    parts.append(box(rev_x, rev_w, *review, t["border"]))

    res_w = 4 * chk_w + 3 * gap
    parts.append(
        f'<rect x="{chk_x}" y="{result_y}" width="{res_w}" height="44" rx="10" fill="{t["accent"]}" fill-opacity="0.12" stroke="{t["accent"]}"/>'
        f'<text x="{chk_x + res_w / 2}" y="{result_y + 27}" font-size="13" font-weight="600" fill="{t["text"]}" text-anchor="middle">{result}</text>'
        f'<text x="24" y="{h - 20}" font-size="13" fill="{t["text2"]}">{footnote}</text>'
    )
    return svg(h, "\n".join(parts), c["a11y"][7])


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


def swimlane(t, c):
    """Detailed flow: one lane per actor, one column per stage of the day."""
    caption, stages, lanes, techs, nodes, sync_label, gps_label, footnote = c["lanes"]
    label_w, grid_x = 112, 140
    col_w = (W - 24 - grid_x) / len(stages)
    node_w, node_h = col_w - 14, 60
    head_y, lane_y, lane_h = 58, 74, 84
    h = lane_y + lane_h * len(lanes) + 52

    def box(lane, col):
        x = grid_x + col * col_w + 7
        y = lane_y + lane * lane_h + (lane_h - node_h) / 2
        return x, y

    parts = [frame(t, W, h), arrow_marker(t), caps(24, 34, caption, t)]
    for col, name in enumerate(stages):
        cx = grid_x + col * col_w + col_w / 2
        parts.append(f'<text x="{cx:.1f}" y="{head_y}" font-size="12" font-weight="600" fill="{t["text2"]}" text-anchor="middle">{name}</text>')
    for i, (lane, tech) in enumerate(zip(lanes, techs)):
        y = lane_y + i * lane_h
        if i % 2 == 0:
            parts.append(f'<rect x="12" y="{y}" width="{W - 24}" height="{lane_h}" rx="4" fill="{t["card"]}" fill-opacity="0.7"/>')
        parts.append(
            f'<text x="24" y="{y + lane_h / 2 - 2}" font-size="13" font-weight="600" fill="{t["text"]}">{lane}</text>'
            f'<text x="24" y="{y + lane_h / 2 + 16}" font-size="12" fill="{t["text2"]}">{tech}</text>'
        )
    parts.append(f'<line x1="{grid_x - 6}" y1="{lane_y}" x2="{grid_x - 6}" y2="{lane_y + lane_h * len(lanes)}" stroke="{t["border"]}"/>')

    def right(k):
        x, y = box(*k)
        return x + node_w, y + node_h / 2

    def left(k):
        x, y = box(*k)
        return x, y + node_h / 2

    def top(k):
        x, y = box(*k)
        return x + node_w / 2, y

    def bottom(k):
        x, y = box(*k)
        return x + node_w / 2, y + node_h

    links = []
    for a, b in [((0, 0), (1, 0)), ((1, 0), (2, 0)), ((2, 1), (3, 1)), ((1, 3), (3, 3)), ((3, 3), (4, 3)),
                 ((1, 4), (3, 4)), ((3, 4), (4, 4))]:
        (x1, y1), (x2, y2) = bottom(a), top(b)
        links.append(connector(t, f"M{x1:.1f},{y1 + 3:.1f} V{y2 - 3:.1f}"))
    for a, b in [((2, 0), (2, 1)), ((2, 1), (2, 2)), ((1, 3), (1, 4))]:
        (x1, y1), (x2, y2) = right(a), left(b)
        links.append(connector(t, f"M{x1 + 3:.1f},{y1:.1f} H{x2 - 3:.1f}"))
    (x1, y1), (x2, y2) = top((2, 2)), left((1, 3))
    links.append(connector(t, f"M{x1:.1f},{y1 - 3:.1f} C{x1:.1f},{y2:.1f} {x1:.1f},{y2:.1f} {x2 - 3:.1f},{y2:.1f}"))
    gx, gy = bottom((2, 1))

    for (lane, col), lines in nodes.items():
        x, y = box(lane, col)
        hero = (lane, col) == (2, 2)
        parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{node_w:.1f}" height="{node_h}" rx="6" '
            f'fill="{t["card"]}" stroke="{t["accent"] if hero else t["border"]}" stroke-width="{1.5 if hero else 1}"/>'
        )
        first = y + (node_h - 15 * (len(lines) - 1)) / 2 + 4
        for j, line in enumerate(lines):
            weight = ' font-weight="600"' if j == 0 else ""
            color = t["text"] if j == 0 else t["text2"]
            parts.append(f'<text x="{x + 10:.1f}" y="{first + j * 15:.1f}" font-size="12"{weight} fill="{color}">{line}</text>')
    parts.extend(links)
    parts.append(f'<text x="{gx + 6:.1f}" y="{gy + 16:.1f}" font-size="12" fill="{t["text2"]}">{gps_label}</text>')
    sx, sy = left((1, 3))
    parts.append(f'<text x="{sx - 12:.1f}" y="{sy - 12:.1f}" font-size="12" fill="{t["accent"]}" text-anchor="end">{sync_label}</text>')
    parts.append(f'<text x="24" y="{h - 20}" font-size="13" fill="{t["text2"]}">{footnote}</text>')
    return svg(h, "\n".join(parts), c["a11y"][8])


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
    title = "Light theme" if mode == "light" else "Dark theme"
    return svg(size, frame_ + icon, title, width=size)


def spanish_panel(t):
    """Full-width bar used as the summary of the collapsible Spanish version."""
    w, h = 840, 64
    cx, cy = w - 40, h / 2
    body = (
        f'<rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="8" fill="{t["panel"]}" stroke="{t["accent"]}" stroke-width="1.5"/>'
        f'<rect x="20" y="17" width="40" height="30" rx="15" fill="{t["accent"]}"/>'
        f'<text x="40" y="37" font-size="13" font-weight="700" fill="{t["on_accent"]}" text-anchor="middle">ES</text>'
        f'<text x="76" y="29" font-size="16" font-weight="600" fill="{t["text"]}">Versión en español</text>'
        f'<text x="76" y="48" font-size="13" fill="{t["text2"]}">Haz clic para ver el perfil completo en español</text>'
        f'<path d="M{cx - 7},{cy - 3} L{cx},{cy + 4} L{cx + 7},{cy - 3}" fill="none" stroke="{t["accent"]}" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    return svg(h, body, "Versión en español", width=w)


GRAPHICS = {
    "header": header,
    "impact": impact,
    "case-metrics": case_metrics,
    "architecture": architecture,
    "approach": approach,
    "journey": journey,
    "delivery-flow": delivery_flow,
    "engine-flow": engine_flow,
    "cv-button": cv_button,
    "swimlane": swimlane,
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
        (ASSETS / f"theme-{mode}.svg").write_text(theme_button(theme, mode), encoding="utf-8")
        (ASSETS / f"spanish-panel-{mode}.svg").write_text(spanish_panel(theme), encoding="utf-8")
        count += 2
    print(f"wrote {count} files to {ASSETS}")


if __name__ == "__main__":
    main()
