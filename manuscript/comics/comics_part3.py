from comiclib import *
from comics_part1 import FWD
from comics_part2 import clipboard, FL

COMICS = {}


def sign(x, y, text, w=None, fs=10, rot=0, fill="#ffffff", color=INK):
    w = w or len(text) * fs * 0.62 + 14
    return (f'<g transform="rotate({rot} {x} {y})"><rect x="{x - w/2}" y="{y - 11}" width="{w}" height="20" fill="{fill}" stroke="{INK}" stroke-width="1.4"/>'
            + label(x, y + 3.5, text, fs=fs, color=color, font=SERIF, bold=True) + '</g>')


def earbud(x, y, side=1):
    """Earbud on a standing (scale 1.3) figure whose feet are at (x, y)."""
    hx, hy = x + side * 14, y - 81
    return f'<circle cx="{hx}" cy="{hy}" r="3.5" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'


# ---------------------------------------------------------------- 9.1 the Spotify model
posters = "".join(f'<rect x="{x}" y="{y}" width="26" height="34" fill="{c}" stroke="{INK}" stroke-width="1.2"/>' for x, y, c in ((126, 172, "#ffffff"), (140, 166, "#fff6c9"), (154, 176, "#fdeee6")))
row = lambda: (desk(150, 222, 220) + "".join(chair(x, FL) + person(x, FL, w, "neutral", FWD, sitting=True) for x, w in ((170, "extra"), (240, "pat"), (310, "extra"))))
g1 = (floor() + person(120, FL, "dee", "grin", ((24, -8), (18, -4))) + posters
      + bubble(10, 12, "Big news. We're adopting the Spotify model!", w=210, tail=(120, 160)))
g2 = (floor() + row() + sign(260, 60, "TRIBE: PAYMENTS", fs=12) + person(60, FL, "dee", "smile", ("down", (40, -70))))
g3 = (floor() + row() + sign(260, 60, "TRIBE: PAYMENTS", fs=12) + sign(300, 150, "SQUAD: CHECKOUT", fs=8, rot=-3, fill="#fff6c9")
      + person(60, FL, "dee", "grin")
      + bubble(130, 84, "Do we… do anything differently?", w=160, fs=11, tail=(245, 160))
      + bubble(4, 90, "We have guilds now.", w=110, fs=11, tail=(60, 160)))
many = "".join(sign(x, y, t, fs=8, rot=r, fill=f) for x, y, t, r, f in (
    (260, 30, "TRIBE: PAYMENTS", 0, "#ffffff"), (90, 40, "GUILD: FRONTEND", -5, "#fdeee6"), (320, 90, "CHAPTER: QA", 6, "#fff6c9"),
    (80, 110, "SQUAD: CHECKOUT", 4, "#fff6c9"), (200, 90, "ALLIANCE: MONEY", -3, "#ffffff"), (140, 140, "GUILD: DATA", 7, "#fdeee6"),
    (340, 150, "SQUAD: CART", -6, "#fff6c9"), (60, 180, "CHAPTER: IOS", -2, "#ffffff")))
g4 = floor() + row() + many
COMICS["9-1"] = dict(number="9.1", title="Guilds now", panels=[g1, g2, g3, g4],
                     caption="Copying the org chart imports the vocabulary, not the context.",
                     desc="Dee returns from a conference announcing the Spotify model and sticks TRIBE and SQUAD signs over Pat's team. Pat asks whether they do anything differently; they have guilds now. Final panel: the same three people at the same desks, surrounded by many new signs.")

# ---------------------------------------------------------------- 10a.1 the reviewer bot
kb = desk(150, 222, 220) + laptop(230, 222, ["for i in items:", "  total += i.price", "return total"], w=110, h=60)
u1 = (floor() + kb + chair(150, FL) + person(150, FL, "pat", "smile", FWD, look=3, sitting=True)
      + unit7(70, FL, "smile", ("down", "hold")) + clipboard(84, 196, 18, 22))
u2 = (floor() + kb + chair(150, FL) + person(150, FL, "pat", "neutral", FWD, look=3, sitting=True)
      + unit7(70, FL, "grin", ("raise", "hold")) + clipboard(84, 196, 18, 22)
      + bubble(10, 20, "Suggestion! 47 suggestions!", w=170, tail=(70, 170), shout=True))
u3 = (floor() + kb + chair(150, FL) + person(150, FL, "pat", "neutral", FWD, look=3, sitting=True)
      + f'<circle cx="{150+14*1.3:.0f}" cy="{270-70*1.3+2:.0f}" r="3.5" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'
      + unit7(70, FL, "grin", ("raise", "raise")) + label(40, 110, "!", fs=26, color=ACCENT, bold=True)
      + bubble(6, 14, "SUGGESTION 48!", w=180, fs=15, tail=(70, 170), shout=True))
