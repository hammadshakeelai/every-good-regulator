from comiclib import *
from comics_part1 import thermostat, FWD

COMICS = {}
FL = 270


def clipboard(x, y, w=22, h=28, text=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'
            f'<rect x="{x+w/2-5}" y="{y-3}" width="10" height="5" fill="{GREY}"/>' + (label(x + w / 2, y + h / 2 + 3, text, fs=6) if text else ""))


def chat(x, y, w, h, title, msgs, fs=10):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#ffffff" stroke="{INK}" stroke-width="2"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="20" rx="4" fill="{LIGHT}" stroke="{INK}" stroke-width="2"/>',
         label(x + 8, y + 14, title, fs=10, anchor="start", font="Consolas, monospace")]
    yy = y + 38
    for who, text in msgs:
        s.append(label(x + 8, yy, who, fs=9, anchor="start", color=ACCENT, bold=True, font=SERIF))
        for ln in wrap(text, int((w - 16) / (fs * 0.6))):
            yy += fs + 4
            s.append(label(x + 8, yy, ln, fs=fs, anchor="start"))
        yy += fs + 10
    return "".join(s)


# ---------------------------------------------------------------- 1.1 legible vs load-bearing
r1 = (floor() + green_board(150, 40, 220, 150) + person(90, FL, "dee", "grin", ("down", (34, -30)))
      + bubble(10, 12, "Every team is green on every metric.", w=150, tail=(90, 160)))
r2 = (floor() + desk(120, 222, 250) + chair(80, FL) + person(80, FL, "pat", "neutral", FWD, look=3, sitting=True)
      + chat(150, 30, 220, 160, "#backchannel", [("pat", "can you restart the thing again? the thing from tuesday.")]))
r3 = (floor() + desk(20, 222, 250) + chair(300, FL, -1) + person(300, FL, "extra", "neutral", ((-20, 12), (-24, 8)), look=-3, sitting=True)
      + chat(20, 30, 230, 160, "#backchannel", [("pat", "can you restart the thing again? the thing from tuesday."),
                                                ("sam", "on it. don't tell anyone, it's not on the board.")]))
wires = ("".join(f'<path d="M{x},{0} C {x+30},{80} {x-40},{160} {x+10},{290}" fill="none" stroke="{c}" stroke-width="2"/>'
                 for x, c in ((60, INK), (120, ACCENT), (170, INK), (250, "#4a7fb5"), (320, INK), (360, ACCENT)))
         + "".join(sticky(x, y, t, rot=r) for x, y, t, r in ((20, 60, "restart", -8), (330, 40, "cron??", 6), (40, 200, "DON'T", 4),
                                                            (300, 210, "ask sam", -5), (200, 230, "manual", 3))))
r4 = ((f'<rect width="{PW}" height="{PH}" fill="#2b2b2e"/>' + wires.replace(INK, "#bdbdbd")
       + green_board(95, 55, 200, 140)), "#2b2b2e")
COMICS["1-1"] = dict(number="1.1", title="Load-bearing work", panels=[r1, r2, r3, r4],
                     caption="Legible work on the screen. Load-bearing work behind it.",
                     desc="Dee points at a wall of green metrics. In a backchannel chat, Pat asks a colleague to restart 'the thing from Tuesday' and the colleague says not to tell anyone, it isn't on the board. Final panel: the green screen, and behind it in the dark a tangle of wires and sticky notes holding the wall up.")

