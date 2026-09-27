# SUPERSEDES — read this before using any other file in this folder

Six research files sit in this folder. They were written across two rounds and **they contradict each other in places**, because the second round verified claims the first round had to take on trust. This file lists every claim that has been retired, corrected or replaced.

**Precedence rule:** where files disagree, `gap_fill_round2.md` (23 September 2026) wins. It is the latest and it was checked against primary sources.

Files, in the order they were written:
1. `term_genealogy.md` — what "metasystem" means across fields
2. `existing_books_gap.md` — 34 comparable books and the gap
3. `practitioner_experiences.md` — online stories, Themes 1–4
4. `systems_that_build_systems.md` — platforms, factories, agents 2024–2026
5. `practitioner_experiences_part2.md` — online stories, Themes 5–8
6. `market_positioning.md` — audience, comps, publishing, rights
7. `gap_fill_round2.md` — verification rounds 2 and 3; **wins on conflict with files 1–6**
8. `canonical_stories_and_book_ideas.md` — round 4: the durable cases (Bezos mandate, NUMMI, Columbia, Boeing MAX, Post Office Horizon, Perrow/Dekker) in Part A, and what 18 comparable books contribute in Part B
9. `free_primary_sources.md` — round 5: legitimately free primary material — 245 curated incident post-mortems and the resilience-engineering bibliography on GitHub, Cook's "How Complex Systems Fail" read in full, Leveson's open-access book and STAMP, Therac-25, Ashby's *Introduction to Cybernetics*

### 13. "The good regulator theorem is the neglected spine" — CORRECTED (Leveson read, 23 Sep 2026)
- **Where it appears:** item 5 above; `gap_fill_round2.md` §7 and §19; item 12's "two big ideas".
- **Why it fails:** Nancy Leveson's *Engineering a Safer World* (MIT Press, open access, CC BY-NC-ND) cites Conant & Ashby and builds the idea into STAMP as the "model condition" — every controller must contain a model of the process it controls; accidents occur when the model does not match the process. Applied at every organisational level and to development processes. Taught at MIT, used on real programmes.
- **What replaces it:** the theorem is **not** neglected in safety engineering; it **is** neglected in software management, platform engineering, organisational design and AI-agent practice. The book extends Leveson's control view to every layer we build to run our work, and adds three things she does not centre: **Scott** (why models go wrong systematically), **Bainbridge** (what automation does to the human controller), **Turchin** (layers that build other layers).
- **Bonus:** Leveson's *intent specifications* reconcile StrongDM's outcome-spec school and Goedecke's intent school (item 12's "live disagreement").
- **See:** `free_primary_sources.md` §7.

---

## Retired and corrected claims

### 1. "Nobody connects Stafford Beer's cybernetics to platforms or AI agents" — RETIRED
- **Where it appears:** `market_positioning.md` (the rationale for the recommended "Builders of Builders" positioning); `existing_books_gap.md` (the a × b gap claim).
- **Why it fails:** *Team Topologies* — the most influential book in the space — cites Beer's *Brain of the Firm* (2nd ed., 1995) and Wiener's *Cybernetics* (1961) in its published bibliography. Its lead author, Matthew Skelton, holds a BSc in computer science and **cybernetics**. Verified against the authors' own reference repository.
- **What replaces it:** *the lineage is acknowledged and unused.* Beer appears once, in a bibliography; the book's working apparatus is Conway's law and cognitive load. Ashby, requisite variety, the viable system model and the good regulator theorem are all absent from that bibliography (verified by substring count; the two "requisite" hits are false positives inside "MicroservicePrerequisites"). Proposal line: *Team Topologies put cybernetics in the bibliography; this book puts it to work.*
- **Why the replacement is better:** it is checkable, it is modest, and it proves the audience already accepts the ancestry.
- **See:** `gap_fill_round2.md` §10.

### 2. StrongDM spends "$1,000 per engineer per day" on tokens — CORRECTED
- **Where it appears:** `practitioner_experiences_part2.md`, Theme 6.
- **The correction:** that figure is **advice their essay gives readers** ("if you haven't spent at least $1,000 on tokens today per human engineer, your factory has room to improve"), not spend StrongDM reports for itself. Stating it as their cost is a factual error.
- **Also established:** the StrongDM AI team formed 14 July 2025 (Justin McCarthy, Jay Taylor, Navan Chauhan); code must not be written or reviewed by humans; verification is by scenarios held outside the codebase as a holdout set; their metric is "satisfaction"; they publish **no** outcome data and admit no downsides; Simon Willison is publicly sceptical of the economics.
- **See:** `gap_fill_round2.md` §6.

