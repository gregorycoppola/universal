# Prawitz's Natural Deduction

## The Framework

Dag Prawitz's *Natural Deduction: A Proof-Theoretical Study* (1965) is the
theoretical foundation for the QBBN's inference engine. Prawitz systematized
Gentzen's (1934) natural deduction calculus, providing a complete treatment of
proof normalization and a hierarchy of logical systems from first-order through
second-order to modal logic.

Natural deduction is a proof system in which inference rules correspond to the
ways humans naturally reason — unlike resolution or sequent calculus, which are
designed for machine efficiency. Each logical connective has **introduction rules**
(how to prove something) and **elimination rules** (how to use something already
proved).

## The Rules That Matter

The QBBN implements what Prawitz calls the **simple elimination rules** — rules
where the conclusion follows directly from premises without hypothetical reasoning:

**Modus Ponens (→-Elimination)**:
Given `A` and `A → B`, conclude `B`.
Implemented by AND + OR factors with forward π messages.

**Modus Tollens (Contrapositive)**:
Given `¬B` and `A → B`, conclude `¬A`.
Implemented by NEG factors with backward λ messages. This is the key extension in
the 2026 paper.

**Conjunction Introduction/Elimination (∧-Intro/Elim)**:
Given `A` and `B`, conclude `A ∧ B` (and vice versa).
Implemented by AND factors.

**Universal Instantiation (∀-Elimination)**:
Given `∀x: P(x)` and entity `a`, conclude `P(a)`.
Implemented by grounding quantified rules over declared entities.

## Simple vs. Complex Rules

Prawitz distinguishes **simple** rules (conclusion follows directly) from **complex**
rules (requiring discharged assumptions or hypothetical reasoning):

- **∨-Elimination (case analysis)**: Given `A ∨ B`, assume `A` and derive `C`,
  assume `B` and derive `C`, conclude `C`. Requires exploring hypothetical worlds.
- **∃-Elimination (witness search)**: Given `∃x: P(x)`, assume `P(a)` for fresh `a`,
  derive `C`, conclude `C`. Requires inventing entities.
- **¬-Introduction (proof by contradiction)**: Assume `A`, derive contradiction,
  conclude `¬A`. Requires hypothetical reasoning.

The QBBN restricts itself to the simple rules. This is not a limitation — it is a
**design choice** that makes belief propagation tractable. The forward fragment
(simple rules only) is linear time. Adding complex rules introduces search:
∨-Elimination is polynomial, ∃-Elimination is NP-hard, and full first-order
theorem proving is undecidable.

## The Three Tiers

Prawitz's monograph covers three levels of logical expressiveness, each extending
the last:

**Tier 1: First-Order Logic (Chapters I-IV)**
Quantification over entities. `∀x: man(x) → mortal(x)`. This handles most
everyday reasoning: classification, causation, transitivity, spatial and temporal
relations.

**Tier 2: Propositional Arguments (Chapters V-VI)**
Propositions as arguments to predicates. `should(careful(mary))`. This handles
modality, propositional attitudes (believe, want, know), and reported speech.

**Tier 3: Second-Order Logic (Chapter V)**
Quantification over predicates and lambda abstraction. `∀P: P(x) → Q(x)`. This
handles definitions, compound predicates, and quantification over properties.

The QBBN paper argues these three tiers are **sufficient** for natural language
semantics: every sentence decomposes into entities, properties, relations,
quantification, embedded propositions, and compound predicates.

## The Boolean Decomposition

The original contribution of the QBBN is realizing Prawitz's rules as **factor
types** in a probabilistic graphical model:

| Prawitz Rule | Factor Type | Message Direction |
|---|---|---|
| ∧-Introduction | AND factor | Forward (π) |
| →-Elimination (modus ponens) | OR factor | Forward (π) |
| Contrapositive (modus tollens) | NEG factor | Backward (λ) |

This is, to our knowledge, new: encoding natural deduction rules as factors in a
belief propagation network.

## Key Works

- Gentzen, G. "Untersuchungen über das logische Schließen." *Mathematische
  Zeitschrift*, 39:176-210, 405-431, 1934.
- Prawitz, D. *Natural Deduction: A Proof-Theoretical Study*. Almqvist & Wiksell,
  1965.
- Troelstra, A.S. and Schwichtenberg, H. *Basic Proof Theory*. Cambridge University
  Press, 2000.

## Open Questions

- Can the complex rules (∨-Elimination, ∃-Elimination) be approximated by belief
  propagation with bounded search, or do they fundamentally require backtracking?
- Is the forward fragment truly sufficient for natural language, or are there
  common reasoning patterns (counterfactuals, hypotheticals) that require complex
  rules?
- How does Prawitz's normalization theorem (every proof can be reduced to a normal
  form) relate to convergence of belief propagation on the factor graph?