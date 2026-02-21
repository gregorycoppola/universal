# The Verification Bottleneck and LLMs

## The Pattern

The history of formal verification mirrors the history of formal NLP:

| | Formal NLP | Formal Verification |
|---|---|---|
| The representation | Typed predicates, Horn clauses | Pre/postconditions, invariants, models |
| The bottleneck | Linguist-hours for annotation | Engineer-hours for specification |
| The scaling problem | Linear with human effort | Linear with human effort |
| The statistical revolution | HMMs, deep learning | Fuzzing, random testing |
| What was lost | Formal guarantees | Formal guarantees |

In both cases, the formal approach was sound but didn't scale.
In both cases, the statistical approach scaled but lost guarantees.
In both cases, LLMs change the equation.

## LLMs as Specification Generators

Just as LLMs can serve as annotators for natural language — producing
candidate logical forms that a grammar and inference engine verify —
LLMs can serve as specification generators for software.

Given a function, an LLM can propose:
- **Preconditions**: what must be true of the inputs
- **Postconditions**: what is guaranteed about the outputs
- **Invariants**: what properties are maintained
- **Dependencies**: what other components are required
- **Failure modes**: what can go wrong and what happens

These proposals are imperfect — LLMs hallucinate specifications just
as they hallucinate logical forms. But they don't need to be perfect.
They need to be good enough for a formal checker to verify.

## The Architecture

The pipeline is identical to natural language:

    LLM generates specification
    → Formal language compiles it (type checking)
    → Inference engine verifies it (model checking)
    → Violations fed back to LLM for repair

For natural language:

    LLM preprocesses → Grammar parses → QBBN infers

For software verification:

    LLM proposes spec → Type checker compiles → Model checker verifies

Same pattern. Same bottleneck. Same solution.

## The QBBN's Position

The QBBN sits at Level 2 — model checking. It's not a theorem prover
(Level 3) — it doesn't construct proofs over unbounded domains. It's
more than static analysis (Level 1) — it reasons about consequences,
not just structural properties.

Specifically, the QBBN provides:
- **Finite grounding** (like Alloy's bounded scope) — enumerate all
  entities of each type, ground all rules, check all reachable states
- **Forward and backward inference** (like TLA+'s invariant checking) —
  modus ponens for "if this then that," modus tollens for "if not that
  then not this"
- **Probabilistic reasoning** (unique to the QBBN) — soft dependencies,
  unreliable components, degraded-but-functional states

The probabilistic layer is what distinguishes the QBBN from existing
model checkers. TLA+ and Alloy deal in certainties — a property holds
or it doesn't. Real systems have probabilistic failures. The cache
usually works. The network sometimes drops packets. The database
rarely corrupts data. The QBBN's modal quantifiers (always, usually,
sometimes, rarely) capture exactly these distinctions.

## Kowalski's Dream, Realized

Kowalski (1974) dreamed that programs could be written as logic.
That dream failed because the search strategy didn't scale and
because writing logic was as hard as writing code.

LLMs solve the second problem. The QBBN solves the first (for the
forward fragment — DAG-shaped specifications without unbounded loops).

The result is not "programs as logic" but something more practical:
"specifications as logic, with automatic generation and verification."
The LLM writes the code AND proposes the spec. The QBBN verifies
the spec. The human reviews the violations.

This is Kowalski's Algorithm = Logic + Control, reinterpreted:
- **Logic**: the QBBN specification (what should be true)
- **Control**: the LLM generation (how to build it)
- **Verification**: the QBBN inference (is the logic satisfied?)