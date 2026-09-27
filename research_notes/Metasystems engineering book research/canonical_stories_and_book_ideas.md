# Canonical stories and what the existing books contribute

Round 4, 23 September 2026. Two jobs in one file.

**Part A — the canonical cases.** The corpus so far is strong on 2026 and thin on the stories that have held up for decades. These are the durable ones, with primary sources, mapped to the book's mechanisms.

**Part B — what each comparable book contributes.** Not reception and ratings (that is `existing_books_gap.md`) but the *ideas and signature stories* worth absorbing, and where each one stops.

Sourcing rule throughout: paraphrase, quotes under 15 words, primary documents where they exist.

---

# PART A — CANONICAL CASES

## A1. The Bezos API mandate (2002) — the founding story of "build the builder layer"

### Why it belongs
This is the most famous instance of someone deliberately engineering the layer that builds everything else, and it produced AWS. Any book on metasystems engineering that omits it will be asked why.

### Cited findings
- The mandate, as circulated: all teams will expose their data and functionality through service interfaces; no other inter-process communication is allowed — no direct linking, no direct reads of another team's data store, no shared memory, no back doors. Teams must design so the interfaces can be externalised. The closing line, widely quoted, is that anyone who does not do this will be fired.
- Source and date: issued at Amazon in **2002**; Amazon converted to a service-oriented architecture over the following years, and the mandate is widely credited with enabling AWS.
- **Provenance caveat, and it matters.** The public record traces to **Steve Yegge's 2011 "Platforms Rant"**, written as an internal Google post and accidentally made public — [archived copy used in a University of Washington course](https://courses.cs.washington.edu/courses/cse452/23wi/papers/yegge-platform-rant.html), [gist mirror](https://gist.github.com/kislayverma/d48b84db1ac5d737715e8319bd4dd368). Commentators note that **no primary Amazon document has ever surfaced**, and neither Bezos nor his engineers have denied it. Treat it as reported lore with a named, credible source, not as a documented memo — and say so in the book. See [Nordic APIs](https://nordicapis.com/the-bezos-api-mandate-amazons-manifesto-for-externalization/), [Net API Notes](https://netapinotes.com/anyone-who-doesnt-do-this-will-be/).

### How the book should use it
- It is the **cause-controlled regulation** story from Conant & Ashby (see `gap_fill_round2.md` §19): rather than inspecting integration failures after they happen, Bezos changed the rules of communication so the failure class could not arise. He regulated at D, not at the error.
- It is also a legibility story with a happy ending: forcing every team to expose a documented interface made the organisation legible to itself, and that legibility turned out to be a sellable product. Scott's warning and Bezos's mandate are the same mechanism with opposite outcomes — worth confronting directly rather than choosing a side.
- Honest handling of the provenance is itself a selling point in a genre full of repeated anecdotes.

---

## A2. NUMMI (1984–2010) — why copying a metasystem does not work

### Why it belongs
The cleanest natural experiment ever run on whether an operating system can be transplanted. GM was given Toyota's method, in its own plant, with its own workers — and could not spread it.

