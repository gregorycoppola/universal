# Functions in the Universal Language

## The Question

The characteristica currently handles **truth values** — propositions that are true or false, with degrees of belief. But reasoning about the world requires **computed values** — numbers, strings, data structures. E = mc² is not a Horn clause. It's a function.

How do we extend the characteristica to handle functions without losing the properties that make it useful — decidability, tractability, verifiability?

## The Design Space

There are five approaches, each with different tradeoffs:

1. [Functions as Relations](relations.md) — Reify functions as predicates with output roles. Pure FOL, no new machinery. But enumeration-only — no computation.

2. [Function Symbols](symbols.md) — Allow terms like `multiply(m, c)` inside predicates. Standard FOL. But breaks the Datalog safety restriction and risks non-termination.

3. [Constraint Logic Programming](clp.md) — Keep Horn clauses but add a constraint domain with a built-in solver. Well-understood, decidable for decidable domains.

4. [Evaluation as Inference](eval.md) — Define computation rules as Horn clauses that reduce expressions step by step. Turing-complete but stays within the calculus.

5. [Typed Functions in the Lexicon](typed_functions.md) — **The recommended approach.** Extend the lexicon with `function` declarations that the interpreter calls instead of looking up. Minimal new machinery, full computation, decidable if functions terminate, proof trees preserved.

## The Tradeoff

| Approach | Computes | Decidable | New machinery | Proof trees |
|---|---|---|---|---|
| Relations | No | Yes | None | Yes |
| Function symbols | Yes | No | None | Yes |
| CLP | Yes | Depends | External solver | Two systems |
| Eval as inference | Yes | No | None | Yes (verbose) |
| **Typed functions** | **Yes** | **Yes (if total)** | **One lexicon type** | **Yes** |

## Where We Are

The QBBN currently sits at **Relations** — the Datalog boundary. The recommended next step is **Typed Functions** — extending the lexicon with function declarations and teaching the interpreter to call them. This preserves Horn clause structure, the calculus ratiocinator, proof trees, and decidability while adding arbitrary computation.

The path beyond that — CLP for constraint domains, eval-as-inference for theoretical completeness — is mapped by the logic programming tradition and available when needed.