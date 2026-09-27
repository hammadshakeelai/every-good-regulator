# Every Good Regulator

**Why the Systems That Run Our Work Fail — and How to Build Ones That Don't**
*by Muhammad Hammad Shakeel*

**Read it online:** https://hammadshakeelai.github.io/every-good-regulator/
**Download:** [PDF](https://github.com/hammadshakeelai/every-good-regulator/releases/latest/download/EVERY-GOOD-REGULATOR.pdf) · [EPUB](https://github.com/hammadshakeelai/every-good-regulator/releases/latest/download/EVERY-GOOD-REGULATOR.epub) · [Word](https://github.com/hammadshakeelai/every-good-regulator/releases/latest/download/EVERY-GOOD-REGULATOR.docx)

Every organisation builds a second system on top of its work: the dashboards, platforms, reviews and compliance processes — and now the AI agents that write the code and the pipelines that check it. This book is about that layer, the *metasystem*, and why it fails in predictable ways. It is built on five ideas — **Model, Legibility, Remainder, Stop, Jump** — and draws on cybernetics, safety engineering, public inquiries and an original analysis of 240 published outage reports.

It includes 15 chapters, 4 "What If?" interludes, 4 "Dispatches from 2031" (clearly labelled fiction), 15 figures, 17 comic strips, 4 Exploded View drawings, and a haiku at the end of every chapter.

## What's in this repository

| Path | What it is |
|---|---|
| `manuscript/` | The book in Markdown, one file per chapter, plus figures, comics and the build scripts |
| `manuscript/build.sh` | Builds Word, EPUB and PDF (needs pandoc; the PDF step uses Microsoft Edge) |
| `site/` | The reading website's generator; `python site/build_site.py` writes `docs/` |
| `docs/` | The published website (GitHub Pages) |
| `research_notes/` | Research notes, source logs, the permissions log, and the Chapter 8 dataset |
| `research_notes/postmortem_tags_public.csv` | The Chapter 8 tags for all 240 incidents in [Dan Luu's list of post-mortems](https://github.com/danluu/post-mortems), with links to each report. Method in `postmortem_tagging_CODEBOOK.md` |

## Licence

© 2026 Muhammad Hammad Shakeel. All rights reserved. The book is free to read here; please don't republish it without permission.

The Chapter 8 tag data (`research_notes/postmortem_tags_public.csv`) and the codebook are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), so anyone can check or re-tag the analysis.

Quotations and cited facts belong to their original authors and are used with attribution; see each chapter's *Go Deeper* list and `research_notes/permissions_log.md`.
