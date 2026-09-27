# Practitioner Experiences: Building and Running Systems That Govern or Build Other Systems

Research compiled 17 September 2026 for a nonfiction book on "metasystems engineering". Catalog of first-hand stories, official reports, and practitioner lessons, grouped into candidate chapter themes.

## Standing notes (read first)

- **Citation tiers.** **A** = official report (GAO, NAO, Parliament, Inspector General, Royal Commission), peer-reviewed or preregistered study, or first-party company engineering post with named authors. Citable with attribution. **B** = named individual writing on a personal blog, newsletter, podcast, LinkedIn/X, or quoted in trade press. Citable with care; verify context and ideally contact the author. **C** = anonymous or pseudonymous forum post (Hacker News, Reddit). Paraphrase as a pattern only; do not attribute by handle in the book.
- **Quoting.** Every direct quote here is under 15 words. Extended quoting of any individual in a published book needs permission from the author or rights holder. Official government reports are generally reusable with attribution (US federal works are public domain; UK Parliamentary material is under Open Parliament Licence), but check each.
- **Verification rule.** A URL appears in an entry only if it was returned by a search result or fetched during this research. Items recalled but not verified are listed in the final "Leads - unverified" section of the relevant theme's Gaps, without links.
- **Dates.** Publication date as shown in or reported for the source. "Date not verified" means it could not be confirmed.
- **Entry format.** URL | date | platform | author | role/context, then paraphrase, lesson, tier.

---

## Theme 1: Internal developer platforms and platform teams - adopted vs. built-and-ignored

