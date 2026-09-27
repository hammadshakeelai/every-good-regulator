"""Tiny stick-figure comic library for *Every Good Regulator*.

Cast: PAT (messy hair), DEE (bob haircut, lanyard), UNIT 7 (boxy robot, antenna).
Everything is plain SVG so an illustrator can redraw over it later.
"""
import html

INK = "#1a1a1a"
GREY = "#8a8984"
LIGHT = "#e4e3df"
ACCENT = "#eb6834"
GREEN = "#6aa86a"
PAPER = "#fffefb"
FONT = "'Segoe Print', 'Comic Sans MS', cursive"
SERIF = "Georgia, serif"

PW, PH, GAP, M = 390, 290, 14, 16   # panel width/height, gap, margin


def esc(t):
    return html.escape(t, quote=False)


def wrap(text, width_chars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= width_chars:
            cur = (cur + " " + w) if cur else w
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------- text ----------
def bubble(x, y, text, w=170, tail=None, fs=12.5, italic_words=(), shout=False):
    """Speech bubble with top-left at (x, y). tail = (tx, ty) point the tail aims at."""
    cw = fs * 0.62
    lines = wrap(text, max(6, int((w - 16) / cw)))
    lh = fs * 1.35
    h = len(lines) * lh + 14
    out = []
    if tail:
        tx, ty = tail
        bx = min(max(tx, x + 18), x + w - 18)
        by = y + h
        dx, dy = tx - bx, ty - by
        d = (dx * dx + dy * dy) ** 0.5
        if d > 34:
            tx, ty = bx + dx * 34 / d, by + dy * 34 / d
        out.append(f'<path d="M{bx-8},{y+h-2} L{tx},{ty} L{bx+8},{y+h-2}" fill="#ffffff" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"/>')
    stroke = ACCENT if shout else INK
    out.insert(0, "")
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="14" fill="#ffffff" stroke="{stroke}" stroke-width="1.5"/>')
    if tail:  # cover the tail's join
        out.append(f'<line x1="{bx-7}" y1="{y+h-1.5:.1f}" x2="{bx+7}" y2="{y+h-1.5:.1f}" stroke="#ffffff" stroke-width="3"/>')
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x + w/2}" y="{y + 9 + fs + i*lh:.1f}" font-size="{fs}" text-anchor="middle" font-family="{FONT}" fill="{INK}">{esc(ln)}</text>')
    return "\n".join(out)


def label(x, y, text, fs=11, anchor="middle", color=INK, italic=False, bold=False, font=None):
    st = ' font-style="italic"' if italic else ""
    wt = ' font-weight="bold"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{fs}" text-anchor="{anchor}" font-family="{font or FONT}" fill="{color}"{st}{wt}>{esc(text)}</text>'


def cap_box(text, w=PW):
    """Small caption box in the panel's top-left corner (e.g. '9:07 AM')."""
    cw = len(text) * 7.2 + 16
    return (f'<rect x="6" y="6" width="{cw:.0f}" height="22" fill="#fff6c9" stroke="{INK}" stroke-width="1.2"/>'
            + label(6 + cw / 2, 21.5, text, fs=11.5))


# ---------- people ----------
def _face(x, hy, mood, look=0):
    ex = x + look
    eyes = f'<circle cx="{ex-4}" cy="{hy-1}" r="1.4" fill="{INK}"/><circle cx="{ex+4}" cy="{hy-1}" r="1.4" fill="{INK}"/>'
    if mood == "sleep":
        eyes = f'<path d="M{ex-6},{hy-1} q2,2 4,0 M{ex+2},{hy-1} q2,2 4,0" stroke="{INK}" fill="none" stroke-width="1.2"/>'
    if mood == "crossed":
        eyes = (f'<path d="M{ex-6},{hy-3} l4,4 m0,-4 l-4,4 M{ex+2},{hy-3} l4,4 m0,-4 l-4,4" stroke="{INK}" stroke-width="1.1"/>')
    if mood == "wide":
        eyes = f'<circle cx="{ex-4}" cy="{hy-1}" r="2.4" fill="none" stroke="{INK}"/><circle cx="{ex+4}" cy="{hy-1}" r="2.4" fill="none" stroke="{INK}"/><circle cx="{ex-4}" cy="{hy-1}" r="0.9" fill="{INK}"/><circle cx="{ex+4}" cy="{hy-1}" r="0.9" fill="{INK}"/>'
    mouths = {
        "smile": f'M{ex-4},{hy+4} q4,4 8,0',
        "grin": f'M{ex-5},{hy+3} q5,6 10,0 z',
        "neutral": f'M{ex-3},{hy+5} h6',
        "worried": f'M{ex-4},{hy+6} q4,-3 8,0',
        "sleep": f'M{ex-2},{hy+5} h4',
        "crossed": f'M{ex-3},{hy+5} q3,-2 6,0',
        "wide": f'M{ex-2},{hy+5} a2,2 0 1 0 4,0 a2,2 0 1 0 -4,0',
        "open": f'M{ex-3},{hy+4} q3,5 6,0 z',
    }
    return eyes + f'<path d="{mouths.get(mood, mouths["neutral"])}" stroke="{INK}" fill="none" stroke-width="1.3" stroke-linecap="round"/>'


