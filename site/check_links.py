"""Check every internal link, anchor and image in docs/. Exit 1 on any broken one.
Run from the repository root: python site/check_links.py"""
import os, re, sys
from html.parser import HTMLParser

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")


class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        for k in ("href", "src"):
            if a.get(k): self.refs.append(a[k])


pages = {}
for f in os.listdir(DOCS):
    if f.endswith(".html"):
        p = P(); p.feed(open(os.path.join(DOCS, f), encoding="utf-8").read()); pages[f] = p
bad = []
for f, p in pages.items():
    for r in p.refs:
        if re.match(r"^(https?:|mailto:|data:|//)", r) or r == "#":
            continue
        path, _, frag = r.partition("#")
        target = path or f
        if not os.path.exists(os.path.join(DOCS, target)):
            bad.append(f"{f}: missing file {r}"); continue
        if frag and target in pages and frag not in pages[target].ids:
            bad.append(f"{f}: missing anchor {r}")
print(f"checked {len(pages)} pages, {sum(len(p.refs) for p in pages.values())} links/images")
if bad:
    print("\n".join(bad)); sys.exit(1)
print("all internal links, anchors and images resolve")
