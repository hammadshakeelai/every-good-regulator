"""Generate Appendix H — Index (by chapter) into 18-index.md.
Run from manuscript/: python build/make_index.py   (build.sh runs it automatically)
Each entry lists where the term appears: P = Prologue, 1–15 = chapters, 2a/3a/10a/12a = What If? interludes,
EV1–EV4 = Exploded Views, E = Epilogue. Dispatches count as part of the chapter that follows them.
"""
import io, re, glob, os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABEL = {"00": "P", "16": "E"}


def label(fname):
    k = fname.split("-")[0]
    if k in LABEL:
        return LABEL[k]
    if k.endswith("b"):
        return "EV" + {"04b": "1", "09b": "2", "12b": "3", "15b": "4"}[k]
    return k.lstrip("0")


def sortkey(l):
    order = ["P"] + [str(i) for i in range(1, 16)] + ["E"]
    base = re.match(r"(EV|P|E|\d+)", l).group(1)
    if l.startswith("EV"):
        return (100 + int(l[2:]), "")
    return (order.index(base) if base in order else 99, l)


# term -> list of regex patterns (case-sensitive unless marked with (?i))
TERMS = {
    # people
    "Allen, David": [r"David Allen"], "Appleton, Maggie": [r"Maggie Appleton"], "Ashby, W. Ross": [r"\bAshby\b"],
    "Bainbridge, Lisanne": [r"Bainbridge"], "Bates, Alan": [r"Alan Bates"], "Beck, Kent": [r"Kent Beck"],
    "Beer, Stafford": [r"Stafford Beer|\bBeer's\b|\bBeer\b(?! game)"], "Bezos, Jeff": [r"Bezos"], "Böckeler, Birgitta": [r"Böckeler"],
    "Brooks, Fred": [r"Fred Brooks"], "Chaillan, Nicolas": [r"Chaillan"], "Conant, Roger": [r"Conant"],
    "Cook, Richard": [r"Richard Cook|Richard I\. Cook|\bCook's\b"], "Dekker, Sidney": [r"Dekker"], "Deming, W. Edwards": [r"Deming"],
    "Dickerson, Mikey": [r"Dickerson"], "Ellsworth, Jeri": [r"Ellsworth"], "Feynman, Richard": [r"Feynman"],
    "Fournier, Camille": [r"Fournier"], "Gall, John": [r"\bGall\b|Gall's"], "Gawande, Atul": [r"Gawande"],
    "Geldreich, Rich": [r"Geldreich"], "Goedecke, Sean": [r"Goedecke"], "Goldratt, Eliyahu": [r"Goldratt"],
    "Goodhart, Charles": [r"Goodhart"], "Hashimoto, Mitchell": [r"Hashimoto"], "Huang, Jeff": [r"Jeff Huang|\bHuang's\b"],
    "Larson, Will": [r"Will Larson|\bLarson\b"], "Lemkin, Jason": [r"Lemkin"], "Leveson, Nancy": [r"Leveson"],
    "Mackworth, Norman": [r"Mackworth"], "Meadows, Donella": [r"Meadows"], "Medina, Eden": [r"Medina"],
    "Newton, Casey": [r"Casey Newton"], "Ohno, Taiichi": [r"Ohno"], "Orosz, Gergely": [r"Orosz"],
    "Osmani, Addy": [r"Osmani"], "Perrow, Charles": [r"Perrow"], "Pronovost, Peter": [r"Pronovost"],
    "Rasmussen, Jens": [r"Rasmussen"], "Scott, James C.": [r"James C\. Scott|\bScott's\b|\bScott\b"], "Senge, Peter": [r"Senge"],
    "Stenberg, Daniel": [r"Stenberg"], "Strathern, Marilyn": [r"Strathern"], "Toyoda, Sakichi": [r"Toyoda"],
    "Turchin, Valentin": [r"Turchin"], "Vik, Tomas": [r"Tomas Vik|\bVik's\b"], "Walker, Jon (Suma)": [r"\bWalker\b"],
    "Westenberg, Joan": [r"Westenberg"], "Widrich, Leo": [r"Widrich"], "Williams, Sir Wyn": [r"Wyn Williams"],
    "Yegge, Steve": [r"Yegge"],
    # organisations and cases
    "737 MAX (Boeing)": [r"737 MAX"], "ALIS (F-35 logistics system)": [r"\bALIS\b"], "Amazon": [r"Amazon"],
    "Anthropic": [r"Anthropic"], "Backstage": [r"Backstage"], "Buffer": [r"\bBuffer\b"], "Cloudflare": [r"Cloudflare"],
    "Cognition": [r"Cognition\b"], "Columbia (space shuttle)": [r"Columbia\b"], "curl": [r"\bcurl\b"],
    "Cybersyn, Project": [r"Cybersyn"], "Every (compound engineering)": [r"\bEvery, gave|Every's"],
    "Future Combat Systems": [r"Future Combat"], "Gas Town": [r"Gas Town"], "GitHub": [r"GitHub"],
    "Google": [r"Google\b"], "Healthcare.gov": [r"Healthcare\.gov"], "Horizon (Post Office)": [r"Horizon\b"],
    "Kessel Run": [r"Kessel Run"], "Mars Polar Lander": [r"Polar Lander"], "Medium": [r"\bMedium\b"],
    "Meta": [r"\bMeta\b"], "METR": [r"\bMETR\b"], "NHS National Programme for IT": [r"National Programme for IT"],
    "NUMMI": [r"NUMMI"], "Overleaf": [r"Overleaf"], "Phoenix pay system": [r"Phoenix\b"], "Replit": [r"Replit"],
    "Robodebt": [r"Robodebt"], "SCiO": [r"SCiO"], "Segment": [r"\bSegment\b"], "Sonos": [r"Sonos"],
    "Spotify": [r"Spotify"], "Stripe": [r"Stripe"], "StrongDM": [r"StrongDM"], "Suma": [r"\bSuma\b"],
    "Tesla": [r"Tesla"], "Therac-25": [r"Therac"], "Toyota": [r"Toyota"], "Valve": [r"\bValve\b"], "Zappos": [r"Zappos"],
    # ideas
    "algedonic signal": [r"(?i)algedonic"], "andon cord": [r"(?i)\bandon\b"], "backchannel": [r"(?i)backchannel"],
    "beer game": [r"beer game"], "compound engineering": [r"(?i)compound engineering"], "constraint (Goldratt)": [r"Goldratt"],
    "dark factory": [r"(?i)dark factory"], "error budget": [r"(?i)error budget"], "Gall's law": [r"Gall's law"],
    "golden path / paved road": [r"(?i)golden path|paved road"], "Goodhart's law": [r"Goodhart's law"],
    "harness engineering": [r"(?i)harness engineering"], "holdout scenarios": [r"(?i)holdout"],
    "intent specification": [r"(?i)intent specification"], "jidoka": [r"(?i)jidoka"], "Jump (the fifth word)": [r"\*\*Jump\*\*|\bJump\b"],
    "latent failure": [r"(?i)latent (flaw|failure)"], "Legibility": [r"(?i)\blegib"], "mechanisms (Amazon)": [r"(?i)mechanisms? over intentions|Mechanisms do"],
    "metasystem transition": [r"(?i)metasystem transition"], "metis": [r"(?i)\bmetis\b"], "Model (the first word)": [r"\*\*Model\*\*"],
    "normal accidents": [r"(?i)normal accident"], "red bead experiment": [r"(?i)red bead"], "Remainder": [r"(?i)\bremainder\b"],
    "requisite variety": [r"(?i)requisite variety|only variety can absorb variety"], "reward hacking": [r"(?i)reward hacking"],
    "root cause": [r"(?i)root cause"], "second brain": [r"(?i)second brain"], "single-threaded leader": [r"(?i)single-threaded"],
    "software factory": [r"(?i)software factor(y|ies)"], "spec-driven development": [r"(?i)spec-driven"],
    "Stop (the fourth word)": [r"\*\*Stop\*\*|stop the line"], "two-pizza teams": [r"(?i)two-pizza"],
    "viable system model": [r"(?i)viable system"], "Zettelkasten": [r"Zettelkasten"],
}