# ---------------------------------------------------------------- 2a.1 the lander
def lander(x, y, face="open", legs="open", s=1.0):
    eyes = {"open": f'<circle cx="{x-8}" cy="{y-2}" r="2" fill="{INK}"/><circle cx="{x+8}" cy="{y-2}" r="2" fill="{INK}"/>',
            "narrow": f'<path d="M{x-12},{y-2} h7 M{x+5},{y-2} h7" stroke="{INK}" stroke-width="2"/>',
            "closed": f'<path d="M{x-12},{y-2} q3.5,3 7,0 M{x+5},{y-2} q3.5,3 7,0" stroke="{INK}" fill="none" stroke-width="1.8"/>'}[face]
    mouth = {"open": f'M{x-5},{y+7} q5,4 10,0', "narrow": f'M{x-4},{y+8} h8', "closed": f'M{x-7},{y+6} q7,6 14,0'}[face]
    leg = (f'<path d="M{x-18},{y+14} L{x-34},{y+40} M{x+18},{y+14} L{x+34},{y+40} M{x},{y+18} L{x},{y+42}" stroke="{INK}" stroke-width="2.5"/>'
           f'<path d="M{x-40},{y+40} h12 M{x+28},{y+40} h12 M{x-6},{y+42} h12" stroke="{INK}" stroke-width="2.5"/>'
           if legs == "open" else
           f'<path d="M{x-18},{y+14} L{x-22},{y+24} M{x+18},{y+14} L{x+22},{y+24}" stroke="{INK}" stroke-width="2.5"/>')
    body = (f'<path d="M{x-26},{y+16} L{x-20},{y-18} L{x+20},{y-18} L{x+26},{y+16} Z" fill="#ffffff" stroke="{INK}" stroke-width="2.2"/>'
            f'<rect x="{x-30}" y="{y-26}" width="60" height="8" fill="{LIGHT}" stroke="{INK}" stroke-width="1.5"/>')
    g = body + leg + eyes + f'<path d="{mouth}" stroke="{INK}" fill="none" stroke-width="1.8"/>'
    return f'<g transform="translate({x},{y}) scale({s}) translate({-x},{-y})">{g}</g>'


SKY = "#1c1c2b"
stars = "".join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="#ffffff"/>' for x, y in ((30, 30), (80, 70), (150, 20), (220, 55), (300, 25), (350, 80), (40, 140), (330, 150), (260, 110)))
mars = f'<ellipse cx="195" cy="330" rx="330" ry="90" fill="#c8643b"/>'
l1 = ((stars + mars + lander(195, 110, "open", "open", 1.4)
       + label(270, 170, "CLUNK!", fs=18, color="#ffd24a", bold=True)
       + '<path d="M140,150 l-12,8 M250,150 l12,8" stroke="#ffd24a" stroke-width="2"/>'), SKY)
l2 = ((stars + '<g transform="translate(195,150) scale(2.6) translate(-195,-150)">' + lander(195, 150, "narrow", "open") + '</g>'
       + bubble(20, 14, "…was that the ground?", w=190, tail=(150, 90))), SKY)
l3 = ((stars + mars + lander(195, 100, "closed", "open", 1.4)
       + bubble(230, 20, "Landed. Nailed it.", w=140, tail=(225, 80))
       + '<path d="M195,160 v10 M195,186 v10" stroke="#8a8984" stroke-dasharray="3 5" stroke-width="1.5"/>'
       + label(210, 200, "40 m", fs=11, color="#ffffff", anchor="start", font=SERIF)), SKY)
l4 = ((stars + f'<rect x="0" y="200" width="{PW}" height="90" fill="#c8643b"/>'
       + '<path d="M0,200 q60,-18 120,-4 q70,14 140,-6 q70,-14 130,4" fill="#b85a33"/>'
       + '<g fill="#e08a5e" opacity="0.9"><circle cx="300" cy="192" r="7"/><circle cx="310" cy="186" r="5"/><circle cx="292" cy="186" r="4"/></g>'), SKY)
COMICS["2a-1"] = dict(number="2a.1", title="Every part performed as specified", panels=[l1, l2, l3, l4],
                      caption="Every part performed as specified.",
                      desc="A little lander with a thermostat's face snaps its legs open high above Mars with a clunk, wonders whether that was the ground, decides it has landed, and switches off. Final panel: a quiet Martian landscape and a small puff of dust far away.")

# ---------------------------------------------------------------- 3.1 who checks the agents
s1 = (floor() + person(110, FL, "dee", "grin", ((-14, -24), (14, -24))) + person(290, FL, "pat", "neutral", look=-2)
      + bubble(10, 14, "Great news. The agents write all the code now.", w=190, tail=(110, 160))
      + bubble(230, 60, "Who checks the agents?", w=150, tail=(290, 160)))
s2 = (floor() + person(110, FL, "dee", "smile") + person(290, FL, "pat", "neutral", look=-2)
      + bubble(20, 40, "Other agents.", w=130, tail=(110, 160))
      + bubble(210, 40, "Who checks those agents?", w=170, tail=(290, 160)))
