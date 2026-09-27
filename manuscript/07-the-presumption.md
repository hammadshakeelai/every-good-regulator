# 7. The Presumption

*When a governing system is presumed to be right, its errors become other people's crimes.*

---

*A note before this chapter. The rest of this book uses comics, jokes and small games to make its ideas easier to carry. This chapter does not. It is about real people, many of whom are still living with what happened to them, and some of whom are not living at all. It is told as plainly as possible.*

---

Between 1999 and 2015, the Post Office in the United Kingdom pursued the people who ran its branches for money that was missing from their accounts — through demands for repayment, suspensions and dismissals, and, for around a thousand of them, criminal convictions.

The people were sub-postmasters — the individuals, often running a village or high-street shop, who operate Post Office branches under contract. The accounts were kept on a computer system called Horizon, supplied to the Post Office by the company ICL, which later became part of Fujitsu. When Horizon showed a shortfall at a branch, the Post Office treated the shortfall as real, and the sub-postmaster as responsible for it.

The shortfalls were not real, or not in the way the Post Office claimed. They were caused by faults in the software.

In July 2025, a public inquiry chaired by the retired judge Sir Wyn Williams published the first volume of its final report. It concluded that it was likely that around **1,000 people** had been prosecuted and convicted on the basis of false data from Horizon, and that between 50 and 60 more had been prosecuted but not convicted. It found that people who had done nothing wrong had been impoverished and bankrupted, had lost their jobs, their marriages, their reputations and their health. It recorded that the families of **13 people** say their relatives took their own lives because of shortfalls that Horizon showed but that were not real; the chair said he could not make a definitive finding about the cause of each death, but did not rule out the connection as a real possibility. He also received evidence from at least 59 people who had contemplated suicide, and attributed it to what had happened to them.

This is the gravest story in the book. It belongs here because, stripped to its structure, it is the story of a governing system — a piece of software and the organisation around it — whose picture of reality was trusted over the people who could see that the picture was wrong. And the reason it was trusted turned on a single rule.

---

## The rule

From the mid-1980s, English criminal law did not simply assume that computers worked. Under section 69 of the Police and Criminal Evidence Act 1984, a statement in a document produced by a computer could not be admitted as evidence unless it was shown, among other things, that there were no reasonable grounds for believing the statement was inaccurate because of improper use of the computer — and that at all material times the computer had been operating properly, or, if not, that the fault could not have affected the document or the accuracy of what it said.

On 14 April 2000, that section was repealed by the Youth Justice and Criminal Evidence Act 1999. From then on, courts operated on a common-law presumption that a computer was working correctly unless there was evidence to the contrary.

In practice, this turned the burden around. If Horizon said a branch was short, the question in court was not whether Horizon's figure was reliable. It was whether the sub-postmaster could prove that it was not — and a sub-postmaster had no access to the system's inner workings, its error logs, or the knowledge of the people who maintained it. And in many cases, the organisation that controlled the evidence was the same organisation bringing the case: the Post Office conducted its own prosecutions, and "the prosecution strategy used by the Post Office" is one of the subjects the public inquiry was set up to examine.

In the language of this book, a presumption of correctness is a rule about the governing layer's model. It declares, in advance, that the model matches reality. And once that is declared, there is no route for evidence that it does not.

---

## How it looked from the branch

The inquiry that examined the scandal is one of the largest ever held in Britain. By the time its first final volume was published, it had sat for 226 days of hearings, heard oral evidence from 298 witnesses and received around 274,600 documents. That volume, published on 8 July 2025, was built around the human impact of what happened and the question of compensation, and it records seventeen first-hand accounts in detail. It describes people who became seriously ill, who struggled with their mental health — including alcohol addiction — and who were made bankrupt; people whose reputations were destroyed; people held liable for small sums the Post Office said they had lost, and others who were wrongly imprisoned; and people who died before receiving compensation. Sir Wyn Williams called the impact "disastrous."

The chair chose his seventeen "Case Illustrations" from more than 200 witness statements. He deliberately included people who were far less well known than the scandal's public faces. He was careful to say that, at that stage, he was recording the human impact as each person described it, not making findings about exactly what happened in each case. Three of those accounts, summarised here from the report itself, show the pattern this chapter is about.

