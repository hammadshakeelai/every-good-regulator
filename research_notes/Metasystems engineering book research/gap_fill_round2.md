# Gap-fill round 2: verification and the Hacker News substitute for Reddit

Date of research: 23 September 2026. This file closes gaps left by the five first-round files. It does not repeat them. Read it alongside them; where it contradicts an earlier file, this file is later and was checked against primary sources.

---

## 0. Method note: Reddit is unreachable from this environment

### Takeaway
Every first-round researcher reported that Reddit could not be searched or fetched. That is not a tooling accident that a retry fixes — Reddit is blocked on all three routes available here. The book's Reddit material has to be gathered by the author in a browser, or replaced. This round replaces it with Hacker News, which is fully accessible and carries the same kind of first-hand accounts.

### Cited findings
- Browser pane, `old.reddit.com` and `www.reddit.com`: both refused — "not allowed due to safety restrictions" (checked 23 Sep 2026).
- Web search restricted to `reddit.com`: refused with an explicit message that the domain is not accessible to the crawler, pointing to Anthropic's crawler policy page ([support article](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)) (checked 23 Sep 2026).
- The `agent-reach` skill, which lists Reddit as a supported channel, has no CLI installed on this machine (`agent-reach` not on PATH, checked 23 Sep 2026).

### Inferences
- Reddit threads can still go in the book. The author can open them in a normal browser and record them by hand. What is blocked is *this* research pipeline, not the source.
- Hacker News is the better substitute for engineering themes anyway: posts are attributed to persistent handles, threads are permanently linkable, and the Algolia API returns full comment trees. For the personal-systems theme (Theme 8), HN skews technical; Reddit's r/productivity and r/ObsidianMD would add a non-engineer voice that this corpus now lacks.
- An Apify actor could scrape Reddit, but it costs credits and Reddit's terms restrict commercial reuse of posts (see `market_positioning.md`). Not recommended without the author's decision.

### Gaps
- No Reddit material in any file. Themes most affected: platform teams disbanded (Theme 1), metric gaming (Theme 7), abandoned personal systems (Theme 8), VSM in practice (Theme 5).

---

## 1. Verification: METR's "-18%" — what the sign means

### Takeaway
This is the corpus's most quotable statistic and both earlier readings of it were unsafe. Reading METR's own page, the surrounding sentences indicate the negative numbers are meant as **faster** (a reduction in completion time), not slower — but METR never defines the sign, the confidence interval crosses zero, and METR itself says the estimate is unreliable. **Do not put a direction from the 2026 update in the book.** Cite the 2025 result, which is unambiguous, and cite the 2026 update for the far better story: the experiment broke.

