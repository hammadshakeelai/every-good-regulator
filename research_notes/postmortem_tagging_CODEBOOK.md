# Post-mortem tagging — codebook and method

**Dataset:** `postmortem_tagging.csv` — all 240 incident entries in Dan Luu's *A List of Post-mortems!* (github.com/danluu/post-mortems, README as of the last commit, 31 Aug 2026). The six incident sections are Config Errors (59), Hardware/Power Failures (15), Conflicts (11), Time (5), Database (12) and Uncategorized (138). The "Other lists", "Analysis" and "Contributors" sections are excluded.

**Coded:** 26–27 Sep 2026, by a single coder, from the **one-line summaries in the list**, not the full reports. A tag is applied only when the summary supports it. Each incident has one trigger and any number of mechanism tags.

## Trigger (one per incident)
| Code | Meaning |
|---|---|
| CH | A change: deploy, configuration change, upgrade, migration, new rule or feature |
| OP | A manual operation by a person: maintenance, debugging, a command, a button |
| LD | Load or growth: traffic spike, capacity limit, counter/ID exhaustion |
| HW | Hardware, power, cooling, weather, fire |
| TM | Time: leap seconds, dates, certificate expiry |
| EX | External: a supplier or upstream outage, an attack or breach |
| UN | Not stated in the summary |

## Mechanism tags (any number)
| Code | Meaning |
|---|---|
| G | **Governing-layer error spread widely** — a fault in the layer that configures, provisions, deploys, routes or controls other systems (config systems, control planes, orchestration, admin tooling, automated jobs), reaching far beyond its origin |
| D | **Silent default / unchecked input** — a blank field, default value, generated file or bad data accepted without validation, or a limit silently changed |
| F | **Feedback failed** — tests, monitoring, alarms, bug triage or review missed or masked the problem, or detection was late or misleading |
| R | **Recovery impeded** — rollback failed, recovery tools depended on the failed system, the fix caused new harm, or restoration took unusually long |
| M | **Manual rescue** — the summary says people restored service by hand (manual capacity, hand-deploys, restarts, remote patches) |
| H | **Human action triggered it** — a typo, wrong command, wrong button, accidental deletion |
| L | **Latent flaw activated** — a defect present beforehand, exposed by a change, condition or load |
| P | **A protective or automated mechanism caused or worsened it** — failover, health checks, throttles, retries, cleanup jobs, safety rules, security tooling |
| B | **Backup or redundancy failed** when needed |
| C | **Cascade** — the failure spread across services, dependencies or sites |
| T | **Time-related coupling** |
| S | **Security incident** (breach, leak, attack) |

## Results (n = 240)
- Triggers: change 96 (40%) · external 37 (15%) · manual operation 27 (11%) · not stated 26 (11%) · load 25 (10%) · hardware/power 24 (10%) · time 5 (2%).
- Mechanisms: cascade 99 (41%) · latent flaw 94 (39%) · governing-layer error 53 (22%) · protective mechanism caused/worsened 41 (17%) · feedback failed 38 (16%) · silent default/unchecked input 31 (13%) · recovery impeded 21 (9%) · human action triggered 20 (8%) · security 18 (8%) · manual rescue 16 (7%) · backup failed 13 (5%) · time 5 (2%). 13 entries had no mechanism tag (summary too thin).
- Combinations: protective mechanism **or** failed backup: 49 (20%). Governing-layer errors that also cascaded: 30 of 53. Of the 96 change-triggered incidents, 36 involved a governing-layer error and 46 activated a latent flaw.
- Organisations: 104 distinct; most frequent Cloudflare 25, Google 20, Amazon 19, GitHub 19, CircleCI 10.

## Re-test reliability (27 Sep 2026)
A random 50 entries (seed 20260927) were re-tagged blind from their summaries, without looking at the original tags (`postmortem_retag_sample.csv`; compute with `retag_agreement.py`).
- **Trigger:** 86% agreement, Cohen's kappa 0.82.
- **Mechanisms (kappa):** governing layer G 0.83 · latent flaw L 0.92 · cascade C 0.78 · defence P 0.65 · feedback F 0.63 · silent default D 0.63 · human H 1.00 · backup B 1.00 · security S 0.88. Rare tags (R, M, T) are too few to judge.
- The re-tag was slightly more conservative on P (7 vs 10) and C (15 vs 20). The headline direction holds (defences > human error), but treat P as the least stable count.
- **This is intra-rater (test–retest) reliability, not inter-rater.** The same method and coder produced both passes, so an independent second coder is still recommended before publication.

## Limits (state these wherever the numbers appear)
1. **Not a sample of failures.** It is a list of *published* post-mortems, curated by volunteers. Companies that publish well (Cloudflare, Google, AWS, GitHub) dominate; famous historical disasters are over-represented.
2. **Summaries, not reports.** One-line summaries omit most contributing factors, so every mechanism count is a *floor*. Manual rescue in particular is almost certainly undercounted: summaries rarely mention it.
3. **One coder.** A blind re-test on 50 random entries gave kappa 0.63–1.00 for the main tags (see above), but there is no inter-rater check yet. An independent second coder should re-tag a random 50 before publication, and the tags should be shared openly so readers can check them.
4. Counts describe what the list's summaries *say*, not the true causes of any incident.