Harjinder Butoy bought a post office in Sutton-in-Ashfield, Nottinghamshire, in 2004, using a redundancy payment and a loan from his brother. His family lived above the shop. In April 2007 his branch was audited, and he was told everything was fine. A week later it was audited again, and this time he was told there was a shortfall — eventually alleged to be more than £200,000. He was arrested, charged with theft, and in September 2008 convicted on ten counts. He recalls being offered some form of plea arrangement and refusing it, because he believed he had done nothing wrong. He was sentenced to 39 months in prison. While he was inside, tax demands he could not pay led to his bankruptcy, which lasted ten years. The premises were sold at a loss, and he has not been able to find work since. His convictions were quashed by the Court of Appeal on 23 April 2021.

Jacqueline McDonald became the postmistress at Broughton, a village near Banbury, in December 2006, and lived with her family above the branch. In October 2008 her line manager arrived to say that Horizon showed the branch holding about £50,000 in excess cash. After an audit she was suspended and asked to pay the Post Office more than £93,000. She pleaded guilty to false accounting and later, on legal advice intended to reduce her sentence, to theft; she was sentenced to 18 months. The report singles out one detail as striking. In the period immediately before the audit, she had made 256 calls to the Horizon Helpdesk about transaction and balancing problems — and, she has always maintained, received no meaningful help. Both she and her husband were made bankrupt; when she signed her statement to the inquiry in January 2022, she had been bankrupt for about ten years and had still not been discharged.

Deirdre Connolly ran the post office at Killeter in Northern Ireland from 2006, and took on two rural outreach sites where, she told the inquiry, Horizon worked badly on a poor line. She rang the Helpdesk two or three times a week and found it did not help. After an unannounced audit in June 2010 she was suspended, shown a shortfall on a screen, and given no chance to check the calculation. Their families gave them about £14,000 towards what the Post Office demanded. She was never prosecuted. She described the day a letter arrived telling her that criminal proceedings would not be brought — a possibility she had not even known existed — as her darkest day. "The shame of [this] still burns," she told the inquiry.

Three people, in three parts of the United Kingdom, with three different outcomes: prison, prison after a guilty plea, and no prosecution at all. What the accounts share is the shape of the system around them. In each, the regulator's figure arrived first and stood as the fact. And in two of them, the person closest to the work had a way to report a problem — a helpdesk — that was used again and again, and led nowhere.

What can be said in general, from the findings, is this. A sub-postmaster would see a shortfall appear in the branch accounts that they could not explain. Under the terms on which they worked, they were treated as responsible for making good losses — terms that were themselves examined by the High Court in the first of the major judgments in the sub-postmasters' group case, in March 2019. In practice, the burden fell on the sub-postmaster to show that a shortfall was not their fault. The court held that this was the wrong way round: under the main contract, a sub-postmaster was responsible for losses caused through their own "negligence, carelessness or error", and it was for the Post Office to prove that there had been such negligence, carelessness or error — not for the sub-postmaster to prove there had not. The judge also held that the contracts were *relational*, so the Post Office was not entitled to act in a way that reasonable and honest people would consider commercially unacceptable; and he found that several of the Post Office's standard terms — in the later contract, liability for losses; pay during and after suspension; termination as the Post Office read it; and the absence of any compensation for loss of office — failed the test of reasonableness imposed by the Unfair Contract Terms Act 1977. "There is no doubt," he wrote, "that the Post Office is in an extraordinarily powerful position compared to each and every one of its SPMs." They might pay the missing sum out of their own money. The shortfalls might recur. And if they could not or would not pay, or if the sums grew large, they could face dismissal, civil action, or criminal prosecution for theft or false accounting — on the strength of the system's figures.

Many of them knew, with complete certainty, that they had not taken the money. That knowledge was exactly the kind this book has been calling *metis* — the local, first-hand understanding of the person who does the work. It could not be entered into the system. It did not appear on any report. And against a legal presumption that the computer was right, it counted for very little.

---

## What the organisation knew

The inquiry's findings about the Post Office are stark. It found that the Post Office "trenchantly resisted" the contention that Horizon sometimes produced false data. It found that some senior Post Office employees knew, or should have known, that the system was faulty — and that staff at the suppliers, ICL and Fujitsu, knew or should have known about the defects too. And it found that the Post Office maintained, in the inquiry's words, "the fiction that its data was always accurate."

