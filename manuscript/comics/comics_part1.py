from comiclib import *

COMICS = {}


def thermostat(x, y, mood="smile", r=18):
    """Wall thermostat with a face, centred at (x, y)."""
    face = {"smile": f'M{x-6},{y+5} q6,5 12,0', "smug": f'M{x-6},{y+5} q6,3 12,-2'}.get(mood, f'M{x-5},{y+6} h10')
    return (f'<rect x="{x-r}" y="{y-r}" width="{2*r}" height="{2*r}" rx="6" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{x-8},{y-4} q2,-3 4,0 M{x+4},{y-4} q2,-3 4,0" stroke="{INK}" fill="none" stroke-width="1.5"/>'
            f'<path d="{face}" stroke="{INK}" fill="none" stroke-width="1.6"/>')


def lamp(x, y, on=True):
    """Desk lamp standing on surface y."""
    s = (f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-50}" stroke="{INK}" stroke-width="2.5"/>'
         f'<line x1="{x-12}" y1="{y}" x2="{x+12}" y2="{y}" stroke="{INK}" stroke-width="3"/>'
         f'<path d="M{x-16},{y-50} L{x+16},{y-50} L{x+8},{y-66} L{x-8},{y-66} Z" fill="{LIGHT}" stroke="{INK}" stroke-width="2"/>')
    if on:
        s = (f'<path d="M{x-16},{y-50} L{x-46},{y} L{x+46},{y} L{x+16},{y-50} Z" fill="#ffe27a" opacity="0.45"/>'
             + s + f'<g stroke="#e0b400" stroke-width="1.6"><line x1="{x-24}" y1="{y-70}" x2="{x-32}" y2="{y-78}"/><line x1="{x}" y1="{y-74}" x2="{x}" y2="{y-86}"/><line x1="{x+24}" y1="{y-70}" x2="{x+32}" y2="{y-78}"/></g>')
    return s


def scarf(x, y):
    """Scarf on a standing person whose feet are at (x, y)."""
    return f'<path d="M{x-10},{y-50} q10,6 20,0 M{x+6},{y-48} l4,14" stroke="{ACCENT}" stroke-width="4" fill="none" stroke-linecap="round"/>'


def coat(x, y):
    return f'<path d="M{x-12},{y-50} L{x+12},{y-50} L{x+16},{y-20} L{x-16},{y-20} Z" fill="#9aa6b8" stroke="{INK}" stroke-width="1.5"/>'


FWD = ((20, 12), (24, 8))        # both arms reaching forward (to the right), for typing
BACK = ((-20, 12), (-24, 8))

# ---------------------------------------------------------------- 2.1
p1 = (floor(270) + desk(190, 215, 140) + lamp(262, 215) + thermostat(232, 110)
      + person(80, 270, "pat", "worried", ((-6, 12), (6, 12)), extra=scarf(80, 270))
      + '<g stroke="#8ec5e8" stroke-width="1.8"><path d="M44,168 q-6,6 0,12"/><path d="M116,168 q6,6 0,12"/></g>'
      + bubble(14, 18, "Why is it freezing in here?", w=170, tail=(80, 160)))
p2 = ('<g transform="translate(150,178) scale(3.2) translate(-150,-178)">' + thermostat(150, 178, "smug") + '</g>'
      + label(150, 266, "29°C", fs=18, color=ACCENT, bold=True, font=SERIF)
      + bubble(12, 12, "Room temperature: 29°C. Heating: OFF. Everything is fine.", w=276, tail=(150, 110)))
p3 = (floor(270) + desk(4, 215, 100) + lamp(40, 215) + thermostat(78, 128)
      + coat(185, 270) + person(185, 270, "extra", "worried", ((-6, 12), (6, 12)))
      + coat(225, 270) + person(225, 270, "pat", "worried", ((-6, 12), (6, 12)))
      + coat(265, 270) + person(265, 270, "dee", "worried", ((-6, 12), (6, 12))))
COMICS["2-1"] = dict(number="2.1", title="The excellent model of the lamp", layout="row", pw=300,
                     panels=[p1, p2, p3],
                     caption="Every good regulator must be a model of the system. This one is an excellent model of the lamp.",
                     desc="Pat shivers in a scarf. The thermostat, next to a glowing lamp, reports 29°C and switches the heating off. Three people in coats huddle at the far end of the office.")

# ---------------------------------------------------------------- 10.1
code = ["def total(x):", "  return sum(x)", "", "def tax(x):", "  return x*0.2"]
clip = '<rect x="96" y="200" width="24" height="30" fill="#ffffff" stroke="#1a1a1a" stroke-width="1.5"/>'
q1 = (floor(270) + person(110, 270, "dee", "grin", ((-12, 14), (30, -4))) + clip
      + person(290, 270, "pat", "neutral", ("down", "down"), look=-2)
      + bubble(18, 18, "Unit 7 writes all the code now. You just check it!", w=230, tail=(110, 160)))
q2 = (cap_box("9:07 AM") + floor(270) + desk(150, 222, 200) + laptop(190, 222, code, w=104, h=62)
      + chair(110, 270) + person(110, 270, "pat", "smile", FWD, look=3, sitting=True)
      + bubble(40, 50, "Looks fine.", w=120, tail=(112, 160)))
q3 = (cap_box("4:52 PM") + floor(270) + desk(150, 222, 150) + laptop(180, 222, code, w=104, h=62)
      + chair(110, 270) + person(110, 270, "pat", "sleep", ((16, 30), (20, 26)), sitting=True)
      + zzz(128, 150) + unit7(335, 270, "grin", ("raise", "down"))
      + bubble(170, 18, "All 412 checks passed!", w=190, tail=(330, 150)))
q4 = (floor(270) + desk(150, 222, 150) + laptop(180, 222, code, w=104, h=62)
      + '<circle cx="268" cy="190" r="4.5" fill="#d9362b"/>'
      + '<g transform="rotate(-8 110 270)">' + chair(110, 270) + '</g>')
COMICS["10-1"] = dict(number="10.1", title="You just check it", panels=[q1, q2, q3, q4],
                      caption="Bainbridge, 1983: nobody can keep watching a display where little happens for more than about half an hour.",
                      desc="Dee tells Pat that Unit 7 writes the code and Pat just checks it. At 9:07 Pat says it looks fine. At 4:52 Pat is asleep while Unit 7 announces 412 passed checks. Final panel: an empty chair, and one small red dot on the screen.")
