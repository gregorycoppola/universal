# Information-Theoretic Parsimony

## The Argument

Given a set of inferential relationships, the typed logical representation is
the minimum description length encoding. By the MDL principle and Kolmogorov
complexity, the shortest description is the most probable true structure.

## Description Length

Consider encoding the knowledge that "all men are mortal" and "Socrates is a
man."

**In a neural network**: This knowledge is distributed across billions of
parameters. The encoding is the full parameter vector — gigabytes of
floating-point numbers. Most of these parameters encode other knowledge too, so
you cannot isolate the bits that represent "all men are mortal." The description
length is, in effect, the entire model.

**In natural language**: "All men are mortal. Socrates is a man." This is about
45 bytes. But the encoding is ambiguous — "men" could mean "adult males" or
"humans," "mortal" could mean "subject to death" or "very embarrassed" (in
informal usage). The description is short but imprecise.

**In typed logical language**:

    predicate man {theme: e}
    predicate mortal {theme: e}
    entity socrates : e
    always [x:e]: man(theme: x) -> mortal(theme: x)
    man(theme: socrates)

This is about 150 bytes. Longer than natural language, but completely
unambiguous. Every symbol has a defined meaning. Every variable has a defined
type. Every rule has a defined weight. The encoding is precise enough to run
inference on — which natural language is not.

## The MDL Principle

The Minimum Description Length principle (Rissanen, 1978) states: given competing
hypotheses that explain the same data, prefer the one with the shortest total
description length (model + data encoded by model).

For inferential content:
- The neural network "model" is gigabytes. It explains the data (can answer
  "is Socrates mortal?") but the model itself is enormous.
- The typed logical representation is bytes. It explains the same data with a
  model that is smaller by a factor of ten million.

By MDL, the typed logical representation is overwhelmingly preferred as the true
generating structure for inferential relationships.

## Kolmogorov Complexity

Kolmogorov complexity K(x) is the length of the shortest program that produces
x. It is the theoretical minimum description length — the most compressed
possible representation.

For a set of inferential relationships (facts and rules), the typed logical
language is close to the Kolmogorov complexity because:

1. Each fact is encoded once, in its minimal form (predicate + arguments)
2. Each rule is encoded once, with variables standing for all instances
3. There is no redundancy — quantified rules compress all instances into one
   statement
4. There is no overhead — no parameters, no architecture specification, no
   training hyperparameters

A neural network encoding the same inferential content has enormous overhead:
the architecture specification, the training procedure, the parameter values
(most of which encode other knowledge unrelated to the target inferences).

The typed logical language is not provably the Kolmogorov-optimal encoding (that
is uncomputable in general), but it is plausibly close — and certainly closer
than any neural network encoding by orders of magnitude.

## The Solomonoff Connection

Solomonoff's theory of inductive inference (1964) assigns prior probability to
hypotheses inversely proportional to their Kolmogorov complexity: shorter
programs are a priori more probable. This is the formalization of Occam's Razor.

Applied to the structure of thought: if the typed logical language is the
shortest encoding of inferential content, then by Solomonoff's prior, it is
the most probable true structure of inferential reasoning.

This is not proof. Kolmogorov complexity is uncomputable, and Solomonoff's prior
is an idealization. But the direction is clear: information theory favors the
typed formal language as the true structure, not just a convenient notation.

## The Difference from Computational Parsimony

Computational parsimony is about **processing cost** — how much work is needed
to perform inference. Information-theoretic parsimony is about **representation
cost** — how many bits are needed to encode the knowledge.

These are genuinely independent. A system could be cheap to run but expensive to
encode (imagine a lookup table of all possible inferences — O(1) lookup, but
exponential storage). Or expensive to run but cheap to encode (a compact but
slow theorem prover).

The typed formal language wins on both. It is both the cheapest to run (among
verified reasoning systems) and the shortest to encode (among precise
representations of inferential content). Two independent optima, same structure.

## Key Works

- Rissanen, J. "Modeling by Shortest Data Description." *Automatica*,
  14(5):465-471, 1978.
- Kolmogorov, A.N. "Three Approaches to the Quantitative Definition of
  Information." *Problems of Information Transmission*, 1(1):1-7, 1965.
- Solomonoff, R.J. "A Formal Theory of Inductive Inference." *Information and
  Control*, 7(1):1-22, 1964.
- Li, M. and Vitányi, P. *An Introduction to Kolmogorov Complexity and Its
  Applications*. Springer, 2008.
- Grünwald, P. *The Minimum Description Length Principle*. MIT Press, 2007.

## Open Questions

- Can the claim that typed logical language is near-Kolmogorov-optimal for
  inferential content be made more precise?
- Does MDL provide a principled way to choose between different typed logical
  languages (different role inventories, different type hierarchies)?
- Is there a formal relationship between the MDL of a knowledge base and the
  convergence rate of belief propagation over its factor graph?