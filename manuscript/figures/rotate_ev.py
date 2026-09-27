"""Make portrait (rotated) copies of the Exploded View PNGs so each fills a full page, long side down."""
import os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
for n in (1, 2, 3, 4):
    im = Image.open(os.path.join(here, f"fig-ev-{n}.png"))
    im.rotate(90, expand=True).save(os.path.join(here, f"fig-ev-{n}-portrait.png"))
    print("rotated", n)