s3 = (floor() + person(110, FL, "dee", "grin", ((-14, -26), (14, -26))) + person(290, FL, "pat", "worried", look=-2)
      + bubble(20, 30, "Better agents!", w=150, tail=(110, 160), shout=True))
tower = []
for i in range(9):
    feet = 168 - i * 74
    x = 195 + (6 if i % 2 else -6)
    tower.append(unit7(x, feet, "smile", ("down", "hold"), scale=0.85)
                 + f'<circle cx="{x+26}" cy="{feet-8}" r="7" fill="none" stroke="{INK}" stroke-width="1.5"/><line x1="{x+31}" y1="{feet-3}" x2="{x+36}" y2="{feet+3}" stroke="{INK}" stroke-width="1.5"/>')
s4 = (floor() + "".join(tower) + person(195, FL, "pat", "worried", ((-12, -28), (12, -28))) + sweat(215, 176))
COMICS["3-1"] = dict(number="3.1", title="Who checks the agents?", panels=[s1, s2, s3, s4],
                     caption="Every jump adds a layer. Somebody still has to hold up the bottom.",
                     desc="Dee announces that agents write all the code; Pat asks who checks them. Other agents, says Dee; and who checks those? Better agents! Final panel: a tall stack of little robots, each inspecting the one below, held up at the bottom by Pat.")

# ---------------------------------------------------------------- 3a.1 the milk (tall column)
def milk(x, y, off=False):
    g = (f'<path d="M{x-12},{y} v-34 l6,-10 h12 l6,10 v34 z" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
         f'<rect x="{x-12}" y="{y-26}" width="24" height="12" fill="#4a7fb5"/>' + label(x, y - 16.5, "MILK", fs=7, color="#ffffff", font=SERIF))
    if off:
        g += (f'<g stroke="{GREEN}" stroke-width="1.5" fill="none"><path d="M{x-8},{y-50} q-4,-8 0,-14 q4,-6 0,-12"/><path d="M{x+6},{y-52} q4,-8 0,-14 q-4,-6 0,-12"/></g>'
              f'<circle cx="{x+14}" cy="{y-58}" r="2" fill="{INK}"/><circle cx="{x-18}" cy="{y-66}" r="2" fill="{INK}"/>')
    return g


FH = 108
floors = [
    floor(96, 0, 390) + milk(195, 96) + label(20, 20, "1", fs=12, color=GREY, font=SERIF),
    floor(96, 0, 390) + sticky(170, 30, "milk", w=50, fs=13, rot=-4) + label(20, 20, "2", fs=12, color=GREY, font=SERIF),
    (floor(96, 0, 390) + f'<rect x="150" y="10" width="90" height="80" rx="8" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
     + '<rect x="160" y="30" width="70" height="44" fill="#fbfaf6" stroke="#c9c8c3"/>' + label(195, 44, "☐ milk", fs=10)
     + label(195, 58, "#errands #dairy", fs=7, color=ACCENT) + label(195, 68, "#someday", fs=7, color=ACCENT)
     + label(20, 20, "3", fs=12, color=GREY, font=SERIF)),
    (floor(96, 0, 390) + desk(200, 70, 120) + person(150, 96, "pat", "neutral", ((22, 4), (26, 0)), scale=0.85)
     + clipboard(178, 40, 26, 32) + f'<rect x="232" y="14" width="140" height="24" fill="#fff6c9" stroke="{INK}"/>' + label(302, 30, "WEEKLY REVIEW OF APP", fs=9.5, bold=True, font=SERIF) + label(20, 20, "4", fs=12, color=GREY, font=SERIF)),
    (floor(96, 0, 390) + f'<path d="M110,96 v-30 h170 v30 M110,66 v-16 h170 v16" fill="#e8dcc8" stroke="{INK}" stroke-width="2"/>'
     + '<g transform="translate(195,70) rotate(-80) translate(-195,-70)">' + person(195, 70, "pat", "sleep", scale=0.8) + '</g>'
     + "".join(laptop(x, y, w=34, h=22) for x, y in ((20, 96), (70, 50), (300, 50), (340, 96), (60, 96), (300, 96), (320, 36)))
     + label(20, 20, "5", fs=12, color=GREY, font=SERIF)),
]
COL_H = FH * 5 + 4 * GAP
column = "".join(f'<g transform="translate(0,{(4-i)*(FH+GAP)})"><rect width="390" height="{FH}" fill="#ffffff" stroke="{INK}" stroke-width="2"/>{c}</g>'
                 for i, c in enumerate(floors))
