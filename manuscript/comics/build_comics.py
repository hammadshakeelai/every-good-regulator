"""Build every comic strip to comics/comic-<n>.svg, then render PNGs with ../figures/render.sh-style Edge call.
Usage (from manuscript/comics):  python build_comics.py [id ...]
"""
import sys, os, io, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comiclib import strip

ALL = {}
for mod in ("comics_part1", "comics_part2", "comics_part3"):
    try:
        ALL.update(importlib.import_module(mod).COMICS)
    except ModuleNotFoundError:
        pass

want = sys.argv[1:] or sorted(ALL)
here = os.path.dirname(os.path.abspath(__file__))
for k in want:
    c = dict(ALL[k])
    svg = strip(c.pop("number"), c.pop("title"), c.pop("panels"), **c)
    path = os.path.join(here, f"comic-{k}.svg")
    io.open(path, "w", encoding="utf-8", newline="").write(svg)
    print("wrote", os.path.basename(path))