It is important to be precise here, for two reasons. First, because this book is not a legal judgment, and the inquiry's full account of who knew what, and when, is set out in its reports; that is where it should be read. Second, because the lesson of this book's Chapter 8 — that disasters are almost never the product of a single cause or a single villain — applies here as much as anywhere. The Horizon scandal required many things at once: software with defects; a contract that placed losses on the sub-postmaster; an organisation that could investigate, prosecute and control the evidence; a legal rule presuming the computer correct; an institutional unwillingness to believe the people reporting problems; and years in which each of those conditions reinforced the others. Remove any one and the story changes.

What the conditions have in common is that each one strengthened the governing layer's picture of reality and weakened every route by which that picture could be corrected.

---

## How it came to light

The correction, when it came, came from the people the system had blamed.

In a group legal action, *Bates and Others v Post Office Ltd*, 555 sub-postmasters took the Post Office to court. The case was heard in the High Court by Mr Justice Fraser between 2017 and 2019. His first major judgment, on 15 March 2019, dealt with the contracts between the Post Office and its sub-postmasters. On 11 December 2019, the Post Office settled the claims, agreeing to pay £57.75 million in damages. Five days later, on 16 December, the judge handed down his judgment on the computer system itself. It found that bugs, errors and defects in Horizon had made it unreliable, with the potential to cause exactly the kind of discrepancies in branch accounts for which sub-postmasters had been blamed.

The group action is named after its lead claimant, Alan Bates. The Post Office had terminated his contract as a sub-postmaster in 2003 over a shortfall he disputed. In November 2009, at a meeting in the village of Fenny Compton, he and other former sub-postmasters founded the Justice for Subpostmasters Alliance, which spent the following decade gathering others who had experienced the same thing. He was later knighted.

In April 2021, in *Hamilton and Others v Post Office Ltd*, the Court of Appeal quashed the convictions of 39 of the 42 former sub-postmasters who had appealed. It found an abuse of process on two grounds: that a fair trial had been impossible, and that it was an affront to the public conscience that they had been prosecuted at all.

Public attention surged in January 2024, when the ITV drama *Mr Bates vs The Post Office* was broadcast in four episodes on consecutive nights, from 1 to 4 January. On 10 January 2024 the Prime Minister announced that the government would legislate to quash the convictions. The Post Office (Horizon System) Offences Act 2024 came into effect on 24 May 2024, overturning convictions en masse so that people could be cleared and compensated without each having to fight their own appeal.

Compensation has been slow. In his July 2025 report, Sir Wyn Williams criticised the "egregious delays" in the schemes set up to pay it, said he very much doubted every claim could be settled before the end of 2026, and made a series of recommendations to speed up and improve redress — asking the government, the Post Office and Fujitsu to respond in writing by 10 October 2025. By 28 August 2026, according to government figures, about £1.7 billion had been paid to more than 13,500 claimants across the various compensation schemes. At the time of writing, in September 2026, the inquiry's remaining volumes — covering Horizon's technical failings, the Post Office's handling of the discrepancies, the prosecutions, and government oversight — had not yet been published; the chair has said they will appear together.

---

## The mechanism, stated plainly

Every chapter in this book describes a mechanism. This one can be stated without a diagram.

A governing system carries a model of the work it governs. In this case, the model was a set of branch accounts. Every regulator's model is sometimes wrong. What matters is whether there is a way for the error to be found and corrected — a feedback loop.

At the Post Office, several things closed that loop at once. A legal presumption declared the model correct. The organisation that relied on the model also controlled the evidence about it. The people who could see the error had no way to show it, no authority to stop anything, and every incentive to stay silent or to pay. And the organisation, faced with repeated reports that the model was wrong, treated the reports as the problem.

When a governing layer's picture of the world is protected from correction, its errors do not disappear. They are transferred — onto the people it governs.

---

## Not only Britain

Horizon is not the only case of its kind, and the parallel matters because it shows the pattern does not depend on one organisation's culture.

From 2015 to 2019, the Australian government ran an automated scheme, widely known as *Robodebt*, that matched welfare records against tax data and used an averaging of people's annual income to calculate that they had been overpaid benefits — and then raised debts against them. The scheme reversed the onus of proof: it was up to the person to show that the calculated debt was wrong. In July 2023, a Royal Commission led by Commissioner Catherine Holmes published a three-volume report. It found that the scheme had been devised without regard to social security law, and that it was unfair and unlawful. It called Robodebt "a crude and cruel mechanism, neither fair nor legal," and found that it had made many people feel like criminals. People took out loans, drained their retirement savings or used credit cards to repay debts that had been wrongly raised against them. The Commission found at least three known suicides connected to the scheme, and said it was confident these were not the only tragedies of their kind. Its report ran to three volumes and almost a thousand pages, with 57 recommendations — including a legislative framework for automated decision-making and a body to oversee it — and a sealed section recommending that individuals be referred for civil and criminal prosecution.

