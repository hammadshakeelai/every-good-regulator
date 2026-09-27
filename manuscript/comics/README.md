# Comics — drawn drafts

These are 17 stick-figure strips, one for every `[COMIC …]` script in the manuscript. None appear in Chapter 7 or in the 737 MAX, Columbia and Therac sections, which are humour-free zones.

- `comiclib.py` holds the cast (PAT has messy hair; DEE has a bob and an orange lanyard; UNIT 7 is the boxy robot), the props, speech bubbles and strip layout.
- `comics_part1.py` to `comics_part3.py` hold one definition per strip.
- To build the SVGs, run `python build_comics.py [ids…]` from this folder.
- To render the PNGs used by the docx, run `bash ../figures/render.sh "$PWD"`.

Each chapter embeds the PNG and keeps the original panel script beside it as an HTML comment, so an illustrator can redraw from the script. These drafts are placeholders for a real illustrator. They are good enough to test timing and layout on the page.
