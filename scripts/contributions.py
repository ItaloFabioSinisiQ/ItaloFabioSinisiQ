"""Render the GitHub contribution calendar as themed SVGs for the profile README.

GitHub's own calendar cannot be placed above the README, so this script draws
one in the same terminal-window style as the other graphics:
    assets/contributions-dark.svg, assets/contributions-light.svg

Online (used by .github/workflows/contributions.yml):
    GITHUB_TOKEN=... LOGIN=<user> python3 scripts/contributions.py

Offline, from a saved GraphQL response:
    python3 scripts/contributions.py --from-json calendar.json

Standard library only. The output depends only on the calendar data, so an
unchanged calendar produces byte-identical files.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://api.github.com/graphql"
QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount contributionLevel } }
      }
    }
  }
}
"""

MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
WINDOW_DOTS = ("#ff5f57", "#febc2e", "#28c840")
THEMES = {
    "dark": {
        "bg": "#0d1117", "panel": "#151b23", "border": "#3d444d", "text": "#e6edf3",
        "muted": "#9198a1", "green": "#3fb950", "orange": "#ffa657",
        "scale": ("#1c232c", "#0e4429", "#006d32", "#26a641", "#39d353"),
    },
    "light": {
        "bg": "#ffffff", "panel": "#f6f8fa", "border": "#d1d9e0", "text": "#1f2328",
        "muted": "#59636e", "green": "#1a7f37", "orange": "#bc4c00",
        "scale": ("#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"),
    },
}
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2,
          "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
MONTHS = ("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic")
# GitHub weeks start on Sunday; label alternate rows like the native calendar.
DAY_LABELS = {1: "lun", 3: "mié", 5: "vie"}

WIDTH, BAR = 880, 36
MAX_WEEKS = 53
CELL, GAP = 12, 3
STEP = CELL + GAP
GRID_X, GRID_Y = 62, 144

STYLE = (
    ".w{animation:reveal .45s ease-out both}"
    "@keyframes reveal{from{opacity:0;transform:translateY(5px)}}"
    "@media (prefers-reduced-motion:reduce){.w{animation:none}}"
)


class CalendarError(Exception):
    """The calendar could not be fetched or has an unexpected shape."""


def fetch(login, token):
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    request = urllib.request.Request(API_URL, data=body, headers={
        "Authorization": f"bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "profile-contributions-graph",
    })
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as err:
        raise CalendarError(f"la API de GitHub respondió HTTP {err.code} {err.reason}") from None
    except (urllib.error.URLError, TimeoutError) as err:
        raise CalendarError(f"no se pudo conectar con la API de GitHub: {err}") from None
    except json.JSONDecodeError:
        raise CalendarError("la API de GitHub devolvió una respuesta que no es JSON") from None


def extract_calendar(payload):
    """Return the contributionCalendar object from a GraphQL response."""
    if not isinstance(payload, dict):
        raise CalendarError("el JSON no es una respuesta GraphQL")
    if payload.get("errors"):
        messages = "; ".join(
            str(e.get("message", e)) if isinstance(e, dict) else str(e) for e in payload["errors"])
        raise CalendarError(f"la API de GitHub devolvió errores: {messages}")
    try:
        user = payload["data"]["user"]
        if user is None:
            raise CalendarError("el usuario no existe o no es visible con este token")
        calendar = user["contributionsCollection"]["contributionCalendar"]
        weeks = calendar["weeks"][-MAX_WEEKS:]
        days = [d for w in weeks for d in w["contributionDays"]]
        for day in days:
            int(day["contributionCount"])
            str(day["date"])[5:7]
        if not days:
            raise CalendarError("el calendario no contiene días")
        return {"total": int(calendar["totalContributions"]), "weeks": weeks, "days": days}
    except (KeyError, TypeError, ValueError):
        raise CalendarError("la respuesta no tiene la forma esperada de contributionCalendar") from None


def streaks(days):
    """Return (current, longest) streaks in days.

    A day without contributions breaks a streak, except the last day of the
    calendar: it may simply not be over yet.
    """
    longest = run = 0
    for day in days:
        run = run + 1 if day["contributionCount"] > 0 else 0
        longest = max(longest, run)
    tail = days[:-1] if days[-1]["contributionCount"] == 0 else days
    current = 0
    for day in reversed(tail):
        if day["contributionCount"] == 0:
            break
        current += 1
    return current, longest


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def plural(n, singular, plural_form):
    return f"{n} {singular if n == 1 else plural_form}"


def format_count(n):
    # Spanish thousands separator.
    return f"{n:,}".replace(",", ".")


def month_labels(weeks):
    """Yield (week index, month name) where a new month starts."""
    labels, previous, last_index = [], None, -10
    for i, week in enumerate(weeks):
        month = int(week["contributionDays"][0]["date"][5:7])
        if month != previous:
            # A label too close to the one before it replaces it: the earlier
            # one belongs to a partial month at the left edge.
            if labels and i - last_index < 3:
                labels.pop()
            labels.append((i, MONTHS[month - 1]))
            last_index = i
            previous = month
    return labels


