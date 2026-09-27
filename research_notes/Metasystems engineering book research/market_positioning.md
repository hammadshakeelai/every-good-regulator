# Market and Positioning for a Book on "Metasystems Engineering"

Research date: 2026-09-17. Data points carry their own dates. "Fetched" means the page was read in this session; "snippet" means only a search-result summary was seen. This is general publishing information, not legal advice. Where rights or contracts matter, the user should check with a publisher or a lawyer.

Note for the report writer: comps with Goodreads counts are cross-referenced from the sibling file `existing_books_gap.md` (sources repeated here so these notes stand alone).

## Q1. Discoverability: is "metasystems engineering" searched, and which adjacent terms grew 2024–2026?

### Takeaway
"Metasystem" gets almost no search-type attention: its English Wikipedia article has held at about 20–25 human views a month for four years. The exact phrase "metasystems engineering" only appears in academic sources (a 1989 book, a few papers). It works as the book's organizing idea but cannot carry discoverability on its own. Nearby terms get 40x to 1,000x more attention. Growing ones: AI agents (large spike in 2025–26), platform engineering (up from near zero in 2023, peak in 2025), and Stafford Beer / the Viable System Model (steady rise). Falling ones: academic systems-of-systems and systems-engineering terms.

### Cited Findings
**Wikipedia pageviews as a proxy for interest.** English Wikipedia, human (`user`) views, monthly average per year, Jan 2023–Aug 2026. Pulled 2026-09-17 from the Wikimedia REST pageviews API:

| Article | 2023 | 2024 | 2025 | 2026 (Jan–Aug) | Source |
|---|---|---|---|---|---|
| Metasystem | ~23 | ~21 | ~20 | ~22 (Aug 2026 = 25) | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Metasystem/monthly/2023010100/2026083100) |
| Metasystem transition (Turchin) | ~307 | ~264 | ~267 | ~242 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Metasystem_transition/monthly/2023010100/2026083100) |
| Systems thinking | ~11,494 | ~13,403 | ~11,022 | ~10,373 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Systems_thinking/monthly/2023010100/2026083100) |
| Systems engineering | ~23,118 | ~22,539 | ~13,879 | ~11,628 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Systems_engineering/monthly/2023010100/2026083100) |
| Systems theory | ~21,445 | ~19,790 | ~14,106 | ~12,301 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Systems_theory/monthly/2023010100/2026083100) |
| Cybernetics | ~24,349 | ~24,082 | ~20,853 | ~21,861 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Cybernetics/monthly/2023010100/2026083100) |
| Viable system model (Beer) | ~2,290 | ~2,530 | ~2,661 | ~3,039 (+33% vs 2023) | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Viable_system_model/monthly/2023010100/2026083100) |
| Stafford Beer | ~3,097 | ~5,062 | ~4,571 | ~5,899 (+90% vs 2023) | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Stafford_Beer/monthly/2023010100/2026083100) |
| Management cybernetics | ~1,245 | ~1,423 | ~1,319 | ~1,328 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Management_cybernetics/monthly/2023010100/2026083100) |
| System of systems | ~2,180 | ~2,123 | ~1,682 | ~1,136 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/System_of_systems/monthly/2023010100/2026083100) |
| System of systems engineering | ~447 | ~499 | ~369 | ~201 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/System_of_systems_engineering/monthly/2023010100/2026083100) |
| Platform engineering | ~49 | ~568 | ~1,337 | ~988 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Platform_engineering/monthly/2023010100/2026083100) |
| Software factory | ~1,003 | ~921 | ~538 | ~837 (Aug 2026 = 1,345) | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Software_factory/monthly/2023010100/2026083100) |
| Vibe coding | — | — | ~137,580 (10 mo) | ~63,075 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Vibe_coding/monthly/2023010100/2026083100) |
| AI agent | — | ~46 | ~1,260 | ~21,359 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/AI_agent/monthly/2023010100/2026083100) |
| Intelligent agent | ~7,863 | ~10,605 | ~13,198 | ~7,070 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Intelligent_agent/monthly/2023010100/2026083100) |
| Agentic AI | — | — | ~20,924 | ~3,279 | [API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Agentic_AI/monthly/2023010100/2026083100) |