The two cases differ in their technology, their law and their politics. The structure is the same: an automated system produced a figure, the figure was treated as correct, and the burden of disproving it fell on the person it was used against.

---

## What this means for the systems we are building now

It would be comfortable to treat Horizon as a story about one organisation, one piece of software and one country. It is not, and the reason is in the rest of this book.

Every day, organisations make decisions about people on the strength of what their systems say. Performance is judged from dashboards. Fraud is flagged by models. Access is granted or refused by automated checks. Increasingly, software written by AI agents is shipped on the strength of automated tests that no human has read. In each case the question from this chapter applies: when the system and a person disagree, **who is presumed to be right?** And if the system is presumed right, what route exists for the person to show that it is not?

These are not rhetorical questions. They have answers in any given organisation, and the answers can be written down and changed. A system whose outputs can seriously harm someone should have a way for its errors to be challenged by that person, access for them to the evidence, and an independent route for the challenge to be heard. Those are not technical features. They are properties of the governing layer — of who is allowed to stop it, and whose knowledge counts.

---

## The Image

A person standing in their own shop, looking at a number on a screen that they know to be wrong, with no way to make anyone believe them.

## The Reversal

The lesson of Horizon is not that computers should be distrusted. Well-built systems are often far more reliable than human memory or testimony, and a world that presumed every computer wrong would be unworkable. The lesson is narrower and harder: that no system — human or machine — should be *presumed* correct in a way that removes the means to show it is not, especially when the consequences fall on someone who has no access to its workings. Reliability is something to demonstrate and keep demonstrating, not something to declare.

## The Rules

1. **No governing system should be presumed correct in a way that removes the means to challenge it.**
2. **The people a system can harm must have access to the evidence about it.**
3. **When many people independently report the same kind of error, the reports are data about the system, not about the people.**

## Diagnose

- In your organisation, which systems make or inform decisions that can seriously harm a person — their job, their money, their record?
- When such a system and a person disagree, who is presumed to be right?
- What route exists for someone to challenge the system's output, and do they have access to the evidence they would need?
- Who investigates when many people report the same kind of problem — and are they independent of the people who own the system?

## In One Paragraph

Between 1999 and 2015 the UK Post Office pursued sub-postmasters for shortfalls produced by faults in its Horizon accounting system; a public inquiry concluded that around 1,000 people were likely prosecuted and convicted on the basis of Horizon data, and recorded that the families of 13 people say their relatives took their own lives because of it. Many conditions combined — software defects, contract terms, an organisation that controlled the evidence, a legal presumption since 2000 that computers work correctly, and repeated refusal to believe the people reporting problems — and each strengthened the system's picture of reality while weakening every way to correct it. When a governing system is presumed right, its errors are transferred onto the people it governs. Every organisation that makes decisions about people from what its systems say should know who is presumed right, and how that presumption can be challenged.

## Go Deeper

- Post Office Horizon IT Inquiry, *Final Report, Volume 1* (8 July 2025), and its later volumes — postofficehorizoninquiry.org.uk. Read the first-hand accounts.
- *Bates and Others v Post Office Ltd (No. 3)* [2019] EWHC 606 (QB), the Common Issues judgment (15 March 2019), especially paragraphs 653 (burden of proof), 705–706 (good faith) and 1108 (unreasonable terms). Nick Wallis's summary at postofficetrial.com is a readable guide.
- *Bates and Others v Post Office Ltd* [2019] EWHC 3408 (QB), the Horizon Issues judgment.
- *Hamilton and Others v Post Office Ltd* [2021] EWCA Crim 577.
- Post Office (Horizon System) Offences Act 2024, and its explanatory notes, on legislation.gov.uk.
- The Criminal Cases Review Commission's pages on the Post Office cases.
- Royal Commission into the Robodebt Scheme, *Report* (7 July 2023), robodebt.royalcommission.gov.au.
