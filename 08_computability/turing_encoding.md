# The Turing Machine Encoding in Horn Clauses

## The Construction

Given any Turing machine M with states Q, alphabet Σ, and transition function
δ, we encode its computation on input w as a set of universally quantified Horn
clauses. The encoding uses three predicates:

    predicate State {step: nat, state: q}
    predicate Head  {step: nat, position: nat}
    predicate Tape  {step: nat, position: nat, symbol: s}

The **initial configuration** is a set of ground facts:

    State(step: 0, state: q_start)
    Head(step: 0, position: 0)
    Tape(step: 0, position: 0, symbol: w₁)
    Tape(step: 0, position: 1, symbol: w₂)
    ...

Each **transition rule** of the Turing machine becomes a universally quantified
Horn clause. For a transition δ(q₁, s₁) = (q₂, s₂, R):

    always [t: nat, p: nat]:
        State(step: t, state: q₁)
        & Head(step: t, position: p)
        & Tape(step: t, position: p, symbol: s₁)
        -> State(step: t+1, state: q₂)
           & Head(step: t+1, position: p+1)
           & Tape(step: t+1, position: p, symbol: s₂)

**Frame axioms** state that tape cells not under the head remain unchanged:

    always [t: nat, p: nat, p2: nat, s: symbol]:
        Tape(step: t, position: p2, symbol: s)
        & Head(step: t, position: p)
        & (p != p2)
        -> Tape(step: t+1, position: p2, symbol: s)

The **query** is: does State(step: t, state: q_halt) become true for any t?

## What Inference Rules Are Used

The proof that the machine halts on input w proceeds by:

1. **Universal instantiation** (∀-Elimination): Ground the transition rules at
   t=0 with the actual tape contents.
2. **Conjunction** (∧-Introduction/Elimination): Check that all premises of the
   transition rule hold simultaneously.
3. **Modus ponens** (→-Elimination): Derive the consequences — the new state,
   head position, and tape contents at t=1.
4. Repeat at t=1, t=2, t=3, ... until q_halt appears.

That is all. No disjunction. No negation. No existential quantification. No
proof by contradiction. No case analysis. Just:

- ∀-Elimination (universal instantiation)
- ∧-Intro/Elim (conjunction)
- →-Elimination (modus ponens)

These are exactly **Prawitz's three simple elimination rules**.

## The Observation

The Turing machine encoding uses only the forward fragment of natural deduction.
The full power of FOL — existential quantifiers, negation, disjunction, proof
by contradiction — is not needed to achieve Turing completeness. Forward
chaining through Horn clauses is already enough.

What makes it Turing complete is not the richness of the inference rules but
the **unboundedness of the grounding**. The variable t ranges over natural
numbers — an infinite domain. At each step, new ground instances are created
(t=0, t=1, t=2, ...) and the chain extends. There is no a priori bound on how
many steps the machine will take before halting. This unbounded grounding is
what gives Horn clauses their computational power.

## The QBBN's Restriction

The QBBN restricts to **finite grounding**: variables range over a declared,
finite set of entities. This means the forward chaining always terminates — there
are only finitely many ground instances to derive. This is exactly the Datalog
restriction, and it is what keeps the QBBN decidable.

The price is that the QBBN cannot simulate an arbitrary Turing machine. The
benefit is that verification always terminates. For natural language reasoning —
where the domain of discourse is always finite (there are finitely many entities
in any text) — this restriction costs nothing in expressiveness.

## Key Works

- Turing, A.M. "On Computable Numbers." 1936. (The original machine model.)
- Kowalski, R.A. "Predicate Logic as Programming Language." IFIP, 1974. (Horn
  clauses as computation.)
- Enderton, H.B. *A Mathematical Introduction to Logic*. 2001. (The encoding
  construction.)