def render(calendar, c):
    weeks, days, total = calendar["weeks"], calendar["days"], calendar["total"]
    current, longest = streaks(days)
    height = GRID_Y + 7 * STEP - GAP + 54
    total_text = plural(total, "contribución", "contribuciones").split(" ", 1)[1]
    label = (f"Contribuciones en GitHub: {format_count(total)} {total_text} en el último año. "
             f"Racha actual: {plural(current, 'día', 'días')}. "
             f"Racha más larga: {plural(longest, 'día', 'días')}.")
    w, h = WIDTH, height
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{esc(label)}" font-family="{SANS}">',
        f"<title>{esc(label)}</title>",
        f"<style>{STYLE}</style>",
        f'<defs><clipPath id="win"><rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10"/></clipPath></defs>',
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="{c["bg"]}"/>',
        f'<rect x="0" y="0" width="{w}" height="{BAR}" fill="{c["panel"]}" clip-path="url(#win)"/>',
        f'<line x1="0.5" y1="{BAR+0.5}" x2="{w-0.5}" y2="{BAR+0.5}" stroke="{c["border"]}"/>',
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="none" stroke="{c["border"]}"/>',
    ]
    for i, colour in enumerate(WINDOW_DOTS):
        out.append(f'<circle cx="{22 + i*20}" cy="{BAR//2}" r="6" fill="{colour}"/>')
    out.append(f'<text x="{w//2}" y="{BAR//2 + 4.5}" text-anchor="middle" font-family="{MONO}" '
               f'font-size="12.5" fill="{c["muted"]}">{esc("git log --since=" + chr(34) + "1 year ago" + chr(34))}</text>')

    # Headline: big number on the left, streaks on the right.
    number = format_count(total)
    out.append(f'<text x="28" y="92" font-size="34" font-weight="700" fill="{c["green"]}">{number}'
               f'<tspan dx="10" font-size="15" font-weight="400" fill="{c["text"]}">'
               f'{total_text} en el último año</tspan></text>')
    right = w - 28
    out.append(f'<text x="{right}" y="76" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{c["muted"]}">'
               f'racha actual: <tspan fill="{c["text"]}" font-weight="700">{plural(current, "día", "días")}</tspan></text>')
    out.append(f'<text x="{right}" y="96" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{c["muted"]}">'
               f'racha más larga: <tspan fill="{c["text"]}" font-weight="700">{plural(longest, "día", "días")}</tspan></text>')

    # Axis labels.
    for i, name in month_labels(weeks):
        out.append(f'<text x="{GRID_X + i*STEP}" y="{GRID_Y - 10}" font-family="{MONO}" font-size="11.5" '
                   f'fill="{c["muted"]}">{name}</text>')
    for row, name in DAY_LABELS.items():
        out.append(f'<text x="28" y="{GRID_Y + row*STEP + 10}" font-family="{MONO}" font-size="11.5" '
                   f'fill="{c["muted"]}">{name}</text>')

    # Heatmap: one group per week so columns can fade in one after another.
    for i, week in enumerate(weeks):
        x = GRID_X + i * STEP
        cells = []
        for day in week["contributionDays"]:
            # The date gives the row, so partial first/last weeks stay aligned.
            row = weekday_row(day["date"])
            count = int(day["contributionCount"])
            level = LEVELS.get(day.get("contributionLevel"), 1 if count else 0)
            cells.append(f'<rect x="{x}" y="{GRID_Y + row*STEP}" width="{CELL}" height="{CELL}" rx="2.5" '
                         f'fill="{c["scale"][level]}"/>')
        out.append(f'<g class="w" style="animation-delay:{i*18}ms">{"".join(cells)}</g>')

    # Scale legend.
    ly = GRID_Y + 7 * STEP - GAP + 18
    lx = GRID_X + (len(weeks) - 1) * STEP + CELL  # right edge of the grid
    out.append(f'<text x="{lx}" y="{ly + 10}" text-anchor="end" font-family="{MONO}" font-size="11.5" '
               f'fill="{c["muted"]}">más</text>')
    sx = lx - 32 - 5 * STEP
    for level, colour in enumerate(c["scale"]):
        out.append(f'<rect x="{sx + level*STEP}" y="{ly}" width="{CELL}" height="{CELL}" rx="2.5" fill="{colour}"/>')
    out.append(f'<text x="{sx - 8}" y="{ly + 10}" text-anchor="end" font-family="{MONO}" font-size="11.5" '
               f'fill="{c["muted"]}">menos</text>')
    out.append("</svg>\n")
    return "\n".join(out)


def weekday_row(date):
    """Row of an ISO date in a Sunday-first week (Sunday = 0)."""
    year, month, day = (int(part) for part in date.split("-"))
    # Sakamoto's algorithm: no datetime import needed, Sunday = 0.
    offsets = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if month < 3:
        year -= 1
    return (year + year // 4 - year // 100 + year // 400 + offsets[month - 1] + day) % 7


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--from-json", metavar="FILE",
                        help="render from a saved GraphQL response instead of calling the API")
    parser.add_argument("--out", metavar="DIR", type=Path,
                        default=Path(__file__).resolve().parent.parent / "assets",
                        help="output directory (default: assets/ next to scripts/)")
    args = parser.parse_args()

    try:
        if args.from_json:
            try:
                payload = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as err:
                raise CalendarError(f"no se pudo leer {args.from_json}: {err}") from None
        else:
            token = os.environ.get("GITHUB_TOKEN", "").strip()
            login = os.environ.get("LOGIN", "").strip()
            if not token or not login:
                raise CalendarError("faltan las variables de entorno GITHUB_TOKEN y LOGIN "
                                    "(o use --from-json FILE)")
            payload = fetch(login, token)
        calendar = extract_calendar(payload)
    except CalendarError as err:
        print(f"contributions.py: error: {err}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    for theme, colours in THEMES.items():
        path = args.out / f"contributions-{theme}.svg"
        path.write_text(render(calendar, colours), encoding="utf-8")
        print(f"escrito {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
