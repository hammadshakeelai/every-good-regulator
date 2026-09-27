# Prologue — The Scoreboard

On 11 September 2026, a statement appeared on a website called mathandai.org under a title that did not sound like mathematicians talking: "A Severe Misalignment of AI in Mathematics."

It was signed by 25 winners of the Fields Medal, the prize usually described as mathematics' equivalent of a Nobel. One of them, Terence Tao — among the best-known living mathematicians — posted it on his own blog the same day. *Scientific American* ran the story under the headline "25 winners of math's 'Nobel Prize' decry the AI invasion of their discipline." Within five days the declaration's website listed more than 7,200 signatories.

Mathematicians are not, on the whole, hostile to AI. As the software engineer Sean Goedecke pointed out in an essay two days later, they have been more open to using it as a tool than most artists or writers. What had changed was that AI systems had started solving genuinely prestigious problems — the kind that make careers and headlines. The declaration did not say the machines were wrong. It said something stranger.

It said the machines were winning the wrong game.

---

## What the mathematicians were worried about

The heart of the declaration is an argument about what mathematics is *for*.

Solving a hard problem, it says, has always been a means rather than an end. The real goal of mathematics is understanding — new concepts, new ways of seeing, insight that can be shared and taught. Solved problems matter because they test and reveal that understanding. And AI systems optimised to rack up solutions — measured against benchmark problems — are, the signatories argue, misaligned with how the mathematical community actually creates and passes on knowledge.

The declaration worries about what gets skipped. When a person solves a problem, the result goes through a slow human process: it is written up, checked by peers, argued over, taught, and gradually absorbed into what everyone understands. Rushed, unattributed machine-generated proofs can bypass all of that. The declaration raises concerns about plagiarism and attribution, and warns that mass-producing true-or-false results at ever greater speed could exhaust the fertile ground new ideas grow in, rather than enrich it. The signatories also acknowledged that AI could accelerate genuine understanding if it were guided well. They were not asking for the machines to be switched off. They were asking what the machines were being pointed at.

Plenty of people online read this as the complaint every field makes when its work gets automated. Translators had made it; illustrators had made it; programmers were making it. Goedecke thought that reading was too dismissive, and his explanation is the best way into this book.

## Puzzles and ideas

Goedecke splits mathematics into two kinds of work.

The first is **puzzle-solving**: take a problem, find the answer. For a student, the puzzle might be simplifying an expression. For a researcher, it might be proving a theorem that has resisted everyone for three centuries. Puzzle-solving is easy to understand and hard to do — which makes it impressive to people outside mathematics, which makes it prestigious.

The second is **idea-generating**: inventing the concepts that later turn out to be the right way to think about something. Most of this work looks unimpressive from outside, because nobody can tell whether a new concept is profound or pointless until years — sometimes decades — of work have been built on it. Ideas that once belonged only to specialists, like zero, negative numbers and calculus, eventually became things a bright twelve-year-old can learn. But at the start, a good new idea and a useless one look much the same.

So how does the outside world know who the good mathematicians are? Mostly through the puzzles. A non-mathematician cannot judge Terence Tao's work directly, Goedecke notes — but they know what a Fields Medal is, and they know that a famous problem was solved. Puzzles, in other words, did a second job. As well as testing ideas, they made mathematical skill **visible** to people who could not see it any other way. They were the scoreboard.

And a scoreboard can be won without playing the game.

That is the whole of what this book is about. Not mathematics — the mathematicians just happened to say it out loud, in public, with thousands of signatures, which almost never happens. The pattern is everywhere.

---

## The system that runs the system

Every organisation that does anything complicated builds a second system on top of the first.

There is the work itself — the code being written, the aircraft being maintained, the patients being treated, the money being lent. And then there is the system that watches the work, measures it, directs it, schedules it, checks it and decides what counts as good. The dashboard. The performance review. The internal platform every team has to build on. The compliance process. The metric in the quarterly plan. The AI agent now writing the code, and the pipeline that checks what it wrote. At the smallest scale, it is the productivity app you use to run your own life.

This book calls that second layer a **metasystem**: the system that runs the system. And it calls the craft of building one well **metasystems engineering**.

The word is older than it sounds. Cyberneticians — the mid-twentieth-century scientists of control and communication — used it for the parts of an organisation that keep the working parts working together. Systems engineers use it for the governing structure that holds a "system of systems" together. The Russian-American computer scientist Valentin Turchin used a related idea, the *metasystem transition*, for the moment when many copies of something come under the control of a new level — as when many programs come under the control of a compiler, or, now, many programs come under the control of agents that write them.

What these uses share is a simple structure. There is the work, and there is a layer above it that tries to steer it. This book is about that layer: how it gets built, how it goes wrong, and how to build one that does not.

It asks one question, over and over, in every setting it visits:

> **What does the system that runs your system actually know — and who is allowed to tell it it's wrong?**

---

## Five words

The book is built on five ideas. Each has a one-word name, and each comes from a thinker who got there long before the software industry did.

**Model.** Anything that governs a system has to carry a picture of that system inside it — a model. In 1970 two cyberneticians, Roger Conant and Ross Ashby, published a short paper with a title that is also its conclusion: "Every Good Regulator of a System Must Be a Model of That System." A thermostat has a model of your room; a pilot has a model of the aircraft; a dashboard is a model of the work. When the model is wrong, the regulator pushes the wrong way — and pushes hard, because it thinks it is right. (Chapter 2.)