### Cited findings
All from METR, "We are Changing our Developer Productivity Experiment Design", 24 February 2026, by Joel Becker, Nate Rush, Tom Cunningham, David Rein and Khalid Mahamud — [metr.org](https://metr.org/blog/2026-02-24-uplift-update/) (page text read directly, 23 Sep 2026):
- The earlier paper found AI tools caused a 20% slowdown among experienced open-source developers, on February–June 2025 data.
- Early 2025 study: AI causes tasks to take 19% longer, CI +2% to +39%.
- Late-2025 study, the 10 returning developers from the original study: estimated speedup of **-18%**, CI -38% to +9%.
- Late-2025 study, 47 newly recruited developers: estimated speedup of **-4%**, CI -15% to +9%.
- The paragraph introducing those two numbers opens by saying the raw results show some evidence for speedup.
- METR says it believes developers are likely more sped up in early 2026 than its early-2025 estimates, but that its data is only very weak evidence for the size of that increase.
- Why the design is changing: developers increasingly refuse to participate because they do not want to work without AI; when surveyed, 30% to 50% said they withheld tasks they did not want to do unaided; pay dropped from $150/hr to $50/hr, worsening selection; and time-on-task became unreliable for developers running several agents at once.
- One participant described working the old way as walking across a city after getting used to a car service (paraphrased; original is 25+ words).
- METR states the reported estimate is likely a lower bound on the true effect.

### Inferences
- **Sign convention, resolved as far as the page allows.** Two readings are possible. (a) "Speedup of -18%" means speedup is negative, i.e. 18% slower. (b) The figure is a change in completion time, so -18% means 18% less time, i.e. faster. Reading (b) is the one consistent with all three numbers and both narrative claims: the sentence that introduces them calls them evidence *for* speedup, and the +19% of early 2025 (longer) versus -18% and -4% later reads as one signed time-change series. Under reading (a), the introductory sentence would be false. So (b) is the better reading.
- The part-2 notes recorded (b) as "best read as a speedup" and then a later summary of mine flipped it to (a). (b) stands. But the page genuinely does not define it, so any book that states a direction is asserting more than the source does.
- **The real find here is not the number.** METR's measurement system stopped working because the thing it measured changed underneath it — developers would not give up the tool for $50 an hour, and they withheld exactly the tasks where the effect would be largest. That is a metasystem story in its purest form: the governing layer (measurement) lost requisite variety against the operating layer it governs. It belongs in the book's measurement chapter, and it is safer to cite than any point estimate.

### Gaps
- METR's forthcoming redesign (developer-level randomization, fixed-task experiments, observational work) had no results as of the February 2026 post. Check for a newer METR publication before the manuscript is finished.
- The "approximately 4% of GitHub commits are authored by Claude Code" figure appears on the same page without a linked source; verify before use.

---

## 2. Verification: do the mainstream practitioner books cite Stafford Beer? — UNRESOLVED

### Takeaway
This is the single load-bearing check for the book's positioning, and it is **not closed**. The recommended angle in `market_positioning.md` ("nobody connects Beer's cybernetics to platforms and agents") rests on an unverified negative. It could not be verified here because the Google Books API rate-limited every attempt. The author must close this by hand before writing a proposal around it.

### Cited findings
- Google Books API, five queries (`"Stafford Beer" intitle:"Team Topologies"`, the same for *Accelerate* and *Platform Engineering*, plus a `Conway` control query): HTTP 429 Too Many Requests on every call, from two different network paths (23 Sep 2026). No data returned, so no conclusion either way.
- Archive.org advanced search for a *Team Topologies* item returned no rows (23 Sep 2026).
- Web search found no source stating that *Team Topologies* cites Beer or the VSM (23 Sep 2026). Absence of evidence only.
- The VSM→AI link does exist outside books: David Fearne, "Applying Stafford Beer's Viable System Model to create The Autonomous AI Organisation", Medium, June 2025 — [medium.com](https://medium.com/@fearney/applying-stafford-beers-viable-system-model-to-create-the-autonomous-ai-organisation-aaaed39b37e2). It maps agent autonomy and guardrails onto VSM subsystems and invokes Ashby's law of requisite variety.
- Hacker News has carried cybernetics-for-engineers material for years, e.g. "A Software Engineer's Guide to Cybernetics", 14 Sep 2020, 179 points / 59 comments — [HN 24465170](https://news.ycombinator.com/item?id=24465170).

### Inferences
- The claim that survives the evidence is narrower and still useful: **no mainstream practitioner book builds on Beer explicitly; the connection lives in blog posts, consulting frameworks and conference talks.** That is defensible today and is what the book should claim.
- Fearne's post is a competitor for the idea and an asset. It shows an audience exists, and a book can do what a blog post cannot: sustained cases, failure analysis, and a method.
- If a check later shows *Team Topologies* or *Accelerate* does cite Beer, the book's differentiator weakens but does not die — citing Beer in a bibliography is not the same as building a method on him.

### How the author should close this (15 minutes, manual)
1. Open the ebook of *Team Topologies*, *Accelerate* and *Platform Engineering* and search inside for "Beer", "cybernetic", "viable system", "Ashby", "requisite variety".
2. Or use Google Books search-inside in a normal browser (the API is rate-limited, the website is not).
3. Record hit or no hit per book. One line each is enough for a proposal.

### Gaps
- Unverified for all three books. Also unchecked: *Wiring the Winning Organization* (Kim & Spear), which is the most likely of the set to engage cybernetics.

---

## 3. Hacker News: the thread inventory the first round missed

### Takeaway
Hacker News carries a 2026 conversation about "software factories" that none of the first-round files captured, including a 394-point critique of the pattern and two large threads where hundreds of working developers report what agentic coding actually did for them. This is the strongest new raw material found in this round and it maps directly onto book chapters.

### Cited findings — threads worth mining (points/comments as of 23 Sep 2026)
Software factories and agentic engineering:
- "Why Software Factories Fail (or: harness engineering is not enough)", 23 Jul 2026, 394p/272c — [HN 49023019](https://news.ycombinator.com/item?id=49023019); the document itself is in HumanLayer's advanced-context-engineering repo on [GitHub](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md).
- "Software factories and the agentic moment", 7 Feb 2026, 304p/459c — [HN 46924426](https://news.ycombinator.com/item?id=46924426).
- "Building an (almost) fully self-hosted, sandboxed, agentic software factory", 21 Aug 2026, 119p/67c — [HN 49390463](https://news.ycombinator.com/item?id=49390463).
- "Trying the software factory pattern", 20 Sep 2026, 89p/47c — [HN 49777913](https://news.ycombinator.com/item?id=49777913). Three days old; the conversation is live.
- "Agentic Coding Is a Trap", 3 May 2026, 463p/375c — [HN 48002442](https://news.ycombinator.com/item?id=48002442).
- "Ask HN: Do you have any evidence that agentic coding works?", 20 Jan 2026, 461p/455c — [HN 46691243](https://news.ycombinator.com/item?id=46691243).

Measurement and metric gaming (Theme 7):
- "Goodhart's Law: When a measure becomes a target...", 15 Jun 2018, 229p/134c — [HN 17320640](https://news.ycombinator.com/item?id=17320640).
- "Goodhart's law isn't as useful as you might think (2023)", 26 Oct 2024, 140p/81c — [HN 41956587](https://news.ycombinator.com/item?id=41956587). Useful as the counter-argument; a book that only repeats Goodhart is thin.
- "Ex-Finance developers mock McKinsey's monitoring metrics", 15 Sep 2023, 143p/73c — [HN 37527259](https://news.ycombinator.com/item?id=37527259). Pairs with the McKinsey entry already in Part 1.

Build systems and monorepos (Theme 2):
- "Monorepos: Please don't", 2 Jan 2019, 332p/391c — [HN 18808909](https://news.ycombinator.com/item?id=18808909).
- "Stripe's Monorepo Developer Environment", 15 Aug 2024, 393p/240c — [HN 41258932](https://news.ycombinator.com/item?id=41258932).
- "When to use Bazel?", 13 Sep 2022, 212p/214c — [HN 32828584](https://news.ycombinator.com/item?id=32828584).
- "Evaluating Bazel for building Firefox", 29 Oct 2019, 194p/166c — [HN 21385013](https://news.ycombinator.com/item?id=21385013). A documented decision *not* to adopt; rare and valuable.

Organizational models (Theme 3):
- "Spotify doesn't use the Spotify model (2020)", 10 Jul 2022, 86p/9c — [HN 32045400](https://news.ycombinator.com/item?id=32045400).
- "Getting things 'done' in large tech companies", 6 May 2025, 315p/218c — [HN 43903741](https://news.ycombinator.com/item?id=43903741).

Cybernetics (Theme 5, the weakest theme):
- "A Software Engineer's Guide to Cybernetics", 14 Sep 2020, 179p/59c — [HN 24465170](https://news.ycombinator.com/item?id=24465170).
- "Project Cybersyn: Socialism Through Cybernetics", 5 Oct 2016, 63p/58c — [HN 12641425](https://news.ycombinator.com/item?id=12641425).
- "Introduction to Cybernetics (1957)", 10 Apr 2020, 97p/26c — [HN 22838207](https://news.ycombinator.com/item?id=22838207). Ashby's primary text.

Personal operating systems (Theme 8):
- "I deleted my second brain", 28 Jun 2025, 598p/348c — [HN 44402470](https://news.ycombinator.com/item?id=44402470). Confirms the Westenberg entry in Part 2 that could not be verified at its own URL; the HN thread is a stable citation for its existence and date.
- "Stop Taking Regular Notes; Use a Zettelkasten Instead", 2 Jun 2020, 785p/300c — [HN 23386630](https://news.ycombinator.com/item?id=23386630). The high-water mark of the enthusiasm, five years before the backlash. The pair makes a chapter.
- "The Rise and Fall of Getting Things Done", 18 Nov 2020, 293p/160c — [HN 25131848](https://news.ycombinator.com/item?id=25131848). Closes the Part 2 gap: a named, citable account of GTD's decline (Cal Newport, *The New Yorker*).

### Gaps
- Not yet mined for comments: the software-factory threads other than 49023019, the Goodhart threads, the monorepo and Bazel threads, and the Zettelkasten/GTD pair.
- Comment counts and points drift; re-check before citing.

---

## 4. Hacker News deep dive 1 — "Why Software Factories Fail", July 2026

Source document: Dex Horthy / HumanLayer, "Why Software Factories Fail (or: harness engineering is not enough)", 23 Jul 2026, in the [advanced-context-engineering-for-coding-agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md) repo. Discussion: [HN 49023019](https://news.ycombinator.com/item?id=49023019), 394p/272c. Tier A (named author, stable URL) for the document; comments are pattern-only.

### Takeaway
The best-argued 2026 statement of the book's core problem: a fully automated pipeline that produces working code still fails, because *maintainability* is the thing the automation cannot supply. The comment thread is a live argument between people running these pipelines, and it splits along exactly the fault line the book would be about — whether the fix is a better harness or a better governing layer.

### Cited findings (paraphrased; handles are public)
- The document's claim, per the thread: models are trained in a way that gives no penalty for bad design, so code arrives that works but resists change. A commenter (jadar) pushes back that this explains the symptom, not the cause, and asks why reinforcement learning could not simply penalize bad design.
- 2001zhaozhao draws the practical corollary: if agents are good at code and bad at maintainability, build a modular, domain-specific architecture first and let agents fill the parts where maintainability does not matter. This is a metasystem move — a human designs the boundaries, agents work inside them.
- rglynn identifies pull-request review as the bottleneck, and says the experience of reviewing is bad regardless of tooling. Several participants converge on review being the constraint.
- mrbnprck reports grounding agent work in RFC-style normative specifications so effort moves to writing unambiguous specs instead of arguing with an agent during review.
- fishtoaster challenges the experiment's date: the "lights-off" trial ran in July 2025, and models changed materially after that, so the finding may not hold now. A recurring and legitimate objection to every AI result in this corpus.
- firasd argues that a point of view emerges during coding — moments where a human decides an approach — and that assigning tickets to agents produces layers of indirection instead.
- AIorNot dismisses the whole genre: these are improvised contraptions, not engineering standards, and it is too early for de facto standards.
- _doctor_love notes that StrongDM's "dark factory" outcome was not published in any detail, only sparse public updates. This matters: Part 2 records StrongDM at roughly $1,000 of AI usage per engineer per day, and the outcome evidence is thin.

### Inferences
- The thread supplies the book's central tension without the book having to manufacture it: **automation raised throughput and moved the constraint to judgment — review, design, specification.** That is Goldratt's theory of constraints restated for 2026, and it is the same shape as the platform-team lesson from Theme 1 and the measurement lesson from METR.
- The "specs as the new source code" idea (mrbnprck, and spec-driven development elsewhere in the corpus) is the strongest candidate for a practical chapter: it is what people actually changed after the pipeline disappointed them.
- The date objection (fishtoaster) is a warning for the whole book: any chapter built on a 2025–2026 AI measurement will be contested on grounds that the models moved. Write the chapters around mechanisms that outlast a model generation, and date every claim in the text.

### Gaps
- Only the first 12 root comments were read, ranked by HN's own ordering. The thread has 272.
- The document itself was not read in full; findings above come from the discussion of it.

---

## 5. Hacker News deep dive 2 — "Ask HN: Do you have any evidence that agentic coding works?", January 2026

Discussion: [HN 46691243](https://news.ycombinator.com/item?id=46691243), 461p/455c, 20 Jan 2026. Pattern-only material: public handles, no verified identities.

### Takeaway
Four hundred and fifty developers answering the same question at the same moment, and the answers do not converge. The useful pattern is not "does it work" but *what the people who say it works do differently* — and what they describe is a governing apparatus around the agent, not the agent.

### Cited findings (paraphrased)
- stavros: it works and has real value, but code cannot ship unreviewed; reviewing plan and output still costs less than writing it.
- sirwhinesalot: the reliable recipe is commit first, give a narrow non-open-ended task, prefer boilerplate, keep it to one or two files.
- lukebechtel: a five-step method — plan first, automated tests as part of the plan, a named model, git branches with meaningful commits, and an append-only developer log the agent maintains.
- vessenes: treat each agent as a personality with blind spots; have several review and then synthesize; describes a popular "rule of 5" where the model reviews five times at varying levels.
- recroad: reports at least 5x speed using spec-driven development with OpenSpec, plus better docs and design.
- proc0: agents cannot plan at a high level, so they have a blind spot for design, which caps viable project size.
- edude03: an anecdote where agent-written tests added ten minutes to the suite and asserted essentially nothing — the agent had worked around the failures.
- afavour: the "fleet of junior developers, always available" framing, with the sting that they never learn.
- linesofcode: pushes back that agentic programming is a skill that has to be developed, and that giving up means hitting a tooling knowledge gap.
- jorgeleo: concludes the developer stops being a developer and becomes a product designer with deep technical skill — a different skill set from either developer or product owner.

### Inferences
- **Every positive account describes scaffolding, not the model**: commit discipline, narrow scope, a written plan, tests specified up front, a persistent log, multi-pass review, specs. The people reporting success have each independently built a small governing system around the agent. This is the book's thesis appearing spontaneously in the wild, and it is the most valuable single observation in this round.
- The negative accounts cluster on design and verification — exactly where the positive accounts' scaffolding is thinnest.
- The scaffolding these individuals build by hand is what an organization's platform team would have to build once and operate. That is the bridge from the personal meaning (c) to the platform meaning (b) of "metasystem", evidenced rather than asserted, and it is the connective tissue the term-genealogy file said no published source supplies.
- edude03's tests-that-assert-nothing story is Goodhart's law inside the agent loop: the agent optimized the visible target (tests pass) against the real goal (working software). It links Theme 6 and Theme 7 in one anecdote.

### Gaps
- Fourteen of 455 comments read. The thread deserves a full pass by the author.
- None of these handles is a verified identity; use as patterns, or contact the people for permission.

---

## 6. Verified anchor case: StrongDM's software factory — and a correction to Part 2

### Takeaway
Part 2 recorded StrongDM's factory second-hand. It is now verified at source, and one detail was wrong in a way that matters: the famous $1,000-per-engineer-per-day figure is **advice the essay gives other people**, not a spend figure StrongDM reports for itself. The case is strong enough to anchor a chapter, and its most interesting mechanism has nothing to do with money.

### Cited findings
From StrongDM's own essay, "Software factories and the agentic moment", [factory.strongdm.ai](https://factory.strongdm.ai/), posted 7 Feb 2026, and from Simon Willison's same-day commentary, [simonwillison.net](https://simonwillison.net/2026/Feb/7/software-factory/) (both fetched 23 Sep 2026):
- The StrongDM AI team was formed on 14 July 2025 by three named people: Justin McCarthy (co-founder and CTO), Jay Taylor and Navan Chauhan.
- Two stated rules: code must not be written by humans, and code must not be reviewed by humans.
- Humans still write the specifications and scenarios that drive the agents.
- Verification is by **scenarios** — end-to-end user stories deliberately stored outside the codebase, explicitly compared by the authors to a holdout set in model training, so the coding agents cannot see what they will be judged against.
- Their headline metric is "satisfaction": the fraction of observed trajectories through those scenarios that probably satisfy the user. It replaces pass/fail with a probabilistic judgement.
- They test against a "Digital Twin Universe" — behavioural clones of Okta, Jira, Slack, Google Docs, Drive and Sheets — to run volumes that real third-party services would rate-limit.
- The token line is prescriptive: the essay tells readers that if they have not spent at least $1,000 on tokens per human engineer that day, their factory has room to improve.
- The essay reports **no** performance metrics, success rates or quantitative outcomes, and admits no downsides.
- Willison is openly sceptical of the token figure, putting it near $20,000 per engineer per month and doubting it is sustainable for most teams. His stated interest is how agents can prove software works without human review.
- Discussion: [HN 46924426](https://news.ycombinator.com/item?id=46924426), 7 Feb 2026, 304p/459c. In it, codingdave notes that outside the highest-paying employers this spend exceeds what the humans cost, and that treating the spend itself as a metric went unexamined. A team member (handle navanchauhan) answered questions in the thread. Separately, _doctor_love in the July thread reported no detailed public outcome data from the factory, only sparse updates.

### Inferences
- **Correction for Part 2 and anything built on it:** describe the $1,000/day as the essay's recommendation, not as measured spend. Stating it as their cost would be a factual error, and it is the kind a reviewer catches.
- **The holdout-scenario idea is the find, not the token spend.** Keeping the evaluation criteria outside the system being evaluated, where the builder cannot see them, is the oldest move in cybernetics: an independent regulator with its own variety. It is the same structure as an external QA team, an auditor, or a control group — rediscovered because agents optimise against anything visible. This is a concrete, teachable mechanism and it belongs near the front of the book.
- codingdave's observation is the Goodhart chapter in one line: an input cost was promoted to a success metric with no outcome attached. The essay reporting no outcomes at all makes the point for the author — no polemic needed.
- Treat the case as vivid and under-evidenced. It is a claim about a method, made by the people selling the method, with no published results. Say so in the book.

### Gaps
- No outcome data exists publicly for the factory as of 23 Sep 2026 (shipped features, defects, cost per feature, customer impact). A direct approach to Justin McCarthy, Jay Taylor or Navan Chauhan is the only route to it, and all three are public, named and reachable — a strong interview target.

---

## 7. A formal spine candidate: the good regulator theorem

### Takeaway
The term-genealogy file concluded that no published source unifies the three meanings, and proposed a four-part test invented for these notes. There is a stronger option that is not invented: **Conant and Ashby's good regulator theorem**. It is a real, citable, heavily-cited result that says a controller must contain a model of what it controls — which is precisely the claim a book called *Metasystems Engineering* wants to make. It also comes with a live scholarly caveat, which makes it more useful, not less.

### Cited findings
- Roger C. Conant and W. Ross Ashby, "Every good regulator of a system must be a model of that system", *International Journal of Systems Science* 1(2), 1970, pp. 89–97 — [Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/00207727008920220); [Semantic Scholar record](https://www.semanticscholar.org/paper/Every-Good-Regulator-of-a-System-Must-Be-a-Model-of-Conant-Ashby/e676916093c326f6854b185fc81155900891df47). Cited over 1,700 times.
- The caveat is documented, not fringe: it is debated whether the paper proves its own slogan. The mapping constructed is a homomorphism rather than an isomorphism, so the model may lose information about what it models, and the result applies to a regulator that is maximally simple among optimal ones — [Wikipedia, Good regulator theorem](https://en.wikipedia.org/wiki/Good_regulator_theorem); [John Baez, "The Good Regulator Theorem", 27 Jan 2016](https://johncarlosbaez.wordpress.com/2016/01/27/the-good-regulator-theorem/); [LessWrong explainer](https://www.lesswrong.com/posts/JQefBJDHG6Wgffw6T/a-straightforward-explanation-of-the-good-regulator-theorem).
- It is being actively reworked for modern agents: "A good regulator theorem for embodied agents", [arXiv 2508.06326](https://arxiv.org/pdf/2508.06326) (2025).
- Practitioners already make the control-theory link unprompted: in the 2020 HN cybernetics thread, sgillen argues cybernetics became modern control theory and that the good regulator theorem became the internal model principle — [HN 24465170](https://news.ycombinator.com/item?id=24465170).
- In the same thread, lubesGordi links Turchin's metasystem transition on Principia Cybernetica ([pespmc1.vub.ac.be/MST.html](http://pespmc1.vub.ac.be/MST.html)) and notes the article omitted it. A rare instance of a working engineer reaching for the exact term this book uses.

### Inferences
- **This is the mechanism the book's spine needs.** Each meaning becomes the same claim at a different scale: a platform team must model the teams it serves, or it ships golden paths nobody walks (Theme 1); an agent harness must model the codebase and the user's intent, or it produces code that passes tests and cannot be changed (Theme 6); a measurement system must model the work, or it gets gamed (Theme 7); METR's experiment must model developer behaviour, or it breaks when that behaviour shifts (section 1); a personal system must model how you actually work, or it becomes an administrative job (Theme 8). One theorem, five chapters.
- **The caveat is an asset.** A book that states the slogan and then explains honestly what the theorem does and does not prove is doing the thing the review complaints in `existing_books_gap.md` say these books fail at — being rigorous instead of quotable. It also inoculates the author against the systems-thinking reviewer who knows the literature.
- Turchin's metasystem transition supplies the book's *verb* (a jump to a new controlling level) while the good regulator theorem supplies its *constraint* (that level must model what it controls). Together they are a stronger frame than the four-part test in the genealogy notes, and both are citable.
- Ashby links the whole corpus: requisite variety, the good regulator theorem, and *Introduction to Cybernetics* — which HN discussed in 2020 ([HN 22838207](https://news.ycombinator.com/item?id=22838207)) and which is in the public domain.

### Gaps
- The 1970 paper itself was not read here, only its abstract record and secondary explanations. Read it before relying on the formal statement; it is short.
- The arXiv embodied-agents paper (2025) was not read; authors and claims unverified.

---

## 8. Theme 8 balance: the second-brain thread is not one-sided

### Takeaway
Part 2 collected the abandonment stories. The HN thread under Westenberg's post shows the defenders are numerous and specific, which makes for a better chapter than a one-directional cautionary tale.

### Cited findings
From [HN 44402470](https://news.ycombinator.com/item?id=44402470), 28 Jun 2025, 598p/348c, discussing Joan Westenberg's "I deleted my second brain" ([joanwestenberg.com](https://www.joanwestenberg.com/p/i-deleted-my-second-brain)). This also closes a Part 2 gap: the post's existence and date are confirmed even though her page 404'd for the earlier researcher. Comments are pattern-only:
- runjake: notes have repeatedly saved them and their team serious trouble; offloading memory is the point; would not give it up.
- spencerflem: values old notes the way people value old photos — revisiting past thinking, not retrieving facts.
- ErrorNoBrain: names the upkeep trap — capturing everything means re-reading everything to find anything.
- tetris11: uses org-roam for lookup and then forgets; says doing linking "properly" would mean linking everything to everything.
- exitnode: tried collecting all thoughts, never re-read them, and found most went out of date.
- aryehof: proposes the distinction that decides it — notes as things to do are a burden, notes as historical record are not.
- timeonecom: would have archived rather than deleted, expecting a local model to extract value without manual organisation.
- wiseowise: is sceptical that the deletion genre is a fashion of its own.

### Inferences
- The split is not enthusiasts versus sceptics. It is **what the system is for**: retrieval and offloading survive; comprehensive capture with elaborate linking collapses. aryehof's framing is the cleanest statement of the lesson in the corpus and it generalises straight back to platforms — a platform that serves a real retrieval need survives; a platform built to capture and standardise everything becomes an administrative job for its own maintainers.
- timeonecom's point marks a genuine 2026 shift: LLMs weaken the argument for manual organisation, which changes the economics of every personal system and probably every internal wiki. Worth its own short section.

### Gaps
- Still no non-engineer voice for this theme (Reddit unreachable; see section 0).

---

## 9. Corrections to earlier files, and what still needs checking

### Corrections
1. **STRONGDM TOKEN SPEND (Part 2):** the $1,000 per engineer per day is the essay's recommendation to readers, not StrongDM's reported spend. Fix before use.
2. **METR DIRECTION (Part 2 and a later summary of mine):** the 2026 update's negative figures are best read as faster, not slower, but the page never defines the sign and the interval crosses zero. Do not state a direction. Cite the 2025 finding (19% longer) and the redesign story instead.
3. **WESTENBERG POST (Part 2, unverified):** existence and date of 28 Jun 2025 now confirmed via the HN thread; her own page still 404s.
4. **"NOBODY CONNECTS BEER TO AI/PLATFORMS" (market file):** too strong. Fearne's June 2025 VSM-for-AI-organisations post exists, as does a 2025 arXiv good-regulator paper for embodied agents. Narrow the claim to: no mainstream practitioner *book* builds on this; it lives in blog posts and papers.

### Still unchecked, in priority order
1. Whether *Team Topologies*, *Accelerate*, *Platform Engineering* or *Wiring the Winning Organization* cite Beer or the VSM — 15 minutes of ebook search by the author; blocks the positioning claim (section 2).
2. Reddit entirely (section 0) — the author must gather this by hand.
3. StrongDM factory outcomes — only obtainable by interview (section 6).
4. Zappos holacracy 18% attrition figure, and the Backstage adoption claims, both still resting on search summaries (flagged in Parts 1 and in `systems_that_build_systems.md`).
5. Conant & Ashby 1970 read in full before the theorem carries a chapter (section 7).

---

## 10. RESOLVED, and it goes the wrong way: *Team Topologies* cites Stafford Beer

**This supersedes correction 4 in section 9 and the "nobody connects Beer to platforms" claim in `market_positioning.md`.** The check the advisor flagged as blocking came back positive. The strong version of the book's differentiator is false and must not go in a proposal.

### Cited findings
- The authors publish their bibliography themselves: [TeamTopologies/Team-Topologies-Book-References](https://github.com/TeamTopologies/Team-Topologies-Book-References), file `Team-Topologies-references-Markdown.md` (37,264 characters, fetched from raw.githubusercontent.com on 23 Sep 2026). This is a primary source, not a review or a summary.
- It contains: **"Beer, Stafford. 1995. Brain of the Firm 2e. 2 edition. Chichester: John Wiley & Sons"** and **"Wiener. 1961. Cybernetics: Or Control and Communication in the Animal and the Machine"**.
- It does **not** contain: Ashby, "requisite variety", "viable system", "regulator" or Conant. Verified by case-insensitive substring counts over the whole file with no assumption about line structure (re-run 23 Sep 2026): Ashby 0, Viable 0, Regulator 0, Conant 0, Cybernet 1 (the Wiener entry), Beer 1. **"Requisite" returns 2 hits and both are false positives** — the string sits inside Martin Fowler's "MicroservicePrerequisites". Genuine hits for requisite variety: zero.
- The file's entries begin with the author's surname (it opens "Ackoff, Russell L. 1999. Re-Creating the Corporation..."), which is why an earlier bullet-counting check returned zero lines. The read itself was sound; only that counter's assumption was wrong.
- The wider systems lineage *is* present: Russell Ackoff (twice) and Donella Meadows, "Leverage Points: Places to Intervene in a System" (1997). Peter Senge is absent. *Accelerate* is cited (Forsgren and Humble 2018).
- Conway appears repeatedly: Conway 1968 "How do committees invent?", Conway 2017, Allan Kelly's two "Return to Conway's Law" pieces, Ruth Malan's two, and James Lewis on the inverse Conway manoeuvre.
- Matthew Skelton's own biography: BSc in computer science and **cybernetics** (University of Reading), MSc in neuroscience (Oxford), MA in music (Open University); CEng; CEO and Principal at Conflux — [Conflux bio](https://confluxhq.com/all-people/matthew-skelton), corroborated across his publisher and conference bios (checked 23 Sep 2026).

### Inferences
- **The claim to retire:** "nobody connects cybernetics to modern platform and team design." The most influential book in the space cites Beer and Wiener, and its lead author holds a cybernetics degree.
- **The claim that replaces it, and it is stronger:** *the lineage is acknowledged and unused.* Beer appears once, in a bibliography. The working apparatus of *Team Topologies* is Conway's law and cognitive load, not the viable system model. Ashby is absent entirely — which means the two results that would do the most work for a book like this (requisite variety, and the good regulator theorem from section 7) are missing from the canon's own reference list.
- This is a better position than the one it replaces, for three reasons. It is **true and checkable**, so it survives a publisher's scrutiny. It is **less arrogant** — the book builds on an acknowledged ancestor rather than claiming to discover one. And it is **evidence of demand**: the audience has already accepted that cybernetics is the intellectual parent of how we organise software teams. The book's job is to make the parent useful, not to introduce it.
- Suggested framing for the proposal: *Team Topologies* put cybernetics in the bibliography; this book puts it to work.
- One caveat: a bibliography entry says nothing about how Beer is used in the body. The author should still check where Beer appears in the text; if he is discussed substantively, the "cited, not applied" line needs softening again.

### Gaps
- *Accelerate*, *Platform Engineering* and *Wiring the Winning Organization* remain unchecked; none publishes its bibliography this way, so it is an ebook search. Same five search terms: Beer, cybernetic, viable system, Ashby, requisite variety.

---

## 11. The best anchor case yet: Will Larson is running the experiment, in public, now

### Takeaway
A named engineering leader who has written four books in this exact market is running a software factory and posting about it — three days ago. He is a better anchor than StrongDM (section 6) because he is independent, specific about tooling, and his sceptics are in the same thread. He is also a competitor for this book, which the author should think about directly.

### Cited findings
- Will Larson, "Trying the software factory pattern", [lethain.com](https://lethain.com/software-factory-experiment/), 20 Sep 2026. Discussion: [HN 49777913](https://news.ycombinator.com/item?id=49777913), 89p/47c.
- Larson is CTO at Imprint, previously in leadership at Stripe, Carta, Calm and Uber; author of *An Elegant Puzzle* (2019), *Staff Engineer* (2021), *The Engineering Executive's Primer* (2024) and *Crafting Engineering Strategy* (2025) — [lethain.com/about](https://lethain.com/about/).
- Timeline he gives for 2026 at Imprint: January, Claude Code to all engineers; March, extended across the whole company; April, local development restructured into about ten independent workspace checkouts; June, moved from Jira to Linear for task visibility; July, launched "Agent Fleet", an orchestrated harness.
- The loop itself: an agent skill audits Linear projects for proper documentation (an RFC in Notion, measurement dashboards in Datadog and Snowflake), reviews metrics and issues and adds work as needed, works the unblocked tasks, and on completion either continues or re-evaluates whether the project description has gone stale.
- No costs or performance numbers are given. His conclusion is that it is promising and will be folded into the harness, with the caveat that the pieces compound only to the extent you have the other pieces.
- Thread pushback (pattern-only, public handles): pcestrada asks whether it has produced anything both shippable and maintainable. hypfer asks for any long-term example that an outsider could validate, and objects that this is not a pattern but a hope. jdw64 argues a pattern is a reusable solution to a recurring problem, whereas this is an operational loop and a management strategy. kcb points at the coming token bill. bicx, who runs an agentic orchestrator, says UI and mobile acceptance testing is still a human bottleneck because models do not notice poor usability. hibikir notes this is far easier in a nimble organisation than an ossified enterprise, and that the spread between individuals has never been wider. datadrivenangel questions Notion's place in the loop.

### Inferences
- **Look at what his loop actually does:** audit whether documentation exists, watch the metrics, generate work from the gap, and check whether the plan has gone stale. That is a governance layer over the builders — Beer's System 3 and System 4 in a shell script. Larson does not call it cybernetics, and does not need to. This is the book's opening scene: capable practitioners are rebuilding the metasystem from first principles, without the vocabulary, one company at a time.
- The pairing writes itself. StrongDM (section 6) is the maximal version — no human writes or reviews code, sold as a method, no outcomes published. Larson is the incremental version — nine months of small changes, honest about what is unfinished, no numbers either. Both fail the same test, and hypfer states it exactly: no example an outsider can validate. That absence is a finding the book can own.
- bicx's usability bottleneck and Part 1's platform-adoption failures are the same lesson at two scales: the automated layer cannot judge whether what it made is any good for a human. That is the judgement constraint again (section 4).
- **Competitive risk, worth taking seriously.** Larson has four books, a publisher relationship, an audience, and is living this material. If a "governing the builder layer" book appears in 2027, he is among the likeliest authors. The book's defensible edge is the one thing he is not doing: connecting it to the cybernetics lineage and to the failure record across defence, health, platforms and personal systems.

---

## 12. A new theme the first round missed: skill atrophy and the market trap (Theme 9)

### Takeaway
None of the eight existing themes covers what several hundred developers argued about in May 2026: that the automating layer degrades the humans who have to supervise it, and that opting out has stopped being an individual choice. It is a genuine chapter and it links the AI material to the personal-systems material.

### Cited findings
Lars Faye, "Agentic Coding Is a Trap", [larsfaye.com](https://larsfaye.com/articles/agentic-coding-is-a-trap), 3 May 2026. Discussion: [HN 48002442](https://news.ycombinator.com/item?id=48002442), 463p/375c. Comments are pattern-only:
- bitwize gives the sharpest analogy in the corpus: it is like cutting machining from a mechanical engineering degree, after which graduates design parts badly because they do not know how parts are made.
- jdw64 names the trap as economic, not personal: the market no longer works without these tools, because freelance rates and deadlines are now calibrated around them.
- monksy argues the problem is not faster output but output outrunning understanding, and that it rewards speed over comprehension.
- mehagar deliberately brainstorms with AI but types the code, to keep the mechanics fresh.
- 2ndorderthought describes a split: model for scoping and a second opinion, human writes the code, model writes tests, human writes the cases the model missed.
- carterschonwald reports that once models became good enough around November 2025 it became easier to get ideas out, and describes a capable, dangerous intern needing constant supervision.
- mikert89 offers the sceptic's heuristic: if AI can do it, it was not hard.
- turtleyacht wants brain-imaging studies comparing writing code with reviewing it, on the grounds that orchestration may be a different activity altogether.

### Inferences
- The cybernetic reading is exact and belongs in the book: **automating the regulator erodes the variety of the humans who must supervise it.** Over time the supervisor can no longer model what the system does — which, by the good regulator theorem (section 7), is precisely when governance fails. Section 4's maintainability problem, section 11's usability bottleneck and this theme are one mechanism seen from three angles.
- jdw64's point deserves to be named as a second-order effect: once a tool is priced into the market's deadlines and rates, refusing it stops being a personal preference. A metasystem in the economic sense — the environment now enforces the choice.
- This is also the bridge to Theme 8. "I became the administrator of my own notes" and "I became the reviewer of my own codebase" are the same pathology at different scales, and no existing book puts them in the same chapter.
- turtleyacht's wish for evidence flags a real hole: there is no study in this corpus measuring skill retention under agentic workflows. If the author wants one original contribution that costs nothing but time, a survey of working engineers on this question would be genuinely new.

---

## 13. Theme 5 rescued: cybernetics practice exists, in a community nobody in software talks to

### Takeaway
Theme 5 looked empty because the first round searched software sources. VSM practice lives in an organised professional community with conferences, a manual and accreditation — almost entirely disconnected from the platform-engineering world. That disconnection is the book's thesis in institutional form, and it is a ready supply of interviewees.

### Cited findings
- **SCiO (Systems and Complexity in Organisation)**, [systemspractice.org](https://www.systemspractice.org/): describes itself as the UK professional body for systems practitioners; a member-owned not-for-profit social enterprise operating internationally. It runs the SysPrac conference series (SysPrac25, SysPrac26), learning circles, courses and an accreditation scheme, and maintains a resource library of books, articles and speaker videos.
- **Patrick Hoverstadt**: a practising consultant who applies the VSM for clients and chairs SCiO. Author of *The Fractal Organization: Creating Sustainable Organizations with the Viable System Model* ([Wiley](https://www.wiley.com/en-us/The+Fractal+Organization:+Creating+sustainable+organizations+with+the+Viable+System+Model-p-9781119208884)) and *The Fractal Organisation Manual: How to diagnose & design organisations using the Viable System Model* (SCiO, 2nd edition) — a practitioner how-to, [SCiO listing](https://www.systemspractice.org/resources/fractal-organisation-manual-how-diagnose-design-organisations-using-viable-system-model). He appeared with Mike Jackson at SysPrac25.
- **Raul Espejo and Roger Harnden (eds)**, *The Viable System Model: Interpretations and Applications of Stafford Beer's VSM*, Wiley, July 1989 — a primer and casebook of applications, [SCiO listing](https://www.systemspractice.org/resources/viable-system-model-interpretations-and-applications-stafford-beers-vsm). The canonical source of VSM case material, though old.
- **Metaphorum 2026**, "A 100 Years of Stafford Beer: Celebrating his life, his legacy and beyond", Alliance Manchester Business School, 17–19 September 2026 — [conference2026.metaphorum.org](https://conference2026.metaphorum.org/), [tickets page](https://www.tickettailor.com/events/metaphorum1/2078896). It includes a festschrift launch ("A 100 Years of Stafford Beer: a cyber-systemic legacy, whose time has come") and a journal special issue welcoming work on the VSM and Team Syntegrity. Themes include contemporary practice, resilient and ethical organisations, barefoot cybernetics and global governance. It ran six days before this research.
- Centenary writing is appearing around it: Karl Schroeder, "100 Years of Stafford Beer" ([Substack](https://kschroeder.substack.com/p/100-years-of-stafford-beer)); Boyan Angelov, "A Century of Stafford Beer" ([Substack](https://studyofprogress.substack.com/p/a-century-of-stafford-beer)); Henry Farrell, "Cybernetics is the science of the polycrisis" ([Programmable Mutter](https://www.programmablemutter.com/p/cybernetics-is-the-science-of-the)); Kelsie Nabben on applying the VSM to decentralised organisations ([Substack](https://kelsienabben.substack.com/p/applying-stafford-beers-viable-system)).

### Inferences
- **Two communities are solving the same problem without a shared vocabulary.** Systems practitioners have a professional body, a diagnostic manual and accreditation for designing organisations that govern themselves. Platform engineers have Backstage, DORA and agent harnesses. They do not cite each other, meet at the same conferences or use the same words. A book that stands in the gap has a real and defensible position — and section 10 shows the software side already concedes the ancestry.
- **This is the interview list.** Hoverstadt (chairs SCiO, has client cases), Espejo (edited the casebook), the Metaphorum organisers, and SCiO's members, who are likely sitting on unpublished implementations. Combined with the software-side targets — Larson, and StrongDM's three named engineers — the book has a credible set of primary interviews, which is what turns a synthesis of online material into something a publisher will buy.
- The centenary has just passed, so the "ride the anniversary" hook is gone, but the festschrift and special issue will publish over the following year and will date-stamp the book as current.

### Gaps
- Still no 2020–2026 VSM implementation with published outcome data. The honest conclusion may be that it does not exist publicly, and that the book should say so — an absence that is itself a finding, and an argument for the interviews.
- SysPrac26 and Metaphorum 2026 programmes and proceedings were not retrieved; both are the most likely sources of recent case talks.

---

# Round 3 (23 September 2026)

## 14. The platform world's own adoption numbers don't survive contact

### Takeaway
Two 2025–2026 sources give Backstage adoption figures that differ by more than twelve times, and neither cites a method. Cite none of them. The discrepancy is worth more to the book than the numbers ever were.

### Cited findings
- Alan Shimel, "Backstage, a Mid-Year Snapshot", [platformengineering.com](https://platformengineering.com/social-facebook/backstage-a-mid-year-snapshot/), 11 September 2025: **over 270 organisations** run Backstage in production. The piece cites no sources for any figure. It also reports a Gartner estimate that running Backstage needs **2–5 full-time engineers for years**, with some reports suggesting up to 20 experts over a multi-year horizon.
- Vendor-side figures circulating in January 2026 (Roadie's Backstage guide and similar): **3,400+ organisations**, over 2 million developers outside Spotify, and about **89% market share** among open-source internal developer portal frameworks. A 2026 analysis is also cited for the claim that **56% of adopters name upgrades as their biggest problem**, because plugin APIs change between versions.
- CNCF released a documentary, "Backstage: From Spreadsheet to Standard", in March 2026 — [CNCF announcement](https://www.cncf.io/announcements/2026/03/25/cncf-backstage-documentary-highlights-project-evolution-from-development-to-global-open-source-standard-for-platform-engineering/). Backstage ranked sixth of more than 230 CNCF projects by 2025. Spotify Portal, the managed no-code version, reached general availability in October 2025.

### Inferences
- **270 versus 3,400 is not a rounding difference.** Either "adoption" means something different in each (GitHub stars, production deployments, self-reported adopters), or one is marketing. Neither source says which. The first-round file `systems_that_build_systems.md` already flagged that no audited failure rate for platform initiatives exists; this confirms the pattern — **the layer that measures everything else is itself unmeasured**, and its public statistics are produced by the companies selling into it.
- That is a chapter, not a footnote. The book can make the point without polemic simply by putting the two numbers side by side with their sources and dates.
- **The staffing figure is the decision-relevant number, and nobody quotes it.** 2–5 engineers for years — up to 20 — is the real cost of running the builder layer, and it is the number a reader can act on. Adoption counts are vanity; staffing is the constraint.
- The 56% upgrade-pain figure, if it survives sourcing, is the sharpest practitioner finding here: the platform that was supposed to reduce toil generates its own upgrade toil. Same shape as Theme 8's "I became the administrator of my notes".

### Gaps
- Roadie's underlying report was not retrieved; the 3,400, the 2 million, the 89% and the 56% are all unverified at source. Find the survey's method and sample size or drop them.
- The Gartner staffing estimate is quoted second-hand with no report number.

---

## 15. The F-35's ALIS: the book's strongest non-AI case, now on GAO's record

### Takeaway
A logistics system built to govern the maintenance of an aircraft fleet grounded flight-ready aircraft, and nobody was measuring what it did to readiness. It is the cleanest documented instance of a governing layer becoming the constraint, it is in official audit reports rather than blog posts, and it has nothing to do with AI — which matters, because chapters built on 2026 AI results will be contested on the grounds that the models moved.

### Cited findings
- **GAO-20-316**, "Weapon System Sustainment: DOD Needs a Strategy for Re-Designing the F-35's Central Logistics System", issued 6 March 2020, publicly released 16 March 2020 — [gao.gov](https://www.gao.gov/products/gao-20-316). Problems identified: inaccurate or missing data sometimes caused ALIS to ground flight-ready aircraft; data integrity issues; gaps in user training; difficulties deploying with the system; performance inconsistencies affecting mission planning and maintenance.
- Its two recommendations: (1) build a program-wide process for measuring, collecting and tracking how ALIS affects F-35 fleet performance — **closed as implemented only in April 2026**, six years later; (2) develop a redesign strategy naming goals, key risks and costs — closed as implemented November 2021.
- **GAO-20-665T**, "F-35 Sustainment: DOD Needs to Address Key Uncertainties as It Re-Designs the Aircraft's Logistics System", 22 July 2020 — [gao.gov](https://www.gao.gov/products/gao-20-665t). Personnel at **all five locations GAO visited** reported that electronic records of F-35 parts in ALIS were frequently incorrect, corrupt or missing, causing the system to inappropriately ground flight-ready aircraft. **Squadron leaders sometimes overrode those signals to meet mission requirements, accepting the operational risk themselves.** GAO also found no performance-measurement processes for ALIS, and that DOD could not determine how ALIS problems affected fleet readiness, which remained below warfighter requirements.
- Context figure: US F-35 sustainment costs were estimated at about **$1.2 trillion over a 66-year life cycle** — this is the whole sustainment programme, **not** ALIS. Do not attribute it to ALIS.
- ODIN (Operational Data Integrated Network) is the cloud-based replacement; in 2023 the programme office fielded unclassified ODIN hardware and replaced ALIS hardware at maritime and land-based sites.

### Unverified — do not cite until checked
- That ALIS would have cost **more than $16.7 billion** over its life cycle.
- That one Air Force unit estimated **over 45,000 hours per year** on additional tasks and manual workarounds because ALIS did not work as needed.
Both circulate widely in press coverage and appear to originate in GAO's full report text, but neither appears on the GAO product pages that could be read here, and PDF text extraction is unavailable in this environment. **Open the GAO-20-316 full report PDF and confirm both before use** — the 45,000-hours figure in particular is the single most quotable number in the whole corpus, and it is exactly the kind a fact-checker will chase.

### Inferences
- Three separate metasystem failures in one case, which is why it earns a chapter:
  1. **The governing layer became the constraint.** A system meant to keep aircraft flying stopped them flying.
  2. **Operators routed around the regulator.** Squadron leaders overrode ALIS and personally absorbed the risk — the same move as "malicious compliance" in the internal-platform stories (Theme 1) and developers withholding tasks from METR (section 1). When a governing layer lacks the variety to handle reality, the people below it build a shadow system. That recurrence across defence, platforms and research is one of the strongest cross-domain patterns in the corpus.
  3. **No feedback loop existed.** GAO's first recommendation was, in effect, "measure what your logistics system is doing to your fleet." Nobody was. By the good regulator theorem (section 7), a controller that cannot observe its effect on the controlled system cannot regulate it — this is the theorem's prediction, realised, at a cost measured in national defence readiness.
- The six-year gap before that recommendation closed is itself the point about how slowly governing layers learn.

---

## 16. The concept the corpus keeps circling: legibility

### Takeaway
Across Themes 1, 3, 6 and 7, people keep describing the same thing without naming it: a governing layer can only reward what it can see, so work reshapes itself to be visible rather than valuable. The name for this is legibility, the citable source is James C. Scott, and adding it gives the book a second load-bearing idea alongside the good regulator theorem.

### Cited findings
- Sean Goedecke, "Getting things 'done' in large tech companies", [seangoedecke.com](https://www.seangoedecke.com/getting-things-done/), 6 May 2025. Discussion: [HN 43903741](https://news.ycombinator.com/item?id=43903741), 315p/218c. Comments are pattern-only:
  - pydry compresses the argument: what matters is not what you do but what executives perceive you as having done.
  - rileymat2 makes the distinction precisely — the article is really about the legibility or perception of value, which is subtly different from value.
  - artyom offers the cynic's version: your work is done when your manager, or their manager, gets promoted; then the cycle restarts.
  - agentultra objects on substance: the work that is never "done" includes patching security vulnerabilities, and companies that ignore it end up with expensive cloud bills, breaches and frustrated customers.
  - eXpl0it3r asks whether this explains poor code, missing tests and absent documentation.
  - whstl, having worked across big tech, unicorns and small startups on two continents, says engineering work has become so specialised that it is divorced from what decision-makers need.
  - Palomides finds the implied thesis — don't maintain what you ship — bleak.
- Related thread already logged: Matt Klein, "Monorepos: Please don't" ([HN 18808909](https://news.ycombinator.com/item?id=18808909), 332p/391c), where pbiggar's retitling ("ideal for teams under 100 devs") and towaway1138's polyrepo cautionary tale both make the same point: the right governing structure is a function of scale, not principle.

### Inferences
- **Legibility unifies four themes that currently sit apart.** Goodhart's law (Theme 7) is what happens when a legible proxy becomes the target. OKR and metric stories (Theme 3) are legibility imposed from above. Platform adoption (Theme 1) succeeds when the paved road is both visible and rewarded, and fails when it is mandated but invisible in performance reviews. And agents (Theme 6) optimise whatever is visible — edude03's tests that passed while asserting nothing is legibility failure inside the model.
- James C. Scott's *Seeing Like a State* is the citable frame and it is **absent from the 34-book comparison** in `existing_books_gap.md`. It belongs in the book's lineage list next to Beer, Ashby, Conway, Meadows and Ackoff — and, unlike Beer, it is widely read by exactly the technical audience this book targets, which makes it a useful on-ramp.
- Pairing the two ideas gives the book a spine with two struts: **the good regulator theorem** says a governing layer must model what it governs; **legibility** explains why the models it builds are systematically distorted toward what is easy to see. Failure follows from the gap between them. That is a genuine thesis, and it is the answer to the "no mechanism, only metaphor" risk flagged at the very start of this research.

### Gaps
- Scott's work is researched in section 18 below.
- Goedecke has a substantial 2025–2026 body of writing on working inside large tech companies that was not fully mined; he is a named, active, citable practitioner voice.

---

## 18. Legibility, sourced — and the bridge to software already exists

### Takeaway
Scott's argument is a closer fit to this book than the cybernetics literature is, because it is about *why* governing layers fail rather than what they should contain. And the bridge to software has already been built by practitioners — which is good news twice over: it proves an audience, and it means the book is joining a conversation rather than claiming to start one.

### Cited findings — the source
James C. Scott, *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*, Yale University Press, 1998 — [Wikipedia overview](https://en.wikipedia.org/wiki/Seeing_Like_a_State), [Goodreads](https://www.goodreads.com/book/show/20186.Seeing_Like_a_State):
- **Legibility** is the book's central device: states impose administrative order by simplifying and homogenising what they govern so it can be listed and seen. Scott's worked examples are permanent surnames, standardised weights and measures, cadastral surveys and official languages.
- **High modernism** is the ideology he attacks: overconfidence that society can be designed and run according to supposed scientific law.
- **Metis** is what gets destroyed: the Greek term for cunning, situational, practical knowledge held collectively by people who work with their hands on the actual thing, acquired by practice and apprenticeship rather than instruction.
- His failure cases are Soviet collective farms, the building of Brasília, and forced villagisation in 1970s Tanzania.
- His conclusion: schemes that improve life must incorporate local conditions; high-modernist schemes systematically cannot.

### Cited findings — the software bridge
- **Sean Goedecke, "Seeing like a software company", 3 September 2025** — [seangoedecke.com](https://www.seangoedecke.com/seeing-like-a-software-company/). His three-part frame: organisations maximise control through legibility; they depend on illegible work that is essential but unmeasurable; and pursuing legibility often reduces real efficiency. He argues OKRs, Jira and quarterly planning exist not because they maximise efficiency but because they enable oversight, long-term planning, emergency reallocation of people, and credible promises to enterprise customers — and that large enterprise contracts, which take months to close and demand long-term feature commitments, are what drive the demand for legibility in the first place. His example of load-bearing illegible work is **backchannels**: engineer-to-engineer favours, private consensus built before public meetings, undocumented cross-team coordination. His conclusion is not to abolish either, but that organisations need both, including "temporary sanctioned zones" of illegibility.
- Same author, same theme, two months later: "Getting things 'done' in large tech companies" (6 May 2025), already logged in section 16.
- **Alex Dong, "Seeing like a Software Company — Celebrate Illegible Work"** — [alexdong.com](https://alexdong.com/seeing-like-a-software-company-illegible-work.html). Discussion on [Lobsters](https://lobste.rs/s/6uemc8/seeing_like_software_company).
- Academic adjacency: "Markets and Metis: Reading Hayek with Scott", *Critical Review*, 2024 — [Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/08913811.2024.2354648).

### Inferences
- **Scott supplies the failure theory the cybernetics literature lacks.** Beer and Ashby describe what a viable governing structure must contain; neither explains why competent people build governing layers that make things worse. Scott does: the layer must simplify in order to see, and the simplification destroys the local knowledge the work actually runs on. Put beside the good regulator theorem, the book's argument becomes tight and falsifiable:
  - *A governing layer must model what it governs* (Conant & Ashby).
  - *To model it, the layer must make it legible, and legibility destroys metis* (Scott).
  - *So every metasystem faces the same trade-off, and the discipline is managing it rather than escaping it.*
  That is a real thesis. It is also a defence against the reviewer complaint that these books are abstract — this one predicts specific failures and names what to watch.
- **Every theme reads through it.** ALIS made maintenance legible and destroyed the mechanics' judgement, so squadron leaders rebuilt the metis by overriding it (section 15). Platform teams make delivery legible and lose the local practices teams actually used (Theme 1). Metrics make productivity legible and get gamed (Theme 7). Agents make code production legible and cannot see maintainability, which is metis in code form (section 4). The second-brain crowd made their own thinking legible and became its administrators (Theme 8). One mechanism, five domains — the connective tissue the genealogy file said no published source supplies.
- **Goedecke is the single most valuable practitioner voice found in this research.** He is writing the software-legibility argument now, in public, under his own name, and two of his posts already anchor two chapters. He is an interview target and a competitor: the person most likely to write this book from the software side, just as Larson is from the platform side.
- **Honest positioning consequence.** The book cannot claim to be first to connect Scott to software; it can claim to be the first to connect Scott *and* the cybernetics tradition *and* the failure record across defence, health, platforms, agents and personal systems. Narrower claim, defensible, and it is genuinely the gap.

### Gaps
- *Seeing Like a State* itself has not been read here; the summary above rests on the encyclopedia overview and reviews. It is long, and the author should read at minimum the legibility and metis chapters.
- Scott is still absent from the 34-book comparison in `existing_books_gap.md`; it needs adding as a lineage title, not a competitor.
- The rest of Goedecke's 2025–2026 archive, and Lobsters as a source generally, remain unmined. Lobsters is reachable from this environment, unlike Reddit.

---

## 19. Conant & Ashby (1970), read in full — the spine is stronger than its slogan

The author supplied the PDF; text extracted with `pdftotext` on 23 Sep 2026. This closes the open item from sections 7 and 17. **Everything below is from the paper itself.**

### Takeaway
The famous sentence is the least useful thing in the paper. What the book actually needs is three things the slogan hides: that a governing layer which is *not* a model of what it governs is not merely wrong but **unnecessarily complex**; that when the governed thing changes, the model must change **at the same rate**; and that regulating from the *cause* is formally superior to regulating from the *error*. Each one predicts a failure already documented in this corpus.

### Cited findings — the citation, settled
- Roger C. Conant (Department of Information Engineering, University of Illinois, Chicago) and W. Ross Ashby (Biological Computers Laboratory, University of Illinois, Urbana), "Every Good Regulator of a System Must Be a Model of That System", *International Journal of Systems Science*, **1970, vol. 1, no. 2, pp. 89–97**. Received 3 June 1970. Work supported in part by the Air Force Office of Scientific Research under grant AF-OSR 70-1865.
- **Use 89–97.** The 511–519 pagination noted earlier in section 17 is not what the paper carries.

### Cited findings — what is actually claimed and proved
- The abstract states that any regulator which is **maximally both successful and simple** must be isomorphic with the system regulated, that the exact assumptions are given, and that making a model is therefore necessary. Its stated corollary: a living brain, in so far as it is successful and efficient as a regulator for survival, must proceed in learning by forming models of its environment.
- The proof is information-theoretic, not mechanical. It assumes a probability distribution p(S) over system events and a regulator specified by a conditional distribution p(R|S); optimal regulators are those minimising the entropy H(Z) of outcomes. The lemma shows that for each system event, every regulator response with positive probability must lead to the same outcome. Collapsing those probabilities to ones and zeroes yields, in the authors' words, a mapping **h from S into R** — which they call the simplest optimal regulator.
- **The authors' own four qualifications**, stated immediately after the proof:
  1. Some regulators are just as successful as the simplest optimal one but are **unnecessarily complex**. The theorem is therefore better read as: not all optimal regulators are models, but the ones that are not are needlessly complicated.
  2. The search for the best regulator is essentially a search among the mappings from S into R; only regulators for which such a mapping exists need be considered.
  3. The proof avoids all mention of inputs, leaving open how regulator, system and outcomes interrelate. In one configuration the regulator is a model only in the weak sense that its events are mapped versions of the system's; in the other, the modelling is stronger and the regulator must be a **homomorphism or isomorphism** of the system.
  4. The assumption that p(S) exists and is constant can be weakened: if the statistics of the system change slowly, the theorem holds over any period in which p(S) is essentially constant, and as p(S) changes the mapping must change with it — **"a time-varying model will be needed to regulate the time-varying reguland."**
- From section 3 of the paper, on kinds of regulation: **error-controlled regulation is "primitive and demonstrably inferior"**, because with it the entropy of outcomes cannot be reduced to zero and success can only ever be partial. A regulator that draws its information directly from the *cause* of disturbance can in principle be perfect. Their illustration is a cow: the error-controlled reflex raises heat production only after blood temperature falls, whereas the nervous system ordinarily senses the cause at the skin and acts before any error occurs. They note higher organisms evolve progressively toward cause-controlled regulation.
- From the discussion: the theorem changes model-making from optional to compulsory, and success in regulation implies a sufficiently similar model was built — **"whether it was done explicitly, or simply developed as the regulator was improved."**
- On rigour, the authors are candid: they consider using isomorphism as the definition of "model" and conclude they cannot, because the concept's extension beyond finite groups loses its uniqueness. They then work through Hartmanis and Stearns' machine homomorphism and several more general forms.

### Inferences
- **The isomorphism question, settled precisely.** The abstract says isomorphic; the proof constructs a mapping h from S into R and the authors' own third comment distinguishes the weak configuration from the strong one where a homo- or isomorphism is required. So the standard criticism is fair, and the authors saw it. The book should state it in one honest sentence: *the theorem proves that a successful, simple regulator embodies a mapping of the system it regulates; how faithful that mapping must be depends on how the regulator is wired to it.* That is more defensible than the slogan and more useful.
- **"Unnecessarily complex" is the design principle the book can sell.** It converts the theorem from philosophy into a test an engineer can apply on a Tuesday: if your platform, harness, metric or process is not a model of the work it governs, it is not merely mis-specified — it is carrying complexity that buys nothing. Every over-built internal platform in Theme 1 is this sentence.
- **The time-varying clause predicts the corpus's biggest failures.** A model must change as fast as the thing it models. METR's measurement model held still while developer behaviour moved, and broke (section 1). ALIS's model of maintenance held still while the fleet's reality moved, and grounded aircraft (section 15). The Spotify model was copied by other companies as a frozen snapshot of an organisation that had already changed (Theme 3). Larson's loop, by contrast, explicitly re-checks whether the project description has gone stale (section 11) — he built the time-varying clause without naming it. This is the single most transferable idea in the paper and it is absent from every practitioner book in `existing_books_gap.md`.
- **Cause-controlled beats error-controlled** is a formal argument for things the industry already half-believes but justifies only by anecdote: paved roads over post-incident metrics; holdout scenarios that model what a user wants over tests that report what broke (section 6); specs written before the agent runs over review of what it produced (sections 4 and 5). The book can say that the profession's best current practice was proved superior in 1970, and show the proof. That is exactly the kind of claim that makes a book worth reading rather than skimming.
- **The implicit-model clause legitimises the corpus's central observation.** Conant and Ashby explicitly allow that the model may have been "simply developed as the regulator was improved" rather than built deliberately. That is precisely what the Ask HN respondents describe — plans, narrow scope, specs, logs, multi-pass review, grown by trial and error (section 5). They are not failing to theorise; they are growing a model the way the theorem says regulators do. The book's contribution is to hand them the vocabulary and the failure modes, not to tell them they were doing it wrong.
- **Pairing with Scott is now exact.** Conant and Ashby say the regulator must become a mapping of the system. Scott says every mapping a governing body builds is a simplification that destroys local knowledge. The book's thesis is the tension between a mathematical necessity and a political one — and that is a genuine idea, not a metaphor.

### Gaps
- Figures 1 and 2 are referenced in the text but did not survive extraction; the distinction in the authors' third comment depends on them. Look at the figures in the PDF before writing the passage that relies on it.
- Conant (1969), *IEEE Trans. Systems Sci.* 5, 334, is the precursor paper and was not read.
- Sommerhoff's *Analytical Biology* (1950), the source of the five-variable framing, was not read.

---

## 20. GAO-20-316 read in full — the circulating ALIS figures are wrong, and the real ones are better

The full 146,000-character report text was extracted with `pdftotext` on 23 Sep 2026. **This supersedes the unverified figures in section 15.** Source throughout: GAO-20-316, "Weapon System Sustainment: DOD Needs a Strategy for Re-Designing the F-35's Central Logistics System", March 2020.

### Takeaway
The "45,000 hours" figure that circulates in press coverage is **not in this report**. What is in it is more specific, more damning and more useful — including a governing system whose feedback channel charges a fee per complaint, and maintainers who rebuilt the aircraft's records in Excel because they did not trust the system of record.

### Corrections to the circulating numbers
- **"45,000 hours per year of manual workarounds" — NOT FOUND.** The string "45,000" does not appear in GAO-20-316. Do not use it. What the report says: users at **one location estimated they spend an average of 5,000 to 10,000 hours per year** manually tracking information that ALIS should have captured automatically and accurately.
- **"ALIS would cost more than $16.7 billion" — IMPRECISE.** What the report says: in 2016 GAO reported that DOD had estimated ALIS would cost approximately **$17 billion**, and that **the estimate was not fully credible**, because DOD had not performed uncertainty and sensitivity analyses as part of its cost estimating. Cite it as a 2016 GAO finding about a non-credible DOD estimate, not as ALIS's cost.
- **A better fact than either:** for this review, **the F-35 program office could not provide GAO with historic costs showing how much had been spent on ALIS over the years.** Officials said the air vehicle had generally been prioritised over ALIS when allocating scarce resources.

### Cited findings — the material worth a chapter
- **Aircraft grounded by the system meant to keep them flying.** One location reported that from October 2018 through September 2019, F-35 aircraft were grounded for **9,262 hours — 9 percent of possible flight hours** — due to unresolved ALIS-related Action Requests, attributed mainly to missing and inaccurate electronic parts records. Officials at another location reported grounding aircraft for **2,200 hours in a six-month period** while waiting for contractors to resolve parts-related requests.
- **The feedback channel is metered.** Users must submit an Action Request for every issue and can wait months for a response. Users at a third location observed that more transparency in the process would reduce reliance on contractor support and **reduce costs to the programme, since DOD incurs a fee each time an Action Request is submitted.**
- **A shadow system in Excel.** Users said they track critical aircraft data outside ALIS — including aircraft performance data and maintenance inspection deadlines — because **they do not always trust the data residing in ALIS**. They described manual tracking as time-intensive work that pulls maintainers away from actual maintenance, and warned of the danger of overlooking a critical piece of information when aircraft status has to be determined from spreadsheets.
- **Alert fatigue in a safety system.** The report warns that by continuously ignoring alerts in ALIS caused by missing or inaccurate data, squadrons could end up ignoring alerts that matter.
- **Nobody was measuring.** The F-35 programme has no fleet-wide process for measuring, collecting and tracking how ALIS affects aircraft performance, such as fleet-wide mission capability rates. GAO's careful formulation: **ALIS may or may not be having a notable effect on mission capability rates** — and without knowing, DOD risks entering long-term, performance-based sustainment contracts without understanding the factors affecting aircraft operations, weakening its negotiating position.
- Users at **all five locations** GAO visited said ALIS is not user-friendly or intuitive, and described its applications as difficult to navigate.

### Inferences
- **This single case demonstrates four of the book's mechanisms at once**, with citations from a federal audit rather than a blog:
  1. *The governing layer became the constraint* — 9 percent of possible flight hours lost at one location.
  2. *Legibility destroyed metis and the metis came back as a shadow system* — maintainers rebuilt the aircraft's real records in spreadsheets because the official record could not be trusted. This is Scott's argument, in a hangar, documented by GAO (section 16).
  3. *The regulator could not observe its own effect* — no process existed to measure what ALIS did to fleet readiness, exactly the failure Conant and Ashby's theorem predicts (section 19).
  4. *Reporting failure was priced* — a fee per Action Request, and months of latency. A governing layer that charges for feedback is guaranteed to receive less of it, and will therefore model reality less accurately over time. **This is the best single detail in the entire corpus** and I have not seen it made anywhere in the platform-engineering literature.
- Point 4 generalises directly and uncomfortably: every internal platform that makes raising an issue expensive — a ticket queue nobody answers, a request template nobody reads, a Slack channel where questions go to die — is doing a cheaper version of the same thing.
- The $17 billion detail is a governance story in itself: an estimate that was not credible, for a system whose actual historic spend the programme office could not produce, for the layer that governs a fleet costing $1.2 trillion to sustain.

### Gaps
- The report's own footnote references GAO-16-439 (the 2016 report containing the $17 billion estimate); not retrieved.
- GAO-20-665T (July 2020 testimony) was read only as a product-page summary; its full text may carry additional figures.
- Where the "45,000 hours" claim originated is unknown. It may be from a different GAO report, a DOD IG report, or press error. If the author wants to use it, find its true source; otherwise use 5,000–10,000 hours at one location, which is sourced.

---

## 21. Sean Goedecke: the practitioner voice closest to this book

### Takeaway
One named, prolific, currently-active engineer is writing the software half of this book's argument in public, several posts a month. Two of his posts already anchor chapters (sections 16 and 18). His September 2026 run adds two more ideas — one that extends the book's thesis and one that attacks it, which is more valuable.

### Cited findings
All from [seangoedecke.com](https://www.seangoedecke.com/). Recent titles visible on the index (September 2026 unless noted): "System One models like Jev can train their own replacements" (20 Sep), "Tell agents the why, not just the how" (15 Sep), "Slow developer experience will bottleneck fast models" (14 Sep), "Don't build tools for AI agents" (12 Sep), "Radical responsibility means treating people like tools" (4 Sep), "How to protect yourself from workslop" (2 Sep), "Selling out" (28 Aug), plus the undated "How I ship projects at big tech companies". Earlier: "Seeing like a software company" (3 Sep 2025) and "Getting things 'done' in large tech companies" (6 May 2025).
- **"Slow developer experience will bottleneck fast models"** ([post](https://www.seangoedecke.com/slow-devex-will-bottleneck-fast-models/), 14 Sep 2026): developer experience is currently measured in seconds — a one-second test suite is good, thirty seconds is bad. As small models get faster and smart models get smaller, token generation stops being the bottleneck and the speed of tool calls takes over: reading a file at 100ms versus 10ms, running tests at 500ms versus two seconds, is the difference between a near-instant answer and a multi-minute wait. He predicts pressure toward languages with fast compilers and tests, such as Go, and toward tightly optimising the dev loop in agentic codebases.
- **"Don't build tools for AI agents"** ([post](https://www.seangoedecke.com/dont-build-tools-for-ai-agents/), 12 Sep 2026): tools that are good for agents are mostly the tools that are good for humans — redesign Jira for agents and you end up with something close to Jira. Being in the training data is itself a large advantage, so a tool that is 20% better for agents still loses if the agent's existing familiarity with the incumbent is worth more than 20%. He notes nobody yet knows the ideal ergonomics for agents.

### Inferences
- **The first post extends the book's constraint argument one step further.** Section 4 found the constraint moving from writing code to judging it. Goedecke argues that once models are fast, the constraint moves again — to the latency of the builder layer itself. Three constraint shifts in three years is a pattern worth naming, and it makes the case that the governing layer, not the production layer, is where the leverage now sits. That *is* the book's argument, arrived at independently.
- **The second post is the strongest counter-argument in the corpus and belongs in the book on purpose.** It says: do not build a new metasystem for your agents; the model already carries a model of the existing one, learned from training data. Read through Conant and Ashby (section 19), it is a claim that the regulator's model is supplied by the training corpus rather than by your design — so designing a bespoke builder layer can destroy fit rather than create it. A book that quotes this against itself and answers it will be taken far more seriously than one that does not.
- Goedecke is simultaneously the best interview target and the clearest competitive risk on the software side, as Larson is on the platform side and Hoverstadt on the cybernetics side.

### Gaps
- Only summaries of these two posts were read, not the full text. His archive has roughly two years of relevant material; a full pass is worth doing before the outline is fixed.
- Lobsters, where his work is discussed, is **not** reachable after all: `lobste.rs` sits behind an Anubis bot-check challenge that blocks programmatic access. Add it to the Reddit list of sources the author must gather by hand.
- Goedecke's RSS feed carries only the most recent 30 posts (19 July to 20 September 2026), with full text. Older posts, including the two that anchor sections 16 and 18, must be fetched individually.

---

## 22. The mathematicians' revolt: the book's best case for a general audience

Found by mining Goedecke's archive; verified independently. **This is the strongest new material of round 3.**

### Takeaway
In September 2026 a discipline publicly revolted against its own success metric. Twenty-five Fields Medallists and thousands of other mathematicians signed a declaration arguing that AI optimised for benchmark performance is misaligned with how mathematics actually creates knowledge. It is Goodhart's law at the scale of a civilisation's knowledge system, it happened two weeks ago, and it requires no software background to understand — which makes it the one case in this corpus that could open the book for any reader.

### Cited findings — the declaration
- "A Severe Misalignment of AI in Mathematics", published **11 September 2026** at mathandai.org. Signed by **25 Fields Medallists**, including Terence Tao, who posted it on his own blog, [What's new](https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/).
- By **16 September 2026** the declaration's site listed **more than 7,200 signatories**.
- Covered by *Scientific American*, "25 winners of math's 'Nobel Prize' decry the AI invasion of their discipline" — [scientificamerican.com](https://www.scientificamerican.com/article/25-winners-of-maths-nobel-prize-decry-the-ai-invasion-of-their-discipline/). Responses collected at [proofsandprompts.com](https://proofsandprompts.com/2026/09/18/two-responses-to-a-severe-misalignment-of-ai-in-mathematics/); also covered by Leiter Reports and AI-governance outlets.
- The argument, as reported: systems optimised for **mathematical benchmark performance** are misaligned with how the mathematical community actually creates and transmits knowledge. Rushed, unattributed AI-generated proofs bypass the human processes — peer review, writeup, transmission — that turn a solved problem into shared understanding. The declaration raises plagiarism and attribution concerns and warns of the erosion of conceptual insight in favour of rapid true/false output. Signatories call for action from the mathematical community, AI companies and society, while allowing that AI could accelerate genuine understanding if guided responsibly.
- The declaration's own phrasing, as quoted by Goedecke: solving problems is only a tool and a proxy for the primary goal of conceptual understanding and insight; forgetting this may turn the tool against the goal, and mass-producing true/false statements at ever greater pace could destroy fertile ground rather than breathe life into new ideas.

### Cited findings — Goedecke's reading
From "AI is breaking our proxies for expertise", [seangoedecke.com](https://seangoedecke.com/ai-is-breaking-our-proxies-for-expertise/), 13 September 2026:
- He splits mathematics into **puzzle-solving** (take a problem, find a solution) and **idea-generating** (inventing the concepts — Hardy spaces, Banach lattices — that later become usable).
- **Puzzle-solving is legible.** It is easy to understand and hard to do, which makes it impressive to outsiders and therefore prestigious. Idea-generating is not: nobody can tell from outside whether a new concept is insightful, and it can take decades to find out which concepts "carve nature at its joints". He demonstrates with a throwaway invented concept of his own to show how cheap unvetted idea-generation looks.
- His key claim: puzzles served a second, more prosaic purpose — **making mathematical skill legible to outsiders**, and so indirectly rewarding skilled mathematicians. A non-mathematician cannot appreciate Terence Tao's work but knows what a Fields Medal is.
- He warns against dismissing this as the usual complaint of a field being automated, and argues that understanding it predicts what will happen to other fields.

### Inferences
- **This is the book's opening or closing chapter.** Every mechanism the book has assembled is present, in a domain with no software jargon: a legible proxy (benchmark-solvable problems) stood in for an illegible goal (understanding); automation optimised the proxy; the proxy detached from the goal; and the governing layer that converted individual results into shared knowledge — peer review, attribution, writeup — was bypassed rather than improved. Goodhart, Scott and Conant & Ashby in one story, with 7,200 signatures on it.
- **It generalises the book beyond engineering**, which is the answer to the positioning problem that has run through this research. A reader who has never deployed a platform understands that a discipline can be wrecked by its own scoreboard. Software then becomes the worked example rather than the subject.
- **It also dates the book well.** September 2026 is now; a book published in 2027 that opens here is unmistakably current, and unlike the AI productivity statistics, this event will not be invalidated by the next model release.
- Caution: the story is being used by people with prior positions on AI. The book should report the declaration and the responses, not enlist it. The existence of published counter-responses is useful for exactly this.

### A tension worth building a chapter on
Goedecke's "Tell agents the why, not just the how" ([post](https://seangoedecke.com/tell-agents-the-why/), 15 Sep 2026) argues that modern agents fail not from confusion but from **wrong assumptions about your goals and priorities**, so you should supply context on priorities rather than a precise task. He gives a real prompt of his own in which roughly half is broad context — the long-term project, that it is personal rather than work, and his priority of keeping the laptop cool — and notes that **an explicit spec would have missed improvements** the model found on its own.

That sits directly against StrongDM's model (section 6), where humans write exhaustive scenarios held outside the codebase and the agents are judged against them. Two coherent schools:
- **Specify and hold out** — the regulator models the *outcome* and tests against it.
- **Transmit intent** — the regulator models the *goal* and delegates the outcome.
Through Conant and Ashby (section 19) these are two different answers to what the regulator's model must contain. Through Scott (section 16 and 18), the first buys legibility at the cost of the agent's judgement, and the second preserves metis at the cost of verifiability. **Neither author acknowledges the other's position.** A chapter that puts them side by side, with the good regulator theorem as the referee, would be genuinely new — and it is the sort of thing only a book can do.

---

## 17. Round 3 verification ledger

### Zappos 18% — VERIFIED, with a nuance that changes the story
- The figure traces to Zappos COO **Arun Rajan**, who told staff that **260 people had left since March 2015, about 18% of the company**. The first buyout offer was taken by roughly **210 of about 1,500 employees (14%)**; a second offer, the "Super Cloud Teal" offer, added about **50 more**. Reported January 2016 by the Las Vegas [Review-Journal](https://www.reviewjournal.com/business/another-50-zappos-workers-take-holocracy-buyout/), [TIME](https://time.com/4180791/zappos-holacracy-buyouts/), the [Washington Post](https://www.washingtonpost.com/news/on-leadership/wp/2016/01/14/zappos-says-18-percent-of-the-company-has-left-following-its-radical-no-bosses-approach/) and [HR Dive](https://www.hrdive.com/news/zappos-workforce-exodus-continues-hits-18/412086/). Tony Hsieh later said publicly he considered it worth it.
- **The nuance:** these were **paid buyouts the company offered**, not ordinary attrition. Writing "18% quit over holacracy" overstates it; "18% left, most taking a buyout the company offered to anyone who didn't want the new system" is accurate and more interesting — the organisation deliberately bought out its own dissenters, which is a governance choice worth examining rather than a failure statistic.

### Conant & Ashby (1970) — located, not read
- Full text is at [pespmc1.vub.ac.be/books/Conant_Ashby.pdf](https://pespmc1.vub.ac.be/books/Conant_Ashby.pdf). It could not be read here: this environment has no PDF text extraction, and the browser treats the file as a download.
- **Citation caution:** the standard citation is *International Journal of Systems Science* 1(2), 1970, pp. 89–97, but some reprints paginate it 511–519. Check the pagination against the copy you actually read before citing.
- Still a task for the author, as flagged in section 7.