### 3. METR's "-18%" means developers got faster — CLOSED AS UNUSABLE, do not relitigate
- **Where it appears:** `practitioner_experiences_part2.md`, Theme 6, flagged as uncertain; reversed twice since.
- **The ruling:** METR's page never defines the sign. The surrounding prose points to *faster*, but the confidence interval crosses zero and METR itself calls the estimate unreliable and likely a lower bound. **Put no direction from the 2026 update in the book.**
- **Cite instead:** the 2025 finding (AI made tasks take 19% longer, CI +2% to +39%) and the far better story — METR is redesigning the experiment because developers now refuse to work without AI at $50/hour, and 30–50% withheld exactly the tasks where AI would help most. The measurement system lost track of what it measured.
- **See:** `gap_fill_round2.md` §1.

### 4. Joan Westenberg's "I deleted my second brain" could not be verified — RESOLVED
- **Where it appears:** `practitioner_experiences_part2.md`, Theme 8 (her page 404'd).
- **Resolution:** existence and date (28 June 2025) confirmed via the Hacker News thread discussing it (598 points, 348 comments). Her own page still 404s; cite the HN thread alongside it.
- **See:** `gap_fill_round2.md` §8.

### 5. The book's spine is the four-part "metasystem test" invented in the genealogy notes — SUPERSEDED
- **Where it appears:** `term_genealogy.md` §8 (the verdict), which states plainly that no published source unifies the three meanings and that the test is original to those notes.
- **What replaces it:** **Conant and Ashby's good regulator theorem** (1970, *International Journal of Systems Science*, 1,700+ citations): every good regulator of a system must be a model of that system. It is citable, formal, and maps onto five chapters — platform teams that don't model their users, harnesses that don't model the codebase, metrics that don't model the work, METR's experiment that stopped modelling developer behaviour, personal systems that don't model how you actually work. Pair it with Turchin's metasystem transition for the *verb* (a jump to a new controlling level).
- **Keep the four-part test** as an inclusion filter for what counts as a metasystem; it just isn't the spine.
- **Known caveat, and an asset:** it is debated whether the 1970 paper proves its own slogan; the mapping is a homomorphism, not an isomorphism. Stating that honestly answers the "too abstract, no rigour" complaint that dominates reviews of comparable books.
- **See:** `gap_fill_round2.md` §7.

### 6. Theme 5 (cybernetics in practice) is nearly empty — SUPERSEDED
- **Where it appears:** `practitioner_experiences_part2.md`, Theme 5, "the weakest theme".
- **What changed:** it was a search problem, not an absence. VSM practice lives in an organised professional community: **SCiO**, the UK professional body for systems practitioners, with the SysPrac conference series, learning circles and accreditation; **Patrick Hoverstadt**, who chairs it, consults on VSM and wrote *The Fractal Organization* plus a practitioner manual; **Espejo and Harnden's** 1989 casebook; and **Metaphorum 2026**, the Beer centenary conference held 17–19 September 2026 with a festschrift and journal special issue.
- **Still true:** no publicly documented 2020–2026 VSM implementation with outcome data. That absence is itself a finding, and an argument for doing interviews.
- **See:** `gap_fill_round2.md` §13.

### 7. Reddit gaps can be closed in a later research round — RETIRED
- **Where it appears:** as an open gap in nearly every first-round file.
- **Why it fails:** Reddit is unreachable from this pipeline by every route — it blocks the web crawler, the browser pane refuses it, and the `agent-reach` CLI is not installed. Hacker News has been substituted for the engineering themes.
- **Consequence:** the author must gather Reddit material by hand, or the book proceeds without it. The themes that suffer most are platform teams disbanded, metric gaming, and abandoned personal systems — and the corpus now has **no non-engineer voice** for the personal-systems theme.
- **See:** `gap_fill_round2.md` §0.

### 8. The book has eight themes — NOW NINE
- **Added:** Theme 9, *skill atrophy and the market trap* — the automating layer degrades the humans who must supervise it, and once the market prices the tool in, opting out stops being an individual choice. Sourced from the May 2026 "Agentic Coding Is a Trap" discussion (463 points, 375 comments).
- **Why it matters:** it is the bridge between the AI chapters and the personal-systems chapter, and it has a precise cybernetic reading — a supervisor who can no longer model the system is, by the good regulator theorem, exactly when governance fails.
- **See:** `gap_fill_round2.md` §12.

### 9. Zappos "18% of staff quit over holacracy" — VERIFIED, but the wording must change
- **Where it appears:** `practitioner_experiences.md`, Theme 3, flagged as needing primary confirmation.
- **Verified:** COO Arun Rajan told staff that 260 people had left since March 2015, about 18% of the company. The first buyout was taken by ~210 of ~1,500 (14%); a second "Super Cloud Teal" offer added ~50. Reported January 2016 by the Review-Journal, TIME, the Washington Post, HR Dive and Fortune.
- **The nuance that matters:** these were **paid buyouts the company offered to anyone who did not want the new system**, not ordinary attrition. "18% quit over holacracy" overstates it. The accurate version is more interesting: the organisation deliberately bought out its own dissenters.
- **See:** `gap_fill_round2.md` §17.

### 10. Backstage adoption figures — DO NOT CITE ANY OF THEM
- **Where they appear:** `systems_that_build_systems.md` (3,000+ adopting companies, ~10% internal usage at non-Spotify adopters, both flagged unverified).
- **What round 3 found:** two 2025–2026 sources differ by more than twelvefold — 270+ organisations in production (platformengineering.com, September 2025, no citations) versus 3,400+ organisations and 89% market share (vendor-side, January 2026). Neither states a method.
- **Use instead:** the staffing estimate — 2–5 full-time engineers for years, some reports up to 20 experts over a multi-year horizon. It is the decision-relevant number and nobody quotes it.
- **And note the finding:** the layer that measures everything else is itself unmeasured, and its public statistics are produced by the companies selling into it. That belongs in the book.
- **See:** `gap_fill_round2.md` §14.

### 11. F-35 ALIS — now sourced to GAO, with two figures still unsafe
- **Where it appears:** `practitioner_experiences.md`, Theme 4, where the GAO PDF could not be parsed.
- **Now sourced:** GAO-20-316 (March 2020) and GAO-20-665T (July 2020). Personnel at all five locations GAO visited reported parts records frequently incorrect, corrupt or missing, causing ALIS to ground flight-ready aircraft; squadron leaders sometimes overrode it and absorbed the risk; there were no performance-measurement processes for ALIS, and DOD could not tell how ALIS affected fleet readiness. GAO's recommendation to start measuring that closed only in April 2026.
- **RESOLVED — both circulating figures are wrong.** The full report was read on 23 Sep 2026. **"45,000 hours" does not appear in it at all**; the sourced figure is **5,000–10,000 hours per year at one location**, spent manually tracking data ALIS should have captured. **"$16.7 billion" is imprecise**: GAO reported in 2016 that DOD estimated ALIS at approximately **$17 billion** and that the estimate **was not fully credible**, because DOD ran no uncertainty or sensitivity analyses. Better than either: the F-35 programme office **could not tell GAO how much had actually been spent on ALIS.**
- **Use these instead**, all from GAO-20-316: one location lost **9,262 hours of possible flight time — 9% — in a year** to unresolved ALIS issues; another grounded aircraft **2,200 hours in six months** awaiting contractor fixes; maintainers kept critical aircraft data in **Excel because they did not trust the system of record**; and **DOD incurs a fee every time a user submits an Action Request** — the governing system charges for its own bug reports.
- **Do not attribute** the $1.2 trillion / 66-year figure to ALIS; that is the whole F-35 sustainment programme.
- **See:** `gap_fill_round2.md` §15.

### 12. The book has one big idea — NOW TWO
- **Added:** *legibility* (James C. Scott, *Seeing Like a State*) as the second strut beside the good regulator theorem. The theorem says a governing layer must model what it governs; legibility explains why the models it builds are systematically distorted toward what is easy to see. Failure lives in the gap.
- **Why it matters:** it unifies four themes that currently sit apart — Goodhart (7), OKRs and metrics (3), platform adoption (1), and agents optimising visible targets (6). Scott is **absent from the 34-book comparison** and is widely read by exactly this book's audience.
- **See:** `gap_fill_round2.md` §16.

---

## New anchor material added in round 2 (not in any earlier file)

- **Will Larson**, CTO at Imprint and author of four books in this market, is running a software factory and writing about it publicly — "Trying the software factory pattern", 20 September 2026. Nine-month timeline, named tooling, no numbers, sceptics in the same thread. The best anchor case in the corpus, and a competitive risk worth watching. `gap_fill_round2.md` §11.
- **A live 2026 Hacker News conversation** on software factories and agentic coding that the first round never saw, including "Why Software Factories Fail" (394 points) and "Ask HN: Do you have any evidence that agentic coding works?" (461 points, 455 comments). In the latter, **every** positive account describes scaffolding the person built around the agent — plans, narrow scope, specs, logs, multi-pass review — which is the book's thesis appearing unprompted in the wild. `gap_fill_round2.md` §3–5.
- **The holdout-scenario mechanism**: StrongDM keeps its evaluation scenarios outside the codebase where the coding agents cannot see them. An independent regulator with its own variety, rediscovered because agents optimise against anything visible. `gap_fill_round2.md` §6.
- **The mathematicians' revolt (September 2026)** — 25 Fields Medallists and 7,200+ signatories declared that AI optimised for mathematical benchmarks is misaligned with how the discipline actually creates knowledge. A whole field publicly rejecting its own success metric, two weeks ago, with no software jargon required. The strongest candidate for the book's opening chapter, and the answer to the "who is this book for" problem: software becomes the worked example, not the subject. `gap_fill_round2.md` §22.
- **A live disagreement worth a chapter**: StrongDM says specify exhaustively and hold the tests back; Goedecke says transmit intent because an explicit spec misses what the model would find. Neither acknowledges the other. The good regulator theorem referees. `gap_fill_round2.md` §22.

---

## Still open, in priority order

1. **Do *Accelerate*, *Platform Engineering* or *Wiring the Winning Organization* cite Beer or Ashby?** No public bibliography exists for these, unlike *Team Topologies*. Requires an ebook search for: Beer, cybernetic, viable system, Ashby, requisite variety. ~15 minutes. Needed before the §10 framing goes in a proposal.
2. **Where does Beer appear in the *body* of *Team Topologies*?** A bibliography entry says nothing about use. If he is discussed substantively, "cited, not applied" needs softening.
3. **Reddit**, entirely — by hand (see item 7 above).
4. **StrongDM factory outcomes** — obtainable only by interview; all three engineers are named and public.
5. ~~Read Conant & Ashby (1970) in full~~ — **done, 23 Sep 2026** (author supplied the PDF). See `gap_fill_round2.md` §19. Citation settled as *Int. J. Systems Science* 1(2), 1970, **89–97**, not 511–519. Three findings the slogan hides: a regulator that is not a model of what it governs is **unnecessarily complex**; a changing system needs a **time-varying model**; and **cause-controlled regulation is formally superior to error-controlled**. Only the paper's two figures remain unread (extraction dropped them).
6. ~~Zappos 18%, the Backstage adoption figures, and the ALIS figures~~ — **all resolved in round 3; see items 9, 10 and 11 below.** The one ALIS thread left is where the bogus "45,000 hours" claim came from, which matters only if you want to use it.
7. **A 2020–2026 VSM implementation with published results** — may not exist; interview SCiO members instead.

## Interview targets the research has surfaced

Software side: Sean Goedecke (writing this book's software half in public — two of his posts already anchor chapters, and "Don't build tools for AI agents" is the best counter-argument found); Will Larson (Imprint); Justin McCarthy, Jay Taylor and Navan Chauhan (StrongDM); Dex Horthy (HumanLayer, "Why Software Factories Fail").
Cybernetics side: Patrick Hoverstadt (chairs SCiO, has client cases); Raul Espejo (edited the VSM casebook); the Metaphorum 2026 organisers.

A set of primary interviews spanning both communities is what turns a synthesis of public material into something a publisher will buy — and it is exactly the bridge no existing book builds.
