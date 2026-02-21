# The Formal Verification Landscape

## The Core Problem

Software is the most complex artifact humans build. A modern system has
millions of lines of code, thousands of interacting components, and
astronomical numbers of possible states. How do you know it's correct?

There are exactly four approaches, and they form a hierarchy of
increasing rigor and increasing cost.

## Level 0: Testing

Run the program with example inputs, check the outputs.

This is what most of the industry does. Unit tests, integration tests,
end-to-end tests. The fundamental limitation was stated by Dijkstra
(1970): "Testing shows the presence of bugs, never their absence."

Testing checks specific paths through the program. A program with n
boolean variables has 2^n possible states. Testing checks a tiny
fraction. The bugs live in the states you didn't test.

## Level 1: Static Analysis

Examine the program without running it. Look for patterns that indicate
bugs: null pointer dereferences, buffer overflows, type mismatches,
data races.

This is what compilers and linters do. Rust's borrow checker is the
most aggressive mainstream static analysis — it proves memory safety
at compile time, eliminating entire classes of bugs that C and C++
programs suffer from.

Static analysis is sound (no false negatives) for the properties it
checks, but it only checks structural properties — types, ownership,
lifetimes. It doesn't know whether your algorithm is correct.

Key tools: Rust's borrow checker, TypeScript's type system, ESLint,
Clippy, Facebook Infer, Coverity.

## Level 2: Model Checking

Exhaustively explore all reachable states of a system and verify that
a property holds in every state.

This is the approach closest to what the QBBN does. You build a formal
model of the system — its states, transitions, and invariants — and
the model checker explores every possible execution path.

### TLA+ (Lamport, 1999)

The most important model checking language for software engineers.
Leslie Lamport (inventor of LaTeX, Paxos, and Lamport clocks) designed
TLA+ specifically for reasoning about concurrent and distributed systems.

A TLA+ specification declares:
- **State variables** — the things that change
- **Initial state** — where the system starts
- **Transitions** — how states change (Next-state relations)
- **Invariants** — properties that must always hold
- **Temporal properties** — things about sequences of states

Amazon Web Services has used TLA+ extensively. In a 2014 paper,
Newcombe et al. reported finding subtle bugs in DynamoDB, S3, and
other core services that testing had missed — including bugs that
would have caused data loss in production.

The connection to Horn clauses: a TLA+ transition
`State1 ∧ Condition → State2` is structurally a Horn clause.
The invariant check is forward inference — if these conditions hold,
does the invariant still hold in the next state?

### Alloy (Jackson, 2002)

A lightweight model checker based on relational logic. You declare
entities (signatures), relations between them, and constraints
(facts). The Alloy Analyzer searches for counterexamples within a
bounded scope.

Alloy's relational model is remarkably close to the QBBN's typed
predicates. Signatures are types. Relations are predicates. Facts
are ground assertions. Constraints are rules. The analyzer's
bounded search is analogous to the QBBN's finite grounding.

### SPIN (Holzmann, 1997)

A model checker for concurrent systems, based on Promela (Process
Meta Language). Used extensively at Bell Labs and NASA/JPL for
verifying communication protocols and flight software.

## Level 3: Theorem Proving

Construct a mathematical proof that the program satisfies its
specification for ALL possible inputs, not just those within a
bounded scope.

This is the gold standard. If you have a proof, you have certainty.
The cost is enormous — often more effort to prove correctness than
to write the program.

### Hoare Logic (1969)

The foundation. C.A.R. Hoare proposed annotating programs with
preconditions and postconditions:

    {P} C {Q}

"If precondition P holds before executing command C, then
postcondition Q holds after."

This is a Horn clause:

    always: P(state: before) & executes(command: C) -> Q(state: after)

Hoare's key rules:
- **Sequence**: {P} C1 {R}, {R} C2 {Q} ⊢ {P} C1;C2 {Q}
  (chaining — transitivity through Horn clauses)
- **Conditional**: {P∧B} C1 {Q}, {P∧¬B} C2 {Q} ⊢ {P} if B then C1 else C2 {Q}
  (branching — two rules with negated condition, uses NEG factor)
- **Loop**: {P∧B} C {P} ⊢ {P} while B do C {P∧¬B}
  (invariant maintenance — the loop doesn't change the invariant)

Every one of Hoare's rules maps to a pattern in the QBBN's factor graph.

### Design by Contract (Meyer, 1986)

Bertrand Meyer embedded Hoare logic into the Eiffel programming language.
Every function has:
- **require**: precondition (must be true when the function is called)
- **ensure**: postcondition (guaranteed true when the function returns)
- **invariant**: class invariant (true before and after every method)

This is practical Hoare logic — the contracts are checked at runtime
rather than proved statically, but they make the specification explicit
and machine-readable.

Modern descendants: Rust's type system (contracts via types), Python's
`assert` statements (informal contracts), Java's JML, C's ACSL,
Ada/SPARK (the most mature contract-based verification system in
production use, used in avionics and rail signaling).

### Interactive Theorem Provers

Tools where a human guides the construction of a proof, and the
machine checks that every step is valid.

**Coq (1984, INRIA)** — Based on the Calculus of Inductive Constructions.
Used to build CompCert, a verified C compiler that is mathematically
proven to compile correctly. Every optimization pass is proven to
preserve program semantics.

**Isabelle/HOL (1986, Cambridge/Munich)** — Used to verify seL4, a
microkernel OS that is mathematically proven to be free of buffer
overflows, null pointer dereferences, memory leaks, and other common
vulnerabilities. seL4 is used in military helicopters and autonomous
vehicles.

**Lean (2013, Microsoft Research)** — The newest major prover, designed
to be both a theorem prover and a programming language. Used to
formalize large parts of mathematics (Mathlib). Growing adoption in
software verification.

**Agda and Idris** — Dependently typed programming languages where the
type system is expressive enough that well-typed programs are correct
by construction. The type checker is the theorem prover.

### The Cost

The seL4 proof took approximately 20 person-years for ~10,000 lines of
C code. CompCert's verification effort is comparable. This is why
theorem proving is reserved for the highest-stakes software — avionics,
medical devices, cryptographic implementations, operating system kernels.

## The Annotation Bottleneck

Every level above testing requires a human to write something formal:
types (Level 1), models (Level 2), or proofs (Level 3). This is the
same annotation bottleneck that killed formal NLP.

The amount of formal specification required scales with the complexity
of the system. For TLA+, Amazon reported that writing the specification
often took as long as writing the code. For theorem proving, the proof
is typically 5-10x longer than the code it verifies.

This is where LLMs enter the picture. See
[The Verification Bottleneck and LLMs](verification_bottleneck.md).