"""Book cover (1600 x 2560) in the book's blueprint style. Writes figures/cover.svg; render.sh-style Edge call renders cover.png."""
import io, os, math

W, H = 1600, 2560
INK, ACC, PAPER, GRID = "#14202b", "#eb6834", "#f6f3ec", "#dfe6ee"
TITLE_FONT = "Georgia, 'Times New Roman', serif"

s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{TITLE_FONT}">',
     '<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">'
     f'<path d="M40,0 H0 V40" fill="none" stroke="{GRID}" stroke-width="1.2"/></pattern>'
     '<pattern id="G" width="200" height="200" patternUnits="userSpaceOnUse">'
     f'<path d="M200,0 H0 V200" fill="none" stroke="#cfd8e3" stroke-width="2"/></pattern></defs>',
     f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
     f'<rect width="{W}" height="{H}" fill="url(#g)"/><rect width="{W}" height="{H}" fill="url(#G)"/>']

# faint staircase of layers in the background (the Jump)
for i in range(6):
    x = 180 + i * 190
    y = 2050 - i * 150
    s.append(f'<rect x="{x}" y="{y}" width="{1600 - x - 120}" height="150" fill="none" stroke="#b9c5d3" stroke-width="3" stroke-dasharray="14 10"/>')

# the control loop, drawn large and faint, around the middle
cx, cy, r = 800, 1480, 470
s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#c4cfdb" stroke-width="5"/>')
for ang in (30, 210):
    a = math.radians(ang)
    x, y = cx + r * math.cos(a), cy + r * math.sin(a)
    s.append(f'<path d="M{x-22},{y-14} L{x+10},{y} L{x-22},{y+14} Z" fill="#c4cfdb" transform="rotate({ang+90} {x} {y})"/>')

# regulator box with model inside, and the work box
s.append(f'<rect x="330" y="1330" width="360" height="300" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>')
s.append(f'<rect x="400" y="1440" width="220" height="130" fill="#fbe3d6" stroke="{ACC}" stroke-width="6"/>')
s.append(f'<text x="510" y="1400" font-size="44" text-anchor="middle" fill="{INK}" font-weight="bold">REGULATOR</text>')
s.append(f'<text x="510" y="1520" font-size="40" text-anchor="middle" fill="{INK}" font-style="italic">model</text>')
s.append(f'<rect x="910" y="1330" width="360" height="300" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>')
s.append(f'<text x="1090" y="1495" font-size="44" text-anchor="middle" fill="{INK}" font-weight="bold">THE WORK</text>')
s.append(f'<line x1="690" y1="1390" x2="890" y2="1390" stroke="{INK}" stroke-width="10"/><path d="M880,1370 L912,1390 L880,1410 Z" fill="{INK}"/>')
s.append(f'<line x1="910" y1="1570" x2="712" y2="1570" stroke="{INK}" stroke-width="4" stroke-dasharray="16 12"/><path d="M722,1555 L692,1570 L722,1585 Z" fill="{INK}"/>')
s.append(f'<text x="800" y="1370" font-size="34" text-anchor="middle" fill="{INK}" font-style="italic">acts</text>')
s.append(f'<text x="800" y="1620" font-size="34" text-anchor="middle" fill="{INK}" font-style="italic">feedback?</text>')

# the andon cord — the one bright thing on the cover
s.append(f'<line x1="1330" y1="0" x2="1330" y2="1180" stroke="{ACC}" stroke-width="16" stroke-linecap="round"/>')
s.append(f'<rect x="1300" y="1170" width="60" height="110" rx="26" fill="{ACC}"/>')

# a small stick figure reaching for it
fx, fy = 1180, 1300
s.append(f'<g fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round">'
         f'<circle cx="{fx}" cy="{fy-190}" r="34"/><line x1="{fx}" y1="{fy-156}" x2="{fx}" y2="{fy-60}"/>'
         f'<line x1="{fx}" y1="{fy-60}" x2="{fx-38}" y2="{fy+20}"/><line x1="{fx}" y1="{fy-60}" x2="{fx+38}" y2="{fy+20}"/>'
         f'<line x1="{fx}" y1="{fy-130}" x2="{fx+108}" y2="{fy-200}"/><line x1="{fx}" y1="{fy-130}" x2="{fx-50}" y2="{fy-90}"/></g>')

# title block
s.append(f'<text x="120" y="330" font-size="190" fill="{INK}" font-weight="bold" letter-spacing="-4">Every Good</text>')
s.append(f'<text x="120" y="530" font-size="190" fill="{INK}" font-weight="bold" letter-spacing="-4">Regulator</text>')
s.append(f'<rect x="120" y="590" width="220" height="14" fill="{ACC}"/>')
s.append(f'<text x="120" y="700" font-size="58" fill="{INK}" font-style="italic">Why the systems that run our work fail —</text>')
s.append(f'<text x="120" y="780" font-size="58" fill="{INK}" font-style="italic">and how to build ones that don\'t</text>')

# five words band
words = ["MODEL", "LEGIBILITY", "REMAINDER", "STOP", "JUMP"]
s.append(f'<text x="800" y="2330" font-size="46" text-anchor="middle" fill="{INK}" letter-spacing="10">{" · ".join(words)}</text>')
s.append(f'<text x="800" y="2450" font-size="78" text-anchor="middle" fill="{INK}">Muhammad Hammad Shakeel</text>')
s.append('</svg>')

here = os.path.dirname(os.path.abspath(__file__))
io.open(os.path.join(here, "cover.svg"), "w", encoding="utf-8", newline="").write("\n".join(s))
print("wrote cover.svg")
