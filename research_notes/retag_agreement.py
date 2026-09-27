"""Compare the blind re-tag of 50 random post-mortems (postmortem_retag_sample.csv) with the original tags."""
import csv, io, re, os
from collections import Counter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
orig = {r['n']: r for r in csv.DictReader(io.open('postmortem_tagging.csv', encoding='utf-8'))}
new = list(csv.DictReader(io.open('postmortem_retag_sample.csv', encoding='utf-8')))
tags = lambda s: set(t for t in re.split(r'[\s;,]+', s or '') if t)
N = len(new)
a = [orig[r['n']]['trigger'] for r in new]; b = [r['trigger'] for r in new]
po = sum(x == y for x, y in zip(a, b)) / N
ca, cb = Counter(a), Counter(b)
pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / N ** 2
print(f"Trigger: agreement {po:.0%}, Cohen's kappa {(po - pe) / (1 - pe):.2f}")
rows = []
for c in 'GDFRMHLPBCTS':
    A = [c in tags(orig[r['n']]['mechanism_tags']) for r in new]
    B = [c in tags(r['mechanism_tags']) for r in new]
    po = sum(x == y for x, y in zip(A, B)) / N
    pa, pb = sum(A) / N, sum(B) / N
    pe = pa * pb + (1 - pa) * (1 - pb)
    k = (po - pe) / (1 - pe) if pe < 1 else float('nan')
    rows.append((c, sum(A), sum(B), po, k))
    print(f"{c}: original {sum(A):2d}  re-tag {sum(B):2d}  agreement {po:.0%}  kappa {k:.2f}")
