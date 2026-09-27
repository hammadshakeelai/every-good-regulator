# Handoff — read this first after a context compaction (27 Sep 2026)

## The book
*Every Good Regulator: Why the Systems That Run Our Work Fail — and How to Build Ones That Don't.* It is a book on metasystems engineering, the "system that runs the system". It combines real-world stories from many people online with research, and aims to be an AAA illustrated book that is fun to read, in the manner of What If?, Thing Explainer and Eating Salad Drunk.

- Five words: Model, Legibility, Remainder, Stop, Jump.
- Structure: 4 Parts, 15 chapters, plus prologue, epilogue and appendices.
- Plans: `../planning/BOOK_PLAN.md` (spine, outline), `../planning/FUN_TOOLKIT.md` (fun devices and humour rules; **no jokes in ch. 7 or in the 737 MAX, Columbia and Therac sections**), `00-STYLE-SHEET.md`.

## State
- ~63,400 words across `00-prologue.md` … `17-appendices.md`. The status table is in `STATUS.md`.
- VERIFY markers: 74 → 2. Both are left for publication time: Suma figures (ch. 4) and Horizon compensation totals (ch. 7).
- Ch. 8 original analysis is done: `../research_notes/postmortem_tagging.csv` and `postmortem_tagging_CODEBOOK.md`, with the chart at `figures/fig-8-1-postmortems.svg`.
- Still open, and the author has to do these: 3 interviews (StrongDM ch. 10, Hoverstadt ch. 4, Larson ch. 13); 2 author experiments (ch. 10, 14); Horizon Volume 1 first-hand accounts (ch. 7, `[SOURCE]`).

## How to rebuild
From `manuscript/`, run `bash build.sh`, or `bash build.sh pdf` to include the PDF.
- The script concatenates `front-matter.md` with the explicit, ordered FILES list. Edit that list when you add files.
- It produces `EVERY-GOOD-REGULATOR-full-draft.md`, `EVERY-GOOD-REGULATOR.docx` (also copied to `-full-draft.docx`) and `EVERY-GOOD-REGULATOR.epub`. With `pdf`, it also produces `EVERY-GOOD-REGULATOR.pdf`: A5, printed from `build/book.html` by headless Edge.
- Title, subtitle, author and date live in `build/meta.yaml`. Author: Muhammad Hammad Shakeel.
- Page breaks before every level-1 heading come from `build/pagebreak.lua`.
- Word styles (Georgia) come from `build/reference.docx`; EPUB and PDF styling from `build/book.css`.
- Figures: `bash figures/render.sh`. Comics: `cd comics && python build_comics.py && bash ../figures/render.sh "$PWD"`. Exploded Views: `cd figures && python exploded.py && bash render.sh`.

## Done 27 Sep (after compaction)
- Four What If? interludes: `02a-what-if-thermostat.md`, `03a-what-if-todo-app.md`, `10a-what-if-swap-jobs.md`, `12a-what-if-stop-the-company.md`. Footnote labels are unique (`[^wi2-1]` etc.). Arithmetic uses only verified inputs or labelled assumptions.
- Four "Dispatches from 2031" inserted directly under each Part heading (01-, 05-, 10-, 13-). Fictional companies only (Brightwater Freight, Hollowmere Health Records, Kettle & Loom, Oakridge Mutual); Pat/Dee/Unit 7 as cast.
- Fixed a pre-existing build bug: the prologue heading was being swallowed into a table because front matter ended in `---` without a blank line.
- Draft now ~70,800 words.
- Figures drafted as SVG + 2x PNG (5 of ~15): 2.1 control loop, 3.1 staircase, 8.1 post-mortems, 12.1 signal vs stop, 12a.1 cord scope. `bash figures/render.sh` re-renders every `fig-*.svg` to PNG via headless Edge. Chapters embed the PNG with `![caption](figures/….png)`; the original illustrator brief is kept beside it as an HTML comment (invisible in the docx).

## Done 27 Sep (second pass)
- **All 15 figures** drafted in SVG + PNG and embedded (no `[FIGURE` placeholders left). Chapter 8's figures were renumbered: 8.1 is the post-mortem chart, 8.2 is the layers diagram.
- **All 17 comics** are drawn as stick-figure strips in `comics/` (see comics/README.md) and embedded. No `[COMIC` placeholders are left.
- `figures/render.sh [dir]` renders both `fig-*.svg` and `comic-*.svg`.