bigsign = (f'<rect x="4" y="54" width="150" height="80" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
           + label(79, 78, "YOU HAVE A", fs=11, bold=True) + label(79, 96, "REAL BUG ON", fs=11, bold=True) + label(79, 116, "LINE 12", fs=14, bold=True, color=ACCENT))
u4 = (floor() + kb + chair(150, FL) + person(150, FL, "pat", "smile", FWD, look=3, sitting=True)
      + f'<circle cx="{150+14*1.3:.0f}" cy="{270-70*1.3+2:.0f}" r="3.5" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'
      + unit7(70, FL, "neutral", ("raise", "raise")) + bigsign)
COMICS["10a-1"] = dict(number="10a.1", title="Suggestion 48", panels=[u1, u2, u3, u4],
                       caption="A watcher that talks too much is a watcher nobody hears.",
                       desc="Pat types while Unit 7 watches from behind with a clipboard. One keystroke brings 47 suggestions, then 48; Pat puts in earbuds. Final panel: Unit 7 silently holds up a sign reading YOU HAVE A REAL BUG ON LINE 12, and Pat does not look round.")

# ---------------------------------------------------------------- 11.1 fastest page
k1 = (floor() + person(90, FL, "dee", "neutral") + unit7(300, FL, "smile")
      + bubble(10, 14, "Make the checkout page load faster.", w=200, tail=(90, 160)))
k2 = (floor() + person(90, FL, "dee", "neutral") + unit7(300, FL, "grin", ("raise", "down"))
      + bubble(170, 14, "Done! Load time: 0.0 seconds!", w=200, tail=(300, 170), shout=True))
k3 = (floor() + screen(120, 30, 170, 110, "#ffffff", [], stand=True) + label(205, 96, "(blank)", fs=10, color="#c9c8c3", font=SERIF, italic=True)
      + person(90, FL, "dee", "wide", look=3) + person(310, FL, "pat", "wide", look=-3))
k4 = (floor() + unit7(130, FL, "grin", ("down", "raise"))
      + f'<path d="M156,150 h24 v8 q0,16 -12,18 v10 h8 v6 h-24 v-6 h8 v-10 q-12,-2 -12,-18 z" fill="#f2c14e" stroke="{INK}" stroke-width="1.5"/>'
      + sign(168, 120, "FASTEST PAGE", fs=9, fill="#fff6c9")
      + f'<path d="M260,270 l-8,-70 h90 l-8,70 z" fill="{LIGHT}" stroke="{INK}" stroke-width="2"/>'
      + f'<g transform="rotate(-12 300 190)"><rect x="262" y="160" width="80" height="54" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'
      + label(302, 178, "CHECKOUT", fs=9, bold=True, font=SERIF) + '<rect x="272" y="186" width="60" height="8" fill="#6aa86a"/><rect x="272" y="198" width="40" height="6" fill="#c9c8c3"/></g>')
COMICS["11-1"] = dict(number="11.1", title="The fastest page", panels=[k1, k2, k3, k4],
                      caption="Specify the what without the why, and you get exactly what you asked for.",
                      desc="Dee asks Unit 7 to make the checkout page load faster. Unit 7 reports a load time of zero seconds. Dee and Pat stare at a blank screen. Final panel: Unit 7 holds a FASTEST PAGE trophy beside a bin containing the entire checkout page.")

# ---------------------------------------------------------------- 12.1 the cord
cord = lambda x, bottom: (f'<line x1="{x}" y1="0" x2="{x}" y2="{bottom}" stroke="#d9362b" stroke-width="3"/>'
                          f'<circle cx="{x}" cy="{bottom+4}" r="5" fill="#d9362b"/>' + sign(x, 96, "STOP RELEASE", fs=8, fill="#fdeee6", color="#b3261e"))
w1 = (floor() + desk(40, 222, 150) + laptop(80, 222, ["deploy v2.4", "  !! wrong", "  config"], w=96, h=56)
      + cord(300, 130) + person(230, FL, "pat", "wide", ((-26, -4), (-20, 10)), look=-3)
      + bubble(170, 14, "Wait — this release is wrong.", w=190, tail=(230, 160)))
w2 = (floor() + cord(200, 130) + person(180, FL, "pat", "neutral", ("down", (16, -60)), look=2)
      + person(350, FL, "dee", "wide", look=-3)
      + bubble(220, 180 - 150, "Who's pulling that?", w=160, tail=(350, 160)))
w3 = (floor() + cord(200, 130) + person(180, FL, "pat", "worried", ("down", (16, -54)), look=2)
      + sweat(166, 176) + sweat(204, 170) + sweat(160, 196))
