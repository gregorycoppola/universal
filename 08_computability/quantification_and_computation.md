
# Quantification and Computation: Why Universal Is Enough

## The Question

Horn clauses use only universal quantification. Every variable in a Horn clause
is implicitly universally quantified. Yet Horn clauses are Turing complete. How
does a system with no existential quantification achieve full computational
power?

## Universal Quantification as Template

A universally quantified Horn clause is a *rule template*:

    always [t: nat, p: nat]:
        State(step: t, state: q1)
        & Head(step: t, position: p)
        & Tape(step: t, position: p, symbol: s1)
        -> State(step: t+1, state: q2)
           & Head(step: t+1, position: p+1)
           & Tape(step: t+1, position: p, symbol: s2)

The `always [t, p]` says: this rule holds for every time step and every
position. It is a schema — an infinite family of ground rules, one for each
(t, p) pair.

## Universal Instantiation as Computation

The computational work happens through **∀-Elimination** (universal
instantiation). Each time you plug in a specific value — t=0, t=1, t=2 — you
get one step of the computation. The rule fires, new facts are derived, and
those facts become premises for the next instantiation.

This is exactly forward chaining: ground the rule at t=0, derive the
configuration at t=1, ground the rule at t=1, derive t=2, and so on. The
chain of instantiations *is* the computation.

## The Absence of Existential Quantification

The striking fact: existential quantification is never needed. You never
assert "there exists a time step t at which the machine halts." Instead, you
construct the witness step by step through forward chaining.

- At t=0: the initial configuration is given (ground facts).
- At t=1: derived by instantiating the transition rule at t=0.
- At t=2: derived by instantiating at t=1.
- At t=k: if q_halt appears, the machine has halted.

The existential claim — "there exists a halting time" — is *witnessed* by the
forward chain itself, never asserted as a logical statement. The proof
constructs the witness rather than reasoning about its existence.

This is why Prawitz's complex rules (∃-Elimination, ∨-Elimination) are not
needed for computation. Those rules handle reasoning *about* existence and
disjunction — "given that some witness exists, conclude C" or "in either case,
conclude C." But forward chaining through Horn clauses never reasons about
existence. It produces existence directly.

## The Connection to Constructive Mathematics

This observation connects to a deep theme in logic. The constructive
(intuitionist) tradition distinguishes between:

- **Witnessing** an existential: producing an actual value that satisfies ∃x.P(x).
- **Asserting** an existential: claiming ∃x.P(x) without producing the witness.

Horn clause computation is radically constructive — it only ever witnesses, never
merely asserts. Every derived fact is a concrete ground instance. There are no
hypothetical arguments, no case splits, no reasoning by contradiction.

The Curry-Howard correspondence tells us that constructive proofs correspond to
programs. Horn clause forward chaining is a particularly restricted form of
constructive proof — one that never even uses →-Introduction (conditional proof).
It only uses the elimination rules: instantiate, combine, and fire.

## What Makes It Turing Complete

Given that Horn clauses use only universal quantification and only simple
elimination rules, what gives them Turing completeness?

**Unbounded grounding.** The variable t ranges over the natural numbers — an
infinite domain. Each forward-chaining step creates new ground instances (t=1,
t=2, t=3, ...) with no a priori bound. This unbounded instantiation is the
sole source of computational power. The rules are finite and fixed. The domain
of instantiation is what determines expressiveness.

## What Makes the QBBN Decidable

The QBBN restricts to **finite grounding**: variables range over a declared,
finite set of entities. The forward chain is bounded — there are only finitely
many ground instances to derive, so the process always terminates.

| System | Quantification | Grounding | Power |
|---|---|---|---|
| Full FOL | ∀ and ∃ | Unbounded | r.e. (Turing complete) |
| Horn clauses (Prolog) | ∀ only | Unbounded | r.e. (Turing complete) |
| QBBN / Datalog | ∀ only | Finite | P (decidable) |

The top two rows have the same computational power. Existential quantification
adds *logical* expressiveness (you can state more theorems) but not
*computational* expressiveness (you cannot compute more functions). The
transition from Turing complete to decidable happens not by restricting which
quantifiers you use, but by restricting the domain over which you instantiate.

## Summary

1. Horn clauses use only universal quantification.
2. Computation happens through universal instantiation — grounding rules at
   specific values and chaining forward.
3. Existential claims are witnessed by the forward chain, never asserted.
4. Turing completeness comes from unbounded grounding, not from the richness
   of quantifiers or inference rules.
5. The QBBN achieves decidability by restricting to finite grounding — the
   Datalog boundary.

## Key Works

- Prawitz, D. *Natural Deduction*. 1965.
- Kowalski, R.A. "Predicate Logic as Programming Language." 1974.
- Tärnlund, S-Å. "Horn Clause Computability." BIT, 1977.
- Dummett, M. *Elements of Intuitionism*. 1977. (Constructive mathematics.)
- Sørensen, M.H. and Urzyczyn, P. *Lectures on the Curry-Howard Isomorphism*.
  2006.