side = (f'<line x1="404" y1="0" x2="404" y2="{COL_H}" stroke="{INK}" stroke-width="2.5"/>'
        + label(482, 30, "Meanwhile,", fs=12) + label(482, 48, "on floor 1:", fs=12)
        + f'<path d="M482,60 v{COL_H-190}" stroke="{GREY}" stroke-dasharray="3 6" stroke-width="1.5"/>'
        + floor(COL_H - 12, 404, 560) + '<g transform="translate(482,{0}) scale(1.6) translate(-482,-{0})">'.format(COL_H - 12) + milk(482, COL_H - 12, off=True) + '</g>')
COMICS["3a-1"] = dict(number="3a.1", title="The tower of to-do", layout="row", pw=560, ph=COL_H,
                      panels=[column + side],
                      caption="Read from the bottom up.",
                      desc="A column of five floors read from the bottom up: a pint of milk; a sticky note saying milk; a phone app with the milk task tagged three ways; Pat with a clipboard for the weekly review of the app; Pat asleep among seven laptops. Beside it, the milk on floor 1 has gone off.")

# ---------------------------------------------------------------- 4.1 nobody is doing System 4
vsm = ("".join(f'<rect x="{x}" y="{y}" width="{w}" height="14" fill="#ffffff" stroke="{INK}" stroke-width="1.2"/>'
               for x, y, w in ((150, 180, 60), (220, 180, 60), (185, 160, 60), (185, 140, 60)))
       + "".join(f'<circle cx="{x}" cy="212" r="10" fill="#ffffff" stroke="{INK}" stroke-width="1.2"/>' for x in (160, 190, 220, 250, 280)))
table = f'<path d="M100,222 L340,222 L360,240 L80,240 Z" fill="#f6f1e4" stroke="{INK}" stroke-width="2"/><line x1="100" y1="240" x2="100" y2="270" stroke="{INK}" stroke-width="2"/><line x1="340" y1="240" x2="340" y2="270" stroke="{INK}" stroke-width="2"/>'
v1 = (floor() + table + vsm + person(60, FL, "pat", "grin", ((24, -10), (30, -2)))
      + bubble(10, 12, "I've mapped our whole company onto Beer's Viable System Model!", w=260, tail=(60, 160)))
v2 = (floor() + table + vsm + person(60, FL, "pat", "neutral") + person(335, FL, "dee", "crossed", look=-3)
      + bubble(210, 12, "And what does it say?", w=160, tail=(335, 160))
      + bubble(10, 80, "Nobody is doing System 4.", w=160, tail=(60, 160)))
v3 = (floor() + table + vsm + person(60, FL, "pat", "neutral") + person(335, FL, "dee", "neutral", look=-3)
      + bubble(230, 12, "What's System 4?", w=140, tail=(335, 160))
      + bubble(10, 60, "Thinking about the future.", w=170, tail=(60, 160)))
cal = (f'<rect x="130" y="30" width="130" height="140" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
       f'<rect x="130" y="30" width="130" height="26" fill="{ACCENT}"/>' + label(195, 48, "NEXT QUARTER", fs=10, color="#ffffff", font=SERIF, bold=True)
       + label(195, 100, "ROADMAP:", fs=16, bold=True) + label(195, 130, "TBD", fs=24, bold=True, color=ACCENT))
v4 = (floor() + cal + person(90, FL, "pat", "neutral", look=3) + person(300, FL, "dee", "neutral", look=-3))
COMICS["4-1"] = dict(number="4.1", title="Nobody is doing System 4", panels=[v1, v2, v3, v4],
                     caption="A diagnosis is not a plan. But it's a start.",
                     desc="Pat has mapped the company onto Beer's Viable System Model. Dee asks what it says; nobody is doing System 4 — thinking about the future. Both turn to a wall calendar whose next-quarter page reads ROADMAP: TBD.")

