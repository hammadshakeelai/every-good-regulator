"""The four Exploded View spreads (one per Part), in the blueprint style of the figures.
Run from manuscript/figures:  python exploded.py   -> ev-1..4 SVGs (renamed fig-ev-*.svg so render.sh picks them up)
"""
import io, os, sys, html
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comics"))
from comiclib import person, unit7

INK, GREY, LIGHT, ACC, PAPER = "#0b0b0b", "#52514e", "#e4e3df", "#eb6834", "#fcfcfb"
W, H = 1200, 820


def t(x, y, s, fs=13, anchor="start", color=INK, bold=False, italic=False):
    b = ' font-weight="bold"' if bold else ""
    i = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{fs}" text-anchor="{anchor}" fill="{color}"{b}{i}>{html.escape(s)}</text>'


def lead(x1, y1, x2, y2, lines, anchor=None, color=INK, hot=False):
    """Dashed leader from a feature (x1,y1) to a label at (x2,y2). Label sits away from the line."""
    if anchor is None:
        anchor = "end" if x2 < x1 else "start"
    c = ACC if hot else GREY
    out = [f'<circle cx="{x1}" cy="{y1}" r="3" fill="{c}"/>',
           f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{c}" stroke-width="1.2" stroke-dasharray="4 3" fill="none"/>']
    dy = 0
    for k, ln in enumerate(lines):
        out.append(t(x2 + (6 if anchor == "start" else -6), y2 + 4 + dy, ln, fs=12.5 if k == 0 else 11,
                     anchor=anchor, color=(ACC if hot and k == 0 else (INK if k == 0 else GREY)), bold=(k == 0), italic=(k > 0)))
        dy += 15
    return "".join(out)


def frame(title, sub, body, n):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Georgia, serif" role="img" aria-labelledby="t">'
            f'<title id="t">Exploded View {n} — {html.escape(title)}</title>'
            '<defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20,0 H0 V20" fill="none" stroke="#e9eef5" stroke-width="1"/></pattern>'
            f'<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<marker id="aa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker></defs>'
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/><rect width="{W}" height="{H}" fill="url(#g)"/>'
            f'<rect x="10" y="10" width="{W-20}" height="{H-20}" fill="none" stroke="{INK}" stroke-width="1.5"/>'
            + t(30, 50, f"EXPLODED VIEW {n}", fs=13, color=ACC, bold=True) + t(30, 80, title, fs=26, bold=True) + t(30, 104, sub, fs=14, color=GREY, italic=True)
            + body + "</svg>")


def desk(x, y, w=60):
    return f'<line x1="{x}" y1="{y}" x2="{x+w}" y2="{y}" stroke="{INK}" stroke-width="2"/><line x1="{x+5}" y1="{y}" x2="{x+5}" y2="{y+26}" stroke="{INK}"/><line x1="{x+w-5}" y1="{y}" x2="{x+w-5}" y2="{y+26}" stroke="{INK}"/>'


def board(x, y, w, h, red=None):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>']
    cols, rows = 6, 3
    tw, th = (w - 6) / cols, (h - 6) / rows
    for r in range(rows):
        for c in range(cols):
            col = ACC if red == (r, c) else "#6aa86a"
            s.append(f'<rect x="{x+3+c*tw+1:.1f}" y="{y+3+r*th+1:.1f}" width="{tw-2:.1f}" height="{th-2:.1f}" fill="{col}"/>')
    return "".join(s)


def sticky(x, y, r=0, c="#fff09a"):
    return f'<rect x="{x}" y="{y}" width="14" height="14" fill="{c}" stroke="{INK}" stroke-width="0.8" transform="rotate({r} {x+7} {y+7})"/>'


def fig(x, y, who="extra", mood="neutral", arms=("down", "down"), s=0.62, sitting=False):
    return person(x, y, who, mood, arms, sitting=sitting, scale=s)