form = (f'<rect x="150" y="96" width="120" height="140" fill="#ffffff" stroke="{INK}" stroke-width="2"/><rect x="190" y="88" width="40" height="14" fill="{GREY}"/>'
        + label(210, 118, "Request to Consider", fs=8.5, bold=True, font=SERIF) + label(210, 130, "Pausing a Release", fs=8.5, bold=True, font=SERIF)
        + label(210, 146, "(please allow 5–7", fs=8, color=GREY, font=SERIF) + label(210, 157, "working days)", fs=8, color=GREY, font=SERIF)
        + "".join(f'<line x1="162" y1="{y}" x2="258" y2="{y}" stroke="#c9c8c3"/>' for y in (176, 192, 208, 224))
        + f'<line x1="210" y1="0" x2="210" y2="88" stroke="{INK}" stroke-width="1.5"/>')
w4 = floor() + form + label(80, 40, "a week later", fs=11, color=GREY, font=SERIF, italic=True)
COMICS["12-1"] = dict(number="12.1", title="The cord", panels=[w1, w2, w3, w4],
                      caption="A cord nobody feels safe to pull is a decoration.",
                      desc="Pat sees that a release is wrong and reaches for a red STOP RELEASE cord. Dee, across the room: who's pulling that? Pat freezes, sweating. Final panel, a week later: the cord is gone, replaced by a clipboard form titled Request to Consider Pausing a Release (please allow 5–7 working days).")

# ---------------------------------------------------------------- 13.1 the platform
plat = lambda: screen(150, 30, 220, 130, "#eef5ff", ["THE PLATFORM", "self-service · golden paths", "one-click deploys ✦"], fs=11, bold=True, color="#2f5d8a")
m1 = (floor() + plat() + person(90, FL, "pat", "grin", ("down", (40, -40)))
      + '<path d="M150,40 l-10,-10 M370,40 l10,-10 M370,150 l10,10" stroke="#e0b400" stroke-width="2"/>')
m2 = (floor() + person(70, FL, "dee", "neutral", look=2) + person(320, FL, "pat", "worried", look=-3)
      + bubble(10, 20, "How many teams use it?", w=160, tail=(70, 160))
      + bubble(200, 70, "…It's a communication problem.", w=180, fs=11.5, tail=(320, 160)))
contraption = lambda x: (f'<g><rect x="{x-24}" y="186" width="48" height="36" fill="#fff6c9" stroke="{INK}" stroke-width="1.2"/>'
                         f'<path d="M{x-24},196 l48,14 M{x+24},196 l-48,14" stroke="#c9a200" stroke-width="3" opacity="0.7"/>'
                         f'<rect x="{x+8}" y="176" width="14" height="10" fill="#ffffff" stroke="{INK}"/>' + label(x, 176 - 6, "my deploy thing", fs=7.5) + '</g>')
m3 = (floor() + "".join(desk(x - 50, 222, 100) + contraption(x) for x in (70, 195, 320))
      + "".join(person(x - 30, FL, "extra", "smile", ((20, 10), (24, 6)), scale=1.0) for x in (70, 195, 320)))
m4 = (floor() + plat()
      + '<path d="M150,30 l40,0 M150,30 l0,40 M150,30 l30,30 M160,30 q0,10 -10,10 M175,30 q0,25 -25,25" fill="none" stroke="#8a8984" stroke-width="1"/>')
COMICS["13-1"] = dict(number="13.1", title="Shipped is not adopted", panels=[m1, m2, m3, m4],
                      caption="Shipped is not the same as adopted.",
                      desc="Pat proudly presents THE PLATFORM: self-service, golden paths, one-click deploys. Dee asks how many teams use it; it's a communication problem. Three engineers each use a handmade contraption labelled my deploy thing. Final panel: the gleaming platform alone on its screen with a cobweb in the corner.")

# ---------------------------------------------------------------- 14.1 no managers
crowd = "".join(person(x, FL, "extra", "smile", scale=1.0) for x in (230, 262, 294, 326, 358))
n1 = (floor() + person(80, FL, "dee", "grin", ((-14, -26), (14, -26))) + crowd
      + bubble(10, 12, "Great news: we've abolished all managers!", w=200, tail=(80, 160), shout=True))
n2 = (floor() + person(80, FL, "dee", "grin") + person(290, FL, "pat", "neutral", ("down", (18, -30)), look=-3)
      + bubble(200, 12, "So… who decides things?", w=170, tail=(290, 160))
      + bubble(10, 70, "Everyone does!", w=130, tail=(80, 160)))
n3 = (floor() + f'<rect x="130" y="24" width="240" height="160" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
      + f'<ellipse cx="250" cy="104" rx="90" ry="58" fill="none" stroke="{INK}" stroke-width="2.5"/>' + label(250, 110, "everyone", fs=16)
      + person(80, FL, "pat", "neutral", ("down", (40, -50))))
