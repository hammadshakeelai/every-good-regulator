# Free, legitimate primary sources — GitHub repos, open-access books, author-hosted papers

Round 5, 23 September 2026.

## Sourcing note

I did not use dokumen.pub or similar sites: they host copyrighted books without the publishers' permission, and material from them can't be cited in a book you intend to sell. Everything below is **legitimately free** — open-access editions, author-hosted papers, public archives, or openly-licensed repositories — and it turned out to be a richer haul than a pirate library would have been, because it is citable.

---

## 1. GitHub: `danluu/post-mortems` — 245 real incident write-ups, categorised

[github.com/danluu/post-mortems](https://github.com/danluu/post-mortems). README is ~96,500 characters with 351 links; **245 linked incident entries**, each with a one-paragraph summary written by contributors.

- **Sections:** Config Errors, Hardware/Power Failures, Conflicts, Time, Database, Uncategorised, plus Other Lists and Analysis.
- **Organisations covered include:** Amazon/AWS (many), Google (many), Cloudflare (many), GitHub, GitLab, Heroku, CircleCI, Slack, Discord, Stripe, Reddit, Spotify, Salesforce, Netflix, Etsy, Dropbox, Okta, OpenAI, CrowdStrike, Intel, Valve, Epic Games, Bungie, CCP Games, Roblox, Kickstarter, Medium — and, crucially for this book, **Knight Capital, Therac-25, Healthcare.gov, NASA (three entries), AT&T, ARPANET, the North American Electric Power System, the Indian Electricity Grid, GPS/GLONASS, the European Space Agency, Sweden, Kings College London, Zerodha and Parity.**
- Example of the summary quality — the AWS Seoul entry: a config change removed the minimum-healthy-hosts setting for the EC2 DNS resolver fleet, the system fell back to a very low default, and in-VPC DNS queries failed for about 84 minutes until capacity was restored manually; AWS added semantic config validation and per-hour throttling on host removal.

### Why this matters for the book
Every case I listed as a known omission is here, already sourced. It also supplies the **base rate** the book needs: the argument that governing layers fail in patterned ways is far stronger when drawn from 245 incidents than from five famous ones. A pass that tags each entry by mechanism — no feedback path, metric gamed, authority to stop absent, config as ungoverned code, time/coupling — would produce a genuinely original table, and nobody in the comparable books has done it.

### Further lists it points to (all free)
- [AWS Post-Event Summaries](https://aws.amazon.com/premiumsupport/technology/pes/) — the vendor's own primary reports.
- [NASA Lessons Learned Information System](https://llis.nasa.gov/) — a searchable official database.
- [Wikimedia incident documentation](https://wikitech.wikimedia.org/wiki/Incident_documentation) — an entire organisation's incident history in public.
- [Awesome Tech Postmortems](https://github.com/snakescott/awesome-tech-postmortems), [icco/postmortems](https://github.com/icco/postmortems) (parsed into a database), [macintux/Service-postmortems](https://github.com/macintux/Service-postmortems) (JSON), [dastergon/postmortem-templates](https://github.com/dastergon/postmortem-templates) — templates from several organisations, useful as evidence of how the ritual is standardised.
- [SRE Weekly](https://sreweekly.com) — ongoing outages section.

---

## 2. GitHub: `lorin/resilience-engineering` — the field's bibliography, curated

[github.com/lorin/resilience-engineering](https://github.com/lorin/resilience-engineering), maintained by Lorin Hochstein; also at resiliencepapers.club. **~117,000 characters, 505 links**, organised person by person with concepts and selected publications and talks, plus an `intro.md` titled "Where do I start?".

- **People covered include:** John Allspaw, Lisanne Bainbridge, Richard I. Cook, Sidney Dekker, John C. Doyle, Erik Hollnagel, Gary Klein, Nancy Leveson, Charles Perrow, Jens Rasmussen, James Reason, Nadine Sarter, Barry Turner, Diane Vaughan, David Woods — **and James C. Scott**, which independently confirms the Scott connection this research arrived at separately (`gap_fill_round2.md` §16, §18).
- **"Some big ideas" it indexes:** the adaptive universe and graceful extensibility (Woods); the dynamic safety model (Rasmussen); Safety-I versus Safety-II (Hollnagel); the ETTO efficiency–thoroughness trade-off principle (Hollnagel); drift into failure (Dekker); robust-yet-fragile (Doyle); STAMP (Leveson).
- Related: [res-eng-short-course-notes](https://github.com/lorin/res-eng-short-course-notes) from David Woods's short course, and a public [Zotero group](https://www.zotero.org/groups/2335189/res-eng/items) with the papers.

### Why this matters
This is a whole discipline — resilience engineering — that has been studying governing layers and their failure for forty years, and it does **not** appear in any of the 34 comparable books. Together with SCiO on the cybernetics side (`gap_fill_round2.md` §13), the book now has two established research communities to draw on that the software-management genre ignores. That is the strongest possible answer to "what makes this book different".

### Bainbridge, "Ironies of Automation" (1983) — READ IN FULL, see section 6 below.

---

## 3. Richard I. Cook, "How Complex Systems Fail" — read in full

Richard I. Cook, MD, Cognitive Technologies Laboratory, University of Chicago. Copyright 1998, 1999, 2000; revision D dated 21 April 2000. Eighteen numbered points over three pages. Free copy hosted by [MIT](https://stuff.mit.edu/afs/athena/course/2/2.75/resources/random/How%20Complex%20Systems%20Fail.pdf); extracted and read on 23 Sep 2026.

The points most load-bearing for this book, paraphrased:

- **Catastrophe needs several failures at once; single-point failures are not enough.** Small, individually harmless faults combine. There are far more opportunities for failure than there are actual accidents, because the defences usually work.
- **Complex systems run in degraded mode** — they operate as broken systems, functioning because of redundancy and because people make them work despite the flaws. Reviews afterwards nearly always find a history of near-misses, and the argument that these should have been noticed rests on a naive picture of how systems perform.
- **Attributing an accident to a single "root cause" is fundamentally wrong**, and **hindsight biases every assessment of the operators' performance** after the fact.
- **Operators hold two roles at once** — producing the output and defending against failure — and **all their actions are gambles**, judged unfairly once the outcome is known.
- **People are the adaptable element** of complex systems, and they **continuously create safety** — restructuring to reduce exposure, concentrating resources where demand is expected, and keeping routes open for retreat and recovery.
- **Change introduces new forms of failure**, and **views of "cause" limit the defences** built against future events.
- **Operating without failure requires experience with failure.**

### How the book should use it
- This is the intellectual bridge between the safety literature and the software audience: it is short, free, already widely read by SREs, and it makes the book's case in advance. It also disciplines the book's own storytelling — the Part A cases (`canonical_stories_and_book_ideas.md`) must not be told as root-cause narratives, which is exactly the trap a book of failure stories falls into.
- "Complex systems run in degraded mode" is the honest frame for every platform, harness and metric system in this corpus: ALIS in degraded mode for years with maintainers in Excel, agent pipelines in degraded mode with humans quietly fixing the output.
- "People continuously create safety" is the positive counterpart to Scott's metis, and it is what the andon cord formalises (`canonical_stories_and_book_ideas.md` B7).

---

## 4. Nancy Leveson — an open-access book and a free canonical paper

- **_Engineering a Safer World: Systems Thinking Applied to Safety_ is genuinely open access** from MIT Press under a Creative Commons Attribution-NonCommercial-NoDerivatives licence: [direct.mit.edu open monograph 2908](https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied). Also on the [Internet Archive](https://archive.org/details/mit_press_book_9780262298247). The MIT Press site refused automated fetching, so **download it in a browser** — it is free and legal.
- **STAMP (Systems-Theoretic Accident Model and Processes)** is her model, and it is startlingly close to this book's thesis: safety is treated as a **control problem, not a component-failure problem**; accidents arise from **inadequate control** rather than from a chain of broken parts; safety is an emergent property of relationships between parts. STAMP rests on safety constraints, a hierarchical safety control structure, and a process model — with controllers, actuators, sensors and the controlled process. STPA is the forward-looking analysis method and CAST the accident-analysis method. Overview: [UL's introduction to STAMP, STPA and CAST](https://www.ul.com/sis/blog/introduction-to-stamp-stpa-and-cast); literature reviews in *Safety Science* ([one](https://www.sciencedirect.com/science/article/abs/pii/S0925753521004367), [two](https://www.sciencedirect.com/science/article/abs/pii/S0925753521004082)).
- **"An Investigation of the Therac-25 Accidents"** (Leveson & Turner, *IEEE Computer* 26(7), July 1993, pp. 18–41) — between June 1985 and January 1987, six known accidents involved massive radiation overdoses, with deaths and serious injuries. Free copies hosted by [RIT](https://www.se.rit.edu/~swen-342/resources/Leveson,%20Turner%20-%20An%20Investigation%20of%20the%20Therac-25%20Accidents%20-%20IEEE%20Computer%20v26n7%20-%201993-07.pdf), [Bowdoin](https://tildesites.bowdoin.edu/~allen/courses/cs260/readings/therac.pdf) and [Chicago](https://classes.cs.uchicago.edu/archive/2022/spring/33100-1/papers/therac25.pdf); an updated version from *Safeware* is on **Leveson's own MIT page**, [sunnyday.mit.edu/therac-25.html](http://sunnyday.mit.edu/therac-25.html) — author-hosted, so unambiguously fine to use.

### Why this is the most important find of the round
**Leveson has already built the formal apparatus this book has been assembling by hand.** "Safety is a control problem, and accidents come from inadequate control" is Conant & Ashby's theorem (`gap_fill_round2.md` §19) applied to a domain where it has been tested for two decades, taught at MIT, and used on real aerospace programmes. The book must engage with STAMP directly and state its own contribution against it — most plausibly: **STAMP governs safety in engineered systems; this book extends the same control view to the layers that build software, run organisations and, with agents, write the code.** Claiming novelty without naming STAMP would be a serious error, and a reviewer from safety engineering would catch it immediately.

---

## 5. Other legitimately free full texts worth downloading

- **W. Ross Ashby, _An Introduction to Cybernetics_ (1956)** — the source of requisite variety, on the [Internet Archive](https://archive.org/details/introductiontocy00ashb) (several copies) and listed by [Penn's Online Books Page](https://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=olbp10975).
- **Conant & Ashby (1970)** — already read in full, `gap_fill_round2.md` §19; PDF hosted by Principia Cybernetica at VUB.
- **The three Google SRE books** — *Site Reliability Engineering*, *The Site Reliability Workbook*, *Building Secure and Reliable Systems* — free to read at [sre.google/books](https://sre.google/books/). Note these are free-to-read, not openly licensed; quote sparingly and cite.
- **Principia Cybernetica Web** — [pespmc1.vub.ac.be](https://pespmc1.vub.ac.be/), including Turchin's metasystem transition material.
- **CAIB Report Volume 1** — full official PDF, linked in `canonical_stories_and_book_ideas.md` A3.
- **House Transportation Committee 737 MAX report** and the **DOT OIG report** — A4.
- **GAO-20-316** — already downloaded and read, `gap_fill_round2.md` §20.

---

## 6. Lisanne Bainbridge, "Ironies of Automation" (1983) — read in full

Lisanne Bainbridge, Department of Psychology, University College London. *Automatica* **19(6), 1983, pp. 775–779**, DOI 10.1016/0005-1098(83)90046-8. Received 16 December 1982, revised 23 May 1983; first presented at an IFAC/IFIP/IFORS/IEA conference in Baden-Baden, September 1982. Over 1,800 citations by 2016 ([Wikipedia](https://en.wikipedia.org/wiki/Ironies_of_Automation)). Free copy: [ckrybus.com PDF](https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf); extracted with `pdftotext` on 23 Sep 2026.

### What the paper actually says (paraphrased; short quotes marked)
- **The core irony:** designers who see the operator as unreliable try to eliminate them, but still leave the operator every task **they could not work out how to automate** — an arbitrary collection of tasks with little support. And designer errors are themselves a major source of operating problems.
- **Skills decay without use.** An experienced operator who has spent years monitoring automation may effectively become an inexperienced one; on take-over they may set the process oscillating. Yet take-over happens precisely when something is wrong, so the operator needs to be **more** skilled and **less** loaded than average.
- **Knowledge only forms through use and feedback.** Classroom knowledge without practice is neither understood nor retained. She notes concern that automated systems monitored by former manual operators are **riding on skills that later generations cannot be expected to have.**
- **Situational awareness takes time.** Manual operators arrived 15–30 minutes early to get a feel for the plant; an operator asked to intervene suddenly acts on minimal information.
- **Monitoring is humanly impossible as specified.** Vigilance research shows even a highly motivated person cannot keep effective attention on a source where little happens for more than about half an hour. People can fill in logs "without noticing what they are" (short quote).
- **The deepest irony:** the automation was installed because it does the job better than the operator — yet the operator is asked to monitor that it is doing it well. If decisions can be fully specified, the computer makes them faster and on more dimensions than a human can check in real time, so the human can only judge at a "meta-level" whether decisions look acceptable. Her verdict: the monitor **"has been given an impossible task."**
- **Automation camouflages failure.** Automatic control can counteract a developing fault so that trends stay invisible until they are beyond control. Automatic systems **"should fail obviously"** — graceful degradation is not a virtue in a machine someone must supervise.
- **If a human must follow the computer's reasoning, the computer must reason in a way and at a pace the human can follow**, even when that is technically less efficient — otherwise the operator cannot trace back why they disagree.
- **Operator attitudes:** she knew of an automated plant where management had to be present on the night shift, or the operators switched the process to manual. A deskilled monitoring job is "very boring but very responsible" with no chance to gain or keep the skill the responsibility needs.
- **Procedures cannot substitute for understanding:** it is ironic to train operators to follow instructions and then place them in the system to provide intelligence.
- **The final irony:** the most successful automated systems, with the rarest need for intervention, **may need the greatest investment in operator training.**
- **Her summary line:** by taking away the easy parts of the task, automation can make the difficult parts **more difficult.**

### Why this is the single most important paper for the book's AI chapters
Replace "process plant" with "codebase" and "operator" with "developer reviewing agent output", and the 1983 paper predicts the 2026 corpus line by line:
- The Ask HN thread's recurring complaint that reviewing agent code is the bottleneck (`gap_fill_round2.md` §5) is **the impossible monitoring task.**
- "Agentic Coding Is a Trap" and the mechanical-engineering-curriculum analogy (§12) is **skills decaying without use** and **riding on the skills of a previous generation** — which is the junior-developer pipeline question exactly.
- Code that passes tests while being unmaintainable (§4), and tests that assert nothing (§5), are **automation camouflaging failure.**
- METR's developers refusing to work without AI (§1) is her night-shift plant in reverse — and her observation that operators need practice to stay capable of take-over is the argument for why that matters.
- StrongDM's "no human reviews code" rule (§6) is the logical endpoint she warns about: if the human cannot check in real time, the only honest options are a machine checker (their holdout scenarios) or a human kept in genuine practice.

A 43-year-old paper that anticipates the current argument this closely is a gift to a book: it makes the point that **none of this is new**, which is both humbling and the book's central claim — the discipline exists, the software industry just has not read it.

---

## 7. Leveson, *Engineering a Safer World* — read in the parts that matter, and it changes the book's claim

Full text obtained legally from the Internet Archive item `mit_press_book_9780262298247`, licensed **CC BY-NC-ND 4.0** (confirmed in the item metadata), via its plain-text file, on 23 Sep 2026. Read: the table of contents, section 4.3 (Process Models), section 10.2 (Intent Specifications), the first discussion of risk migration, and a citation count across the whole text.

### What she has already done
- **She has built the good regulator theorem into engineering practice.** Conant & Ashby (1970) is reference 39 in her bibliography; Ashby's *Introduction to Cybernetics* and "Principles of the self-organizing system" are also cited.
- STAMP's third core concept (after safety constraints and the hierarchical control structure) is the **process model**. She lists four conditions required to control any process: a **goal**, an **action** condition (downward control channels), an **observability** condition (upward feedback), and a **model** condition — any controller, human or automated, needs a model of the process it controls. Her Figure 4.6 caption states it outright: every controller must contain a model of the process being controlled.
- **Accidents happen when the controller's process model does not match the process.** Her examples: Mars Polar Lander software believed the spacecraft had landed and shut down the descent engines; the captain of the *Herald of Free Enterprise* believed the bow doors were closed; the pilots in the Cali B757 crash misread a navigation beacon symbol.
- From that mismatch she derives **four kinds of inadequate control action**: unsafe commands given; required actions not given; correct commands at the wrong time; control stopped too soon or applied too long. These drive her STPA hazard-analysis method.
- **Process models are needed at every level** — the refinery manager needs a model of maintenance and training state; the CEO a broader, less detailed model of the whole — and **during development, not just operation**, including developers' models of the development process itself.
- **Intent specifications (section 10.2):** she observes that the information most often missing from documentation is **why** something was done the way it was — the intent or design rationale — and designs specifications that integrate rationale, safety analysis and assumptions directly into the spec, organised as a hierarchy where each level constrains the one below.
- **Migration toward the boundary (after Rasmussen):** organisations seeking optimal operation naturally migrate toward and across the boundaries of safe practice, through many local decisions by different people under competitive and budgetary pressure, each optimising in their own context. This predates and underpins Dekker's "drift".
- Citation counts across the full text: Rasmussen 41, CAST 48, Columbia 30, Challenger 18, Dekker 12, "migration toward" 13, Therac 4, Perrow 3, Bainbridge 3, Checkland 3, "software" 291.
- **What she does not cite** (zero hits): Stafford Beer, the viable system model, "requisite variety" as a phrase, Goodhart, Diane Vaughan.

### What this means — the book's claim, corrected
- **The good regulator theorem cannot be presented as the book's discovery or as a neglected idea.** Leveson made it an operating principle of safety engineering in 2011 and it is taught at MIT. Earlier notes (`gap_fill_round2.md` §7 and §19, `SUPERSEDES.md` item 5) framed the theorem as the spine the field had missed. For safety engineering, that is wrong. For software management, platform engineering, organisational design and AI-agent practice, it remains true — those communities have not picked it up.
- **The honest position, and a stronger one:** *Leveson showed that safety is a control problem and that every controller needs an accurate model of what it controls. This book asks the same question of every layer we build to run our work — platforms, metrics, operating models, AI agents, personal systems — and adds three things her framework does not centre:*
  1. **Why the models go wrong systematically, not randomly** — Scott's legibility: the model is built from what is easy to see.
  2. **What automation does to the human controller** — Bainbridge: the operator is left the impossible remainder, and loses the skill to do it. (Leveson cites Bainbridge; the book makes it central for the agentic era.)
  3. **What happens when the controlling layer starts building other layers** — Turchin's metasystem transition, from factories to software factories to agents that write agents. Leveson is about controlling systems, not about systems that manufacture systems.
- Standing on Leveson is also a credibility gain: the book's thesis inherits two decades of application on real aerospace, defence and medical programmes instead of resting on an essayist's analogy.
- **The spec-versus-intent chapter now has a proper resolution.** StrongDM (specify outcomes, hold tests back) and Goedecke (tell the agent why) are both halves of Leveson's intent specification, which carries constraints *and* rationale at every level. The chapter can show that the two 2026 schools were reconciled in safety engineering around 2000 — and that nobody in software noticed.
- **Leveson supplies three ready-made model-mismatch cases** — Mars Polar Lander, *Herald of Free Enterprise*, Cali — with her analysis, citable to an open-access source.

---

## What this round changes

1. **The book now has a base rate, not just anecdotes.** 245 curated incidents, free, with the official reports behind many of them.
2. **Two ignored research communities are now in scope** — resilience engineering (Cook, Woods, Hollnagel, Dekker, Rasmussen, Vaughan) and organisational cybernetics (SCiO). Neither appears in the 34 comparable books.
3. **A rival framework has surfaced and must be addressed:** Leveson's STAMP already treats safety as a control problem. The book's claim has to be positioned relative to it rather than around it.
4. **Three new must-reads**, all free: Cook's eighteen points (done), Leveson's open-access book (download in a browser), and Bainbridge's "Ironies of Automation" (find and verify).

### Gaps
- Bainbridge 1983 not located or read.
- Leveson's open-access book not read — only its framework characterised from secondary sources.
- The 245 post-mortems have not been tagged by mechanism; that is a day's work and would produce original analysis.
- `lorin/major-incidents` returned 404 at the path tried; find the correct repo.
