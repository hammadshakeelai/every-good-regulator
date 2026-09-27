# Book Plan — *Metasystems Engineering*

Written 23 September 2026, after five research rounds (~500 KB of notes in `research_notes/Metasystems engineering book research/`). Read `SUPERSEDES.md` in that folder before trusting any individual note.

---

## 1. The verdict

**Yes — there is an exceptional book in this material.** Not a listicle of systems-thinking quotes, but a book with a real argument, primary-source evidence across unrelated domains, and at least one finding nobody has published.

What the research gives us that most books in this genre never have:

- **A spine that holds up under scrutiny.** Five ideas, each with a citable source read in full or in its key sections: Conant & Ashby (1970), Scott (1998), Bainbridge (1983), Cook (2000), Leveson (2011, open access).
- **Cases with primary-source numbers, including corrections to the versions that circulate online.** GAO's actual ALIS figures (not the 45,000-hours myth), the Horizon inquiry, the House 737 MAX report, the CAIB report, METR's own page, StrongDM's own essay.
- **An original cross-domain finding:** Toyota's andon cord, Gawande's checklists, and their absence at ALIS, Horizon, Boeing and Columbia all turn on one question — *who is allowed to stop the work, and what happens to them when they do.*
- **A 1983 paper that predicts the 2026 AI-coding debate line by line** (Bainbridge), which makes the book's hardest claim — "none of this is new" — provable.
- **Perfect timing:** September 2026 gave us the mathematicians' declaration (25 Fields Medallists, 7,200+ signatories), Larson's public software-factory experiment, and Beer's centenary.

**But "AAA" is not something research can produce.** Four things stand between this corpus and a top-tier book, and none of them is another research file:

1. **Reading the anchor texts in full.** Only six primary sources have been read in full or in their key sections. Each chapter's anchor needs a proper read before it is written (list in §7).
2. **Interviews.** There are none yet. Every publisher proposal asks what is here that isn't already public; today the honest answer is "a synthesis". Eight to fifteen interviews change that.
3. **A voice.** The book needs the author's own experience threaded through it. Every proposal template asks "why you?"
4. **A fact-check, rights and editing pass** — every number against its primary source, permissions for every quoted person and every image.

**Has the research been exhausted? No.** Reddit and Lobsters are blocked from this environment; most comparable books were read *about*, not read; the 245 incident post-mortems are untagged; no interviews exist. But research stopped being the constraint several rounds ago. The corpus already holds roughly three books' worth of material. The risk now is not too little — it is a book that tries to hold all of it.

---

## 2. The book in one page

### Working titles
1. ***Every Good Regulator: Why the Systems That Run Our Work Fail — and How to Build Ones That Don't*** — recommended. Elegant for general readers, quietly exact for experts, and the subtitle carries searchable words.
2. ***The System That Runs the System: Metasystems Engineering for the Age of AI Agents*** — keeps the brand term the market research recommends, with "AI agents" doing the discovery work.
3. ***Who May Stop the Line?*** — the book's original finding as a title. Strong, but narrower.

"Metasystems engineering" stays as the book's name for the discipline, but not as the only title words: the market research found the term gets ~20 views a month; the subtitle must carry "AI agents", "systems thinking" or "platforms".

### The reader
The research is unambiguous that "anyone" fails every proposal template. Resolve it like this:
- **Primary reader:** people who build or run the layers that run other people's work — senior engineers, tech leads, platform and engineering managers, founders.
- **Secondary reader:** curious general readers of books like *Thinking in Systems*.
- **How one book serves both:** every chapter opens with a story a general reader can follow, then gives the mechanism, then the practice. The mathematicians' prologue is the proof that the idea needs no software background.

### The promise
*After this book, you will be able to look at any system that governs work — a platform, a dashboard, an org chart, an AI pipeline, your own to-do list — and see what it is modelling, what it cannot see, who is allowed to stop it, and how it is likely to fail.*

### The one question that holds it together
**What does the system that runs your system actually know — and who is allowed to tell it it's wrong?**