## Done 27 Sep (end-to-end pass, step 1: markers)
- Every `[VERIFY]`, `[INTERVIEW]`, `[AUTHOR EXPERIMENT]` and `[SOURCE]` marker is closed. None were closed by invention:
  - The interviews became honest "what we don't know yet" passages (ch4, ch10, ch13).
  - The experiments became TRY IT YOURSELF boxes (ch10, ch14).
  - Ch7 now paraphrases three Case Illustrations (Butoy, McDonald, Connolly) from Inquiry Volume 1 itself (`research_notes/sources/horizon_vol1.pdf/.txt`, paras 3.53–3.73 and 3.204–3.213).
  - Horizon figures were confirmed against gov.uk data as of 28 Aug 2026, with the later volumes still unpublished.
  - The Suma description was aligned to its own 2026 wording.
- Optional author enrichments remain: interviews with Hoverstadt, StrongDM and Larson; the author's own by-hand-day and meta-meeting results.

## Done 27 Sep (end-to-end pass, step 2: fun layer)
- Added Weird True Things to ch4, 5, 8, 11, 13, 14 and 15 (ch14's old "WTT" was a test, so it became a TRY IT box).
- Added haikus to the four interludes. **Appendix G, the Haiku Wall,** collects all 19 haikus in reading order.
- Added four **Exploded Views**: `figures/exploded.py` generates `fig-ev-1..4.svg`. The pages are `04b-`, `09b-`, `12b-` and `15b-exploded-view-*.md`, listed in build.sh and in the contents.
- Measured the text a reader sees (`pandoc -t plain | wc -w`): about 69,900 words.

## Done 27 Sep (end-to-end pass, steps 3–5)
- **Practitioner voices**, all from `research_notes/` entries with sources:
  - ch3: Gas Town, Cognition and Anthropic multi-agent lessons; Goldratt and Brooks.
  - ch4: DAOs and the VSM.
  - ch6: curl's bug bounty; Senge's beer game.
  - ch12: the Replit "freeze".
  - ch13: NHS NPfIT, Future Combat Systems, Sonos, Hashimoto, compound engineering.
  - ch14: Chaillan; the over-built ticketing system.
  - New sources were added to each chapter's Go Deeper.
- **Consistency:**
  - Appendix C regenerated verbatim from the chapters (70 rules).
  - Every Your Turn has a worked answer. Ch7 has none, by design.
  - Myth vs Record matches the chapter boxes.
  - Glossary expanded to 35 terms; the paragraph-merge fault is fixed.
  - The prologue now explains the interludes, Dispatches and Exploded Views.
- **Production:** metadata title page, auto TOC, page breaks, and DOCX, EPUB and PDF outputs (342 A5 pages).
- **Length as read:** ~72,500 words. This is below the old 95–110k plan, which was never a hard requirement. Everything the research supports is now in the book; more length needs new material (interviews or experiments), not padding.

## Done 27 Sep (polish round)
- Author name set: Muhammad Hammad Shakeel (build/meta.yaml).
- Copy-edit scan: spelling consistently British, no repeated-word typos.
- Trimmed duplicated retellings: Columbia in ch12, Healthcare.gov in ch12 and ch14 now point back to ch6 and ch8.
- Corrected the DORA fifth-metric year to 2024 (ch1, ch5).
- **Index** (`18-index.md`, 129 entries, by chapter) is generated automatically by `build/make_index.py`, and the build runs it.

## Done 27 Sep (close-read round)
- **ch7:** corrected an overstatement. The inquiry *records* families' accounts of 13 suicides and makes no definitive finding on cause. The opening now says ~1,000 were convicted, not "hundreds pursued".
- **ch8:** a visible designer note became a credit to James Reason. The ch8 Weird True Thing (Pathfinder patched on Mars) replaced a duplicate.
- **ch9:** a visible editorial note on Feynman's "cargo cult" became proper text.
- **ch4:** removed a duplicated Nabben/Zargham mention and fixed paragraph spacing.
- **ch6:** the "make reporting cheap" rule is reconciled with curl ("make triage strong").
- **ch13:** Every described accurately.
- **Prologue:** now mentions the index.
- Scanned the whole book: no visible bracketed notes remain.

## Done 27 Sep (completion round)
- **Cover:** `figures/cover.py` → cover.svg/png. The EPUB cover comes from `--epub-cover-image`; the PDF's first page from `build/cover.html`.
- **Dedication and fiction note** are in `front-matter.md`. **Acknowledgements** are in `16b-acknowledgements.md`, and **About the Author** in `19-about-the-author.md`; the bio was confirmed with the author.
- **Marketing pack:** `marketing/back-cover.md` (back cover, description, pitch, selling points, audience, comparable titles).
- **Permissions log:** `build/permissions_log.py` writes `../research_notes/permissions_log.md`. It finds 184 quotations; the only web quotation over 15 words (the AWS mechanism definition) is now paraphrased.
- **Post-mortem reliability:** a blind re-tag of 50 random entries gave trigger kappa 0.82 and main mechanism kappas of 0.63–1.00 (see the codebook). Ch8 reports it as a same-coder re-test.
- Page breaks now come before every level-1 heading, including the Prologue.

## Published (27 Sep 2026)
- **Repo (public):** https://github.com/hammadshakeelai/every-good-regulator. `.gitignore` keeps out the reference-book PDFs, the built files, downloaded sources, and the full tagging CSV (Luu's summaries are unlicensed). `postmortem_tags_public.csv` is the public version.
- **Website:** https://hammadshakeelai.github.io/every-good-regulator/. GitHub Pages serves it from `main:/docs`, and `python site/build_site.py` regenerates `docs/`. It is plain static HTML/CSS/JS: reveal-on-scroll, a reading-progress bar, dark mode, a mobile contents drawer, a zoom viewer, ←/→ keys, and resume-where-you-left-off. All motion is off under prefers-reduced-motion.
- **Release v1.0:** PDF, EPUB and DOCX are attached, and the site's download links use `releases/latest/download/`.
- **To publish an update:**
  1. `cd manuscript && bash build.sh pdf`
  2. `cd .. && python site/build_site.py`
  3. commit and push
  4. `gh release create v1.x manuscript/EVERY-GOOD-REGULATOR.{pdf,epub,docx}`

## Only the author can do (the book is otherwise complete)
1. (DONE) Author name, dedication, acknowledgements and About the Author. Add personal thanks to 16b if wanted.
2. Optional enrichments: interviews (Hoverstadt/SCiO, StrongDM, Larson); your own by-hand-day and meta-meeting results (the TRY IT boxes in ch10 and ch14).
3. An *independent* second coder for 50 post-mortems. The same-coder re-test is done: kappa 0.63–1.00.
4. A professional illustrator to redraw the 17 comics, 15 figures and 4 Exploded Views from the drafts. The scripts and briefs are kept as HTML comments beside each image.
5. Permissions check on quotes before commercial publication, and a final refresh of the Horizon figures (as of 28 Aug 2026) and METR/AI-tool claims at press time.

## Next (optional polish)
1. (DONE) Remaining figure SVGs in the same grammar (Georgia, accent #eb6834, greys, faint grid): 6.1 broken feedback loop, 10.1 automation loop + fading skill bar, 15.1 personal loop, 1.1 forest vs ledger, 4.1 VSM, 9.1 copied model, 11.1 triangle, 13.1 ladder, 14.1 three org charts, 8.1 layered defences; then 2a.1 is a comic, not a figure.
2. (DONE) Comics drawn as roughs. Later: a real illustrator redraws them from the scripts kept in the HTML comments.
3. Weird True Things (one per chapter), Haiku Wall, Exploded View briefs.
4. Practitioner-voice passes ("In the Field").
5. (DONE) Ch. 8 figure order: the embedded Figure 8.2 now sits above the Figure 8.1 placeholder. Renumber (ch8, STATUS, codebook, SVG/PNG names) or move one.
6. Fictional company names were checked by web search on 27 Sep: Meridian was renamed Hollowmere because real Meridian health bodies exist. Brightwater Freight, Kettle & Loom and Oakridge Mutual had no exact match.

## Alignment check (27 Sep)
The author's goals, in their words, were: real-world experiences of many people; the best stories from across the internet; ideas from existing books; an AAA book with images and fun elements (haikus, What If?); "complete the book … in as detail like a real book".

The last several sessions drifted towards **fact-checking**. It was necessary, and it caught real errors (the Cybersyn room, the Ohno date, the Valve misattribution), but it was not the main goal. What is still under-built:
- the fun layer: What If? interludes, Dispatches from 2031, the 4 Exploded View spreads, Weird True Things, the Haiku Wall;
- the visual layer: only 1 of ~14 figures and 0 of ~13 comics exist as drafts;
- length and voice: ~71k words against the plan's 95–110k (STATUS.md is the reference);
- more first-hand practitioner voices ("In the Field").

Priority from here: interludes and dispatches, then figure drafts (SVG) and comic scripts, then deeper practitioner-story passes.