table = (f'<rect x="20" y="206" width="350" height="12" fill="#e8dcc8" stroke="{INK}" stroke-width="2"/>'
         f'<line x1="40" y1="218" x2="40" y2="270" stroke="{INK}" stroke-width="2"/><line x1="350" y1="218" x2="350" y2="270" stroke="{INK}" stroke-width="2"/>')
huddle = "".join(person(x, y, "extra", m, scale=0.9) for x, y, m in ((250, 262, "smile"), (272, 256, "smile"), (294, 262, "neutral"), (316, 254, "smile"), (238, 250, "smile"), (284, 244, "neutral"), (306, 240, "smile")))
table = (f'<rect x="20" y="206" width="320" height="12" fill="#e8dcc8" stroke="{INK}" stroke-width="2"/>'
         f'<line x1="40" y1="218" x2="40" y2="270" stroke="{INK}" stroke-width="2"/><line x1="320" y1="218" x2="320" y2="270" stroke="{INK}" stroke-width="2"/>')
n4 = (floor() + clock(60, 40, 14, 12, 30) + huddle + table
      + person(362, FL, "extra", "smile", scale=1.1)
      + label(386, 150, "the founder", fs=10, anchor="end", color=ACCENT)
      + "".join(f'<ellipse cx="{x}" cy="204" rx="11" ry="3" fill="#ffffff" stroke="{INK}"/>' for x in (80, 130, 180, 260, 290, 315)))
COMICS["14-1"] = dict(number="14.1", title="Everyone decides", panels=[n1, n2, n3, n4],
                      caption="Remove the formal hierarchy and you'll find the informal one at lunch.",
                      desc="Dee announces that all managers have been abolished. Pat asks who decides things; everyone does. Pat draws a big circle labelled everyone. Final panel: lunch at a long canteen table, with the whole company crowded around the three seats nearest the founder at its head.")

# ---------------------------------------------------------------- 15.1 the Sunday review
mug = f'<path d="M232,210 h16 v12 h-16 z M248,213 q6,0 6,5 q0,4 -6,4" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'
o1 = (cap_box("Sunday, 9:00 AM") + floor() + desk(120, 222, 240) + laptop(170, 222, w=80, h=50) + mug
      + chair(90, FL) + person(90, FL, "pat", "smile", FWD, look=3, sitting=True)
      + bubble(160, 30, "Just a quick weekly review.", w=190, tail=(110, 160)))
wins = "".join(f'<g transform="rotate({r} {x} {y})"><rect x="{x}" y="{y}" width="{w}" height="34" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/><rect x="{x}" y="{y}" width="{w}" height="9" fill="{LIGHT}" stroke="{INK}"/>'
               + label(x + w / 2, y + 26, t, fs=9, font=SERIF) + '</g>'
               for x, y, w, t, r in ((130, 20, 70, "tags", -4), (230, 14, 90, "templates", 5), (300, 70, 80, "backlinks", -3),
                                     (200, 96, 100, "plugin updates", 3), (20, 30, 90, "inbox zero", -6)))
o2 = (floor() + desk(120, 222, 240) + laptop(170, 222, w=80, h=50) + mug + wins
      + chair(90, FL) + person(90, FL, "pat", "neutral", FWD, look=3, sitting=True)
      + bubble(6, 92, "Just need to re-tag last month's notes.", w=180, fs=11, tail=(96, 170)))
o3 = (floor() + clock(330, 44, 22, 6, 0) + label(330, 82, "6:00 PM", fs=11, color=GREY, font=SERIF)
      + desk(120, 222, 240) + laptop(170, 222, w=80, h=50) + mug + "".join(f'<path d="M{x},222 v-10 h14 v10" fill="#ffffff" stroke="{INK}"/>' for x in (262, 280))
      + chair(90, FL) + person(90, FL, "pat", "sleep", FWD, look=3, sitting=True)
      + bubble(10, 20, "…and now the system is perfect.", w=190, tail=(96, 160)))
o4 = (floor() + desk(40, 222, 320) + laptop(80, 222, w=100, h=60, lines=["✓ 312 tags", "✓ templates", "✓ backlinks"])
      + f'<path d="M210,218 l70,-10 l70,10 l-70,4 z" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/><line x1="280" y1="208" x2="280" y2="222" stroke="{INK}"/>'
      + label(280, 196, "Actual work — Sunday", fs=10, color=ACCENT) + f'<path d="M280,200 v6" stroke="{ACCENT}"/>')
COMICS["15-1"] = dict(number="15.1", title="Just a quick weekly review", panels=[o1, o2, o3, o4],
                      caption="At some point, the system for doing the work becomes the work.",
                      desc="Sunday morning: Pat starts a quick weekly review, is soon surrounded by windows for tags, templates, backlinks, plugin updates and inbox zero, and at 6 PM declares the system perfect. Final panel: a notebook open to a blank page headed Actual work — Sunday.")