### Takeaway
The most repeated platform story is "we built it, nobody came": technically sound platforms fail when run as infrastructure projects instead of products, when adoption is mandated rather than earned, and when old generations are never retired. The counter-examples (Spotify internally, Netflix's paved road) succeeded by making the supported path the easiest path while leaving teams free to leave it.

### Entries

**[1.1] "We built the platform. Nobody used it"**
- URL: https://leaddev.com/technical-direction/we-built-the-platform-nobody-used-it
- Date: 15 September 2026 | Platform: LeadDev | Author: Sandeep Bharadwaj Mannapur | Role: Lead AI/ML engineer who led an internal ML platform team
- Story: Eight months after launching an internal ML deployment platform, the author asked three senior engineers to show how they deployed models; none used the platform (two had built workarounds, one ran manual notebooks). For about a year leadership treated low usage as a communication problem. Recovery came from embedding a platform engineer in product teams' sprints for six weeks, opening the roadmap to product-team prioritization, leadership publicly owning the failure, and setting a "first model deployed in one day" milestone plus a platform NPS.
- Lesson: Low adoption is often a trust problem, not a training problem; "shipped" and "adopted" are different success criteria.
- Tier: B (named author, first-hand, trade publication). Cites a "2026 State of Platform Engineering" figure (45.3% of platform teams name adoption a leading challenge) that should be checked at source.

**[1.2] Backstage: 99% adoption inside Spotify, about 10% average at external adopters**
- URL: https://www.techtarget.com/searchitoperations/news/366558592/Behind-the-scenes-Spotify-Backstage-a-work-in-progress
- Date: 7 November 2023 | Platform: TechTarget | Author: Beth Pariseau | Context: Spotify's head of engineering for Backstage (Helen Greul), Roadie CEO David Tuite, Lunar and U.S. Bank platform leads
- Story: Spotify estimated the average adoption rate of Backstage inside external organizations at roughly 10%, versus near-universal voluntary use inside Spotify. Adopters cited scattered repositories, inconsistent service metadata, stakeholder misalignment over a central catalog, and (in regulated banks) constant compliance pressure. Spotify's stated priority for the year was simply "ease of use".
- Related: The New Stack, "How Spotify Achieved a Voluntary 99% Internal Platform Adoption Rate" - https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/ (date not verified).
- Lesson: A metasystem that works in its home organization does not transfer by installation; the surrounding practices (ownership metadata, golden paths, culture) are what made it work.
- Tier: A/B (trade press quoting named officials).

**[1.3] Spotify golden paths and "rumour-driven development"**
- URL: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem
- Date: August 2020 | Platform: Spotify Engineering blog | Author: Spotify engineering (byline not verified)
- Story: Spotify's autonomy culture produced a fragmented tooling ecosystem in which the only way to learn how to do something was to ask a colleague, which they called rumour-driven development. They responded with Golden Paths: opinionated, supported tutorials per engineering discipline (backend, data, ML, web), later embedded in onboarding and in Backstage.
- Lesson: Autonomy without a supported default path creates fragmentation that a metasystem must actively absorb.
- Tier: A (first-party).

**[1.4] Netflix "paved road" and full cycle developers**
- URL: https://medium.com/netflix-techblog/full-cycle-developers-at-netflix-a08c31f83249
- Date: May 2018 (per search summary) | Platform: Netflix Tech Blog | Authors: Philip Fisher-Ogden, Greg Burrell, Dianne Marsh
- Story: Netflix pushed operational ownership to developers ("operate what you build") and supported them with centrally built self-service tools. Teams may leave the paved road, but then take on responsibility for maintaining their alternative. Tools only spread if they reduce cognitive load for most engineers.
- Follow-up: InfoQ, Greg Burrell at QCon SF on the evolution of full cycle developers - https://www.infoq.com/news/2019/02/full-cycle-dev-netflix/ (February 2019).
- Lesson: Freedom plus a well-maintained default beats mandates; leaving the road has a visible price.
- Tier: A.

**[1.5] Camille Fournier on platform product failures**
- URLs: https://skamille.medium.com/product-for-internal-platforms-9205c3a08142 (fetch blocked; date not verified); The New Stack interview "Platform Engineering: Why You're Doing It Wrong" - https://thenewstack.io/platform-engineering-why-youre-doing-it-wrong/ (date not verified); book *Platform Engineering* (O'Reilly, with Ian Nowland) - https://www.goodreads.com/en/book/show/217312157-platform-engineering
- Author: Camille Fournier | Role: former CTO of Rent the Runway; platform leadership at JPMorgan Chase and Two Sigma
- Story (per search summaries; verify in the book): Fournier describes platform organizations running three generations of solutions to the same problem with no plan to retire any, leaving customers confused and dissatisfied. She identifies two opposite failures: building what the platform team imagines users need, and building every feature users ask for until the platform becomes a "Rube Goldberg" architecture. Small platform teams also fail by imitating big-company systems.
- Lesson: Migration and deprecation are part of the platform product, not an afterthought.
- Tier: B (named expert; the book is the citable source).

**[1.6] "The Internal Platform Nobody Uses" (consultant pattern analysis)**
- URL: https://www.seanlobjoit.com/posts/2026-04-03-the-internal-platform-nobody-uses
- Date: 3 April 2026 | Platform: personal blog | Author: Sean Lobjoit | Role: platform strategy consultant
- Story: Not a single first-hand case but a synthesis of client patterns: golden paths decay without staffed maintenance; one example had 85% of teams registered but about 12% active weekly; mandates are a symptom of poor product-market fit.
- Lesson: "Registration is not adoption"; measure activation and time-to-value.
- Tier: B (opinion; the 85%/12% figure is anecdotal and unsourced).

**[1.7] Will Larson: migrations are the only scalable fix for tech debt, and they rarely fail for lack of staff**
- URLs: https://lethain.com/migrations/ (2018; exact date not verified) and https://lethain.com/migration-isnt-failing-due-to-lack-of-staffing/ (5 May 2022)
- Platform: Irrational Exuberance (personal blog) | Author: Will Larson | Role: engineering leader at Uber, Stripe, Calm, Carta
- Story: At Uber he led a self-service migration off the monolith with a core team that grew only from two to four people over two years by iterating on tooling. At Stripe he argued against a grand migration to services because the context differed. At another company he cancelled a Node.js-to-Go microservices migration and instead moved JavaScript to TypeScript, finishing within a year. His migration recipe: de-risk, enable with tooling, then finish.
- Lesson: Stalled migrations are usually a strategy or design problem; sometimes the right move is to not migrate or to cancel.
- Tier: B (named, first-hand, widely cited; also in his book *An Elegant Puzzle*).

**[1.8] Steve Yegge's "Platforms Rant" (Amazon API mandate vs. Google)**
- URL (copy hosted for a University of Washington course): https://courses.cs.washington.edu/courses/cse452/23wi/papers/yegge-platform-rant.html ; also a GitHub gist copy https://gist.github.com/kislayverma/d48b84db1ac5d737715e8319bd4dd368
- Date: October 2011 (accidentally public Google+ post) | Author: Steve Yegge | Role: ex-Amazon, then Google engineer
- Story: Yegge contrasted Amazon, where around 2002 Bezos mandated that all teams expose data and functionality only through service interfaces, with Google, which he argued built products rather than platforms. The memo was meant to be internal and was published by mistake.
- Lesson: A top-down architectural mandate can create a platform culture, but the painful transition is the price.
- Tier: B (named, first-hand; original post is gone, rely on mirrors carefully).

### Recurring lessons (independent reporters)
- **Treat the platform as a product; adoption must be earned, not mandated.** Reported independently by Mannapur [1.1], Lobjoit [1.6], Fournier [1.5], Netflix [1.4], and Spotify's own adoption framing [1.2]. Five or more sources.
- **What works at the originating company does not transfer by copying the tool.** Backstage 99% vs. ~10% [1.2]; the same pattern recurs in the Spotify model story (Theme 3). Three or more.
- **Retire old generations; migrations are part of the product.** Fournier [1.5], Larson [1.7], and Airbnb's co-existence strategy in Theme 2. Three.
- **Golden paths decay unless someone is staffed to maintain them.** Lobjoit [1.6], Spotify [1.3]. Two (pattern, needs more evidence).

### Gaps
- Could not find a well-documented Reddit thread with a first-hand "our platform team was disbanded" story that could be verified; r/devops and r/platformengineering searches returned vendor content. Forum material here should be treated as pattern only.
- Camille Fournier's Medium post returned HTTP 403; claims attributed to her above come from search summaries and should be checked against her book.
- The "State of Platform Engineering 2026" statistic in [1.1] was not verified at source.

---

## Theme 2: Build systems, monorepos, CI/CD, and developer productivity

### Takeaway
Build-system and repository migrations succeed when they are incremental, tool-driven, and co-exist with the old system (Airbnb, Uber) or when a single decisive automated cutover removes the long tail (Stripe). Several of the best-known "reversals" (Segment, Prime Video) show teams collapsing an over-distributed architecture back into a simpler one once the coordination cost exceeded the benefit. Practitioners on forums are consistently wary of adopting Bazel-class systems without Google-scale need.

### Entries

**[2.1] Segment: "Goodbye Microservices"**
- URL: https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices ; InfoQ coverage https://www.infoq.com/news/2018/07/segment-microservices
- Date: July 2018 | Platform: Segment (now Twilio) engineering blog | Author: Alexandra Noonan (byline from memory, not verified on page)
- Story: Segment split its destination integrations into 140+ microservices, each with its own queue and repo. Shared-library changes had to be deployed across all of them, defect rates rose, and velocity fell. They consolidated into a single service with a unified test suite, cutting test runs from up to an hour to milliseconds and increasing shared-library improvements shipped per year from 32 to 46.
- Lesson: Architecture chosen for isolation can create coordination costs that the team, not the system, has to absorb; reversals are legitimate.
- Tier: A (first-party).

**[2.2] Amazon Prime Video: monitoring service from distributed to monolith**
- URL (archived copy of the original post): https://www.wudsn.com/productions/www/site/news/2023/2023-05-08-microservices-01.pdf ; context in ByteByteGo guide https://bytebytego.com/guides/amazon-prime-video-monitoring-service/
- Date: March 2023 original post (widely discussed May 2023; original date not verified) | Platform: Prime Video Tech blog | Author: Marcin Kolny (from memory, not verified)
- Story: Prime Video's audio/video quality monitoring tool used AWS Step Functions and S3 for intermediate frames, which hit scaling limits and high cost. Moving the components into a single process cut infrastructure cost by about 90%. Only this one service changed; Prime Video as a whole was not re-architected.
- Lesson: The orchestration layer itself can become the bottleneck and the cost center; the lesson is context-specific, not "monoliths win".
- Tier: A (first-party), but popular retellings overstate it.

**[2.3] Stripe: 3.7 million lines from Flow to TypeScript in one pull request**
- URL: https://stripe.com/blog/migrating-to-typescript (also https://stripe.dev/blog/migrating-to-typescript)
- Date: 2022 (migration on Sunday 6 March 2022; exact post date not verified) | Platform: Stripe blog | Author: Andrew Lunny, Tyler Krupicka (Krupicka confirmed via devtools.fm podcast https://www.devtools.fm/episode/33; Lunny not verified)
- Story: Flow's type checker locked up laptops and the editor integration was unreliable. Stripe built a codemod on jscodeshift, ran it over the Dashboard codebase, and merged a single PR on a Sunday; the next day hundreds of engineers started writing TypeScript. The tool was open-sourced.
- Lesson: When tooling can make a migration atomic, a one-shot cutover avoids the long co-existence tail that stalls most migrations (contrast with [2.4]).
- Tier: A.

**[2.4] Airbnb: JVM monorepo from Gradle to Bazel**
- URL: https://airbnb.tech/infrastructure/migrating-airbnbs-jvm-monorepo-to-bazel/ (also on Medium, author Thomas Bao); BazelCon 2024 talk "Lessons from a Large JVM Monorepo" by Janusz Kudelka https://bazelcon2024.sched.com/event/1h6RR/lessons-from-a-large-jvm-monorepo-janusz-kudelka-airbnb
- Date: 2024 (exact date not verified) | Platform: Airbnb Tech Blog | Author: Thomas Bao
- Story: With tens of millions of lines of Java/Kotlin/Scala, local builds of large services took over 20 minutes and pre-merge CI p90 was 35 minutes in 2021. Airbnb migrated breadth-first with Bazel co-existing alongside Gradle, added remote execution and caching, and built a build-file generator. Stated learnings include partnering with pilot teams and avoiding premature optimization.
- Lesson: Co-existence plus automated generation of build metadata lets a build-system migration proceed without stopping product work.
- Tier: A.

**[2.5] Uber: Go monorepo on Bazel**
- URL: https://www.uber.com/us/en/blog/go-monorepo-bazel/ ; follow-up https://www.uber.com/us/en/blog/how-we-halved-go-monorepo-ci-build-time/
- Date: May 2020 | Platform: Uber Engineering blog | Author: Uber Go Developer Experience team (byline not verified)
- Story: Moving Go to a monorepo broke Make and `go build` as workable tools, so Uber adopted Bazel, contributed rule generation upstream, and integrated it with SubmitQueue, its system to keep main always green. Additional work was needed on coverage, sparse checkout, and dependency management.
- Lesson: A monorepo is not a repository decision but a commitment to build a governing metasystem (merge queue, build graph, dependency policy) around it.
- Tier: A.

**[2.6] Hacker News practitioners on Bazel migrations (pattern)**
- Source: Hacker News comments retrieved via HN Algolia API (query "bazel migration", tags=comment), e.g. discussion under "Almost every infrastructure decision I endorse or regret" (Feb 2024), "2 Years at Twitter" (Nov 2022), "When to use Bazel?" (Sep 2022), "Bob: A build system for microservices" (Aug 2022). API query: http://hn.algolia.com/api/v1/search?query=bazel%20migration&tags=comment
- Story (paraphrased patterns): A commenter who led a successful Bazel migration now advises most projects to stay on native toolchains. Another describes two top engineers spending long periods on Twitter's migration and contributing upstream. Others describe teams stuck indefinitely "migrating to remote execution" because toolchains were not hermetic, and one team aborted after two months and built its own alternative over a year.
- Lesson: Google-class build metasystems impose Google-class maintenance; the fit to codebase size matters more than the tool's reputation.
- Tier: C (anonymous handles; paraphrase as pattern only).

**[2.7] Measuring developer productivity: McKinsey framework vs. Beck and Orosz**
- URL: https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity (Part 1) and https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity-part-2
- Date: late August / early September 2023 (per LinkedIn post timing; exact date not verified) | Platform: The Pragmatic Engineer newsletter | Authors: Gergely Orosz and Kent Beck
- Story: McKinsey published a claim that developer productivity can be measured with a framework used at nearly 20 companies. Beck and Orosz argued it measures effort and output rather than outcomes and impact, predicted it would backfire and damage engineering culture for years, and noted it never mentioned revenue or profit.
- Lesson: A measurement metasystem imposed on engineers shapes behavior toward what is measured (see Theme 7, Goodhart).
- Tier: B (named, prominent practitioners; McKinsey's article is the primary counterpart).

### Recurring lessons (independent reporters)
- **Incremental co-existence or atomic automated cutover; avoid the long manual middle.** Airbnb [2.4], Uber [2.5], Stripe [2.3], Larson [1.7]. Four.
- **Distribution and orchestration layers carry costs that can exceed their benefits; reversal is a valid outcome.** Segment [2.1], Prime Video [2.2], HN Bazel regrets [2.6]. Three.
- **Heavy build metasystems need dedicated owners and upstream contributions.** Uber [2.5], Airbnb [2.4], HN [2.6]. Three.

### Gaps
- Not yet verified in this pass: Google's "Why Google Stores Billions of Lines of Code in a Single Repository" (CACM 2016), Google engineering productivity research (Ciera Jaspan, Collin Green), Shopify's modular monolith posts, Meta Buck2, Dropbox and Twitter Pants-to-Bazel write-ups. All are strong Tier A candidates.
- Author bylines for Segment, Prime Video, and Stripe posts are from memory and must be confirmed.

---

## Theme 3: Organizational operating models - Spotify model, Amazon mechanisms, holacracy, flat structures, OKRs

### Takeaway
The best-documented organizational "metasystems" were described in public in idealized form and then quietly revised or abandoned by their originators: Spotify's squads-and-chapters matrix, Zappos and Medium holacracy, Buffer's no-managers experiment, Amazon's two-pizza teams. The recurring finding is that autonomy structures fail without explicit alignment and accountability mechanisms, and that copying another company's snapshot imports its vocabulary but not its context.

### Entries

**[3.1] "Spotify's Failed #SquadGoals"**
- URL: https://www.jeremiahlee.com/posts/failed-squad-goals/ ; podcast follow-up (Engineering Enablement by DX, 11 January 2023) https://getdx.com/podcast/spotify-squads/
- Date: 19 April 2020 | Platform: personal blog | Author: Jeremiah Lee | Role: product manager at Spotify from 2017, later at Stripe
- Story: Lee argues the famous model never worked as described. Chapter leads handled career development but had no accountability for delivery, engineering managers were not true peers to product managers, and disagreements escalated through multiple chapter leads. Spotify published the "autonomy" material but never finished the "alignment and accountability" part, and teams received little Agile coaching. He quotes Joakim Sundén (Spotify agile coach 2011-2017) saying that even at the time of writing they were not doing it, and co-author Anders Ivarsson worrying that people treat it as a framework to copy.
- Lesson: A published operating model is a snapshot of aspiration; matrix structures without delivery accountability create escalation bottlenecks.
- Tier: B (named, first-hand insider; quotes from other named Spotify staff).

**[3.2] "There is no Spotify model" (Spotify's own staff)**
- URL: https://www.infoq.com/news/2016/10/no-spotify-model
- Date: 6 October 2016 | Platform: InfoQ | Author: Ben Linders, reporting a talk by Marcin Floryan (Spotify chapter lead)
- Story: Floryan told audiences not to copy the Spotify model, warning about halo-effect imitation of successful companies. Spotify's actual practice was continuous evolution around principles (autonomy with alignment, trust, data-informed bets), not a fixed structure.
- Related: Crisp blog summary of Henrik Kniberg's views (6 February 2023) https://blog.crisp.se/2023/02/06/leadingcomplexity/leading-complexity-series-summary-1-henrik-knibergs-thoughts-on-the-spotify-model ; Kniberg's original disclaimer framed it as a snapshot, not a recipe (per search summaries, verify in original).
- Lesson: Copy principles, not org charts.
- Tier: B (trade press quoting named insider).

**[3.3] Medium leaves Holacracy**
- URL: https://blog.medium.com/management-and-organization-at-medium-2228cc9d93e9
- Date: 12 August 2016 (per search summary) | Platform: Medium company blog | Author: Andy Doyle | Role: Medium head of operations (role not verified)
- Story: After several years on Holacracy, Medium concluded it was getting in the way of the work. The company kept principles it valued (distributed authority, explicit roles) but replaced the formal system with its own principles, a decision-making rubric, an ownership and greenlighting process, and tools to map the organization.
- Lesson: A governance protocol can become meta-work that competes with the real work; keep the principles, drop the ritual.
- Tier: A (first-party).

**[3.4] Zappos: holacracy ultimatum, exits, and a quiet retreat**
- URLs: Quartz, "Zappos has quietly backed away from holacracy" https://qz.com/work/1776841/zappos-has-quietly-backed-away-from-holacracy (fetch blocked; January 2020 per URL era, date not verified); CNBC, "Zappos CEO Tony Hsieh on getting rid of managers: What I wish I'd done differently" https://www.cnbc.com/2016/09/13/zappos-ceo-tony-hsieh-the-thing-i-regret-about-getting-rid-of-managers.html (13 September 2016); Inc. on the later market-based system https://www.inc.com/cameron-albert-deitch/zappos-tony-hsieh-holacracy-market-system.html (date not verified)
- Story: Zappos adopted Holacracy in 2014 under CEO Tony Hsieh; in 2015 an ultimatum to embrace self-management or take a buyout led about 18% of staff to leave (figure per search summaries; verify at primary source). Over the following years Zappos moved to a market-based system in which teams run like small businesses with their own P&L, and coverage described a quiet move away from Holacracy.
- Lesson: An imposed self-management system needs a transition path and a way to evolve; the "system" eventually gets adapted beyond recognition.
- Tier: A/B (reputable press, named CEO interview).

**[3.5] Buffer: "What We Got Wrong About Self-Management"**
- URL: https://buffer.com/resources/self-management-hierarchy/
- Date: 5 August 2015 | Platform: Buffer blog | Author: Leo Widrich | Role: Buffer co-founder
- Story: Buffer removed all managers, dropped one-on-ones, and used an "advice process". Within months new staff felt lost and experienced staff could not see where to contribute strategically. Buffer reintroduced mentoring and higher-level strategic roles, calling the result an "actualized hierarchy" that emerges from experience without granting veto power.
- Lesson: Flatness is not the same as self-management; removing structure without replacing guidance and accountability overwhelms people.
- Tier: A (first-party, named co-founder).

**[3.6] Valve's flat structure, from a former engineer**
- URLs: PC Gamer, "Ex-Valve employee describes ruthless internal politics at 'self-organizing' companies" https://www.pcgamer.com/ex-valve-employee-describes-ruthless-industry-politics/ (2018; exact date not verified); PC Gamer, "Valve's unusual corporate structure causes its problems, report suggests" https://www.pcgamer.com/valves-unusual-corporate-structure-causes-its-problems-report-suggests/ (date not verified)
- Author/subject: Rich Geldreich | Role: former Valve graphics/engine programmer (Portal 2, Dota 2, CS:GO)
- Story (per search summaries): Geldreich said a hidden corporate layer controls the "self-organizing" part, that informal social networks (who eats lunch with whom) reveal the real power structure, and that stack ranking drove politics and anxiety despite the public employee handbook.
- Lesson: When formal hierarchy is removed, an informal one forms; peer-ranking systems become the real governance.
- Tier: B (named, but social-media origin; verify original posts before quoting).

**[3.7] Amazon: two-pizza teams gave way to single-threaded leaders; mechanisms over intentions**
- URLs: Colin Bryar and Bill Carr, *Working Backwards* (2021); review by Yevgeniy Brikman https://www.ybrikman.com/blog/2023/03/15/working-backwards/ (15 March 2023); analysis https://www.infraculture.org/2021-04-28-working-backwards-separable-single-threaded-teams-and-herbert-simon/ (28 April 2021); "The myth of Amazon's 2-pizza teams" https://www.productleadership.io/p/the-myth-of-amazons-2-pizza-teams-d14f2b4d834f (date not verified); on mechanisms, Adrian Hornsby (AWS) https://medium.com/the-cloud-architect/towards-operational-excellence-part-3-8b727f06a4b6 (date not verified)
- Authors: Bryar (Bezos's former chief of staff) and Carr (former Amazon VP) | Tier A for the book itself
- Story: According to the book (as summarized in reviews), two-pizza teams originally reported to a single multi-disciplinary manager, but such general managers were very hard to find, and some initiatives needed more people. Amazon found team success depended less on size than on having a leader with the skills, authority, and experience to run a dedicated team, which became the single-threaded leader model. Separately, Amazon teaches that good intentions do not work but mechanisms (tool, adoption, audit) do.
- Lesson: Even Amazon's famous structure was an iteration; the durable idea was a mechanism with an owner, not a team size.
- Tier: A (book by insiders) / B (reviews).

**[3.8] "Why We Stopped Using OKRs"**
- URL: https://www.linkedin.com/pulse/why-we-stopped-using-okrs-kyle-racki
- Date: 23 December 2022 | Platform: LinkedIn article | Author: Kyle Racki | Role: company founder/leader (page does not state; widely known as Proposify co-founder, not verified here)
- Story: The company rolled OKRs out organization-wide at once. Teams retrofitted existing projects into objectives (e.g., "launch a company wiki" with page-count key results), forced multi-year ambitions into quarters, used binary or baseline-free key results, and spent heavily on software, training, and planning offsites. They replaced OKRs with a short list of "Big Rocks" set by management, with teams choosing execution.
- Lesson: A goal-setting metasystem can generate more administrative work than alignment; roll out gradually or not at all.
- Tier: B (named, first-hand).

### Recurring lessons (independent reporters)
- **Autonomy without explicit alignment and accountability fails.** Lee/Spotify [3.1], Floryan [3.2], Buffer [3.5], Amazon single-threaded leaders [3.7]. Four.
- **Published models are idealized snapshots; copying them imports vocabulary, not context.** Lee [3.1], Floryan/Kniberg [3.2], Backstage transfer gap [1.2]. Three.
- **Removing hierarchy creates hidden hierarchy.** Valve/Geldreich [3.6], Buffer's "actualized hierarchy" [3.5], Zappos's evolution to internal markets [3.4]. Three.
- **Governance protocols can become meta-work that crowds out real work.** Medium [3.3], OKRs at Racki's company [3.8]. Two (plus Theme 7).

### Gaps
- Quartz Zappos article and PC Gamer Valve articles could not be fetched (403 / truncated). The 18% Zappos exit figure is from search summaries and needs primary confirmation.
- No verified first-hand account from a large-company OKR rollout (Google-scale) was collected; academic evidence on OKR effectiveness was not searched.
- GitHub's 2014 move away from flat structure and Gitlab/Basecamp's operating models were not verified in this pass.

---

## Theme 4: Systems of systems in defense, aerospace, healthcare, and government IT

### Takeaway
Official audits of large integration programs repeat the same diagnosis across countries and decades: unclear ownership of the whole, requirements not understood, warnings from the front line not heeded, contractors owning critical data or architecture, and launch decisions driven by schedule. Recovery stories (Healthcare.gov) begin with someone taking visible ownership, adding monitoring, and putting all parties in one room.

### Entries

**[4.1] F-35 ALIS: GAO calls for a re-design strategy; replaced by ODIN**
- URL: https://www.gao.gov/products/gao-20-316 (report PDF https://www.gao.gov/assets/gao-20-316.pdf)
- Date: 6 March 2020 (publicly released 16 March 2020) | Platform: US Government Accountability Office | Report: GAO-20-316, "Weapon System Sustainment: DOD Needs a Strategy for Re-Designing the F-35's Central Logistics System"
- Story: Personnel at five F-35 locations reported that the Autonomic Logistics Information System still had inaccurate or missing data that unnecessarily grounded aircraft, ineffective training, and deployment difficulties, and that they relied on workarounds. GAO found unclear ownership and governance across multiple improvement efforts, data integrity problems, and uncertainty about the software development approach, and noted DOD had not measured ALIS's effect on readiness since a 2014 recommendation.
- Follow-ups: Air & Space Forces Magazine, "F-35 Program Dumps ALIS for ODIN" https://www.airandspaceforces.com/f-35-program-dumps-alis-for-odin/ (January 2020, date not verified); Defense News on first phase of replacement https://www.defensenews.com/air/2022/01/31/pentagon-completes-first-phase-in-replacing-troubled-f-35-logistics-system/ (31 January 2022); GAO-22-105128 https://www.gao.gov/assets/gao-22-105128.pdf (not reviewed).
- Lesson: When the governing information system of a fleet is owned by a contractor and nobody measures its operational effect, users build shadow systems and the metasystem degrades readiness.
- Tier: A.

**[4.2] UK NHS National Programme for IT: "dismantled" but still costing**
- URL: https://publications.parliament.uk/pa/cm201314/cmselect/cmpubacc/294/294.pdf ; committee news release https://committees.parliament.uk/committee/127/public-accounts-committee/news/181704/dismantled-national-programme-for-it-in-nhs-report-published/
- Date: 2013 (Public Accounts Committee, 19th report of session 2013-14; per search summary published July 2013 - verify) | Platform: UK Parliament
- Story: Launched in 2002 to centralize NHS England's use of information, the programme was the subject of three NAO reports, Committee reports, and a Major Projects Authority review before the government announced in September 2011 that it would be dismantled, keeping component parts under separate management. The Committee expected total cost above £9.8 billion and described it as among the worst contracting fiascos in public sector history, with component programmes still running up costs.
- Related: Computer Weekly, "MPs brand NHS National Programme for IT a 'fiasco'" https://www.computerweekly.com/news/2240205626/MPs-brand-NHS-National-Programme-for-IT-a-fiasco-as-posthumous-costs-rise
- Lesson: A centrally imposed national system that bypasses local owners generates resistance and contractual lock-in that outlive the program itself.
- Tier: A.

**[4.3] HealthCare.gov: HHS Inspector General case study**
- URL: https://oig.hhs.gov/reports/all/2016/healthcaregov-case-study-of-cms-management-of-the-federal-marketplace (full report PDF https://oig.hhs.gov/documents/evaluation/2981/OEI-06-14-00350-Complete%20Report.pdf)
- Date: 22 February 2016 | Platform: HHS Office of Inspector General | Report: OEI-06-14-00350
- Story: Based on interviews with 86 officials, staff, and contractors and thousands of documents covering 2010-2015, OIG concluded the failed October 2013 launch stemmed largely from avoidable organizational missteps rather than technology alone. A central finding was that different CMS divisions each believed they were in charge. Recovery involved clearer leadership, decision-making, and communication.
- Lesson: In a multi-contractor system of systems, the missing component is often the integrator with authority.
- Tier: A.

**[4.4] Mikey Dickerson on rescuing HealthCare.gov**
- URLs: USENIX LISA14 talk, "One Year After the healthcare.gov Meltdown: Now What?" https://www.usenix.org/conference/lisa14/conference-program/presentation/dickerson (November 2014); Nextgov, "Mikey Dickerson on failures and fixes" https://www.nextgov.com/people/2015/03/mikey-dickerson-on-failures-and-fixes/207520/ (March 2015); Complex Systems podcast with Patrick McKenzie https://www.complexsystemspodcast.com/episodes/fixing-government-technology-with-mikey-dickerson/ (date not verified); US Digital Service origins oral history https://usdigitalserviceorigins.org/interviews/mikey-dickerson/
- Role: Google SRE (2006-2013) who took leave to join the rescue, later first administrator of the US Digital Service
- Story (per search summaries): The system depended on dozens of vendors and products; Dickerson worked daily with at least 20 companies. At launch there was no monitoring, so the team learned about outages from CNN. His fixes were deliberately simple: install monitoring, and put everyone in one room so someone was visibly coordinating.
- Lesson: The first move in rescuing a system of systems is to create feedback (monitoring) and a single coordination point.
- Tier: B (named, first-hand, conference talk and interviews).

**[4.5] US Air Force ECSS: $1.1 billion ERP cancelled**
- URLs: Senate Permanent Subcommittee on Investigations report https://www.hsgac.senate.gov/subcommittees/investigations/library/files/report_-air-forces-expeditionary-combat-support-system-ecss-program/ ; IEEE Spectrum, "The U.S. Air Force Explains its $1 Billion ECSS Bonfire" https://spectrum.ieee.org/the-us-air-force-explains-its-billion-ecss-bonfire (date not verified)
- Date: Program 2005-2012, cancelled November 2012; Senate report 2014 (date not verified)
- Story: ECSS aimed to replace over 200 legacy logistics systems with one ERP. After about $1.1 billion, the Air Force concluded it had yielded no significant military capability. Investigators cited an unclear idea of what the system should accomplish, weak leadership, and cultural resistance to changing processes to fit the software. An Air Force official (McGrath, per Defense Daily https://www.defensedaily.com/air-forces-canceled-itprogram-ecsswas-simply-toobig-mcgrathsays/air-force/) said it was simply too big.
- Lesson: Consolidating hundreds of systems into one is a business-process change program, not a software installation.
- Tier: A.

**[4.6] Army Future Combat Systems: the archetypal system-of-systems cancellation**
- URLs: RAND, "Lessons from the Army's Future Combat Systems Program" https://www.rand.org/pubs/monographs/MG1206.html (2012); GAO testimony GAO-09-793T https://www.gao.gov/assets/gao-09-793t.pdf (2009); Nextgov, "Future Combat Systems: Lessons learned" https://www.nextgov.com/people/2009/06/future-combat-systems-lessons-learned/202677/ (June 2009)
- Story: FCS was the Army's largest planned acquisition, meant to field a brigade as a networked system of systems. It was cancelled in 2009 after aggressive timelines, poorly understood requirements, and uncertain costs; vehicle designs did not reflect combat lessons from Iraq and Afghanistan. GAO noted the problems were apparent from the start rather than discovered late, while praising its holistic vision and experimentation.
- Lesson: A system-of-systems vision needs knowledge-based decision points per component; the network cannot be integrated faster than its parts mature.
- Tier: A.

**[4.7] Canada's Phoenix pay system**
- URLs: New Zealand Digital Government lessons summary https://www.digital.govt.nz/showcase/phoenix-payroll-project-lessons-learned ; CBC, "Phoenix pay system fiasco: 10 years of mistakes and lessons" https://www.cbc.ca/news/canada/ottawa/federal-phoenix-pay-system-10-year-anniversary-9.7093933 (2026, date not verified); Auditor General 2026 report "Modernizing the Pay System" https://www.canada.ca/en/auditor-general/our-work/audit-reports/auditor-general-report-2026-modernizing-pay-system.html
- Date: Go-live 2016; Auditor General's 2018 report called it an "incomprehensible failure" of project management and oversight
- Story: Executives cut functionality and testing to meet budget and schedule, and ignored warnings from the Miramichi pay centre and departments. After go-live, employees were underpaid, overpaid, or unpaid. The Auditor General judged the go-live decision unreasonable given information available at the time, and recommended simplifying pay rules before automating them and independent assurance at go-live.
- Lesson: Automating unsimplified rules encodes complexity into the system; the go-live gate needs independent authority.
- Tier: A (Auditor General) / B (secondary summaries).

**[4.8] Australia's Robodebt: Royal Commission on automated decision-making**
- URL: https://robodebt.royalcommission.gov.au/publications/report
- Date: 7 July 2023 | Platform: Royal Commission into the Robodebt Scheme (Commissioner Catherine Holmes AC SC)
- Story: From 2015 to 2019 an automated data-matching system averaged annual tax income to raise welfare debts, reversing the onus of proof onto recipients. The three-volume report found the scheme was devised without regard to social security law and was unfair and unlawful, and made 57 recommendations including a legislative framework and an oversight body for automated decision-making.
- Lesson: An automated governing system with no meaningful review path scales injustice; oversight of the automation must itself be designed.
- Tier: A.

**[4.9] Kessel Run: the Air Force software factory's rise and pivot**
- URLs: Air & Space Forces Magazine, "Air Force Software Factory Kessel Run Is Pivoting. Not Everyone Is Happy" https://www.airandspaceforces.com/kessel-run-air-force-software-factor-pivoting/ (1 March 2025, Shaun Waterman); Defense One, "Kessel Run works through growing pains" https://www.defenseone.com/defense-systems/2020/09/kessel-run-works-through-growing-pains/194802/ (September 2020); Modern War Institute https://mwi.westpoint.edu/software-wins-modern-wars-air-force-learned-kessel-run/ (date not verified)
- Story: Kessel Run, founded in 2017, brought agile and DevSecOps practices to Air Force software with mixed teams of airmen, civilians, and contractors, growing to about 2,000 people in three years. By 2022 it was described as failing its mission (the article attributes this assessment; attribution to founder Bryon Kroger vs. others should be checked). Critics cited 50% staff turnover every six months, no career paths, contractor budget pressure, full C-suite rotation every two years, and drift from core practices. In 2025 leadership moved to a "government-led, vendor-managed" model with a single vendor per portfolio; some engineers called it a return to how DOD built "monstrosities".
- Lesson: A software factory is itself a system that needs stable staffing, career paths, and leadership continuity; without them it regresses toward the model it was built to replace.
- Tier: B (trade press; named officials plus anonymous engineers).

**[4.10] Nicolas Chaillan resigns as Air Force Chief Software Officer**
- URLs: Defense One https://www.defenseone.com/defense-systems/2021/09/air-force-chief-software-officer-to-resign/195157/ (September 2021); Nextgov https://www.nextgov.com/emerging-tech/2021/09/air-forces-first-software-chief-steps-down/185066/ ; Air & Space Forces Magazine https://www.airandspaceforces.com/air-force-software-chief-quit-officials-considering-recommendations/
- Date: resignation announced 2 September 2021, effective about 2 October 2021 | Role: first Air Force CSO, led Platform One (DoD DevSecOps platform)
- Story: In his resignation memo Chaillan wrote that DOD was the largest software organization on the planet with almost no shared repositories and little collaboration across services, that his office still had no billet and no funding, and that he was tired of chasing support.
- Lesson: An enterprise platform effort without budget, authority, and headcount becomes one person's campaign.
- Tier: B (named, first-hand memo reported by multiple outlets).

### Recurring lessons (independent reporters)
- **Nobody owns the whole.** HealthCare.gov OIG [4.3], F-35 ALIS GAO [4.1], ECSS [4.5], Chaillan [4.10]. Four.
- **Front-line warnings ignored; launch driven by schedule.** Phoenix [4.7], HealthCare.gov [4.3], FCS [4.6]. Three.
- **Automating complex or unlawful rules scales the harm.** Robodebt [4.8], Phoenix [4.7], ECSS [4.5]. Three.
- **Feedback first in a rescue: monitoring and one room.** Dickerson [4.4], and echoed in OIG recovery findings [4.3]. Two.
- **Software factories regress without stable staffing and leadership.** Kessel Run [4.9], Chaillan [4.10]. Two.

### Gaps
- GAO-20-316 PDF could not be parsed; findings are from the GAO product page summary. Later GAO reports on ODIN (2023-2025) were not reviewed.
- The UK NAO's own NPfIT reports (2006, 2008, 2011) and the Post Office Horizon inquiry were not pulled in this pass.
- Federal News Network's "10 lessons" summary of the OIG report returned 403.