### How it stands against the nearest work
- **Leveson** showed that safety is a control problem and every controller needs an accurate model. This book asks the same question of every layer we build to run our work, and adds what her framework does not centre: *why* the models go wrong systematically (Scott), what automation does to the human controller (Bainbridge), and what happens when layers start building layers (Turchin).
- ***Team Topologies*** put Beer and Wiener in its bibliography and then used neither. This book puts cybernetics to work.
- **Gene Kim's *Wiring the Winning Organization*** is the nearest neighbour in practice. The difference is range and rigour: evidence from aviation, spaceflight, postal software, defence logistics, platforms, agents and personal systems, built on primary sources.
- **Osmani's *Agentic Engineering*** and ***Thinking in Platforms*** (both August 2026) cover the current practice without the lineage.

---

## 3. The spine — five ideas, five words

A deliberately small vocabulary, because "too much jargon" is one of the seven recurring complaints about comparable books.

| Word | The idea | Source (read) |
|---|---|---|
| **Model** | Anything that governs a system must carry a model of it. Regulating from the cause beats regulating from the error. A changing system needs a changing model. | Conant & Ashby 1970; Leveson 2011 §4.3 |
| **Legibility** | To govern something, you must simplify it until it is visible — and the simplification destroys the local knowledge the work runs on. | Scott 1998 (key chapters to read in full) |
| **Remainder** | Automation takes the easy parts and leaves humans the impossible remainder — while eroding the skill they need to do it. | Bainbridge 1983 |
| **Stop** | The decisive property of a governing layer is not what it signals but who may halt it, and whether they are thanked. | Ohno/Toyota; Deming; Gawande; ALIS/Horizon/Boeing/Columbia |
| **Jump** | Layers that build layers: product → factory → factory of factories → agents that write agents. Each jump creates a new layer that must itself be governed. | Turchin; Bemer 1968 → StrongDM 2026 |

**And one honest limit, stated up front:** complex systems run broken as a normal condition, catastrophe needs several failures at once, and some systems can only be made safe by being made less coupled, not better governed (Cook; Perrow). The book never promises more than this.

---

## 4. The structure — every case assigned

Target length **95,000–110,000 words**: a prologue, fifteen chapters in four parts, an epilogue, and five appendices. Roughly 6,000–7,000 words per chapter.

### Prologue — *The Scoreboard*
September 2026: twenty-five Fields Medallists and thousands of mathematicians declare that AI optimised for benchmark problems is misaligned with how mathematics creates understanding. A discipline rejects its own scoreboard. Goedecke's reading: puzzles were the legible proxy for insight. Sets up all five ideas without a line of jargon.

### PART ONE — THE LAYER YOU CAN'T SEE

**1. The Forest That Died** — *Legibility.*
Cold open: Prussian and Saxon foresters, ~1765–1800, and the *Normalbaum* — the standard tree that made forests countable, then made them die. Mirror: golden paths, DORA dashboards, OKRs, eval suites. Goedecke's "Seeing like a software company" and the backchannels that keep companies running.