files = sorted(f for f in glob.glob(os.path.join(HERE, "[01][0-9]*.md"))
               if not re.search(r"STYLE|appendices|index|full-draft|acknowledg|about-the-author", f))
texts = {}
for f in files:
    s = io.open(f, encoding="utf-8").read()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"\n## Go Deeper.*?(?=\n---|\Z)", "", s, flags=re.S)   # don't index reading lists
    texts[label(os.path.basename(f))] = s

out = ["# Index", "",
       "*References are to chapters, not pages: P = Prologue; 1–15 = chapters; 2a, 3a, 10a, 12a = What If? interludes; EV1–EV4 = Exploded Views; E = Epilogue.*", ""]
entries = []
for term, pats in TERMS.items():
    hits = [lab for lab, s in texts.items() if any(re.search(p, s) for p in pats)]
    if hits:
        entries.append((term, sorted(set(hits), key=sortkey)))
entries.sort(key=lambda e: re.sub(r"[^a-z0-9 ]", "", e[0].lower()))
cur = None
for term, hits in entries:
    first = term[0].upper() if term[0].isalpha() else "#"
    if first != cur:
        out += ["", f"**{first}**", ""]
        cur = first
    out.append(f"{term} — {', '.join(hits)}  ")
io.open(os.path.join(HERE, "18-index.md"), "w", encoding="utf-8", newline="").write("\n".join(out) + "\n")
print(len(entries), "index entries")