def _arms(x, sy, arms):
    """sy = shoulder y. arms = (left, right) each one of: down, out, up, point, reach, hold, type, hip, raise."""
    shapes = {
        "down": (10, 22), "out": (24, 6), "up": (14, -26), "point": (30, -4),
        "reach": (20, -30), "hold": (16, 12), "type": (22, 16), "raise": (8, -30),
    }
    out = []
    for side, a in ((-1, arms[0]), (1, arms[1])):
        if a == "hip":
            out.append(f'<path d="M{x},{sy} L{x+side*12},{sy+10} L{x+side*4},{sy+18}" fill="none" stroke="{INK}" stroke-width="2"/>')
            continue
        if isinstance(a, tuple):          # absolute (dx, dy), not mirrored
            ex, ey = x + a[0], sy + a[1]
        else:
            dx, dy = shapes.get(a, shapes["down"])
            ex, ey = x + side * dx, sy + dy
        out.append(f'<line x1="{x}" y1="{sy}" x2="{ex}" y2="{ey}" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    return "".join(out)


def person(x, y, who="pat", mood="neutral", arms=("down", "down"), look=0, sitting=False, facing=1, scale=1.3, extra=""):
    """Stick figure with feet at (x, y). who: pat | dee | extra. Sitting figures face `facing` (1 right, -1 left)."""
    s = []
    hip = y - 24 if not sitting else y - 30
    hy = hip - 38 if not sitting else hip - 40
    s.append(f'<circle cx="{x}" cy="{hy}" r="11" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    if who == "pat":
        s.append(f'<path d="M{x-9},{hy-6} l-3,-6 l6,3 l2,-7 l4,6 l3,-7 l2,7 l5,-4 l-1,7" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>')
    elif who == "dee":
        s.append(f'<path d="M{x-12},{hy+4} C {x-14},{hy-16} {x+14},{hy-16} {x+12},{hy+4} L{x+9},{hy+4} C {x+9},{hy-8} {x-9},{hy-8} {x-9},{hy+4} Z" fill="{INK}"/>')
    elif who == "extra":
        s.append(f'<path d="M{x-10},{hy-4} q10,-10 20,0" fill="none" stroke="{INK}" stroke-width="2"/>')
    s.append(_face(x, hy, mood, look))
    s.append(f'<line x1="{x}" y1="{hy+11}" x2="{x}" y2="{hip}" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    if who == "dee":
        s.append(f'<path d="M{x-4},{hy+13} L{x},{hy+24} L{x+4},{hy+13}" fill="none" stroke="{ACCENT}" stroke-width="1.3"/><rect x="{x-3}" y="{hy+24}" width="6" height="8" fill="{ACCENT}"/>')
    s.append(_arms(x, hy + 20, arms))
    if sitting:
        f = facing
        s.append(f'<path d="M{x},{hip} L{x+f*20},{hip} L{x+f*20},{y}" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
        s.append(f'<path d="M{x},{hip} L{x+f*17},{hip+3} L{x+f*15},{y}" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/>')
    else:
        s.append(f'<path d="M{x-8},{y} L{x},{hip} L{x+8},{y}" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(extra)
    g = "".join(s)
    if scale != 1.0:
        g = f'<g transform="translate({x},{y}) scale({scale}) translate({-x},{-y})">{g}</g>'
    return g


def chair(x, y, facing=1, scale=1.3):
    """Office chair under a sitting person whose feet are at (x, y); seat at hip height."""
    f = facing
    g = (f'<line x1="{x-f*8}" y1="{y-30}" x2="{x+f*18}" y2="{y-30}" stroke="{INK}" stroke-width="3"/>'
         f'<line x1="{x-f*8}" y1="{y-30}" x2="{x-f*10}" y2="{y-66}" stroke="{INK}" stroke-width="3"/>'
         f'<line x1="{x+f*5}" y1="{y-30}" x2="{x+f*5}" y2="{y-8}" stroke="{INK}" stroke-width="2.2"/>'
         f'<path d="M{x-f*8},{y-2} L{x+f*5},{y-8} L{x+f*18},{y-2}" fill="none" stroke="{INK}" stroke-width="2"/>'
         f'<circle cx="{x-f*8}" cy="{y}" r="2" fill="{INK}"/><circle cx="{x+f*18}" cy="{y}" r="2" fill="{INK}"/>')
    return f'<g transform="translate({x},{y}) scale({scale}) translate({-x},{-y})">{g}</g>'


def unit7(x, y, mood="smile", arms=("down", "down"), scale=1.3, extra=""):
    """Boxy robot, feet (treads) at (x, y)."""
    s = [
        f'<rect x="{x-16}" y="{y-10}" width="32" height="10" rx="5" fill="{LIGHT}" stroke="{INK}" stroke-width="1.8"/>',
        f'<rect x="{x-15}" y="{y-44}" width="30" height="34" rx="3" fill="#ffffff" stroke="{INK}" stroke-width="2"/>',
        f'<rect x="{x-7}" y="{y-36}" width="14" height="9" fill="{ACCENT}" opacity="0.8"/>',
        label(x, y - 15, "7", fs=9, font=SERIF),
        f'<rect x="{x-14}" y="{y-70}" width="28" height="24" rx="4" fill="#ffffff" stroke="{INK}" stroke-width="2"/>',
        f'<line x1="{x}" y1="{y-70}" x2="{x}" y2="{y-80}" stroke="{INK}" stroke-width="1.8"/><circle cx="{x}" cy="{y-82}" r="3" fill="{ACCENT}"/>',
    ]
    hy = y - 58
    if mood == "smile":
        s.append(f'<rect x="{x-8}" y="{hy-4}" width="4" height="4" fill="{INK}"/><rect x="{x+4}" y="{hy-4}" width="4" height="4" fill="{INK}"/><path d="M{x-6},{hy+4} q6,5 12,0" stroke="{INK}" fill="none" stroke-width="1.6"/>')
    elif mood == "grin":
        s.append(f'<path d="M{x-9},{hy-1} l3,-3 l3,3 M{x+3},{hy-1} l3,-3 l3,3" stroke="{INK}" fill="none" stroke-width="1.6"/><path d="M{x-7},{hy+3} h14 q-7,7 -14,0 z" fill="{INK}"/>')
    else:
        s.append(f'<rect x="{x-8}" y="{hy-4}" width="4" height="4" fill="{INK}"/><rect x="{x+4}" y="{hy-4}" width="4" height="4" fill="{INK}"/><path d="M{x-5},{hy+5} h10" stroke="{INK}" stroke-width="1.6"/>')
    ax = {"down": (6, 22), "up": (10, -24), "out": (22, 0), "hold": (14, 10), "raise": (6, -26)}
    for side, a in ((-1, arms[0]), (1, arms[1])):
        dx, dy = ax.get(a, ax["down"])
        sx = x + side * 15
        s.append(f'<line x1="{sx}" y1="{y-36}" x2="{sx + side*dx}" y2="{y-36+dy}" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    s.append(extra)
    g = "".join(s)
    if scale != 1.0:
        g = f'<g transform="translate({x},{y}) scale({scale}) translate({-x},{-y})">{g}</g>'
    return g


# ---------- props ----------
def floor(y=270, x1=0, x2=PW):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{INK}" stroke-width="1.5"/>'


def desk(x, y, w=120):
    return (f'<line x1="{x}" y1="{y}" x2="{x+w}" y2="{y}" stroke="{INK}" stroke-width="2.5"/>'
            f'<line x1="{x+8}" y1="{y}" x2="{x+8}" y2="{y+40}" stroke="{INK}" stroke-width="2"/>'
            f'<line x1="{x+w-8}" y1="{y}" x2="{x+w-8}" y2="{y+40}" stroke="{INK}" stroke-width="2"/>')


def laptop(x, y, lines=(), fill="#ffffff", w=60, h=40, fs=8):
    """Laptop sitting on a surface at y; screen above, x = left."""
    s = [f'<rect x="{x}" y="{y-h-4}" width="{w}" height="{h}" rx="2" fill="{fill}" stroke="{INK}" stroke-width="1.8"/>',
         f'<path d="M{x-6},{y} L{x+w+6},{y} L{x+w},{y-4} L{x},{y-4} Z" fill="{LIGHT}" stroke="{INK}" stroke-width="1.5"/>']
    for i, ln in enumerate(lines):
        s.append(label(x + 4, y - h + 6 + i * (fs + 3), ln, fs=fs, anchor="start", font="Consolas, monospace"))
    return "".join(s)


def screen(x, y, w, h, fill="#ffffff", lines=(), fs=11, stand=True, color=INK, bold=False):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{INK}" stroke-width="2"/>']
    if stand:
        s.append(f'<line x1="{x+w/2}" y1="{y+h}" x2="{x+w/2}" y2="{y+h+14}" stroke="{INK}" stroke-width="2"/><line x1="{x+w/2-14}" y1="{y+h+14}" x2="{x+w/2+14}" y2="{y+h+14}" stroke="{INK}" stroke-width="2"/>')
    lh = fs * 1.3
    top = y + h / 2 - (len(lines) - 1) * lh / 2 + fs / 3
    for i, ln in enumerate(lines):
        s.append(label(x + w / 2, top + i * lh, ln, fs=fs, color=color, bold=bold, font=SERIF))
    return "".join(s)


def green_board(x, y, w, h, cols=5, rows=3, red=None):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#ffffff" stroke="{INK}" stroke-width="2"/>']
    tw, th = (w - 8) / cols, (h - 8) / rows
    for r in range(rows):
        for c in range(cols):
            col = GREEN
            if red and (r, c) == red:
                col = ACCENT
            s.append(f'<rect x="{x+4+c*tw+2:.1f}" y="{y+4+r*th+2:.1f}" width="{tw-4:.1f}" height="{th-4:.1f}" rx="2" fill="{col}"/>')
    return "".join(s)


def zzz(x, y):
    return (label(x, y, "z", fs=13, color=GREY) + label(x + 9, y - 12, "z", fs=16, color=GREY))


def sweat(x, y):
    return f'<path d="M{x},{y} q-4,7 0,9 q4,-2 0,-9 z" fill="#8ec5e8" stroke="{INK}" stroke-width="0.8"/>'


def sticky(x, y, text="", color="#fff09a", w=34, fs=8, rot=0):
    return (f'<g transform="rotate({rot} {x+w/2} {y+w/2})"><rect x="{x}" y="{y}" width="{w}" height="{w}" fill="{color}" stroke="{INK}" stroke-width="1"/>'
            + label(x + w / 2, y + w / 2 + 3, text, fs=fs) + '</g>')


def clock(x, y, r=14, h=6, m=0):
    import math
    ha = math.radians((h % 12) * 30 - 90)
    ma = math.radians(m * 6 - 90)
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" stroke="{INK}" stroke-width="1.8"/>'
            f'<line x1="{x}" y1="{y}" x2="{x + r*0.5*math.cos(ha):.1f}" y2="{y + r*0.5*math.sin(ha):.1f}" stroke="{INK}" stroke-width="2"/>'
            f'<line x1="{x}" y1="{y}" x2="{x + r*0.8*math.cos(ma):.1f}" y2="{y + r*0.8*math.sin(ma):.1f}" stroke="{INK}" stroke-width="1.3"/>')


# ---------- strip assembly ----------
DEFS = f'''<defs>
<filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="1.8"/></filter>
</defs>'''


def panel(gx, gy, content, w=PW, h=PH, bg="#ffffff"):
    return (f'<g transform="translate({gx},{gy})">'
            f'<clipPath id="c{gx}_{gy}"><rect width="{w}" height="{h}"/></clipPath>'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>'
            f'<g clip-path="url(#c{gx}_{gy})"><g filter="url(#rough)">{content}</g></g>'
            f'<rect width="{w}" height="{h}" fill="none" stroke="{INK}" stroke-width="2.5"/></g>')


def strip(number, title, panels, caption=None, layout="grid", pw=PW, ph=PH, desc=""):
    """panels: list of SVG content strings (or (content, bg) tuples). layout: grid (2x2) | row."""
    n = len(panels)
    if layout == "row":
        cols, rows = n, 1
    else:
        cols, rows = 2, (n + 1) // 2
    W = M * 2 + cols * pw + (cols - 1) * GAP
    cap_lines = wrap(caption, int((W - 2 * M) / 7.0)) if caption else []
    H = M * 2 + rows * ph + (rows - 1) * GAP + (len(cap_lines) * 18 + 10 if cap_lines else 0) + 16
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" aria-labelledby="t d">',
           f'<title id="t">Comic {number} — {esc(title)}</title><desc id="d">{esc(desc or title)}</desc>', DEFS,
           f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    for i, p in enumerate(panels):
        bg = "#ffffff"
        if isinstance(p, tuple):
            p, bg = p
        c, r = (i, 0) if layout == "row" else (i % cols, i // cols)
        out.append(panel(M + c * (pw + GAP), M + r * (ph + GAP), p, pw, ph, bg))
    y = M + rows * ph + (rows - 1) * GAP + 24
    for i, ln in enumerate(cap_lines):
        out.append(label(W / 2, y + i * 18, ln, fs=13, italic=True, font=SERIF))
    out.append(label(W - M, H - 8, f"Comic {number}", fs=9, anchor="end", color=GREY, font=SERIF))
    out.append("</svg>")
    return "\n".join(out)