- **Caveat on the table.** Several series are distorted by article creation, renames and redirects. "Platform engineering" at ~49/month in 2023 and "AI agent" with no data before Dec 2023 suggest the articles were new or were redirects then. The 2026 fall in "Intelligent agent" and "Agentic AI" alongside the rise in "AI agent" looks like traffic moving between articles. So the growth multiples overstate real interest growth; read them as direction, not size (researcher's reading of the API output). The "Metasystem" row is the cleanest series in the table: a long-standing article with no creation event or redirect shift in the window, flat at ~20–25/month for 44 months. The "no discoverability" verdict therefore holds even though the growth multiples for platform engineering and AI agents are soft.
- **Stafford Beer's dates:** born 25 September 1926, died 23 August 2002 (English Wikipedia infobox, read via the MediaWiki API on 2026-09-17; article last edited 2026-08-18). — [Wikipedia: Stafford Beer](https://en.wikipedia.org/wiki/Stafford_Beer)
- **The exact phrase "metasystems engineering"** turned up only academic and technical sources in a web search (2026-09-17):
  - Arthur D. Hall's *Metasystems Methodology* (Pergamon, 1989) ([Amazon](https://www.amazon.com/Metasystems-Methodology-Unification-International-Engineering/dp/0080369561))
  - Kent Palmer's "Meta-systems Engineering" papers ([academia.edu](https://www.academia.edu/3796373/Meta-systems_Engineering))
  - Katina and Keating et al., "The Role of 'Metasystem' in Engineering a System of Systems" ([ODU Digital Commons](https://digitalcommons.odu.edu/emse_fac_pubs/192/))
  - Grimshaw's "Metasystems", CACM 1998 ([ACM DL](https://dl.acm.org/doi/10.1145/287831.287839))
  - No trade or popular book appeared.
- Hall's 1989 book has 2 Goodreads ratings and 0 reviews (fetched 2026-09-17 by the sibling researcher) — [Goodreads](https://www.goodreads.com/book/show/3534708-metasystems-methodology)
- **Platform engineering community size.** PlatformCon 2025 (online, plus live days in London and NYC, June 23–27, 2025) drew 40,000+ registrants and 150+ talks. — [platformengineering.com report (2025)](https://platformengineering.com/features/platformcon-2025-live-day-nyc-a-front-row-report/); [PlatformCon 2025 site](https://2025.platformcon.com/)
- **Low-reliability adoption stats** (secondary blog citing Gartner and others; not verified): 55% of organizations adopted platform engineering in 2025, and Gartner forecasts 80% by 2026. — [DEV Community post (2026)](https://dev.to/meena_nukala/platform-engineering-in-2026-the-numbers-behind-the-boom-and-why-its-transforming-devops-381l)
- **New direct competitors.** Two August 2026 books overlap with the "systems that build systems" lane (compiled by the sibling researcher):
  - Addy Osmani, *Agentic Engineering* (O'Reilly, scheduled Aug 2026). It spans "from individual workflow to the software factory" and discusses an "orchestration tax". — [O'Reilly listing (snippet; page returned 403)](https://www.oreilly.com/library/view/agentic-engineering/0642572392291/)
  - Kaspar von Grünberg & Luca Galante, *Thinking in Platforms: Platform engineering as the operating model for work in the AI era* (Weave Intelligence, 18 Aug 2026). It extends platform engineering to all knowledge work and to managing AI-generated work (compiled by the sibling researcher). — [Launch post, 2026-07-06](https://kasparvongruenberg.substack.com/p/my-new-book-thinking-in-platforms); [Amazon](https://www.amazon.com/Thinking-Platforms-Platform-engineering-operating/dp/3982887720)
- *Wiring the Winning Organization* (Gene Kim & Steven J. Spear, IT Revolution, 2023), a leadership/organization comp. It won the Shingo Publication Award; reviewers call it repetitive (sibling notes). — [IT Revolution](https://itrevolution.com/product/wiring-the-winning-organization/); [SoBrief (aggregator)](https://sobrief.com/books/wiring-the-winning-organization)
- **"Agentic engineering" as a term.** Andrej Karpathy reportedly promoted it in 2026 as the professional successor to "vibe coding". Secondary, not re-verified. — [Karpathy Sequoia Ascent 2026 notes](https://karpathy.bearblog.dev/sequoia-ascent-2026/)

### Inferences
- **"Metasystems engineering" as a title word:** distinctive and free to own, but no discoverability. At ~20 Wikipedia views a month, the term has roughly 1/500th the attention of "systems thinking" and 1/1,000th of "cybernetics". A title that relies on it alone would depend entirely on the author's own platform to be found.
- **Recommended title rule:** use the coinage as the brand ("Metasystems Engineering" or "The Metasystem") and put searchable terms in the subtitle and keywords: *AI agents*, *platform engineering*, *systems thinking*, *operating system*, *cybernetics*.
- **Lane (a) splits in two.** Popular interest in management cybernetics (Beer, VSM) has been rising since 2023, while academic "system of systems engineering" roughly halved. The cybernetics-revival framing has a tailwind; the INCOSE/defense systems-of-systems framing does not (at least on this proxy).
- **Lane (b)** has the steepest interest curve (AI agents, vibe coding, platform engineering) but also decays fastest. "Vibe coding" views fell by more than half from 2025 to 2026, and "Agentic AI" traffic moved elsewhere. Terms churn every 12–18 months, so a book should not stake its title on the current buzzword.
- **Broader traffic decline.** Many established articles (Systems engineering −50%, Systems theory −43% from 2023 to 2026) fell sharply. This may partly reflect a site-wide drop in Wikipedia human traffic as people shift to AI answers, which was not verified here (see Gaps). Compare terms against each other rather than reading absolute declines as falling interest in the field.
- **Why now: the Beer centenary.** Stafford Beer's centenary falls on 25 Sep 2026 (sourced below), eight days after this research date. Together with rising Beer/VSM pageviews, it gives lane (a)/(c) a datable reason to publish now. The centenary itself will pass before any book ships, so it works better as a proposal hook ("the cybernetics revival around Beer's centenary") than as a launch date.

### Gaps
- Google Trends numbers could not be pulled directly: the site renders in JavaScript, and installing `pytrends` would have required a package download without user approval. Wikipedia pageviews were used as a proxy. A manual Google Trends check (topics: "platform engineering", "systems thinking", "AI agent", "metasystem"; 2021–2026; worldwide) would strengthen Q1.
- No direct Amazon search-volume or keyword-tool data (Publisher Rocket, Helium 10) was gathered for "metasystems engineering" or the adjacent terms.
- Subreddit sizes (r/systemsthinking, r/platform_engineering, r/EOS, r/ExperiencedDevs), newsletter and YouTube audience sizes, and INCOSE conference attendance were not retrieved; Reddit domains were blocked for fetch in this session.
- No verified figure was found for the site-wide decline in Wikipedia human pageviews in 2025–2026, so the adjustment for that decline is unquantified.
- Wikipedia article creation dates (to cleanly separate new articles from growth in interest) were not retrieved; the API call was rate-limited.

## Q2. Comparable books by lane and their sales/following signals

### Takeaway
Self-published and indie engineering-leadership books by authors who already had an audience sold 40,000–100,000 copies. The breakout titles (*Accelerate*, *The Manager's Path*) reached about 300,000–500,000. Business "operating system" books built around an implementer network are the largest market: Wickman reports 3 million+ copies across his books. Systems-thinking classics have the largest reader followings (tens of thousands of Goodreads ratings). AI-engineering titles are now the most-read books on O'Reilly's platform, but the lane is crowding fast. No existing book combines all three meanings of "metasystem".

### Cited Findings
**Engineering leadership / builder lane (b):**
- **Gergely Orosz, *The Software Engineer's Guidebook*** (self-published Nov 2023). Figures from his recap post dated 2025-11-11:
  - About 40,000 copies (38,373 print and ebook) and $611,911 in royalties over two years.
  - Amazon KDP print: 29,806 copies for about $470k (~$16 per book).
  - DRM-free ebooks: 2,713 sales for $54,963.
  - Translations: 5 languages, $17k upfront.
  - About 4 years of writing.
  - Source: [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-software-engineers-guidebook) (fetched)
- **Will Larson.** Figures from a post dated 2024-02-24:
  - *An Elegant Puzzle* (Stripe Press, 2019): ~100,000 copies.
  - *Staff Engineer* (self-published 2021): ~70,000 copies.
  - He calls these very good but not breakout, compared with *Accelerate* and *The Manager's Path* at ~300–500k.
  - Source: [lethain.com, "More (self-)publishing thoughts"](https://lethain.com/more-publshing-thoughts/) (fetched)
- **Goodreads snippets** (compiled 2026-09-17 by the sibling researcher):
  - *An Elegant Puzzle*: 4.07 / ~3,941 ratings ([Goodreads](https://www.goodreads.com/en/book/show/45303387-an-elegant-puzzle))
  - *Staff Engineer*: 4.04 / ~3,046 ([Goodreads](https://www.goodreads.com/book/show/56481725-staff-engineer))
  - *Accelerate*: 4.05 / 8,172 ([Goodreads](https://www.goodreads.com/author/show/17037914.Nicole_Forsgren))
  - *Team Topologies*: ~4.18 / ~5,500 ([Goodreads](https://www.goodreads.com/book/show/51338386-team-topologies))
- ***Team Topologies* 2nd edition** (IT Revolution, 23 Sep 2025): added a case-study appendix (ING NL, KFC UK&I, Creditas, Yassir) and made cognitive load a core design principle. — [IT Revolution](https://itrevolution.com/articles/team-topologies-2nd-edition-real-world-lessons-from-the-global-business-community/)
- ***Platform Engineering*** (Fournier & Nowland, O'Reilly, Nov 2024): Goodreads 4.01 / 140 ratings (fetched 2026-09-17). Some experienced readers call it common sense or superficial. — [Goodreads](https://www.goodreads.com/en/book/show/217312157-platform-engineering)

**AI / agentic engineering (b, 2025–2026):**
- Chip Huyen's *AI Engineering* (O'Reilly, 2025) is described on the author's site as the most-read book on O'Reilly since its release, with translations into 6 languages under way. — [huyenchip.com/books](https://huyenchip.com/books/) (fetched 2026-09-17; self-reported)
- ***Vibe Coding*** (Gene Kim & Steve Yegge, IT Revolution, 2025; foreword by Dario Amodei):
  - Awards: Gold, 2026 Axiom Business Book Awards (Business Technology); Silver, 2026 IBPA Benjamin Franklin Awards (snippet). — [IT Revolution product page](https://itrevolution.com/product/vibe-coding-book/)
  - Goodreads 3.71, with reviews calling it repetitive or padded (sibling notes). — [Goodreads](https://www.goodreads.com/book/show/228438060-vibe-coding)
- Other O'Reilly 2026 agent titles: *AI Agents: The Definitive Guide* (Koenigstein) and *The Agentic Enterprise* (strategy for senior technology leaders). — [O'Reilly](https://www.oreilly.com/library/view/ai-agents-the/0642572247775/); [O'Reilly](https://www.oreilly.com/library/view/the-agentic-enterprise/0642572274566/)

**Operating-system-for-organizations / individuals lane (c):**
- Gino Wickman's site claims over 3 million copies sold across his books. The Traction Library includes:
  - *Traction*
  - *Get A Grip* (fable format)
  - *Rocket Fuel*
  - *What the Heck is EOS?* (for employees)
  - *How to Be a Great Boss*
  - *The EOS Life* (personal-life extension)
  - Source: [ginowickman.com/books](https://www.ginowickman.com/books) (fetched 2026-09-17)
- A 2022 press release marked *Traction*'s 15th anniversary and "more than a million lives changed". — [PR Newswire](https://www.prnewswire.com/news-releases/gino-wickmans-bestseller-traction-celebrates-15-years---and-more-than-a-million-lives-changed-301509276.html)
- *Building a Second Brain* (Forte, 2022), a personal-OS comp: Goodreads 4.03 / 21,649 ratings (snippet). Some reviewers say it reads like a blog post turned into a book. — [Goodreads](https://www.goodreads.com/book/show/59616977-building-a-second-brain)

**Systems thinking / cybernetics lane (a):**
- *Thinking in Systems* (Meadows): Goodreads 4.17 / ~24,700 ratings (snippet). — [Goodreads](https://www.goodreads.com/book/show/3828902-thinking-in-systems)
- *The Fifth Discipline* (Senge): Goodreads 3.93 / ~35,900 ratings; more than 1M copies in print (snippet). — [Goodreads](https://www.goodreads.com/book/show/255127.The_Fifth_Discipline)
- *Brain of the Firm* (Beer): ~4.28 / ~137 ratings across editions. — [Goodreads editions](https://www.goodreads.com/work/editions/1293720-brain-of-the-firm-classic-beer-series)
- *The Unaccountability Machine* (Dan Davies, Profile Books / University of Chicago Press, Apr 2024) revives Beer's management cybernetics for general readers:
  - Goodreads 3.74 / 1,460 ratings (fetched by the sibling researcher).
  - Reviewers praise the diagnosis but call the prescriptions weak or abstract.
  - Source: [Goodreads](https://www.goodreads.com/book/show/197716282-the-unaccountability-machine)
- *Learning Systems Thinking* (Montalion, O'Reilly 2024), systems thinking aimed at software professionals: Goodreads 3.37 / 100 ratings (snippet). This is the lowest in the sibling set. — [Goodreads](https://www.goodreads.com/book/show/205977642-learning-systems-thinking)

**Crowdsourced or interview formats:**
- *Tribe of Mentors* (Ferriss): Kindle edition ~4.05 / 15,383 ratings; criticized as shallow. — [Goodreads editions](https://www.goodreads.com/work/editions/57830167-tribe-of-mentors)
- *Coders at Work*: 3.95 / 5,381. — [Goodreads](https://www.goodreads.com/book/show/6713575-coders-at-work)
- *97 Things Every Software Architect Should Know*: 3.62 / 788. — [Goodreads](https://www.goodreads.com/book/show/5487765-97-things-every-software-architect-should-know)

### Inferences
- **Lanes compared:**
  - **Lane (b), engineering leadership / AI builders:** a realistic ceiling of about 40–100k copies for a well-executed book by an author with a platform, and the most measurable demand right now. Two August 2026 competitors (Osmani, *Thinking in Platforms*) mean the book must differentiate on *governance of the builders* (cybernetics, control, viability) rather than on agent techniques.
  - **Lane (c), organizational operating systems:** the largest proven market (millions of copies), but it is driven by implementer networks and consulting businesses. A book competes there by offering a named, teachable system, not a synthesis.
  - **Lane (a), systems thinking / cybernetics:** a large, durable readership, but recent entries targeting software people (Montalion 3.37) or general readers (Davies 3.74) rated poorly when they were abstract or light on prescription. Execution risk is high.
- **Weaker execution scores lower.** Books built as collections or stitched from blogs get "disjointed" or "shallow" complaints (*An Elegant Puzzle*, *Tribe of Mentors*, *Building a Second Brain*, *97 Things*). A book blending three meanings from many online stories carries that exact risk; a strong single framework is the mitigation.

### Gaps
- No verified unit sales were found for *Thinking in Systems*, *Team Topologies*, *Vibe Coding*, *AI Engineering*, *Platform Engineering* or *Traction* specifically. Wickman's figure is an aggregate claim across his books. Circana BookScan and bestseller-list positions were not accessed.
- EOS adoption numbers (200,000+ companies, 700+ implementers) appeared only in an unattributed search snippet and were not verified on an EOS Worldwide primary page.
- Amazon category bestseller rankings (e.g., "Systems Analysis & Design", "Software Development") were not captured.
- Tanya Reilly (*The Staff Engineer's Path*) and Camille Fournier (*The Manager's Path*) sales posts were not retrieved. Only Larson's secondhand ~300–500k range for *The Manager's Path* is cited.

## Q3. What tech/systems publishers ask for in proposals (2024–2026)

### Takeaway
Tech and trade publishers consistently ask for five things:
1. A specific reader and problem, with "why now" urgency.
2. A chapter-by-chapter outline.
3. Sample chapters.
4. Recent comps (IT Revolution asks for five from the last 3 years; Jane Friedman advises 5–10).
5. Hard author-platform numbers.

IT Revolution, the most on-brand publisher for this topic, is not accepting unsolicited proposals. Pragmatic, Manning, Apress and O'Reilly accept direct pitches. Routledge/CRC suits a practitioner or academic version.

### Cited Findings
- **IT Revolution** (fetched 2026-09-17). Not accepting unsolicited proposals at the time of fetch. Its focus is software delivery, organizational architecture, leadership and ways of working. The proposal asks for:
  - Title, subtitle, hook, one-paragraph description, page count, and schedule.
  - Answers to five questions: what problem the book solves, what solution it offers, the urgency, the audience, and why readers should trust the author.
  - A table of contents with 2–3 sentence chapter summaries.
  - Two sample chapters, including the introduction or preface.
  - A marketing plan with platform numbers (email subscribers, social media, contributors and promoters).
  - A competitive analysis of five titles from the last 3 years.
  - A 3–5 paragraph bio and publishing history with sales.
  - Source: [IT Revolution submission guidelines](https://itrevolution.com/submission-guidelines/)
- **Pragmatic Bookshelf** (fetched 2026-09-17):
  - Pitch to proposals@pragprog.com, attaching its proposal template.
  - Royalties start at 42% for first-time authors and rise on later titles.
  - Pioneered "beta books" (early-access ebooks).
  - Also distributes self-published technical books.
  - Categories include AI/ML and "Management and Teams".
  - Source: [pragprog.com/publish-with-us](https://pragprog.com/publish-with-us/)
- **Manning** (fetched 2026-09-17):
  - Proposals should explain why the topic matters now, how it differs from the competition, what the reader gains, and why the author is the right person.
  - Prior experience "not required".
  - Catalog includes AI Agents; the MEAP early-access program exists (terms not shown).
  - Source: [manning.com/write-for-us](https://www.manning.com/write-for-us)
  - An author's account describes a ~6-page template (author, subject, summary, typical questions, target reader, competition, size) and Manning's preference for practical over theoretical books. — [Tune The Web](https://www.tunetheweb.com/blog/writing-a-technical-book-for-manning/)
- **O'Reilly** (fetched 2026-09-17):
  - The public page points to workwithus@oreilly.com and a linked Google Doc proposal guide.
  - Formats: books, online and live courses, interactive scenarios.
  - Source: [oreilly.com/work-with-us](https://www.oreilly.com/work-with-us.html)
  - An O'Reilly author's account lists marketing description, audience size, competing books, detailed outline and schedule. — [Sheen Brisals, Medium](https://sbrisals.medium.com/the-making-of-the-serverless-book-part-1-0444aa8dde42)
- **Apress** (Springer Nature; snippet): submit via a proposal form with supporting material (CV, sample chapter). Wants authors with technical expertise who can explain complex topics clearly. — [Apress submit a proposal](https://www.apress.com/us/write-for-us/submit-a-proposal)
- **Routledge / CRC Press** (Taylor & Francis; fetched 2026-09-17):
  - Stresses a unique selling point, market demand and author expertise.
  - Publishes textbooks, research monographs, and books that help practitioners do their job better; covers engineering.
  - Authors contact the subject commissioning editor; detailed requirements are in a PDF.
  - Source: [T&F Author Services](https://authorservices.taylorandfrancis.com/publish-your-book/submit-your-book-proposal/)
- **Jane Friedman's proposal guide** (updated 2026-02-23, fetched):
  - Overview written last.
  - Target audience defined as the readers "easiest to convince", backed by concrete evidence.
  - 5–10 comps from reputable publishers that are still selling.
  - Chapter summaries under 3,000 words, plus sample chapters.
  - A marketing plan of concrete current activities.
  - For prescriptive business and self-help nonfiction, platform is critical, typically visibility to tens of thousands of people with verifiable influence.
  - A finished manuscript does not remove the need for a proposal.
  - Source: [janefriedman.com](https://janefriedman.com/start-here-how-to-write-a-book-proposal/)
- **Publisher trade-offs** (Larson, 2024-02-24): Stripe Press priced ~$20 hardcover to maximize distribution; O'Reilly ~$40 paperback. He earns roughly 2x per copy on self-published *Staff Engineer* versus his O'Reilly book. Publishers help first-time authors with the learning curve, print quality and international rights. — [lethain.com](https://lethain.com/more-publshing-thoughts/)
- **Orosz and Manning:** he left a Manning deal after ~3 months, citing a restrictive template, loss of title control, and limits on sharing drafts online (2025-11-11). — [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-software-engineers-guidebook)

### Inferences
- An "anyone" audience would fail every one of these proposal templates, since each asks for a specific reader and a specific problem. Picking one of the Q6 options is a precondition for any traditional route.
- **Publisher fit by option:**
  - **Engineering or AI framing:** Pragmatic, Manning, O'Reilly or Apress.
  - **Organizational or leadership framing:** IT Revolution (its page said it was not accepting unsolicited proposals "at this time" as of 2026-09-17; recheck before pitching, or approach through its community or events) or a business or trade press.
  - **Rigorous systems-engineering or cybernetics framing:** Routledge/CRC or Wiley (see Gaps).
- **Two constraints if the book is built in public:** Manning's template rigidity and limits on sharing drafts online (per Orosz) matter for a build-in-public plan. Pragmatic's beta books and Manning's MEAP are the most compatible with iterating in public.

### Gaps
- O'Reilly's Google Doc proposal guide, Pragmatic's template sections, Manning's MEAP terms and royalty rates, and the Routledge proposal PDF were not opened.
- Stripe Press submission policy was not found; the search returned no policy page. Stripe Press appears to commission rather than take open submissions, but this is unverified.
- Wiley (including INCOSE-affiliated titles) proposal guidelines were not researched. Given falling interest in systems-of-systems terms, this academic route was deprioritized.
- No 2025–2026 statement was found from any tech publisher about AI-generated or AI-assisted manuscripts. The user should ask directly, since it may affect a book assembled with AI help.

## Q4. Self-publishing and build-in-public routes (Leanpub, Gumroad, Substack, newsletters, crowdsourced interview books)

### Takeaway
The best-documented engineering self-publishing successes (Orosz ~$612k over 2 years; Larson ~70k copies) both came from authors who built an audience first. Larson did it by publishing ~20 practitioner interviews on staffeng.com for months before launch, which is the closest existing model for a book "built from many people's experiences". Self-publishing roughly doubles per-copy income but moves all production, rights and distribution work onto the author. Leanpub (80% royalty, sells in-progress books) and Gumroad fit the build-in-public phase; Amazon KDP carries volume at launch.

### Cited Findings
- **Larson, *Staff Engineer*.** Figures from his post dated 2021-02-17 (fetched):
  - Published staffeng.com stories starting June 2020 and reached ~20 interviews before the Feb 2021 launch. The stories grounded the book in real experiences and built the email list.
  - Upfront budget: $1,760 without audiobook, ~$4,760 with it.
  - Priced $25 for paperback and digital.
  - 3,324 copies by 2021-02-15, about 10–15 days after launch (Gumroad 1,618; KDP paperback 944; Kindle 762).
  - Interviewees were featured with bylines on staffeng.com; compensation is not described.
  - Source: [lethain.com, "Self-publishing Staff Engineer"](https://lethain.com/self-publishing-staff-engineer/)
- **Orosz, *The Software Engineer's Guidebook*** (post dated 2025-11-11, fetched):
  - Channels: KDP, IngramSpark, Gumroad (DRM-free, ~$20 net per ebook), Kobo, Google Play, PublishDrive.
  - Tools: Vellum, Overleaf with a hired LaTeX expert, Betabooks for reader feedback, Canva for the cover.
  - Economics: Amazon takes about 40% of print revenue; print-on-demand costs ~$8 per copy on Amazon versus ~$16 on IngramSpark.
  - An email list and work-in-progress chapters shared on social media drove launch sales.
  - The newsletter he started in Aug 2021 to support the book delayed it by about two years.
  - He removed product names such as "Google Bard" so the book would not date.
  - Source: [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-software-engineers-guidebook)
- **Leanpub** (snippet, help center):
  - 80% royalty on purchases of $7.99 or more (80% minus $0.50 between $0.99 and $7.98), including in-progress books.
  - Readers get free updates.
  - Authors may also sell elsewhere.
  - Source: [Leanpub Help Center: royalty rate](https://help.leanpub.com/en/articles/5468013-what-is-leanpub-s-royalty-rate-are-there-any-restrictions-on-where-i-can-self-publish-my-book-and-what-price-i-can-charge); [What is Leanpub?](https://help.leanpub.com/en/articles/110765-what-is-leanpub)
- **Pragmatic Bookshelf** distributes self-published technical books, which offers a hybrid path. — [pragprog.com/publish-with-us](https://pragprog.com/publish-with-us/)
- **Larson's warning** (2024-02-24): self-publishing is risky if no publisher would take the book. Self-publishing makes sense when you already have distribution and want control over timing and pricing. — [lethain.com](https://lethain.com/more-publshing-thoughts/)
- **Community-to-book precedent:** the *97 Things* series was crowdsourced on an open O'Reilly wiki under CC BY 3.0 and then published by O'Reilly. — [GitHub 97-things](https://github.com/97-things/97-things-every-programmer-should-know); [InfoQ 2008](https://www.infoq.com/news/2008/08/97things)

### Inferences
- **Recommended sequence for this user:**
  1. A public site or newsletter publishing curated practitioner "metasystem stories", staffeng.com style, with explicit permissions.
  2. Leanpub or Gumroad in-progress sales to test willingness to pay.
  3. A KDP or IngramSpark launch, or a pitch to a publisher using the audience numbers as proof of platform.

  This one path serves both routes, because the IT Revolution and Friedman templates both ask for subscriber and platform numbers.
- **Decisive variable:** the user's existing audience size is unknown. With under a few thousand engaged subscribers, a publisher (or a hybrid such as Pragmatic, or Manning MEAP) likely beats self-publishing on reach. With tens of thousands, the Orosz and Larson economics apply.
- **Cost of the newsletter route:** a newsletter can swallow the book (Orosz lost ~2 years). Build the site around book chapters, not a general publication.

### Gaps
- No verified public revenue or reader figures were found for Substack-serialized nonfiction books or for Leanpub bestsellers; this was not searched in depth.
- Gergely Orosz's newsletter subscriber count at launch was not captured from the fetched recap.
- Current Gumroad fee terms were not fetched.

## Q5. Building a book from many people's online experiences: ethics, permissions, fair use, contributor agreements

### Takeaway
Posts on Reddit, forums, LinkedIn and blogs remain their authors' copyrighted work; being public does not make them free to reprint. Short quotations used for commentary or to support an argument can qualify as fair use, but a book that mostly consists of other people's words cannot count on that defense. Platform terms (e.g., Reddit's) add their own restrictions. The safest pattern, used by Larson and *97 Things*: get consent from the people whose stories carry the book (interview releases or contributor agreements with an explicit license and attribution), paraphrase and synthesize the rest, and keep direct quotes short. Rights, platform terms, defamation and privacy questions should be checked with a publisher or a lawyer.

### Cited Findings
- **Authors Alliance guide** (2017, CC-licensed): nonfiction fair use commonly covers three scenarios — criticizing or commenting on material, using material to support a point, and non-consumptive research. — [Authors Alliance announcement](https://www.authorsalliance.org/2017/11/29/announcing-the-authors-alliance-guide-to-fair-use-for-nonfiction-authors/); [guide PDF](https://www.authorsalliance.org/wp-content/uploads/2017/11/AuthorsAllianceFairUseNonfictionAuthors.pdf)
- **Author-facing guidance on quoting** (snippets; exact page attribution within this set not verified):
  - No fixed word count makes a quote safe.
  - One former publisher's rule of thumb was 200–300 words from a book-length work.
  - A work that depends entirely on quotes from others is not OK.
  - Heavy quoting that substitutes for the original weighs against fair use.
  - Sources: [Vervante blog](https://vervante.com/blog/2019/02/fairuseguide); [Geoff Affleck](https://geoffaffleck.com/permission-to-use-quotes/); [Writer's Guide to Permissions and Fair Use (Goodreads blog mirror)](https://www.goodreads.com/author_blog_posts/15316125-a-writer-s-guide-to-permissions-and-fair-use?tab=author)
- **Reddit terms** (secondary summary; date not confirmed):
  - Users keep ownership of their posts but grant Reddit a perpetual, worldwide, royalty-free license.
  - Others may not commercially reproduce Reddit content except as fair use or with Reddit's written authorization.
  - Source: [The Mary Sue](https://www.themarysue.com/reddit-user-agreement-update/). The primary [Reddit User Agreement](https://redditinc.com/policies/user-agreement) could not be fetched (domain blocked for this tool).
- **Interview releases** (snippets):
  - Typically grant the author the right to quote or paraphrase all or part of an interview, worldwide, in all languages and editions including electronic, often in perpetuity.
  - Releases reduce misquotation, defamation and privacy-claim risk; interviewing without a release leaves the writer exposed.
  - Sources: [University of Illinois Press interview release form](https://www.press.uillinois.edu/authors/forms/Interview%20Release%20Form.doc); [Copylaw (Lloyd Jassin), "Do I Need an Interview Release?"](https://www.copylaw.org/2010/09/ask-lawyer-do-i-need-interview-release.html); [Sidebar Saturdays](https://www.sidebarsaturdays.com/2020/01/04/interview-release/)
- ***97 Things*** contributions were gathered on a public wiki with each piece under CC BY 3.0, with attribution to named contributors (more than four dozen architects for the architect edition). — [GitHub 97-things](https://github.com/97-things/97-things-every-programmer-should-know); [InfoQ 2008](https://www.infoq.com/news/2008/08/97things)
- **Larson's *Staff Engineer*** used first-party interviews, published with bylines on staffeng.com before being collected into the book (2021-02-17). — [lethain.com](https://lethain.com/self-publishing-staff-engineer/)
- **Scraping litigation:** Reddit has sued AI companies over content use (e.g., Reddit v. Anthropic). Platforms are actively enforcing their content terms, which matters if posts are collected at scale. — [RightsTech Substack](https://rightstech.substack.com/p/reddit-v-anthropic-is-one-to-watch)

### Inferences
Researcher's best-practice synthesis; not legal advice.
1. **Tier the sources.**
   - **Tier 1, spine stories:** first-party interviews or submitted essays under a written release or contributor agreement. Specify the rights granted (all editions, formats, languages, translations, excerpts for marketing), attribution or anonymity choice, a right to review quotes for accuracy (not veto), and any compensation (free copy, donation, revenue share).
   - **Tier 2, public posts:** short quotes (a sentence or two) with attribution and a link, used for commentary. Ask for permission when a quote is long, emotionally revealing, or central to a chapter.
   - **Tier 3, patterns:** paraphrase and aggregate ("dozens of practitioners on r/ExperiencedDevs describe…") without reproducing text.
2. **Contact authors** of posts you rely on. Many are reachable, and asking also recruits future readers and promoters (Larson's pattern).
3. **Watch identity and harm.** Forum posts often describe employers, colleagues or incidents. Anonymize or composite when naming could expose someone, and label composites as composites.
4. **Keep a permissions log** (source URL, date captured, quote, permission status, license, attribution wording). Traditional publishers typically require the author to clear permissions and warrant non-infringement.
5. **Open-license option.** A CC BY contribution model (*97 Things*) makes rights simple, but a traditional publisher may not accept content already under an open license. Settle this before collecting contributions.
6. **AI-assisted collection:** do not bulk-scrape platforms to gather stories. Platform terms and current litigation make that risky.

### Gaps
- The US Copyright Office fair use pages and Authors Guild guidance were not fetched this session. The user should read the [US Copyright Office Fair Use Index](https://www.copyright.gov/fair-use/) and Authors Guild member resources.
- Current primary text of Reddit's User Agreement, and the terms of LinkedIn, Hacker News, X and Medium, were not verified.
- No sample contributor agreement from a tech publisher (O'Reilly *97 Things*, Manning, Pragmatic) was retrieved.
- Non-US law (EU/UK copyright exceptions, GDPR for named individuals, moral rights) was not researched; it is relevant if contributors or the author are outside the US.

## Q6. Positioning options (reader, problem, promise, titles, format, route, comps, why now, risks)

### Takeaway
Ranked recommendation:
- **Option A (lead): "Builders of builders".** Governing AI agents, platforms and teams as one metasystem, for senior engineers and engineering leaders. It has the strongest measurable "why now" and the most accessible publishers, but it must be differentiated from Osmani's *Agentic Engineering*.
- **Option B: "Your organization's operating system".** Cybernetics for the AI-augmented company, for founders, operators and managers. It has the largest proven market, but it depends heavily on platform and competes with established systems like EOS.
- **Option C: "The metasystem idea for everyone".** A narrative, idea-driven book riding the Beer/cybernetics revival. It has the broadest audience but the highest execution and platform risk for a first book.

The "anyone" audience should be dropped: every proposal template requires a specific reader. The route choice depends on the user's current audience size.

### Cited Findings
Evidence each option rests on (all sourced above):
- **Interest signals:**
  - AI agent, vibe coding and platform engineering interest rose sharply in 2024–2026 ([Wikimedia API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/AI_agent/monthly/2023010100/2026083100)).
  - PlatformCon 2025 had 40k+ registrants ([platformengineering.com](https://platformengineering.com/features/platformcon-2025-live-day-nyc-a-front-row-report/)).
  - *AI Engineering* is O'Reilly's most-read book since release ([huyenchip.com](https://huyenchip.com/books/)).
- **Crowded agent lane:** Osmani's *Agentic Engineering* (O'Reilly, Aug 2026) discusses an orchestration tax and runs from individual workflow to the software factory ([O'Reilly listing, snippet](https://www.oreilly.com/library/view/agentic-engineering/0642572392291/)).
- **Engineering-leadership sales ceiling:** 40k–100k copies for platform-backed authors (the authors' own figures). Breakout titles such as *Accelerate* and *The Manager's Path* are at roughly 300–500k, but that range is Larson's secondhand estimate, not publisher data ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-software-engineers-guidebook); [lethain.com](https://lethain.com/more-publshing-thoughts/)).
- **Operating-system books:** 3M+ copies across Wickman's books, including a personal-life extension, *The EOS Life* ([ginowickman.com](https://www.ginowickman.com/books)).
- **Cybernetics revival:** Beer and VSM interest rising (+90% and +33% since 2023) ([Wikimedia API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Stafford_Beer/monthly/2023010100/2026083100)). *The Unaccountability Machine* brought Beer to general readers but was criticized for weak prescriptions ([Goodreads](https://www.goodreads.com/book/show/197716282-the-unaccountability-machine)).
- **Execution risk:** *Learning Systems Thinking* rates 3.37 ([Goodreads](https://www.goodreads.com/book/show/205977642-learning-systems-thinking)); *Vibe Coding* 3.71 and called padded ([Goodreads](https://www.goodreads.com/book/show/228438060-vibe-coding)).
- **Platform requirement for prescriptive nonfiction:** tens of thousands of people reached, with verifiable influence ([Jane Friedman, 2026-02-23](https://janefriedman.com/start-here-how-to-write-a-book-proposal/)).
- **Interview-driven model that worked:** staffeng.com to *Staff Engineer*, ~70k copies ([lethain.com](https://lethain.com/self-publishing-staff-engineer/); [lethain.com](https://lethain.com/more-publshing-thoughts/)).

### Inferences
Researcher-constructed options. Titles and promises are proposals, not sourced facts.

**Option A (recommended lead): "Builders of Builders", metasystems engineering for the age of AI agents and platforms**
- **Reader:** senior, staff+ and platform engineers, tech leads and engineering managers (roughly 5–20 years' experience). Their job has shifted from writing code to designing the systems (agents, internal platforms, pipelines, teams) that produce code.
- **Problem:** AI agents and platforms multiply output, but coordination, verification, governance and accountability break. Teams fall into orchestration overhead, runaway complexity, and blurred ownership of who is steering the builders. Existing books cover *how to use agents* or *how to build a platform*, not *how to govern the whole system that builds your software*.
- **Promise:** a practical control model (a metasystem drawing on Beer's VSM functions: coordination, control, audit, intelligence, identity) for running a human-plus-agent software factory, told through dozens of practitioner stories of what worked and what failed.
- **Why now:**
  - AI-agent interest spiked in 2025–26.
  - Platform engineering has become mainstream (PlatformCon 40k+).
  - Engineers increasingly act as "builders of builders".
  - The 2026 Beer centenary offers a hook for the cybernetics lens.
- **Working titles** (coinage as brand, searchable subtitle):
  - *Metasystems Engineering: How to Govern the AI Agents, Platforms, and Teams That Build Your Software*
  - *Builders of Builders: Metasystems Engineering for the Age of AI Agents*
  - *The Software Metasystem: Systems Thinking for Engineers Who Build With Agents and Platforms*
- **Format:** practical trade/technical book of 250–320 pages. A framework in each chapter, 3–5 curated practitioner stories, and checklists or diagnostics. Keep tool and product names out of the core text (per Orosz's lesson on dating) and put the tool-specific playbooks online.
- **Route:**
  - *Build in public:* a staffeng-style story site plus newsletter, then in-progress sales on Leanpub or Gumroad.
  - *Then either* self-publish (KDP, IngramSpark, Gumroad) if the audience reaches the several-thousand range, *or* pitch Pragmatic (beta books, 42% royalty), Manning (MEAP) or O'Reilly with those platform numbers.
  - IT Revolution is the best-fit brand, but it was not accepting unsolicited proposals as of 2026-09-17 (the page says "at this time"; recheck later).
- **Comps (3–5):**
  - *Team Topologies* 2e (IT Revolution, 2025)
  - *Platform Engineering* (Fournier & Nowland, O'Reilly, 2024)
  - *Vibe Coding* (Kim & Yegge, IT Revolution, 2025)
  - *Staff Engineer* (Larson, 2021; format comp)
  - Position against *Agentic Engineering* (Osmani, O'Reilly, Aug 2026) and *Thinking in Platforms* (Aug 2026) as competitors rather than sales comps.
- **Risks:**
  - Fastest-moving lane: buzzwords churn (vibe coding interest halved in 2026) and content dates quickly.
  - Direct competition from authors with large platforms (Osmani).
  - "Metasystem" may read as academic jargon to engineers; lead with outcomes.
  - The three-meanings blend could dilute focus. Meaning (c) should be limited to "the team's and engineer's own operating system" as part of the software metasystem.

**Option B: "The Operating System of Your Organization", cybernetics for the AI-augmented company**
- **Reader:** founders, COOs, operators, heads of engineering or product, and middle managers in 20–500-person companies who already feel the limits of EOS, OKRs or ad-hoc rituals, especially as AI agents start doing real work in the org.
- **Problem:** the company "operating system" (meetings, metrics, decision rights, feedback loops) was designed for humans only and breaks under growth and AI automation. Existing systems are prescriptive templates without a theory of *why* they work or how to adapt them.
- **Promise:** diagnose and redesign your organization's operating system (and your own) as a viable metasystem, using practitioner stories of OS migrations, failures and fixes.
- **Why now:** agents entering business workflows (*The Agentic Enterprise*, O'Reilly 2026), the Beer revival and centenary, and fatigue with one-size templates.
- **Working titles:**
  - *The Company Metasystem: Designing an Operating System for Humans and AI Agents*
  - *Metasystems Engineering: How to Build the Operating System That Runs Your Organization*
  - *Operating Systems for Organizations: A Field Guide to Running Companies of People and Agents*
- **Format:** business book of 220–280 pages with diagnostic tools and templates. Possibly a companion workbook or course (the Traction Library shows the spin-off model).
- **Route:** business or trade publishers usually need an agent and a platform of tens of thousands (Friedman). Without that platform, self-publish plus consulting or workshops, or use a hybrid. IT Revolution is a possible fit for a tech-org angle, but it was not accepting unsolicited proposals as of 2026-09-17.
- **Comps (3–5):**
  - *Traction* (Wickman)
  - *The Unaccountability Machine* (Davies, 2024)
  - *Team Topologies* 2e (2025)
  - *The Agentic Enterprise* (O'Reilly, 2026)
  - *Wiring the Winning Organization* (IT Revolution, 2023)
  - Classics as lineage: *Brain of the Firm*, *The Fifth Discipline*
- **Risks:**
  - Market dominated by frameworks backed by implementer networks and brands.
  - Platform-heavy; prescriptive business books without author platform rarely get traction.
  - Must deliver a concrete, teachable system (Davies was criticized for weak prescriptions).
  - Less natural fit for the user's "systems that build systems" material.

**Option C: "The Metasystem", why everything that works is a system that manages systems (idea-driven narrative nonfiction)**
- **Reader:** curious general nonfiction readers, knowledge workers and systems-thinking fans (the *Thinking in Systems* and *The Unaccountability Machine* crowd).
- **Problem:** people sense that institutions, software and their own lives are run by invisible "systems of systems" that nobody designs well, but they lack a unifying lens.
- **Promise:** one big idea (the metasystem, from Beer's cybernetics and Turchin's metasystem transitions to AI agents building software and personal operating systems), told through vivid real stories, with practical takeaways at the end of each chapter.
- **Why now:** rising Beer/VSM interest, the 2026 centenary, public anxiety about AI systems building systems, and accountability failures in large institutions.
- **Working titles:**
  - *The Metasystem: How Systems That Build and Govern Systems Shape Our Companies, Our Software, and Our Lives*
  - *Systems Above Systems: The Hidden Engineering of Everything That Works*
- **Format:** narrative nonfiction of 70–90k words, story-led.
- **Route:** a trade publisher via a literary agent (narrative nonfiction rewards writing quality over platform, per Friedman, but still needs a strong proposal and sample chapters). Self-publishing is weakest here because it lacks the bookstore and press distribution a general-audience book needs.
- **Comps (3–5):**
  - *The Unaccountability Machine* (2024)
  - *Thinking in Systems* (Meadows)
  - *The Fifth Discipline* (Senge)
  - *Building a Second Brain* (Forte, 2022; personal-OS angle)
  - *Brain of the Firm* as lineage
- **Risks:**
  - Broad appeal means a weak hook and hard discoverability, with "metasystem" at ~20 Wikipedia views a month.
  - Systems-thinking books that stay abstract rate poorly (Davies 3.74; Montalion 3.37).
  - Hardest option for a first-time author to sell or self-publish.
  - Crowdsourced stories must be woven into narrative, not listed.

**Cross-option recommendations**
- **Title strategy (all options):** keep "Metasystems Engineering" or "The Metasystem" as the brand, and carry the discoverability load with the subtitle, Amazon keywords and categories (systems thinking, platform engineering, AI agents, operating system, cybernetics).
- **Start with A.** Its build-in-public story site generates the platform numbers that B and C would later need. A later companion book or workbook could extend into B (Wickman's multi-title model).
- **Open question for the user (decisive):** current audience size (newsletter or email subscribers, followers, community reach), whether they have a publisher or agent in mind, and whether they prefer control and per-copy income (self-publish) or distribution and editorial help (publisher). Also ask which of the three meanings the user has the most first-hand experience in, since every proposal template asks "why you".

### Gaps
- None of the options has been tested with real readers. A quick validation step would be to publish 3–5 story-led posts per framing and compare sign-ups; this was not done.
- No market-size estimate (number of staff+/platform engineers, number of small-company operators) was retrieved to size Option A versus B.
- Trademark and domain availability for "Metasystems Engineering", "Builders of Builders" or the other working titles was not checked.
- Price elasticity and format preferences (print vs ebook vs audio) for this category were only indicated by Orosz's channel split (KDP print dominant) and not studied further.