### Cited findings
- In 1984 GM and Toyota opened **NUMMI** in Fremont, California as a joint venture, and Toyota taught GM the production system that made better cars for less money. The plant's workforce had been considered among the worst in the industry; under the new system quality improved rapidly.
- GM's attempt to replicate it at **Van Nuys**, without retraining people, failed.
- Reported obstacles: senior GM leaders treated the lesson as optional; union members saw efficiency as a threat to headcount; workers resented the loss of seniority-based privileges; managers resisted losing familiar control and perks.
- GM began implementing the system seriously in **1993**, and spread it over more than a decade — too slowly to prevent bankruptcy.
- Primary-ish sources: *This American Life* episode **403: NUMMI (2010)** and the updated **561: NUMMI (2015)**, both with full transcripts — [403](https://www.thisamericanlife.org/403/transcript), [561](https://www.thisamericanlife.org/561/transcript). Commentary at [Lean Blog](https://www.leanblog.org/2015/07/throwback-thursday-this-american-life-on-nummi-lessons/).

### How the book should use it
- It is the **Spotify-model failure** (Theme 3) with thirty years of evidence behind it: what transfers is the artefact, not the metasystem. A governing system is a model of a particular organisation's reality; lift it out and the model no longer fits — which is exactly what Conant & Ashby's time-varying clause implies.
- It answers the reader's obvious question — "so should I copy Team Topologies / the Spotify model / StrongDM's factory?" — with the strongest possible no, from outside software.
- It is also a legibility story: the andon cord made problems visible *and* gave the person who saw the problem the authority to stop the line. Most copies imported the visibility and not the authority.

---

## A3. Columbia (2003) — an official finding that organisation caused the accident

### Why it belongs
A federal investigation board put organisational structure on an equal footing with physical cause. That is a metasystems verdict from the most credible possible venue, and it is quotable in a proposal.

### Cited findings
- The **Columbia Accident Investigation Board (CAIB)** concluded that NASA's organisational culture had **as much to do with the accident as the foam** that struck the orbiter, and that physical and organisational causes played an equal role.
- Organisational causes were rooted in the Shuttle Program's history and culture: original compromises made to win approval, years of resource constraint, fluctuating priorities, schedule pressure, mischaracterisation of the shuttle as operational rather than developmental, and no agreed national vision for human spaceflight.
- Detrimental practices named include **reliance on past success as a substitute for sound engineering** — for example, not testing to understand why systems were not performing as required.
- After Challenger, NASA made many management reforms, yet the human-spaceflight culture and many institutional practices remained intact; the Board noted cultural norms are resilient and resist externally imposed change.
- Chapter 7 carries the Board's position that without management changes, there is no confidence other corrective actions will improve safety.
- Primary source: [CAIB Report, Volume 1 (full PDF)](https://s3.amazonaws.com/akamai.netstorage/anon.nasa-global/CAIB/CAIB_lowres_full.pdf); [HTML edition](https://www.globalsecurity.org/space/library/report/2003/caib-report_vol-1_august2003.htm).

### How the book should use it
- "Reliance on past success as a substitute for sound engineering" is the single most transferable line in the corpus for the AI chapters: it is exactly what a team does when an agent pipeline has worked for six months and nobody has tested why it works.
- The Challenger-to-Columbia continuity is the book's argument about how slowly governing layers learn — the same point as GAO's six-year recommendation gap on ALIS (`gap_fill_round2.md` §20).

---

## A4. Boeing 737 MAX — when the regulator delegates itself out of existence

### Why it belongs
The purest documented case of a metasystem failing because oversight was delegated to the thing being overseen. For a book about governing layers, this is the cautionary extreme — and it has official reports.

### Cited findings
- MCAS certification was ultimately **delegated to Boeing** under the FAA's delegation scheme. Boeing presented MCAS in 2012 as part of the existing speed trim system, and it drew little scrutiny in certification.
- Boeing **did not classify MCAS as safety-critical**, which would have triggered greater FAA scrutiny.
- Internal Boeing engineers had raised the specific questions that later mattered: triggering from a single sensor, consequences of a faulty sensor, effects of repeated activations on pilot control, and whether pilots would react in time.
- The House investigation found that Boeing employees delegated to act on the regulator's behalf **failed to represent the FAA's interests** in four instances, and concluded that excessive delegation **eroded the FAA's oversight capability**.
- The Committee's conclusion, in substance: that a compliant aeroplane crashed twice in under five months is evidence the regulatory system itself is flawed.
- Primary sources: [House Transportation Committee final report, 15 September 2020 (PDF)](https://democrats-transportation.house.gov/imo/media/doc/2020.09.15%20FINAL%20737%20MAX%20Report%20for%20Public%20Release.pdf); [DOT Inspector General report on FAA certification, February 2021 (PDF)](https://www.oig.dot.gov/sites/default/files/FAA%20Certification%20of%20737%20MAX%20Boeing%20II%20Final%20Report%5E2-23-2021.pdf). Coverage: [Seattle Times](https://www.seattletimes.com/business/boeing-aerospace/u-s-house-probe-of-737-max-finds-disturbing-pattern-of-boeing-failures-and-grossly-insufficient-faa-oversight/).

### How the book should use it
- "Compliant and fatal" is the sharpest possible statement of Goodhart's law in a safety system: the process was satisfied and the outcome was catastrophic.
- Direct line to the AI chapters: when the entity being governed writes the evidence of its own compliance — an agent generating its own tests, a team self-reporting its own DORA metrics — this is the failure mode, with bodies attached.

---

## A5. Post Office Horizon — when the law assumes the system is right

### Why it belongs
The most consequential metasystem failure in this corpus, and it turns on a single governing assumption: that computers work correctly unless proven otherwise.

### Cited findings
- Between **1999 and 2015** the Post Office pursued hundreds of sub-postmasters for shortfalls caused by faults in its Horizon accounting software.
- The public inquiry chaired by **Sir Wyn Williams** (report 2025) found it likely that **around 1,000 people were prosecuted and convicted** on false data, with a further 50–60 prosecuted but not convicted.
- The inquiry found the Post Office **trenchantly resisted** the claim that Horizon produced false data, and that some senior employees knew or should have known the system was faulty while the organisation maintained the fiction that its data was always accurate.
- **The legal metasystem is the root cause.** Courts have operated on a presumption that computers work correctly since **section 69 of the Police and Criminal Evidence Act 1984 was repealed in 2000** — so the burden fell on the accused to prove the machine wrong.
- Human cost: the report links **13 suicides** to the scandal, with at least 59 others having contemplated suicide.
- Coverage: [Globe and Mail](https://www.theglobeandmail.com/world/article-britain-post-office-inquiry-report/), [CBS News](https://www.cbsnews.com/news/suicides-linked-post-office-wrongful-convictions-scandal-uk-report/), [NBC](https://www.nbcnews.com/world/united-kingdom/least-13-killed-uks-post-office-wrongful-convictions-scandal-rcna217676). The inquiry's own reports are the primary source and should be cited directly in the book.

### How the book should use it
- This is the chapter that makes the stakes real for a general reader, and it must be handled soberly — real people died. No clever framing, no metaphor-mining.
- The mechanism is exact: a **presumption of correctness** is a governing rule that removes the feedback loop. If the system cannot be wrong, its errors become other people's crimes. Compare ALIS, where maintainers were free to distrust the record and keep spreadsheets; Horizon's victims were not.
- It is also the strongest available argument for the book's central claim — that the design of the governing layer is a moral question and not only a technical one.

---

## A6. Normal accidents and drift — the two theories of how systems fail

These are books, and they belong in Part B too, but they function as the theoretical backbone for Part A.

### Cited findings
- **Charles Perrow, *Normal Accidents: Living with High Risk Technologies*** (Princeton) — [publisher page](https://press.princeton.edu/books/paperback/9780691004129/normal-accidents). The argument: systems with **interactive complexity** and **tight coupling** will inevitably produce accidents; multiple unexpected failures are built into such systems, so these accidents are "normal" — system accidents — and cannot simply be designed around.
- **Sidney Dekker, *Drift into Failure***. The argument: organisations do not fail because something breaks but because, under production pressure, competition and scarcity, they **incrementally normalise risk while appearing to perform well**, inching toward their safety limits without noticing. See [Dekker's paper on drift](https://safetydifferently.com/wp-content/uploads/2014/08/SDDriftPaper.pdf).
- The distinction: Perrow is **structural inevitability**; Dekker is **gradual organisational drift**. Counterpoint literature exists — high reliability organisation theory, and Leveson's critique — [MIT paper](http://sunnyday.mit.edu/papers/hro.pdf).

### How the book should use it
- These two give the book its failure vocabulary, and they are **absent from the 34-book comparison** in `existing_books_gap.md`. Adding them raises the book's credibility with any reader from safety-critical engineering.
- Dekker's drift is what the AI chapters are describing without the word: a pipeline that works, month over month, while nobody re-tests why — which is also CAIB's "past success as a substitute for sound engineering" (A3).
- Perrow supplies the honest limit on the book's optimism: some of this cannot be fixed by better governance, only by less coupling. A book that admits this is more trustworthy than one that promises a method for everything.

---

# PART B — WHAT THE EXISTING BOOKS CONTRIBUTE

For each: the idea worth absorbing, its signature story, and where the book stops. Entries marked **[verified this round]** were checked against sources on 23 Sep 2026. Entries marked **[standard account — verify before quoting]** are widely-held summaries that need a primary check before any specific claim goes in the manuscript.

## B1. James C. Scott, *Seeing Like a State* (1998) — **[verified this round]**
- **The idea:** legibility. A governing body must simplify what it governs in order to see it, and the simplification destroys the local knowledge (metis) the thing actually runs on.
- **The signature story — use this one.** From roughly **1765 to 1800**, Prussian and Saxon foresters developed ways to calculate timber volume and revenue using a **Normalbaum**, a standard tree. Through the nineteenth century, management increasingly made real forests resemble the abstraction: fewer species, often monoculture, same-age stands, cleared underbrush, straight rows. It worked beautifully for the state — trees countable, yields predictable, harvesting easier. **Then the forests started dying**, because the microbial and inter-species relationships that sustained them had been cleared away with the underbrush. The map was imposed on the territory until the territory died.
- Sources: [Scott, intro and chapters 1–3 (PDF)](http://kokolabs.org/Scott%20-%20Seeing%20Like%20a%20State%20(Intro,%20cp%201-3).pdf); [full text](https://theanarchistlibrary.org/library/james-c-scott-seeing-like-a-state); [Normalbaum background](https://nolessthan.com/normalbaum/).
- **Where it stops:** Scott is about states, not software or teams. He offers no method for governing well — only a warning. That gap is the book's opportunity: pair his diagnosis with Conant & Ashby's requirement and you get a discipline rather than a caution.
- **The line the book can draw:** the Normalbaum *is* the internal platform's golden path, the DORA dashboard, the OKR, the agent's eval suite. Same move, same risk, smaller trees.

## B2. Conant & Ashby (1970) and W. Ross Ashby — **[verified, see `gap_fill_round2.md` §19]**
- **The idea:** a successful, simple regulator must embody a model of what it regulates; and regulating from the cause beats regulating from the error.
- Ashby's *Introduction to Cybernetics* (1956) supplies **requisite variety** — only variety absorbs variety — and is in the public domain. It was discussed on HN in 2020 ([22838207](https://news.ycombinator.com/item?id=22838207)).
- **Where it stops:** pure theory, no cases, unreadable for a general audience. The book's job is to carry it, not to cite it.

## B3. Stafford Beer, *Brain of the Firm* / *The Heart of Enterprise* — **[see `term_genealogy.md`]**
- **The idea:** the viable system model — the minimum structure any organisation needs to stay viable, applied recursively.
- **The signature story:** Project Cybersyn, Chile 1971–73.
- **Where it stops:** the diagrams lose readers (a 2025 practitioner post in `practitioner_experiences_part2.md` admits people bounce off them), and there is **no published 2020–2026 implementation with outcome data** (`gap_fill_round2.md` §13). The book should use Beer for structure and get its evidence elsewhere.

## B4. Donella Meadows, *Thinking in Systems* — **[verified this round]**
- **The idea:** intervene at the right depth. Her **twelve leverage points**, ranked by power, put parameters and numbers at the weak end and goals, paradigms and the power to transcend paradigms at the strong end. Her essay "Leverage Points: Places to Intervene in a System" (1997) is cited in *Team Topologies*' own bibliography — [Wikipedia summary](https://en.wikipedia.org/wiki/Twelve_leverage_points), [SCiO listing](https://www.systemspractice.org/resources/leverage-points-places-intervene-system).
- **Use it as the book's diagnostic ladder:** most platform, metric and agent interventions sit at the weakest leverage points — tweaking numbers and buffers — while the powerful ones (who gets to stop the line, what counts as done) go untouched.
- **Where it stops:** ecological and economic examples, no engineering practice.

## B5. John Gall, *Systemantics* — **[verified this round]**
- **The idea — Gall's law:** a complex system that works is invariably found to have evolved from a simple system that worked; a complex system designed from scratch never works and cannot be patched into working — you must start over from a simple working system. [Wikipedia](https://en.wikipedia.org/wiki/Systemantics), [Andy Matuschak's note](https://notes.andymatuschak.org/z4GDrXLY7RaUDcvZLim3mfA).
- **Why it matters here:** it is the sharpest argument against big-bang metasystems — the platform designed complete before anyone uses it, the agent harness architected up front. It also explains why the Ask HN respondents who succeeded (`gap_fill_round2.md` §5) grew their scaffolding incrementally.
- **Where it stops:** aphoristic, deliberately comic, no evidence base. Cite it as a heuristic, never as proof.

## B6. W. Edwards Deming — **[verified this round]**
- **The idea:** Deming estimated that roughly **94% of the variation** in a system comes from the system, not the people in it. Judge the system, not the worker.
- **The signature story — the Red Bead Experiment (1982).** Volunteers dip a paddle into a box of beads, 80% white and 20% red, and are praised or punished for how many red beads they draw — though the outcome is entirely determined by the box. It demonstrates the futility of ranking people on results produced by the system. [Deming Institute](https://deming.org/explore/red-bead-experiment/), [detailed write-up](https://maaw.info/DemingsRedbeads.htm).
- **Use it directly against 2026 practice:** ranking engineers by AI token spend (the "tokenmaxxing" and Meta leaderboard stories in `practitioner_experiences_part2.md`, Theme 7) is the red bead experiment with a bigger budget.

## B7. Taiichi Ohno / Toyota Production System — **[verified this round]**
- **The idea — andon, and jidoka.** The andon cord, introduced in Toyota plants around the 1960s and descended from Sakichi Toyoda's loom that stopped itself on a broken thread, lets **any worker stop the entire line** on spotting an abnormality. The essential part is not the signal but the **authority**: without operator authority to stop the line, it is signalling, not andon. The cultural norm is that pulling it is praised.
- Sources: [Toyota's own TPS page](https://global.toyota/en/company/vision-and-philosophy/production-system/index.html), [Andon overview](https://en.wikipedia.org/wiki/Andon_(manufacturing)), [Vorne on origins](https://www.vorne.com/learn/key-concepts/andon/origins/).
- **This is the book's clearest positive mechanism.** Most governing layers give people dashboards (signal) and withhold the cord (authority). Ask of any platform, metric or agent pipeline: *who can stop it, and are they thanked?* ALIS answered badly — the feedback channel cost a fee (`gap_fill_round2.md` §20). Horizon answered worst — postmasters who reported errors were prosecuted (A5).

## B8. Eliyahu Goldratt, *The Goal* — **[verified this round]**
- **The idea — theory of constraints,** with five focusing steps: identify the constraint, exploit it, subordinate everything else to it, elevate it, then repeat — and never let inertia become the constraint. [Wikipedia](https://en.wikipedia.org/wiki/Theory_of_constraints), [TOC Institute](https://www.tocinstitute.org/five-focusing-steps.html).
- **Why it is load-bearing for this book:** the whole AI story in this corpus is a constraint moving. Writing code stopped being the constraint; judgement and review became it (`gap_fill_round2.md` §4); Goedecke argues the next one is dev-loop latency (§21). Goldratt supplies the vocabulary and the discipline of subordinating everything else to wherever it now sits.
- **Where it stops:** a manufacturing novel; the constraint in knowledge work is rarely as visible as a machine.

## B9. Charles Perrow and Sidney Dekker — **[verified this round, see A6]**
- Perrow gives structural inevitability; Dekker gives drift. Together they are the failure theory the software books lack, and **both are missing from the 34-book comparison**.

## B10. Peter Senge, *The Fifth Discipline* — **[standard account — verify before quoting]**
- **The idea:** the learning organisation, systems archetypes, and the beer game — a simulation in which ordinary people, each behaving sensibly, generate wild oscillations because of delays in the feedback loop.
- **Use:** the beer game is the best available teaching device for why a governing layer with slow feedback produces chaos even when everyone is competent. Directly applicable to ALIS's months-long Action Request latency.
- **Where it stops:** reviews complain it is abstract; note that `existing_books_gap.md` flags the "too abstract" criticism as unconfirmed.

## B11. Fred Brooks, *The Mythical Man-Month* — **[standard account — verify before quoting]**
- **The ideas:** adding people to a late project makes it later; the second-system effect; the distinction between essential and accidental complexity ("No Silver Bullet").
- **Use:** essential versus accidental is the cleanest way to frame what agents actually removed. They demolished accidental complexity — typing, boilerplate, lookup — and left essential complexity untouched, which is exactly why maintainability and design remain the bottleneck (`gap_fill_round2.md` §4).

## B12. Melvin Conway (1968) — **[verified: in Team Topologies' bibliography, `gap_fill_round2.md` §10]**
- **The idea:** organisations design systems that mirror their own communication structures.
- **Use:** Conway is the bridge everyone already accepts. The book's move is to point out that Conway describes a constraint while Beer and Ashby describe what to do about it — and that the industry adopted the first and ignored the second.

## B13. *Team Topologies* (Skelton & Pais, 2019) — **[bibliography verified this round]**
- **The idea:** four team types, three interaction modes, and cognitive load as the limit on what a team can own; the platform exists to reduce the cognitive load of stream-aligned teams.
- **What the book takes:** the cognitive-load framing is the most useful operational idea in the modern canon, and "platform as a product" follows from it.
- **Where it stops, and this is the book's opening:** it cites Beer's *Brain of the Firm* and Wiener's *Cybernetics* and then uses neither. No Ashby, no requisite variety, no viable system model, no good regulator theorem. The lineage is acknowledged and unused.

## B14. *Accelerate* (Forsgren, Humble, Kim, 2018) and DORA — **[standard account; bibliography unchecked]**
- **The idea:** four measurable delivery outcomes, derived from survey research, that correlate with organisational performance.
- **What the book takes:** the demonstration that this domain can be measured at all, and honest engagement with its limits — DORA metrics are the most gamed numbers in the industry (`systems_that_build_systems.md`, Theme 7).
- **Open item:** whether *Accelerate* cites Beer or Ashby is still unverified; no public bibliography exists (`SUPERSEDES.md`, open item 1).

## B15. *The Phoenix Project* / *Wiring the Winning Organization* (Gene Kim et al.) — **[standard account — verify before quoting]**
- **The ideas:** the three ways (flow, feedback, continual learning); and in the 2023 book, slowification, simplification and amplification as the mechanisms for moving work out of the danger zone.
- **What the book takes:** *amplification* is Kim's name for the andon cord generalised, and it is the closest any modern software book comes to this book's thesis. Treat Kim as the nearest neighbour and say what is different: he is prescriptive about practice, this book is about the governing layer's structure and its failure modes across domains.

## B16. *Platform Engineering* (Fournier & Nowland, 2024) and the Google SRE book — **[standard account]**
- **What the book takes:** the operational reality — that a platform is a product with users who can refuse it, and that reliability work is a governing function with explicit budgets (error budgets are a metasystem mechanism: a rule that converts an argument into a number both sides pre-agreed).
- **Where it stops:** no theory of why platforms fail beyond practice-level advice, and no cross-domain evidence.

## B17. Atul Gawande, *The Checklist Manifesto* — **[standard account — verify before quoting]**
- **The idea:** a short, well-designed checklist measurably improves outcomes in complex, high-stakes work, largely by distributing authority to speak up rather than by aiding memory.
- **Use:** it is the counter-example to the book's pessimism — a minimal, cheap governing artefact that worked, and whose key ingredient (junior staff empowered to halt) is the andon cord again. Three independent domains converging on *who may stop the work* is a genuine finding.

## B18. Andy Grove, *High Output Management* — **[standard account — verify before quoting]**
- **The idea:** managerial leverage — a manager's output is the output of the organisation under them, so the work is choosing which few activities multiply.
- **Use:** it is the personal-scale version of the book's claim and a natural on-ramp for the founder/manager reader if that positioning is chosen.

---

## What Part B changes about the book's positioning

Three things fall out of this pass:

1. **The book's lineage list is now concrete and defensible:** Ashby and Conant & Ashby (the requirement), Scott (why it distorts), Perrow and Dekker (how it fails), Gall (how it must be grown), Deming and Ohno (who gets to stop it), Goldratt (where to look), Meadows (how deep to intervene), Conway and Team Topologies (how the field got here). Nine of these are absent from the 34-book comparison.
2. **One mechanism recurs across three unrelated domains** — Toyota's andon cord, Gawande's checklists, and the absence of both at ALIS, Horizon, Boeing and Columbia. *Who is allowed to stop the work, and what happens to them when they do.* That is a book-worthy finding, it is testable against any organisation, and no book in the comparison set states it across domains.
3. **The honest competitive line:** Gene Kim's *Wiring the Winning Organization* is the nearest neighbour. The differentiator is not novelty of practice but **range and rigour** — the cybernetic requirement, the legibility failure theory, and case evidence from aviation, spaceflight, postal software, defence logistics, platforms, agents and personal systems.

---

## Status of this file

Part A covers six canonical cases. Part B covers eighteen books. **Neither is exhaustive** — see the "not yet done" list in `SUPERSEDES.md`. Known omissions in Part A that are worth a later pass: Therac-25, Knight Capital (2012), the CrowdStrike outage (2024), Cloudflare (November 2025), Wells Fargo's cross-selling scandal, the NHS A&E four-hour target, Healthcare.gov, and Chernobyl/Three Mile Island as the classic tight-coupling cases. Part B omissions: Leveson's *Engineering a Safer World*, Vaughan's *The Challenger Launch Decision* (the origin of "normalisation of deviance"), Hubbard's *How to Measure Anything*, Illich, and Hayek's knowledge problem — the economics counterpart to Scott's metis.
