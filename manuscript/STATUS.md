# Manuscript status — 27 September 2026 (complete draft)

**Complete, end to end.** ~73,800 words as read; 0 open markers. Includes a cover, dedication, acknowledgements, About the Author, an index, 15 figures, 17 comics and 4 Exploded Views. Outputs: `EVERY-GOOD-REGULATOR.docx`, `.epub` and `.pdf` (`bash build.sh pdf`). Marketing copy is in `marketing/back-cover.md`; the permissions log is in `research_notes/permissions_log.md`.

| # | File | Title | Words | Open [VERIFY] |
|---|---|---|---|---|
| P | 00-prologue.md | The Scoreboard | 2,371 | 0 |
| 1 | 01-the-forest-that-died.md | The Forest That Died | 3,240 | 0 |
| 2 | 02-every-good-regulator.md | Every Good Regulator | 3,882 | 0 |
| 3 | 03-the-jump.md | The Jump | 3,645 | 0 |
| 4 | 04-the-viable-system.md | The Viable System | 4,123 | 1 |
| 5 | 05-compliant-and-fatal.md | Compliant and Fatal | 3,556 | 0 |
| 6 | 06-the-fee-for-bug-reports.md | The Fee for Bug Reports | 3,268 | 0 |
| 7 | 07-the-presumption.md | The Presumption | 3,140 | 1 |
| 8 | 08-running-broken.md | Running Broken | 5,255 | 0 |
| 9 | 09-the-model-you-copied.md | The Model You Copied | 3,359 | 0 |
| 10 | 10-the-ironies-of-automation.md | The Ironies of Automation | 6,210 | 0 |
| 11 | 11-specify-or-explain.md | Specify or Explain | 3,218 | 0 |
| 12 | 12-who-may-stop-the-line.md | Who May Stop the Line | 3,986 | 0 |
| 13 | 13-grow-it-dont-design-it.md | Grow It, Don't Design It | 3,596 | 0 |
| 14 | 14-the-organisations-operating-system.md | The Organisation's Operating System | 3,492 | 0 |
| 15 | 15-your-own-operating-system.md | Your Own Operating System | 2,947 | 0 |
| 2a | 02a-what-if-thermostat.md | What If? Thermostat (Mars Polar Lander) | 1,610 | 0 |
| 3a | 03a-what-if-todo-app.md | What If? To-do app (Turchin, geometric series) | 1,405 | 0 |
| 10a | 10a-what-if-swap-jobs.md | What If? Swap jobs (Bainbridge, Mackworth) | 1,397 | 0 |
| 12a | 12a-what-if-stop-the-company.md | What If? Stop the company (cord scope arithmetic) | 1,283 | 0 |
| E | 16-epilogue.md | Back to the Scoreboard | 1,122 | 0 |
| A | 17-appendices.md | Appendices A–F | 3,731 | 0 |

## Open items before this is submission-ready

- **2 `[VERIFY]` markers** (down from 74), both deliberately left for publication time: Suma's current figures (ch. 4) and the Horizon compensation totals and inquiry volumes (ch. 7). Everything else has been checked against a primary source, including on 27 Sep:
  - Scott, *Seeing Like a State* (Yale, 1998): epigraph verbatim (p. 11); forest story (pp. 19–20), which gives a sharper figure (20–30% production loss) than the draft had.
  - Medina (2006 article): the Cybersyn **operations room never became operational**. The chapter now says so.
  - Ohno's own chronology: andon and line stop on the main plant's line in **1955**, not "the 1960s". Ohno also supplied the ch. 12 epigraph ("There is no reason to fear a line stop", p. 128).
  - Gawande (*New Yorker*, 2007, via the Internet Archive): the Pronovost checklist story, now a new ch. 12 section.
  - Fournier's own 2020 essay (ch. 13).
  - *Working Backwards* p. 75, plus consistent independent reviews (ch. 14 and appendix).
  - Horizon Common Issues judgment [2019] EWHC 606 (QB), full text from the National Archives: paras 653, 705–706, 1108 (ch. 7).
  - **Corrected misattribution (ch. 14):** "a hidden layer of powerful management" was Jeri Ellsworth in 2013, not Rich Geldreich. Geldreich's 2018 tweets did not name Valve. This is now fixed.
- **Original analysis done (ch. 8):** all 240 post-mortems tagged. The dataset is `research_notes/postmortem_tagging.csv`, the method and results are in `postmortem_tagging_CODEBOOK.md`, and the draft chart is `figures/fig-8-1-postmortems.svg`. **Before publication, have a second person re-tag a random 50** and report the agreement rate.
- **3 `[INTERVIEW]` slots**: StrongDM (ch. 10), Patrick Hoverstadt/SCiO (ch. 4), Will Larson (ch. 13).
- **2 `[AUTHOR EXPERIMENT]` slots**: ch. 10 and ch. 14 (plus the Foer-style thread in FUN_TOOLKIT.md §H).
- **1 `[SOURCE]` placeholder**: the Horizon inquiry's first-hand accounts (ch. 7, Volume 1). Handle with care.
- **Dispatches from 2031**: done — one page of labelled fiction under each Part heading (in 01-, 05-, 10-, 13-).
- **Figures and comics**: all 15 figures and all 17 comic strips are drafted and embedded in the docx (`figures/`, `comics/`; render with `bash figures/render.sh [dir]`). These are roughs for an illustrator to redraw.

## Where the length will grow

The draft is ~70,800 words against the plan's 95–110k. The gap is not padding to be added; it is the material research could not supply: interviews (roughly 1,000–2,000 words per chapter where used), the author's own experiments and voice, the original post-mortem analysis, and the What If? interludes and "Dispatches from 2031" planned in FUN_TOOLKIT.md. A finished length of 75–90k is realistic.
