"""Build the reading website for *Every Good Regulator* into ../docs (served by GitHub Pages).

Run from the repository root:   python site/build_site.py
Needs: pandoc on PATH. No other dependencies. Output is plain static HTML/CSS/JS.
"""
import html
import io
import json
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(ROOT, "manuscript")
OUT = os.path.join(ROOT, "docs")
SITE = os.path.join(ROOT, "site")
REPO = "https://github.com/hammadshakeelai/every-good-regulator"
DL = REPO + "/releases/latest/download/"

TITLE = "Every Good Regulator"
SUBTITLE = "Why the Systems That Run Our Work Fail — and How to Build Ones That Don't"
AUTHOR = "Muhammad Hammad Shakeel"

# (file, short label for navigation, kind)
ORDER = [
    ("00-prologue.md", "Prologue", "front"),
    ("01-the-forest-that-died.md", "1", "ch"), ("02-every-good-regulator.md", "2", "ch"),
    ("02a-what-if-thermostat.md", "What If?", "interlude"), ("03-the-jump.md", "3", "ch"),
    ("03a-what-if-todo-app.md", "What If?", "interlude"), ("04-the-viable-system.md", "4", "ch"),
    ("04b-exploded-view-company.md", "Exploded View", "ev"),
    ("05-compliant-and-fatal.md", "5", "ch"), ("06-the-fee-for-bug-reports.md", "6", "ch"),
    ("07-the-presumption.md", "7", "ch"), ("08-running-broken.md", "8", "ch"),
    ("09-the-model-you-copied.md", "9", "ch"), ("09b-exploded-view-alis.md", "Exploded View", "ev"),
    ("10-the-ironies-of-automation.md", "10", "ch"), ("10a-what-if-swap-jobs.md", "What If?", "interlude"),
    ("11-specify-or-explain.md", "11", "ch"), ("12-who-may-stop-the-line.md", "12", "ch"),
    ("12a-what-if-stop-the-company.md", "What If?", "interlude"), ("12b-exploded-view-factory.md", "Exploded View", "ev"),
    ("13-grow-it-dont-design-it.md", "13", "ch"), ("14-the-organisations-operating-system.md", "14", "ch"),
    ("15-your-own-operating-system.md", "15", "ch"), ("15b-exploded-view-personal.md", "Exploded View", "ev"),
    ("16-epilogue.md", "Epilogue", "back"), ("16b-acknowledgements.md", "Thanks", "back"),
    ("17-appendices.md", "Appendices", "back"), ("18-index.md", "Index", "back"),
    ("19-about-the-author.md", "Author", "back"),
]
PART_START = {"01-the-forest-that-died.md": "Part One — The Layer You Can't See",
              "05-compliant-and-fatal.md": "Part Two — How the Layer Fails",
              "10-the-ironies-of-automation.md": "Part Three — The Human in the Loop",
              "13-grow-it-dont-design-it.md": "Part Four — Layers That Work, at Every Scale"}

BOXES = {  # first bold words of a blockquote -> css class
    "WEIRD TRUE THING": "box-weird", "IN SMALL WORDS": "box-small", "THE MECHANISM": "box-mech",
    "MYTH": "box-myth", "AT THE MOVIES": "box-movies", "TRY IT YOURSELF": "box-try",
    "HOW THIS WAS COUNTED": "box-note", "BEER'S MAXIM": "box-note", "BEER’S MAXIM": "box-note",
}


def slug(fname):
    return re.sub(r"^\d+[ab]?-", "", fname[:-3])


def pandoc(md_text):
    p = subprocess.run(["pandoc", "-f", "markdown-yaml_metadata_block", "-t", "html5", "--wrap=none"],
                       input=md_text.encode("utf-8"), capture_output=True, check=True)
    return p.stdout.decode("utf-8")


def clean_md(s):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = s.replace("-portrait.png", ".png")                       # landscape Exploded Views on screen
    s = re.sub(r"\]\((figures|comics)/", r"](img/", s)            # flatten image paths
    s = s.replace("*The drawing is printed sideways: turn the book.*", "")
    s = s.replace(" The drawing is printed sideways: turn the book.", "")
    return s


def enhance(h):
    # images: lazy, async, zoomable
    h = re.sub(r"<img ", '<img loading="lazy" decoding="async" ', h)
    # boxes
    def box(m):
        inner = m.group(1)
        mm = re.match(r"\s*<p><strong>([^<]+)</strong>", inner)
        cls = ""
        if mm:
            key = mm.group(1).split(":")[0].strip().rstrip(".")
            cls = BOXES.get(key, "")
        if "<img" in inner and not cls:
            cls = "box-mech"
        return f'<blockquote class="box {cls} reveal">{inner}</blockquote>'
    h = re.sub(r"<blockquote>(.*?)</blockquote>", box, h, flags=re.S)
    # haiku: the blockquote after "The Haiku Line"
    h = re.sub(r'(<p><em>The Haiku Line</em></p>\s*)<blockquote class="box\s*(reveal)?">',
               r'\1<blockquote class="box haiku reveal">', h)
    # figures: pandoc wraps standalone images in <figure>
    h = h.replace("<figure>", '<figure class="reveal">')
    # external links open safely in a new tab
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    # section headings get anchors
    def anchor(m):
        lvl, attrs, text = m.group(1), m.group(2), m.group(3)
        idm = re.search(r'id="([^"]+)"', attrs)
        if not idm:
            return m.group(0)
        return f'<h{lvl}{attrs}><a class="anchor" href="#{idm.group(1)}" aria-hidden="true">#</a>{text}</h{lvl}>'
    h = re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", anchor, h)
    return h