# =====================================================================  1. The company as a metasystem
def ev1():
    b = []
    GY = 730
    b.append(f'<line x1="30" y1="{GY}" x2="1170" y2="{GY}" stroke="{INK}" stroke-width="2"/>')
    # background forest in rows (ch1)
    for i, x in enumerate(range(40, 150, 22)):
        b.append(f'<polygon points="{x},{GY-40} {x-8},{GY-6} {x+8},{GY-6}" fill="#ffffff" stroke="{GREY}"/><line x1="{x}" y1="{GY-6}" x2="{x}" y2="{GY}" stroke="{GREY}"/>')
    b.append(lead(90, GY - 40, 36, 610, ["The forest (ch. 1)", "what the ledger sees"], anchor="start"))
    # building
    X1, X2 = 240, 900
    floors = [(640, GY, "BASEMENT"), (520, 640, "THE WORK"), (420, 520, "COORDINATION"), (320, 420, "DASHBOARDS"), (270, 320, "POLICY")]
    for top, bot, name in floors:
        b.append(f'<rect x="{X1}" y="{top}" width="{X2-X1}" height="{bot-top}" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
        b.append(t(X1 + 30, top + 16, name, fs=10, color=GREY, bold=True))
    # basement: the remainder
    b.append(f'<rect x="{X1+2}" y="642" width="{X2-X1-4}" height="{GY-644}" fill="#f1efe9"/>')
    b.append(t(X1 + 30, 658, "BASEMENT", fs=10, color=GREY, bold=True))
    for x in (330, 420, 520):
        b.append(f'<rect x="{x}" y="690" width="44" height="30" fill="#e4e3df" stroke="{INK}"/>')
    b.append(fig(640, GY, "pat", "worried", ((10, 14), (-10, 14))))
    b.append(lead(640, 690, 1000, 690, ["The remainder (ch. 10)", "the hard part nobody automated;", "one person keeps the skill alive"], hot=True))
    # work floor
    for i, x in enumerate((300, 400, 500, 600, 700, 800)):
        b.append(desk(x - 30, 612, 56) + fig(x - 40, 638, "extra" if i % 3 else "pat", "neutral", ((14, 8), (16, 6)), sitting=True))
    for x, y, r in ((300, 540, -6), (318, 548, 8), (560, 536, 4), (740, 544, -8), (756, 538, 10)):
        b.append(sticky(x, y, r))
    b.append(lead(318, 548, 1000, 560, ["Metis (ch. 1)", "sticky notes, workarounds,", "the thing from Tuesday"]))
    # backchannel pipes (load-bearing work) running inside the wall
    b.append(f'<path d="M{X2-18},630 V300" stroke="{ACC}" stroke-width="4" stroke-dasharray="10 6" fill="none"/>')
    b.append(f'<path d="M{X2-30},630 V330 H{X2-60}" stroke="{GREY}" stroke-width="3" fill="none"/>')
    b.append(lead(X2 - 18, 470, 1000, 470, ["The backchannel (Comic 1.1)", "load-bearing work behind", "the wall, on no board"], hot=True))
    # coordination floor: meeting room with many chairs, clock, thermostat next to a lamp
    b.append(f'<rect x="300" y="450" width="220" height="60" fill="#fbfaf6" stroke="{INK}"/>')
    for x in range(312, 510, 22):
        b.append(f'<rect x="{x}" y="490" width="12" height="12" fill="#ffffff" stroke="{INK}"/>')
    b.append(t(410, 470, "meeting about meetings", fs=10, anchor="middle", color=GREY, italic=True))
    b.append(lead(410, 450, 228, 400, ["System 2: coordination (ch. 4)", "necessary, until it isn't (ch. 14)"]))
    # thermostat + lamp joke
    b.append(f'<rect x="640" y="445" width="20" height="20" rx="4" fill="#ffffff" stroke="{INK}"/><path d="M644,458 q6,4 12,0" stroke="{INK}" fill="none"/>')
    b.append(f'<line x1="690" y1="518" x2="690" y2="470" stroke="{INK}" stroke-width="2"/><path d="M676,470 h28 l-7,-12 h-14 z" fill="{LIGHT}" stroke="{INK}"/><path d="M676,470 L660,518 H720 L704,470 Z" fill="#ffe27a" opacity="0.5"/>')
    b.append(lead(650, 445, 1000, 395, ["A thermostat next to a lamp", "an excellent model of the lamp (ch. 2)"]))
    # dashboard floor
    b.append(board(330, 340, 200, 70))
    b.append(fig(580, 418, "dee", "grin", ("down", (-30, -26))))
    b.append(lead(430, 340, 228, 300, ["The dashboard (ch. 2)", "a model of the work,", "not the work. All green."]))
    # policy / roof: documents = the model
    for i in range(5):
        b.append(f'<rect x="{430+i*6}" y="{280-i*4}" width="90" height="30" fill="#ffffff" stroke="{INK}"/>')
    b.append(t(480, 300, "THE MODEL", fs=10, anchor="middle", bold=True))
    b.append(lead(490, 266, 228, 200, ["The model (ch. 2)", "what the building thinks", "the work looks like"]))
    b.append(t(560, 300, "5 · identity", fs=11, bold=True) + t(560, 314, "\"who we are\"", fs=10, color=GREY, italic=True))
    # System 4 antenna, empty chair
    b.append(f'<line x1="780" y1="270" x2="780" y2="200" stroke="{INK}" stroke-width="2"/><path d="M760,200 q20,-30 40,0" fill="none" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<path d="M800,196 C 880,170 960,160 1060,150" stroke="{ACC}" stroke-dasharray="3 6" fill="none" marker-end="url(#aa)"/>')
    b.append(f'<path d="M820,300 v-18 h14 M822,300 h12 v12 M834,300 v12" stroke="{INK}" fill="none" stroke-width="1.5"/>')
    b.append(lead(828, 286, 1000, 250, ["System 4: the future (ch. 4)", "antenna up; chair empty"], hot=True))
    # environment
    for x, y in ((1060, 150), (1110, 180)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="40" ry="18" fill="#ffffff" stroke="{GREY}"/>')
    b.append(t(1085, 112, "the market, customers,", fs=11, anchor="middle", color=GREY, italic=True) + t(1085, 126, "next year", fs=11, anchor="middle", color=GREY, italic=True))
    # andon cord with cobweb on the outside wall
    b.append(f'<line x1="{X1+14}" y1="270" x2="{X1+14}" y2="600" stroke="#d9362b" stroke-width="3"/><circle cx="{X1+14}" cy="604" r="5" fill="#d9362b"/>')
    b.append(f'<path d="M{X1+2},272 l20,0 M{X1+2},272 l0,20 M{X1+2},272 l16,16 M{X1+8},272 q0,8 -6,8" stroke="{GREY}" fill="none" stroke-width="0.8"/>')
    b.append(lead(X1 + 14, 560, 228, 520, ["The cord (ch. 12)", "within reach; never pulled;", "note the cobweb"], hot=True))
    # layer being added on the roof (jump)
    b.append(f'<rect x="480" y="236" width="150" height="34" fill="none" stroke="{GREY}" stroke-dasharray="5 4"/>' + t(555, 257, "new layer (planned)", fs=10, anchor="middle", color=GREY, italic=True))
    b.append(lead(560, 236, 540, 170, ["The next jump (ch. 3)", "a layer to govern the layers"]))
    return frame("The company as a metasystem", "Part One in one drawing: the layer you can't see, cut open.", "".join(b), 1)


# =====================================================================  2. The ALIS loop
def ev2():
    b = []
    GY = 740
    b.append(f'<line x1="30" y1="{GY}" x2="1170" y2="{GY}" stroke="{INK}" stroke-width="2"/>')
    # hangar
    b.append(f'<path d="M60,{GY} V430 Q 300,300 540,430 V{GY}" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    b.append(t(300, 400, "HANGAR", fs=11, anchor="middle", color=GREY, bold=True))
    # aircraft (simple jet)
    jet = (f'<path d="M140,600 L420,600 L470,585 L420,570 L300,570 L260,520 L235,520 L250,570 L160,570 L140,545 L122,545 L130,580 Z" fill="#dfe6ee" stroke="{INK}" stroke-width="2"/>'
           f'<path d="M300,600 L330,640 L352,640 L340,600" fill="#dfe6ee" stroke="{INK}" stroke-width="1.5"/>')
    b.append(jet + f'<circle cx="300" cy="612" r="4" fill="{INK}"/><line x1="300" y1="604" x2="300" y2="{GY-8}" stroke="{INK}"/><circle cx="300" cy="{GY-6}" r="6" fill="{INK}"/>')
    b.append(f'<rect x="170" y="648" width="120" height="26" fill="#fff1ea" stroke="#b3261e"/>' + t(230, 666, "NOT FIT TO FLY", fs=11, anchor="middle", color="#b3261e", bold=True))
    b.append(lead(230, 674, 250, 772, ["Grounded by a record, not a fault", "the part is fitted; the record says it isn't (ch. 6)"], anchor="start", hot=True))
    b.append(fig(460, GY, "pat", "worried", ((-16, -6), (10, 16))) + f'<rect x="474" y="{GY-78}" width="16" height="20" fill="#ffffff" stroke="{INK}"/>')
    b.append(lead(476, GY - 88, 540, 470, ["The maintainer", "sees the truth; holds metis"]))
    # system tower (the regulator)
    b.append(f'<rect x="740" y="170" width="240" height="220" fill="#ffffff" stroke="{INK}" stroke-width="2"/>' + t(850, 196, "THE LOGISTICS SYSTEM", fs=11, anchor="middle", bold=True))
    b.append(f'<rect x="790" y="220" width="140" height="70" fill="#ece9e1" stroke="{GREY}"/>')
    for k in range(4):
        b.append(f'<line x1="800" y1="{236+k*14}" x2="{920 - k*18}" y2="{236+k*14}" stroke="#b7b4ad" stroke-width="3"/>')
    b.append(t(860, 310, "parts records", fs=11, anchor="middle", color=GREY, italic=True))
    b.append(lead(860, 290, 1004, 300, ["The model, going stale", "records incorrect, corrupt,", "missing (GAO)"], hot=True))
    # thick 'acts' arrow from system to aircraft
    b.append(f'<path d="M760,300 C 620,330 520,420 440,560" fill="none" stroke="{INK}" stroke-width="7"/><path d="M430,548 L436,576 L456,558 Z" fill="{INK}"/>')
    b.append(t(860, 412, "ACTS: grounds, orders, schedules", fs=12, anchor="middle", bold=True))
    # feedback path: action request box with fee meter and queue
    b.append(f'<rect x="600" y="600" width="90" height="100" fill="#ffffff" stroke="{INK}" stroke-width="2"/>' + t(645, 622, "ACTION", fs=10, anchor="middle", bold=True) + t(645, 634, "REQUESTS", fs=10, anchor="middle", bold=True))
    b.append(f'<rect x="615" y="570" width="60" height="22" fill="#ffffff" stroke="{INK}"/>' + t(645, 586, "fee", fs=11, anchor="middle", color=ACC, bold=True))
    b.append(f'<path d="M500,660 H598" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/>')
    b.append(lead(690, 600, 700, 704, ["A fee per report (ch. 6)", "paid by the programme"], hot=True))
    # queue of envelopes up to the tower
    for k in range(9):
        x, y = 700 + k * 30, 660 - k * 26
        b.append(f'<g transform="translate({x},{y})"><rect width="20" height="14" fill="#ffffff" stroke="{GREY}"/><path d="M0,0 L10,7 L20,0" fill="none" stroke="{GREY}"/></g>')
    b.append(lead(850, 530, 1000, 540, ["The queue", "months per request; at one site,", "aircraft grounded while it waited"]))
    # the spreadsheet everyone trusts
    b.append(f'<rect x="980" y="620" width="160" height="96" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    for k in range(1, 6):
        b.append(f'<line x1="980" y1="{620+k*16}" x2="1140" y2="{620+k*16}" stroke="#c9c8c3"/>')
    for k in range(1, 4):
        b.append(f'<line x1="{980+k*40}" y1="620" x2="{980+k*40}" y2="716" stroke="#c9c8c3"/>')
    b.append(t(1060, 612, "REAL RECORDS (DO NOT DELETE)", fs=10, anchor="middle", bold=True))
    b.append(f'<path d="M510,700 C 700,760 880,740 976,690" stroke="{ACC}" stroke-dasharray="6 4" fill="none" marker-end="url(#aa)"/>')
    b.append(lead(1060, 716, 1150, 772, ["The spreadsheet everyone actually trusts", "where feedback goes when the official loop is blocked"], anchor="end", hot=True))
    # compliance badge on tower
    b.append(f'<circle cx="990" cy="176" r="22" fill="#6aa86a" stroke="{INK}"/>' + t(990, 172, "100%", fs=10, anchor="middle", color="#ffffff", bold=True) + t(990, 184, "compliant", fs=7, anchor="middle", color="#ffffff"))
    b.append(lead(975, 164, 900, 62, ["Compliant (ch. 5)", "the governed write their own evidence"]))
    # cord missing: an empty hook
    b.append(f'<path d="M100,440 v24 q0,8 8,8 q8,0 8,-8" fill="none" stroke="{GREY}" stroke-width="2"/>' + t(108, 490, "(no cord)", fs=10, anchor="middle", color=GREY, italic=True))
    b.append(lead(108, 452, 140, 300, ["Where a cord would hang", "nobody here may stop the system (ch. 12)"], anchor="start"))
    return frame("A loop that acts but cannot hear", "Part Two in one drawing: the F-35 logistics loop, and where each failure of Part Two lives in it.", "".join(b), 2)


# =====================================================================  3. The software factory
def ev3():
    b = []
    GY = 740
    b.append(f'<line x1="30" y1="{GY}" x2="1170" y2="{GY}" stroke="{INK}" stroke-width="2"/>')
    # hopper: specs in
    b.append(f'<path d="M90,200 L230,200 L190,280 L130,280 Z" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    for k in range(4):
        b.append(f'<rect x="{104+k*28}" y="{170-k*6}" width="24" height="30" fill="#ffffff" stroke="{INK}" transform="rotate({k*7-10} {116+k*28} {185})"/>')
    b.append(lead(160, 170, 262, 136, ["Specifications in (ch. 11)", "what — and, if you're wise, why"]))
    # conveyor
    b.append(f'<rect x="160" y="420" width="760" height="20" fill="{LIGHT}" stroke="{INK}" stroke-width="2"/>')
    for x in range(180, 920, 40):
        b.append(f'<circle cx="{x}" cy="430" r="7" fill="#ffffff" stroke="{INK}"/>')
    b.append(f'<path d="M160,280 V420" stroke="{INK}" stroke-width="2" marker-end="url(#ah)"/>')
    # agents along conveyor
    for x in (260, 400, 540, 680):
        b.append(unit7(x, 418, "smile", ("hold", "hold"), scale=0.9))
    b.append(lead(690, 336, 706, 128, ["Agents that write, test and ship (ch. 3)", "tireless; confident; never say \"I don't know\""]))
    # boxes of code on conveyor
    for x in (330, 470, 610, 760, 840):
        b.append(f'<rect x="{x}" y="398" width="24" height="20" fill="#eef5ff" stroke="{INK}"/>' + t(x + 12, 412, "{ }", fs=9, anchor="middle"))
    # vault with holdout scenarios
    b.append(f'<rect x="980" y="170" width="160" height="150" rx="6" fill="#e4e3df" stroke="{INK}" stroke-width="2"/><circle cx="1060" cy="245" r="30" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
             f'<line x1="1060" y1="215" x2="1060" y2="275" stroke="{INK}"/><line x1="1030" y1="245" x2="1090" y2="245" stroke="{INK}"/>')
    b.append(t(1060, 160, "HOLDOUT SCENARIOS", fs=11, anchor="middle", bold=True))
    b.append(lead(1000, 320, 1150, 370, ["Locked where the agents can't see (ch. 11)", "checkable; blind to the unwritten"], anchor="end"))
    b.append(f'<path d="M920,430 C 980,430 1040,380 1060,322" stroke="{GREY}" fill="none" stroke-dasharray="4 4" marker-end="url(#ah)"/>')
    # review desk with sleeping human
    b.append(f'<line x1="820" y1="640" x2="1000" y2="640" stroke="{INK}" stroke-width="3"/><line x1="830" y1="640" x2="830" y2="{GY}" stroke="{INK}"/><line x1="990" y1="640" x2="990" y2="{GY}" stroke="{INK}"/>')
    b.append(f'<rect x="880" y="590" width="80" height="48" fill="#ffffff" stroke="{INK}"/>' + t(920, 612, "412 passed", fs=10, anchor="middle", color="#6aa86a", bold=True) + f'<circle cx="948" cy="628" r="3" fill="#d9362b"/>')
    b.append(person(790, GY, "pat", "sleep", ((20, 30), (24, 26)), sitting=True, scale=0.9) + t(816, 600, "z", fs=14, color=GREY) + t(826, 588, "z", fs=17, color=GREY))
    b.append(lead(948, 628, 1160, 560, ["The review desk (ch. 10)", "4.52 p.m.; one small red dot"], anchor="end", hot=True))
    b.append(lead(790, 670, 560, 700, ["The remainder", "watching is humanly impossible", "for more than about half an hour"], anchor="end", hot=True))
    # output chute to customers
    b.append(f'<path d="M920,430 H1000 L1040,470" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#ah)"/>' + t(1080, 490, "to customers", fs=11, anchor="middle", color=GREY, italic=True))
    # stop cord along the line with a question mark
    b.append(f'<line x1="160" y1="360" x2="920" y2="360" stroke="#d9362b" stroke-width="2"/>')
    b.append(f'<circle cx="720" cy="376" r="12" fill="#fdeee6" stroke="{ACC}"/>' + t(720, 381, "?", fs=14, anchor="middle", color=ACC, bold=True))
    b.append(lead(720, 388, 740, 540, ["Who may pull it? (ch. 12)", "the agent? the reviewer? the customer?"], hot=True))
    # practice room
    b.append(f'<rect x="80" y="560" width="220" height="150" fill="#ffffff" stroke="{INK}" stroke-width="2"/>' + t(190, 584, "PRACTICE ROOM", fs=11, anchor="middle", bold=True))
    b.append(desk(130, 660, 110) + person(120, 700, "dee", "smile", ((18, 10), (22, 6)), sitting=True, scale=0.8))
    b.append(t(190, 640, "by hand, once a shift", fs=10, anchor="middle", color=GREY, italic=True))
    b.append(lead(300, 600, 360, 560, ["Keep the skill alive (ch. 10)", "Bainbridge: manual control,", "or simulators if that's laughable"]))
    # alarms on alarms
    for k, c in enumerate(("#d9362b", "#f2c14e", "#d9362b", "#6aa86a", "#d9362b")):
        b.append(f'<circle cx="{560+k*22}" cy="250" r="7" fill="{c}" stroke="{INK}"/>')
    b.append(f'<circle cx="604" cy="226" r="7" fill="#d9362b" stroke="{INK}"/>' + t(604, 212, "alarm on the alarms", fs=9, anchor="middle", color=GREY, italic=True))
    b.append(lead(626, 250, 720, 205, ["Alarms, even alarms on alarms", "and the flashing lights that confuse"]))
    return frame("Inside a software factory", "Part Three in one drawing: the human in the loop, and where the loop left them.", "".join(b), 3)


# =====================================================================  4. One person's operating system
def ev4():
    b = []
    cx, cy = 470, 470
    b.append(f'<circle cx="{cx}" cy="{cy}" r="300" fill="#f3f2ee" stroke="#c9c8c3" stroke-width="2" stroke-dasharray="2 5"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="190" fill="none" stroke="{GREY}" stroke-width="1.5"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="95" fill="#fdeee6" stroke="{ACC}" stroke-width="3"/>')
    b.append(person(cx, cy + 40, "pat", "smile", scale=1.0))
    b.append(t(cx, cy - 58, "you", fs=13, anchor="middle", bold=True))
    # today list (text file)
    b.append(f'<rect x="{cx+30}" y="{cy-30}" width="54" height="66" fill="#ffffff" stroke="{INK}"/>')
    for k in range(5):
        b.append(f'<line x1="{cx+36}" y1="{cy-20+k*11}" x2="{cx+78-k*5}" y2="{cy-20+k*11}" stroke="{GREY}"/>')
    b.append(lead(cx + 84, cy - 20, 800, 330, ["Today's list (ch. 15)", "one plain text file; refreshed nightly"], hot=True))
    # calendar on middle ring
    b.append(f'<rect x="{cx-40}" y="{cy-205}" width="80" height="44" fill="#ffffff" stroke="{INK}"/><rect x="{cx-40}" y="{cy-205}" width="80" height="12" fill="{ACC}"/>')
    b.append(lead(cx + 40, cy - 190, 800, 230, ["The calendar", "only things with dates"]))
    # inbox on middle ring
    b.append(f'<path d="M{cx-200},{cy+10} h60 l10,24 h-80 z" fill="#ffffff" stroke="{INK}"/><rect x="{cx-190}" y="{cy-6}" width="40" height="16" fill="#ffffff" stroke="{INK}"/>')
    b.append(lead(cx - 200, cy + 20, 150, 560, ["The inbox", "a queue, not a to-do list"]))
    # notes vault / archive on outer ring
    b.append(f'<g transform="translate({cx+180},{cy+180})" fill="#ecebe6" stroke="#a9a8a2"><rect width="70" height="86"/><rect x="8" y="8" width="54" height="20"/><rect x="8" y="33" width="54" height="20"/><rect x="8" y="58" width="54" height="20"/></g>')
    b.append(lead(cx + 250, cy + 220, 800, 710, ["The archive", "asks nothing of you (ch. 15)"]))
    # AI assistant
    b.append(unit7(cx - 200, cy + 250, "smile", scale=0.8))
    b.append(lead(cx - 214, cy + 200, 205, 760, ["The assistant (ch. 10)", "it does the filing;", "you keep the thinking"]))
    # the Sunday machine, off to the side
    mx, my = 960, 520
    b.append(f'<rect x="{mx-70}" y="{my-40}" width="140" height="90" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    for k, (dx, dy, r) in enumerate(((-40, -10, 16), (0, 10, 22), (40, -12, 14))):
        b.append(f'<circle cx="{mx+dx}" cy="{my+dy}" r="{r}" fill="none" stroke="{GREY}" stroke-width="3" stroke-dasharray="4 3"/>')
    b.append(t(mx, my - 50, "THE SUNDAY MACHINE", fs=11, anchor="middle", bold=True))
    b.append(t(mx, my + 68, "tags · templates · backlinks · plugins", fs=10, anchor="middle", color=GREY, italic=True))
    b.append(f'<path d="M{mx-70},{my} C 820,500 760,480 {cx+120},{cy}" stroke="{GREY}" fill="none" stroke-dasharray="3 4" marker-end="url(#ah)"/>')
    b.append(f'<g transform="translate({mx},{my+130})"><polygon points="-18,-44 18,-44 44,-18 44,18 18,44 -18,44 -44,18 -44,-18" fill="{ACC}"/>' + t(0, 6, "STOP", fs=16, anchor="middle", color="#ffffff", bold=True) + "</g>")
    b.append(lead(mx + 30, my + 164, 1170, 770, ["The system for maintaining the system", "the level that controls only itself (3a)"], anchor="end", hot=True))
    # seedling
    b.append(f'<g transform="translate(110,300)"><path d="M-20,0 L-24,-28 H24 L20,0 Z" fill="#e4e3df" stroke="{INK}"/><line x1="0" y1="-28" x2="0" y2="-56" stroke="#3f7a3f" stroke-width="2"/><path d="M0,-46 C -14,-54 -20,-64 -16,-70 C -8,-66 -2,-58 0,-46 Z" fill="#8fbf7f" stroke="#3f7a3f"/><path d="M0,-52 C 12,-60 20,-68 16,-74 C 8,-70 2,-62 0,-52 Z" fill="#8fbf7f" stroke="#3f7a3f"/></g>')
    b.append(lead(126, 250, 150, 190, ["Gall's law, at home (ch. 13)", "start with one file that works"]))
    # mausoleum
    b.append(f'<g transform="translate({cx+110},{cy-280})"><path d="M0,40 h80 v-26 l-40,-18 l-40,18 z" fill="#ffffff" stroke="{GREY}"/><line x1="16" y1="14" x2="16" y2="40" stroke="{GREY}"/><line x1="40" y1="14" x2="40" y2="40" stroke="{GREY}"/><line x1="64" y1="14" x2="64" y2="40" stroke="{GREY}"/></g>')
    b.append(lead(cx + 190, cy - 250, 800, 150, ["A mausoleum of old interests", "notes about a person you no longer are"]))
    return frame("One person's operating system", "Part Four in one drawing: a governing layer small enough to keep alive.", "".join(b), 4)


here = os.path.dirname(os.path.abspath(__file__))
for n, f in enumerate((ev1, ev2, ev3, ev4), 1):
    io.open(os.path.join(here, f"fig-ev-{n}.svg"), "w", encoding="utf-8", newline="").write(f())
    print("wrote fig-ev-%d.svg" % n)
