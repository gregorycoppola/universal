# Sutton's Bitter Lesson

## The Argument

Rich Sutton's "The Bitter Lesson" (March 2019) is a one-page blog post that has
become one of the most influential arguments in AI. The claim is simple and
sweeping:

**General methods that leverage computation are ultimately the most effective, and
by a large margin.**

Sutton surveys the history of AI — chess, Go, speech recognition, computer vision,
game playing — and observes the same pattern in every domain: researchers build
systems incorporating human knowledge (hand-crafted features, expert rules,
domain-specific representations), these systems work well initially, but they are
eventually overtaken by general methods (search, learning) that scale with
available computation.

## The Pattern

The pattern repeats across decades:

**Chess**: Expert systems with hand-coded evaluation functions (piece values,
positional heuristics) dominated for years. Deep Blue combined expert knowledge
with massive search. Then AlphaZero learned to play chess from self-play alone,
using no human chess knowledge beyond the rules, and crushed everything before it.

**Computer vision**: Hand-designed feature extractors (SIFT, HOG, Haar cascades)
dominated for a decade. Then deep convolutional networks trained on large datasets
surpassed all hand-engineered approaches, and the engineered features became
irrelevant.

**Speech recognition**: Hidden Markov Models with hand-designed phonetic features
gave way to end-to-end neural models trained on raw audio.

**Go**: The strongest Go programs used Monte Carlo tree search with hand-tuned
evaluation. AlphaGo combined neural networks with search, learning from human
games. AlphaZero dropped human games entirely.

In every case, the lesson is bitter because researchers invested careers in
domain-specific knowledge that was eventually rendered obsolete by brute-force
computation.

## The Prescription

Sutton's conclusion is a prescription for AI research:

> "The biggest lesson that can be read from 70 years of AI research is that general
> methods that leverage computation are ultimately the most effective."

Do not encode human knowledge into your system. Build systems that scale with
compute. Search and learning are the two fundamental methods that do this. Bet on
them.

## Why It Matters for This Project

The formal NLP pipeline described in *Statistical Parsing for Logical Information
Retrieval* — grammar rules, typed predicates, Horn clauses, factor graphs — sits
squarely on the side Sutton warns against. It is hand-engineered knowledge
representation. It is exactly the kind of system that, historically, loses.

The bitter lesson is the strongest objection to the entire project. If Sutton is
right, then building a typed logical language and a slot grammar is a waste of time
— some general method (bigger LLMs, more data, more compute) will eventually do
the same thing without any of the formal machinery.

The response to this objection occupies the next two documents in this section.

## Key Source

- Sutton, R. "The Bitter Lesson." Blog post, March 13, 2019.
  http://www.incompleteideas.net/IncIdeas/BitterLesson.html

## Open Questions

- Is the bitter lesson a universal law of AI, or a historical observation that
  holds until it doesn't?
- Are there domains where formal structure is *necessary* — where no amount of
  compute can substitute for getting the representation right?
- Does the bitter lesson apply to *reasoning* the same way it applies to
  *perception*? Chess and vision are pattern-matching tasks; logical inference
  may be fundamentally different.