def page_title(md):
    heads = re.findall(r"^# (.+)$", md, flags=re.M)
    for hd in heads:
        if not hd.startswith("Part "):
            return re.sub(r"\s*\{.*\}$", "", hd).strip()
    return heads[0] if heads else TITLE


def toc_items(pages, current):
    out, part = [], None
    for p in pages:
        if p["file"] in PART_START:
            out.append(f'<li class="toc-part">{html.escape(PART_START[p["file"]])}</li>')
        cls = ' class="current"' if p["slug"] == current else ""
        aria = ' aria-current="page"' if p["slug"] == current else ""
        out.append(f'<li{cls}><a href="{p["slug"]}.html"{aria}><span class="toc-k">{html.escape(p["label"])}</span>'
                   f'<span class="toc-t">{html.escape(p["short"])}</span></a></li>')
    return "\n".join(out)


def short_title(t):
    return re.sub(r"^(What If\? — |Exploded View \d — |\d+\. |Prologue — |Epilogue — )", "", t)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8", newline="").write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "img"))
    # assets
    for sub in ("figures", "comics"):
        d = os.path.join(MS, sub)
        for f in os.listdir(d):
            if f.endswith(".png") and "portrait" not in f:
                shutil.copy(os.path.join(d, f), os.path.join(OUT, "img", f))
    for f in ("style.css", "app.js"):
        shutil.copy(os.path.join(SITE, f), os.path.join(OUT, f))
    tpl = io.open(os.path.join(SITE, "page.html"), encoding="utf-8").read()
    home = io.open(os.path.join(SITE, "home.html"), encoding="utf-8").read()

    pages = []
    for f, label, kind in ORDER:
        md = io.open(os.path.join(MS, f), encoding="utf-8").read()
        t = page_title(md)
        pages.append({"file": f, "slug": slug(f), "label": label, "kind": kind, "title": t, "short": short_title(t), "md": md})

    search = []
    for i, p in enumerate(pages):
        body = enhance(pandoc(clean_md(p["md"])))
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        mins = max(1, round(words / 230))
        prev_p = pages[i - 1] if i > 0 else None
        next_p = pages[i + 1] if i + 1 < len(pages) else None
        nav = ('<nav class="pager" aria-label="Chapter navigation">'
               + (f'<a class="prev" href="{prev_p["slug"]}.html"><span>Previous</span><strong>{html.escape(prev_p["short"])}</strong></a>' if prev_p else '<a class="prev" href="index.html"><span>Back to</span><strong>The cover</strong></a>')
               + (f'<a class="next" href="{next_p["slug"]}.html"><span>Next</span><strong>{html.escape(next_p["short"])}</strong></a>' if next_p else '<a class="next" href="index.html"><span>Back to</span><strong>The cover</strong></a>')
               + "</nav>")
        page = (tpl.replace("{{TITLE}}", html.escape(p["title"]))
                   .replace("{{BOOK}}", TITLE)
                   .replace("{{KIND}}", p["kind"])
                   .replace("{{LABEL}}", html.escape(p["label"] if p["kind"] != "ch" else "Chapter " + p["label"]))
                   .replace("{{MINUTES}}", str(mins))
                   .replace("{{TOC}}", toc_items(pages, p["slug"]))
                   .replace("{{BODY}}", body)
                   .replace("{{PAGER}}", nav)
                   .replace("{{DL}}", DL).replace("{{REPO}}", REPO))
        write(os.path.join(OUT, p["slug"] + ".html"), page)
        search.append({"s": p["slug"], "t": p["title"], "k": p["label"]})

    # home page chapter grid
    cards, part = [], None
    for p in pages:
        if p["file"] in PART_START:
            cards.append(f'<h3 class="grid-part reveal">{html.escape(PART_START[p["file"]])}</h3>')
        kind_label = {"ch": "Chapter " + p["label"], "interlude": "Interlude", "ev": "Exploded View"}.get(p["kind"], p["label"])
        cards.append(f'<a class="card card-{p["kind"]} reveal" href="{p["slug"]}.html"><span class="card-k">{html.escape(kind_label)}</span>'
                     f'<span class="card-t">{html.escape(p["short"])}</span></a>')
    homepage = (home.replace("{{CARDS}}", "\n".join(cards)).replace("{{DL}}", DL).replace("{{REPO}}", REPO)
                    .replace("{{FIRST}}", pages[0]["slug"] + ".html").replace("{{TOC}}", toc_items(pages, "")))
    write(os.path.join(OUT, "index.html"), homepage)
    write(os.path.join(OUT, "pages.json"), json.dumps(search, ensure_ascii=False))
    write(os.path.join(OUT, ".nojekyll"), "")
    write(os.path.join(OUT, "404.html"), homepage.replace("<main", '<main data-404="1"', 1))
    print(f"built {len(pages)} pages into docs/")


if __name__ == "__main__":
    main()
