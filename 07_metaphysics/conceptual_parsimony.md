# Conceptual Parsimony

## The Argument

The typed logical language is the simplest representation of reasoning that a
mind can grasp, manipulate, and teach. It is the cognitive version of
information-theoretic parsimony — not just short in bits, but short in cognitive
load.

## Beyond Bits

Information-theoretic parsimony measures description length in bits. But not all
bits are equal to a mind. Consider two 100-bit strings:

    1010101010101010101010101010101010...
    0110100111010011100101110111001010...

Both are 100 bits. The first has low cognitive complexity — you grasp the pattern
instantly. The second has high cognitive complexity — it looks random, and you
cannot hold it in working memory.

Cognitive complexity is not the same as Kolmogorov complexity (though they are
related). It is about the ease with which a structure can be:

- **Grasped**: understood on first encounter
- **Remembered**: held in working memory
- **Manipulated**: reasoned about, combined, transformed
- **Communicated**: taught to another mind

The typed logical language scores high on all four.

## Why the Formal Language Is Cognitively Simple

**Grasped**: The basic elements — entity, predicate, role, rule — correspond to
concepts that children acquire by age three. "Socrates" is a thing. "Mortal" is
something you can say about a thing. "All men are mortal" is a rule. These are
not technical abstractions imposed by logicians. They are the natural categories
of human understanding. Aristotle did not invent them; he observed them.

**Remembered**: A typed predicate like man(theme: socrates) has exactly two
chunks: the predicate and its argument. A rule like always [x:e]: man(theme: x)
-> mortal(theme: x) has three chunks: quantifier, premise, conclusion. These fit
comfortably within the limits of working memory (Miller's 7±2, or more
conservatively Cowan's 4±1). By contrast, a neural network's representation of
the same knowledge spans millions of parameters — it is not rememberable by any
mind.

**Manipulated**: Given man(theme: socrates) and the rule above, you can derive
mortal(theme: socrates) in one step. The manipulation is mechanical — substitute
socrates for x, check the premise, conclude. A child can do it. A computer can
do it. The step is transparent and verifiable. By contrast, manipulating a neural
network's representation of the same inference requires backpropagation through
billions of weights — it is not manipulable by any mind.

**Communicated**: You can teach someone the typed logical language in an
afternoon. Entities, predicates, roles, rules, quantifiers — five concepts. You
can teach the QBBN's inference mechanism (belief propagation on AND/OR/NEG
factors) in a day. You cannot teach someone how a transformer performs inference,
because nobody knows — the mechanism is opaque.

## The Cognitive Parsimony Principle

We propose: **the cognitively simplest representation of a domain that supports
all necessary operations on that domain is the most likely to reflect the true
structure of that domain.**

This is stronger than Occam's Razor (which says prefer the simplest hypothesis)
because it adds a constraint: the simplicity must be *cognitive*, not just
formal. A representation could be Kolmogorov-simple but cognitively complex
(imagine a highly compressed encoding that requires a complex decompression
algorithm to read). Cognitive parsimony requires that the representation be
simple *to a mind* — graspable, rememberable, manipulable, communicable.

The typed logical language satisfies this constraint. It is not just short in
bits. It is short in thoughts.

## Relation to Information-Theoretic Parsimony

Conceptual parsimony and information-theoretic parsimony are related but
distinct:

| Criterion | Information-Theoretic | Conceptual |
|---|---|---|
| Measures | Bits | Cognitive load |
| Optimizes for | Compression | Understanding |
| Unit | Kolmogorov complexity | Working memory chunks |
| Agent | Universal Turing machine | Human mind |
| Weakness | Uncomputable | Subjective |

They converge when the shortest encoding happens to also be the most cognitively
transparent — which is the case for typed logical language. The formal language
is both the shortest encoding of inferential content AND the most cognitively
accessible representation of inferential content. This convergence is not
guaranteed in general (compressed files are short but not cognitively
accessible), so when it occurs, it is evidence that the representation is
*natural* — aligned with both mathematical and cognitive structure.

## The Pedagogical Test

A practical test of conceptual parsimony: **how quickly can a newcomer learn the
representation and use it correctly?**

- Typed predicates: teachable in hours
- First-order logic: teachable in a semester
- Lambda calculus: teachable in a semester
- Neural network internals: arguably not teachable at all (nobody fully
  understands them)

The typed logical language is the most teachable formal representation of
reasoning. This is not a coincidence. Teachability reflects cognitive simplicity,
and cognitive simplicity (we argue) reflects structural truth.

## Key Works

- Miller, G.A. "The Magical Number Seven, Plus or Minus Two." *Psychological
  Review*, 63(2):81-97, 1956.
- Cowan, N. "The Magical Number 4 in Short-Term Memory." *Behavioral and Brain
  Sciences*, 24(1):87-114, 2001.
- Feldman, J. "Minimization of Boolean Complexity in Human Concept Learning."
  *Nature*, 407:630-633, 2000.
- Chater, N. and Vitányi, P. "Simplicity: A Unifying Principle in Cognitive
  Science?" *Trends in Cognitive Sciences*, 7(1):19-22, 2003.

## Open Questions

- Can cognitive parsimony be formalized, or is it necessarily subjective?
- Does the teachability of typed predicates reflect something about human
  cognitive architecture, or just about the culture of logic education?
- If a non-human intelligence (an alien, an AI) encountered the same reasoning
  problems, would it arrive at the same typed formal language? If so, conceptual
  parsimony is universal. If not, it is anthropocentric.