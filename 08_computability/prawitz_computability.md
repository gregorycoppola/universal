# Prawitz's Rules and Computability

## The Claim

Prawitz (1965) classified the inference rules of natural deduction into two
categories:

**Simple elimination rules**: The conclusion follows directly from the premises.
- ∀-Elimination (universal instantiation): from ∀x.P(x), derive P(a)
- →-Elimination (modus ponens): from A→B and A, derive B
- ∧-Elimination (conjunction): from A∧B, derive A (or B)
- ∧-Introduction: from A and B, derive A∧B

**Complex rules**: Require discharged assumptions or hypothetical reasoning.
- ∨-Elimination (case analysis): from A∨B, assuming A derive C, assuming B
  derive C, conclude C
- ∃-Elimination (witness): from ∃x.P(x), assuming P(a) for fresh a, derive C
- ¬-Elimination (proof by contradiction)
- →-Introduction (conditional proof)

The claim: **the simple elimination rules alone, with unbounded grounding, are
Turing complete.**

## The Argument

As shown in [The Turing Machine Encoding](turing_encoding.md), an arbitrary
Turing machine can be simulated using only:

1. ∀-Elimination — to instantiate transition rules at each time step
2. ∧-Intro/Elim — to check and construct conjunctive premises and conclusions
3. →-Elimination — to fire transition rules (modus ponens)

No complex rules are used. No disjunction, no existential quantification, no
negation, no proof by contradiction, no case analysis, no conditional proof.

The Turing completeness comes entirely from unbounded ∀-Elimination: the
variable t ranges over natural numbers, so new ground instances can be created
indefinitely.

## Why This Matters

This result connects two literatures that rarely interact:

**Proof theory** (Prawitz's tradition) classifies inference rules by their
logical structure — simple vs. complex, introduction vs. elimination. The
classification is motivated by proof-theoretic concerns (normalization,
harmony, the subformula property).

**Computability theory** (Turing's tradition) classifies problems by their
computational complexity — decidable vs. undecidable, P vs. NP vs. PSPACE.
The classification is motivated by resource bounds.

The connection: Prawitz's simple/complex distinction aligns exactly with the
decidability boundary when grounding is controlled.

| Fragment | Prawitz Rules | Grounding | Complexity |
|---|---|---|---|
| QBBN | Simple only | Finite | P (Datalog) |
| Horn logic programming | Simple only | Unbounded (function symbols) | r.e. (Turing complete) |
| Full natural deduction | Simple + complex | Finite | coNP (propositional) to undecidable (FOL) |

The simple elimination rules are exactly what is needed for computation. The
complex rules add logical expressiveness (disjunction, existence, negation) but
not computational power — Horn clauses are already Turing complete without them.

## The Novel Framing

The logic programming community knows that Horn clauses with function symbols
are Turing complete (Kowalski, 1974; Tärnlund, 1977). The proof theory
community knows Prawitz's simple/complex classification (Prawitz, 1965). But
the explicit statement — **Prawitz's simple elimination rules constitute the
minimal Turing-complete fragment of natural deduction** — connects these
results in a way that (to our knowledge) has not been stated before.

This framing highlights why the QBBN's restriction to the forward fragment is
principled rather than arbitrary. The forward fragment is not a random subset of
logic chosen for convenience. It is the computationally complete core — the
minimum set of inference rules that achieves Turing completeness. Everything
beyond it (complex rules) adds logical structure but not computational power.
And restricting grounding to finite domains (the Datalog restriction) is the
precise move that trades Turing completeness for decidability.

## The Sufficiency Question

If the simple elimination rules are already Turing complete (with unbounded
grounding) and P-complete (with finite grounding), do we ever need the complex
rules?

For **computation**: No. Anything computable can be computed with simple rules
alone.

For **natural language reasoning**: This is the QBBN paper's sufficiency claim.
The 44 inference tests and 33 parsing tests use only simple rules (plus NEG
factors for modus tollens, which extend but do not leave the forward fragment).
The claim is that natural language reasoning — predication, classification,
quantified rules, transitivity, modality, causation, spatial and temporal
reasoning — lives entirely within the forward fragment.

For **mathematics**: Sometimes no, sometimes yes. Mathematical proofs often
require case analysis (∨-Elimination) and existence proofs (∃-Elimination).
But constructive mathematics (the intuitionist tradition) restricts to
methods that are computationally interpretable — and constructive proofs
correspond to programs (Curry-Howard). The QBBN's forward fragment is more
restricted than constructive logic, but for the domain of natural language
reasoning, the restriction appears to cost nothing.

## Key Works

- Prawitz, D. *Natural Deduction*. 1965. (The simple/complex classification.)
- Kowalski, R.A. "Predicate Logic as Programming Language." 1974. (Horn clauses
  as computation.)
- Tärnlund, S-Å. "Horn Clause Computability." BIT, 17:215-226, 1977. (Turing
  completeness of Horn clauses.)
- Immerman, N. "Relational Queries Computable in Polynomial Time." 1986.
  (Datalog captures P.)
- Vardi, M.Y. "The Complexity of Relational Query Languages." 1982.

## Open Questions

- Can the claim "Prawitz's simple elimination rules are the minimal
  Turing-complete fragment" be stated as a formal theorem with a precise proof?
- Is there a smaller set of rules that is still Turing complete? (Probably not —
  you need all three: instantiation to create new ground terms, conjunction to
  combine premises, modus ponens to fire rules.)
- What is the relationship between the QBBN's NEG factors (modus tollens) and
  the simple/complex boundary? NEG extends the forward fragment but does not
  add complex rules. Where exactly does it sit?