# ---------------------------------------------------------------- 5.1 token legend
t1 = (floor() + screen(170, 40, 200, 130, "#fff6e6", ["TOKEN LEGEND", "of the month:", "PAT"], fs=14, bold=True, color=ACCENT)
      + person(90, FL, "dee", "grin", ("down", (34, -30))) + '<path d="M180,60 l-10,-10 M360,60 l10,-10 M180,150 l-10,10" stroke="#e0b400" stroke-width="2"/>'
      + bubble(8, 12, "Great news. Pat is our number one Token Legend this month!", w=180, tail=(90, 160)))
t2 = (floor() + desk(120, 222, 250) + chair(80, FL) + person(80, FL, "pat", "neutral", FWD, look=3, sitting=True)
      + chat(150, 30, 225, 170, "AI chat", [("pat", "what is 2 + 2"), ("AI", "4.")]))
long = " ".join(["Great question! Let's explore this in detail. Addition is one of the four fundamental operations of arithmetic, dating back to"] * 3)
t3 = (floor() + desk(120, 222, 250) + chair(80, FL) + person(80, FL, "pat", "smile", FWD, look=3, sitting=True)
      + chat(150, 30, 225, 300, "AI chat", [("pat", "what is 2 + 2 (please explain in detail)"), ("AI", long)], fs=8.5))
