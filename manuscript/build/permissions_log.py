"""Write ../research_notes/permissions_log.md: every direct quotation of 4+ words, flagging those over 15 words.
Run from manuscript/: python build/permissions_log.py"""
import io, re, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rows = []
for f in sorted(glob.glob('[01][0-9]*.md')):
    if re.search('STYLE|index|acknowledg', f):
        continue
    s = re.sub(r'<!--.*?-->', '', io.open(f, encoding='utf-8').read(), flags=re.S)
    for line in s.split('\n'):
        for m in re.finditer(r'"([^"]{3,400}?)"', line):
            q = m.group(1)
            if len(q.split()) >= 4:
                rows.append((f, len(q.split()), q))
long = [r for r in rows if r[1] > 15]
out = ["# Permissions log — direct quotations", "",
       "Every direct quotation of four words or more in the manuscript, by file. Regenerate with `python build/permissions_log.py`.", "",
       "- **House rule** (style sheet): quotations should be under 15 words and attributed.",
       "- **What is generally reusable with attribution:** epigraphs, and quotations from official reports and court judgments. UK Parliamentary and court material falls under the Open Parliament Licence and the Open Justice Licence; US federal works are public domain.",
       "- **What may need permission** for a commercial edition, depending on length and the publisher's fair-dealing policy: quotations from books, articles, blogs and newsletters.",
       "- Titles of essays and articles also appear in quotation marks and need no permission. Nor do lines spoken by fictional characters in the Dispatches, or Myth statements, which quote popular claims.",
       f"- **Total:** {len(rows)} quoted strings; **{len(long)} over 15 words** (listed first).", "",
       "## Over 15 words — check first", "", "| File | Words | Quotation |", "|---|---|---|"]
out += [f"| {f} | {w} | {q[:220].replace('|', '/')} |" for f, w, q in long]
out += ["", "## All quotations (4+ words)", "", "| File | Words | Quotation |", "|---|---|---|"]
out += [f"| {f} | {w} | {q[:160].replace('|', '/')} |" for f, w, q in rows]
io.open('../research_notes/permissions_log.md', 'w', encoding='utf-8', newline='').write("\n".join(out) + "\n")
print(len(rows), "quotations;", len(long), "over 15 words")