**2. Every Good Regulator** — *Model.*
Cold open: Conant and Ashby's cow, which raises its heat production before its blood temperature falls. The theorem, told honestly — including what it does not prove. Leveson's process models and her model-mismatch cases (Mars Polar Lander, *Herald of Free Enterprise*, Cali). Regulating at the cause: the Bezos API mandate — **with its provenance problem stated openly** (the only source is Yegge's 2011 rant).

**3. The Jump** — *Jump.*
Turchin's metasystem transition. The three lives of the "software factory": Bemer 1968 and the Japanese factories; the US Department of Defense factories (Kessel Run, Platform One) and their staffing regressions; the 2026 "dark factory". Every jump creates a layer nobody has yet learned to govern.

**4. The Viable System** — *the structural map.*
Stafford Beer, Project Cybersyn, and the Suma wholefood co-op that ran old and new structures side by side and had to redo its plan. *Team Topologies* cited Beer and used him for nothing. SCiO: a whole profession that designs self-governing organisations, disconnected from the software world. Keep the diagrams simple — readers "bounce off" the full VSM.

### PART TWO — HOW THE LAYER FAILS

**5. Compliant and Fatal** — *when the governed write their own evidence.*
Boeing's MCAS certification delegated to Boeing; a compliant aeroplane that crashed twice in five months. Deming's red beads. Goodhart. 2026's "tokenmaxxing" leaderboards. DORA metrics gamed. *(Wells Fargo is a candidate — not yet researched.)*

**6. The Fee for Bug Reports** — *the regulator that cannot see its effect.*
GAO on ALIS: 9,262 hours of possible flight time lost at one location in a year; maintainers keeping the real records in Excel because they distrusted the system; a fee charged for every Action Request. METR's experiment breaking because developers would not work without AI. **Myth vs Record box:** the "45,000 hours" and "$16.7 billion" figures that circulate versus what GAO actually wrote.

**7. The Presumption** — *a chapter of its own, told with gravity.*
The Post Office Horizon scandal: around 1,000 people convicted on false data from 1999 to 2015; thirteen suicides linked by the inquiry. The mechanism is a single governing rule — the legal presumption that computers are correct — which removed the feedback loop and turned software errors into other people's crimes. **Tone rule for this chapter:** told through the inquiry record and the people, no clever framing, no metaphor-mining, placed so it does not sit beside lighter material.

**8. Running Broken** — *failure is normal, and there is no root cause.*
Cook's eighteen points. Perrow's normal accidents; Rasmussen's migration to the boundary and Dekker's drift. Columbia: the CAIB found organisation as much a cause as the foam, and named reliance on past success as a substitute for engineering. **Original contribution:** the 245 danluu post-mortems tagged by mechanism, presented as the book's own dataset and chart.

**9. The Model You Copied** — *the time-varying model.*
NUMMI: Toyota taught GM its system in GM's own plant, and GM could not spread it for a decade. The Spotify model its originators never ran. Zappos — **Myth vs Record:** 18% left, mostly by taking a buyout the company offered. A model is fitted to one organisation at one moment; lifted out, it stops fitting.

### PART THREE — THE HUMAN IN THE LOOP

**10. The Ironies of Automation** — *Remainder. The chapter that sells the book.*
Bainbridge 1983 set side by side with the 2026 agentic-coding record: the "impossible task" of monitoring, skills decaying unused, automation camouflaging failure, "systems should fail obviously", the plant whose night shift switched to manual. Therac-25 as the historical warning. The HN thread where every success story turns out to be scaffolding. The market trap: once deadlines assume the tool, opting out is no longer a choice.

**11. Specify or Explain** — *what the model must contain.*
StrongDM's factory — no human writes or reviews code, scenarios held out where agents cannot see them, no published outcomes. Goedecke's counter: tell agents *why*, because a spec misses what the model would find. The resolution: Leveson's intent specifications carried both constraints and rationale around 2000. The two 2026 schools were reconciled in safety engineering a generation ago.

**12. Who May Stop the Line** — *Stop. The book's original finding.*
The andon cord and Toyota's rule that pulling it is praised. Gawande's checklists and the junior nurse who may halt the surgeon. Then the pattern in reverse: ALIS charging for complaints, Horizon prosecuting the people who reported errors, Boeing's delegated oversight, Columbia's engineers. Error budgets as a modern cord. The five-question test for any organisation.

### PART FOUR — LAYERS THAT WORK, AT EVERY SCALE

**13. Grow It, Don't Design It**
Gall's law. Migrations that worked (Airbnb, Uber, Stripe) and reversals that were right (Segment, Prime Video). Platforms as products: adoption earned, not mandated; the real cost is staffing — two to five engineers for years. Larson's nine-month experiment at Imprint, and the loop that re-checks whether its own plan has gone stale. Meadows' leverage ladder as the tool for choosing where to intervene.

**14. The Organisation's Operating System**
Hidden hierarchy after "flat" (Valve, Buffer); holacracy; Amazon's mechanisms and single-threaded leaders; Healthcare.gov's rescue — visible ownership, monitoring, and everyone in one room.

**15. Your Own Operating System**
The same five ideas at the smallest scale. The "second brain" that became a job — Westenberg deleting hers, Khalesi becoming the administrator of his notes, Huang's single text file kept for fourteen years. The rule that survives: notes as a record are light; notes as obligations are a burden.

### Epilogue — *Back to the Scoreboard*
What the mathematicians got right. The five questions to ask of any metasystem. The honest limit: some systems can only be fixed by less coupling.

### Appendices
- **A. Field Guide** — one page per idea: diagnostic questions and warning signs.
- **B. Myth vs Record** — every widely repeated claim this research corrected, with sources. A signature feature: rigour as a pleasure.
- **C. The 245 Incidents** — the tagged dataset and method.
- **D. Further Reading** — free and open-access sources first.
- **E. Glossary** — under 25 terms.

### Deliberately left out
Kent Palmer's meta-systems theory; Hall's 1989 book (a footnote); grid-computing "metasystems"; the 2026 BDCC paper; the ODU nine-function model (an endnote for specialists); vendor adoption statistics; Wikipedia pageview analysis; most tooling specifics; OpenAI's unverifiable "research intern" claims; most of the 34 comparable books.

---

## 5. Making it enjoyable and teachable

**See `FUN_TOOLKIT.md` for the full set of fun devices** — haikus, What If? interludes, "In Small Words" boxes, giant labelled Exploded View diagrams, a stick-figure comic cast, Greene's Image-and-Reversal endings, the author-as-experiment thread, and the rules that keep humour out of the serious chapters. The rhythm below is the minimum every chapter keeps.

Every chapter follows the same rhythm, so readers always know where they are:

1. **Cold open** — a scene, not a summary. A forest, a hangar, a cow, a courtroom, a pull request.
2. **The Mechanism** — one diagram, three sentences.
3. **The mirror** — the same mechanism in software, organisations or personal life.
4. **In the Field** — practitioner voices, from interviews and with permission.
5. **Myth vs Record** — where the popular version is wrong, and what the source says.
6. **Diagnose** — five questions to ask about your own system.
7. **Try This** — one small exercise for Monday.
8. **In one paragraph**, and what to read next.

Design principles:
- **One visual grammar.** The control loop — goal, action, feedback, model — is drawn in chapter 2 and redrawn in every chapter with the failing part highlighted. By the end, readers read systems the way musicians read notation.
- **Alternating stakes.** High-stakes chapters (aviation, spaceflight, the Post Office) alternate with everyday ones (dashboards, note apps) to give the reader air.
- **Honesty as a feature.** Every AI claim is dated. Where nobody knows, the book says so. A book of failure stories must not tell them as single-villain root-cause stories — Cook's warning applies to the author too.

---

## 6. Images and visuals — plainly

**Original diagrams — no rights issues, and the core of the look.** About twenty, all in one consistent style:
the control loop and its failure variants; legibility versus local knowledge; the Normalbaum forest before and after; Turchin's staircase of jumps; a simplified viable system; Meadows' leverage ladder; the constraint moving from typing to review to latency; Bainbridge's irony (automation up, skill down); Cook's stacked defences; the andon cord versus a dashboard; the StrongDM, Goedecke and Leveson triangle; the three lives of the software factory; METR's results as ranges rather than points.

**Original data visualisations:** the 245 incidents by mechanism; ALIS's lost flight hours; the Zappos exits by buyout wave.

**Usable with care:**
- Works of US federal employees — GAO, CAIB and House report figures, most NASA imagery — are generally public domain. Check each figure's credit line, because reports sometimes include third-party images.
- Wikimedia Commons images, checking each licence.
- **Leveson's figures are CC BY-NC-ND — non-commercial only.** A book you sell needs MIT Press's permission to reproduce them; redraw the ideas originally and cite her instead.

**Needs a licensing budget:** press photographs (NUMMI, Horizon, the 737 MAX), figures from copyrighted books, and Cybersyn's operations-room photographs. Each is a per-image quote and clearance process — plan for it rather than discovering it at the end.

**For the premium look:** commission an illustrator for the chapter openers. AI-generated images are a risk: some publishers refuse them and their copyright status is uncertain; if used, disclose it.

---

## 7. What has to happen before it is AAA

### Phase 1 — close the gaps that change the book
**Read the anchor texts in full** (all legally obtainable):
- Scott, *Seeing Like a State*, chapters 1–2 — buy or borrow.
- Leveson, *Engineering a Safer World*, chapters 2–4 and 10 — open access (already downloaded).
- The CAIB report, volume 1, chapters 5–8 — free official PDF.
- The House Transportation Committee 737 MAX report (2020) — free.
- The Post Office Horizon inquiry reports — free, and needed for chapter 7's tone as much as its facts.
- *This American Life* 403 and 561 (NUMMI) transcripts — free.
- Leveson and Turner on Therac-25 — free on her MIT page.
- Turchin, *The Phenomenon of Science* — on Principia Cybernetica.
- Meadows, "Leverage Points" — free.
- Beer, *Brain of the Firm*; Vaughan, *The Challenger Launch Decision*; Gawande, *The Checklist Manifesto* — buy or borrow.

**Interviews (8–15):** Will Larson; Sean Goedecke; Justin McCarthy, Jay Taylor or Navan Chauhan at StrongDM; Dex Horthy (HumanLayer); Patrick Hoverstadt (SCiO); someone from the Metaphorum community; a platform-team lead whose platform failed; an SRE who has run incident reviews at scale; ideally someone with first-hand knowledge of aviation or medical safety practice.

**Fact-check ledger:** every number in every anchor case checked against its primary source, extending the Myth vs Record appendix. Known items still open: Backstage's 99%/~10% adoption contrast, whether *Accelerate* cites Beer, Wells Fargo.

**Original work:** tag the 245 post-mortems by mechanism (about a day). Consider a short survey of working engineers on skill retention under agentic workflows — nobody has measured it, and it would be the book's own evidence.

**Voices from Reddit and Lobsters** (blocked here — gather by hand in a browser, with permission), especially for chapter 15, which currently has no non-engineer voice.

### Phase 2 — the proposal
A one-page pitch; this outline; **two sample chapters (recommended: the Prologue and chapter 10)**; five recent comparable titles (*Team Topologies* 2e, *Platform Engineering*, *The Unaccountability Machine*, *Wiring the Winning Organization*, *Staff Engineer*); author-platform numbers. IT Revolution is the best brand fit but is not taking unsolicited proposals; Pragmatic, Manning and O'Reilly accept direct pitches. Self-publishing is the alternative if an audience comes first.

### Phase 3 — build in public
The closest proven model is Larson's staffeng.com: publish six to ten story-led essays and interviews over several months, test which chapters land, and build the audience the proposal needs.

### Phase 4 — draft, fact-check, clear rights, edit.

---

## 8. Risks, stated plainly

- **Breadth.** "An ultimate book that encompasses a lot" is precisely the profile of the comparable books rated 3.4–3.7: an ambitious frame, scattered execution. The defence is the one question and the five words. Every case must earn its place against them.
- **The AI chapters will date.** Build them on mechanisms that outlast a model generation — Bainbridge, not benchmarks — and date every claim.
- **Competition.** Osmani and *Thinking in Platforms* on the practice; Larson and Goedecke are the people most likely to write something adjacent. Speed and the cross-domain range are the answers.
- **Tone.** The Horizon chapter must be handled with the seriousness thirteen deaths demand.
- **Root-cause storytelling** — Cook's warning, applied to the author.
- **Rights.** Stories people posted online remain theirs; the book needs their permission for anything more than short quotation and paraphrase.

---

## 9. What I can do next

1. **Write the Prologue and chapter 10 as sample chapters**, in the book's voice. This is the real test of whether it reads as AAA — better than any further research.
2. **Tag the 245 post-mortems** and produce the book's original dataset and chart.
3. **Draft the interview requests** and a tailored question set for each person.
4. **Design the diagram set** as clean SVGs in one visual style.

My recommendation: **start with 1.** A sample chapter tells you more about the book than another research round would.