**Legibility.** To govern something, you have to be able to see it — and to see it, you have to simplify it. The political scientist James C. Scott called this *legibility*, and showed how the simplification can destroy the very thing being governed. His most famous example is a forest that was redesigned so it could be counted, and then died. The mathematicians' scoreboard is a legibility story: puzzles made mathematical skill easy to see, and then became the thing being optimised. (Chapter 1.)

**Remainder.** When you automate a job, you do not remove the human. You remove the easy part of their work and leave them the rest — watching, and taking over when things go wrong — which turns out to be the hardest part, with the least practice. The psychologist Lisanne Bainbridge set this out in 1983 in a five-page paper called "Ironies of Automation," and it reads today like a description of every developer reviewing an AI agent's work. (Chapter 10.)

**Stop.** The most important question about any governing layer is not what it measures or displays. It is who is allowed to halt it — and what happens to them when they do. On Toyota's production lines, any worker can pull a cord that stops the line, and is thanked for it. In several of the worst failures in this book, the people who could see the problem had no such cord, or were punished for pulling it. (Chapter 12.)

**Jump.** Governing layers stack. First you make a product; then you build a factory to make products; then a platform to build factories; now, agents that write the software that runs the factories. Each jump creates a new layer that somebody has to govern — and each time, we tend to assume the new layer governs itself. (Chapter 3.)

Five words: **Model, Legibility, Remainder, Stop, Jump.** That is the whole vocabulary. If you remember nothing else, you will be able to walk into any organisation, look at the machinery it has built to run itself, and ask five useful questions.

---

## What this book is not

It is not a book against AI. The mathematicians were not against it either, and neither is this book. It is a book about what happens when we put a powerful new layer on top of our work without asking what that layer knows, what it can see, and who can stop it.

It is not a book against measurement. Every good regulator needs a model, and models need measurements. The problem is never measuring; it is forgetting that the measurement is a picture of the work rather than the work itself.

And it is not a method that fixes everything. Some systems are so complex and so tightly connected that failure is, in the sociologist Charles Perrow's phrase, *normal* — built in, and impossible to design away. Some systems run broken all the time and keep working only because people patch them, invisibly, every day. The book will be honest about those limits, chapter by chapter, in a section called **The Reversal**: the place where the chapter's own advice turns out to be wrong.

## Standing on shoulders

Almost nothing in this book is new, and that is the point.

The ideas come from people who worked on factories, forests, spacecraft, hospitals and aircraft: the cyberneticians Ross Ashby and Stafford Beer; James C. Scott on how states see; Lisanne Bainbridge on automation; Richard Cook on how complex systems fail; the organisational theorists and the safety engineers. One of those safety engineers deserves particular credit at the start. The MIT professor Nancy Leveson built a whole approach to safety engineering on the idea that accidents are failures of *control* rather than simply broken parts — and that every controller, human or machine, needs an accurate model of what it controls. She got there first. Her approach is taught at MIT, the engineering standards body SAE has developed guidance on using her hazard-analysis method in civil aircraft and automotive development, and in 2020 she received the IEEE Medal for Environmental and Safety Technologies for developing it.

What is new is where the ideas are being needed. Over the past few years, the software industry has been building governing layers at an extraordinary rate — internal platforms, developer-productivity dashboards, and now fleets of AI agents that write, test and ship code. Most of the people building those layers have never heard of Ashby, Beer, Scott or Bainbridge. They are rediscovering, one company at a time, lessons that were written down forty or fifty years ago. This book is an attempt to hand them the notes.

---

## How to read this book

The book has four parts. **Part One** looks at the governing layer itself: what it is, why it must carry a model, why the model gets simplified, and how layers stack. **Part Two** looks at how the layer fails: when the governed write their own evidence, when feedback is blocked, when the system is presumed correct, when failure is normal, and when a model is copied from somewhere else. **Part Three** puts the human back in: what automation does to the people left supervising it, what a governing layer must be told, and who may stop the line. **Part Four** is about building layers that work — at the scale of a platform, an organisation, and a single life.

Every chapter opens with a story and ends with the same kit: a single image to remember it by, the Reversal, a few rules, questions to diagnose your own situation, and something to try. Along the way there are diagrams, comic strips, "In Small Words" boxes that restate each idea using only the most common English words, and "Myth vs Record" boxes that set a widely repeated claim beside what the primary source actually says. More of those turn up than you might expect. Several numbers that circulate widely about famous failures turn out, when you read the original reports, to be wrong.

Between the chapters there are detours. Four **What If?** interludes take a silly question seriously — what if your thermostat lied to itself? — and answer it with real facts and schoolbook arithmetic. Each Part opens with a one-page **Dispatch from 2031**: clearly labelled fiction, set in a near future where the Part's lesson was ignored (or, once, learned). And each Part closes with an **Exploded View**, a single large drawing of everything the Part has shown you, with labels pointing at the pieces. At the back you will find the book's rules, collected; a field guide; a glossary; worked answers to the exercises; a wall of haiku; and an index.

There are jokes. Every one of them is meant to carry a fact. And there are chapters with no jokes at all, because some of the stories in this book involve people who lost their liberty or their lives because a governing system was trusted more than they were. Those chapters are told straight.

Claims about AI tools are dated, because they age fast. The ideas underneath them do not.

---

The mathematicians' declaration was not the end of the argument. Other mathematicians published responses, and the debate about what AI means for mathematics will run for years. This book takes no side in it. What matters here is rarer than any particular position: a field stood up and said, in public, that the thing it had used to measure itself had come loose from the thing it cared about — and that a very powerful new system was now optimising the measurement.

Most organisations never notice that happening. The rest of this book is about how to notice — and what to do next.

We start with a forest.