paper = "M230,150 C 230,200 170,230 150,250 C 120,275 60,262 30,272 L0,272"
t4 = (floor() + f'<rect x="220" y="110" width="100" height="60" rx="4" fill="{LIGHT}" stroke="{INK}" stroke-width="2"/><rect x="235" y="100" width="70" height="12" fill="#ffffff" stroke="{INK}"/>'
      + f'<path d="{paper}" fill="none" stroke="{INK}" stroke-width="21"/><path d="{paper}" fill="none" stroke="#ffffff" stroke-width="18"/>'
      + label(150, 238, "INVOICE", fs=9, color=ACCENT, font=SERIF, bold=True)
      + f'<rect x="-2" y="120" width="20" height="150" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
COMICS["5-1"] = dict(number="5.1", title="Token Legend", panels=[t1, t2, t3, t4],
                     caption="Measure the tokens and you will get tokens.",
                     desc="Dee announces Pat as the month's Token Legend. Pat asks an AI what 2 + 2 is, then asks again, 'please explain in detail', and the reply scrolls off the panel. Final panel: an empty office printer feeding out an invoice that trails across the floor and out of the door.")

# ---------------------------------------------------------------- 6.1 fee for bug reports
def overalls(x, y):
    return f'<path d="M{x-9},{y-52} h18 v30 h-18 z" fill="#4a7fb5" opacity="0.75"/>'


h1 = (floor() + screen(170, 50, 200, 100, "#fff1ea", ["AIRCRAFT 7:", "NOT FIT TO FLY", "part record missing"], fs=12, color="#b3261e", bold=True)
      + person(90, FL, "pat", "worried", ((-12, 12), (22, -4)), extra=overalls(90, FL))
      + bubble(10, 12, "The part's right there. I installed it yesterday.", w=170, tail=(90, 160)))
box = (f'<rect x="200" y="70" width="110" height="130" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
       + label(255, 92, "ACTION", fs=11, bold=True, font=SERIF) + label(255, 106, "REQUESTS", fs=11, bold=True, font=SERIF)
       + f'<rect x="230" y="126" width="50" height="6" fill="{INK}"/>'
       + f'<rect x="215" y="40" width="80" height="26" fill="#ffffff" stroke="{INK}" stroke-width="2"/>' + label(255, 58, "$ 1,240", fs=12, color=ACCENT, font="Consolas, monospace")
       + f'<path d="M230,150 h50" stroke="{INK}"/>' + label(255, 176, "(fee per request)", fs=8, color=GREY, font=SERIF))
h2 = (floor() + box + person(120, FL, "pat", "neutral", ((-10, 18), (60, -58)), extra=overalls(120, FL))
      + f'<rect x="232" y="128" width="16" height="20" fill="#ffffff" stroke="{INK}"/>')
pages = "".join(f'<g transform="rotate({r} {x} {y})"><rect x="{x}" y="{y}" width="40" height="48" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/><rect x="{x}" y="{y}" width="40" height="10" fill="{ACCENT}"/></g>'
                for x, y, r in ((160, 90, 0), (210, 60, 18), (260, 40, 35), (300, 30, 55), (100, 60, -20)))
h3 = cap_box("Three months later.") + pages
h4 = (floor() + screen(250, 30, 130, 80, "#fff1ea", ["NOT FIT", "TO FLY"], fs=12, color="#b3261e", bold=True)
      + desk(40, 222, 200) + laptop(90, 222, ["A  B  C  D", "7  ok ok ok", "8  ok ok ok", "9  ok ok --"], w=120, h=70, fs=8)
      + label(150, 142, "REAL RECORDS", fs=8, bold=True, font=SERIF) + label(150, 132, "(DO NOT DELETE)", fs=7, color=ACCENT, font=SERIF)
      + chair(20, FL) + person(20, FL, "pat", "neutral", FWD, sitting=True, extra=overalls(20, FL + 6)))
COMICS["6-1"] = dict(number="6.1", title="The real records", panels=[h1, h2, h3, h4],
                     caption="When the official system can't be corrected, the real one moves into a spreadsheet.",
                     desc="In a hangar, a screen says aircraft 7 is not fit to fly because a part record is missing; Pat installed the part yesterday. Pat posts an Action Request into a box with a fee meter above it. Three months pass. Final panel: Pat keeps a huge spreadsheet labelled REAL RECORDS (DO NOT DELETE) while the official screen still says NOT FIT TO FLY.")

# ---------------------------------------------------------------- 8.1 root cause
wb = lambda inner: (f'<rect x="120" y="24" width="250" height="160" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
                    f'<line x1="120" y1="190" x2="370" y2="190" stroke="{INK}" stroke-width="4"/>' + inner)
tangle = ("".join(f'<rect x="{x}" y="{y}" width="46" height="18" fill="#ffffff" stroke="{c}" stroke-width="1.2"/>'
                  for x, y, c in ((135, 40, INK), (200, 36, ACCENT), (270, 44, INK), (320, 80, INK), (140, 100, ACCENT), (215, 90, INK), (280, 130, ACCENT), (160, 150, INK), (230, 150, INK)))
          + "".join(f'<path d="M{a},{b} C {c},{d} {e},{f} {g},{h}" fill="none" stroke="{INK}" stroke-width="1"/>'
                    for a, b, c, d, e, f, g, h in ((158, 58, 180, 90, 200, 60, 223, 54), (246, 50, 300, 90, 250, 120, 238, 108), (163, 118, 220, 150, 300, 90, 343, 98),
                                                   (293, 62, 350, 140, 320, 150, 303, 148), (183, 168, 260, 120, 230, 60, 223, 54), (253, 168, 300, 160, 330, 100, 343, 98))))
e1 = (floor() + wb("") + person(70, FL, "dee", "neutral", look=2)
      + bubble(12, 200 - 190, "So. What was the root cause of the outage?", w=150, tail=(70, 160)))
e2 = (floor() + '<g transform="translate(160,86) scale(0.88) translate(-120,-24)">' + wb(tangle) + '</g>'
      + person(90, FL, "pat", "wide", ((-14, 16), (40, -30)))
      + bubble(6, 8, "Well, there were eleven contributing conditions. The permissions change, the query, the size limit, the propagation—", w=270, fs=10.5, tail=(90, 170)))
e3 = (floor() + person(195, FL, "dee", "neutral", ((-10, 20), (14, -34)))
      + bubble(110, 30, "Just pick one.", w=170, tail=(195, 160)))
e4 = (floor() + wb(f'<circle cx="245" cy="104" r="46" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>'
                  + person(245, 136, "extra", "worried", scale=0.6) + label(245, 170, "the intern", fs=11, color=ACCENT)))
COMICS["8-1"] = dict(number="8.1", title="Just pick one", panels=[e1, e2, e3, e4],
                     caption='Richard Cook, 2000: post-accident attribution to a "root cause" is fundamentally wrong.',
                     desc="Dee asks for the root cause of the outage. Pat stands at a whiteboard covered in a tangle of eleven contributing conditions. Dee: just pick one. Final panel: the whiteboard wiped clean except for one small circle containing a stick figure labelled the intern.")
