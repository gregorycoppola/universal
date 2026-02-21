# Functions in the Universal Language

## The Question

The characteristica currently handles **truth values** — propositions that are true or false, with degrees of belief. But reasoning about the world requires **computed values** — numbers, strings, data structures. E = mc² is not a Horn clause. It's a function.

How do we extend the characteristica to handle functions without losing the properties that make it useful — decidability, tractability, verifiability?

## The Design Space

There are four approaches, each with different tradeoffs:

1. [Functions as Relations](relations.md) — Reify functions as predicates with output roles. Pure FOL, no new machinery. But enumeration-only — no computation.

2. [Function Symbols](symbols.md) — Allow terms like `multiply(m, c)` inside predicates. Standard FOL. But breaks the Datalog safety restriction and risks non-termination.

3. [Constraint Logic Programming](clp.md) — Keep Horn clauses but add a constraint domain with a built-in solver. The natural next step. Decidable if the constraint domain is decidable.

4. [Evaluation as Inference](eval.md) — Define computation rules as Horn clauses that reduce expressions step by step. Turing-complete but stays within the calculus. Essentially encoding an interpreter in FOL.

## The Tradeoff

| Approach | Expressiveness | Decidability | Stays in FOL | Computes |
|---|---|---|---|---|
| Relations | Low | Yes (Datalog) | Yes | No — lookup only |
| Function symbols | High | No (in general) | Yes | Yes — but may not terminate |
| CLP | Medium-High | Depends on domain | Extends FOL | Yes — via external solver |
| Eval as inference | Full (Turing-complete) | No | Yes | Yes — but may not terminate |

## Where We Are

The QBBN currently sits at **Relations** — the Datalog boundary. This is sufficient for propositional reasoning (who trusts whom, what follows from what). It is not sufficient for quantitative reasoning (E = mc², compound interest, sorting algorithms).

The natural next step is **CLP** — it preserves the Horn clause structure, keeps the calculus ratiocinator intact, and adds computation via domain-specific solvers. The logic programming tradition (Prolog → CLP(R) → CLP(FD) → CHR) has mapped this path thoroughly.

The question is not *whether* to extend to functions but *how much* to extend while preserving the properties that matter: verifiability, tractability, and human readability.