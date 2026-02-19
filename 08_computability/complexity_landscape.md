# The Complexity Landscape

## Where Everything Sits

The following table maps logical fragments to their computational complexity,
showing where the QBBN sits in the landscape:

| Fragment | Logic | Inference | Complexity |
|---|---|---|---|
| Propositional logic | No quantifiers, finite variables | SAT / validity | coNP-complete (validity), NP-complete (SAT) |
| Horn SAT | Propositional Horn clauses | Unit propagation | P (linear time) |
| Datalog | Horn clauses, finite domain | Bottom-up evaluation | P-complete |
| **QBBN** | **Weighted Horn clauses + NEG, finite domain** | **Belief propagation** | **P (empirically fast)** |
| Description logics (ALC) | Restricted quantification | Tableau | EXPTIME |
| Prolog | Horn clauses + function symbols | SLD resolution | r.e. (Turing complete) |
| Full FOL | All connectives, all quantifiers | Any complete prover | r.e. (undecidable) |
| SOL (second-order) | Quantification over predicates | — | Beyond r.e. |

## Reading the Table

**Below P**: Horn SAT is solvable in linear time by unit propagation. This is
the propositional fragment of the QBBN — no variables, no grounding, just fire
rules.

**At P**: Datalog and the QBBN live here. Polynomial time. All queries
terminate. This is the sweet spot for verification.

**At NP/coNP**: Full propositional logic (SAT). Adding disjunction to Horn
clauses jumps from P to NP. This is the cost of Prawitz's complex rules at
the propositional level.

**At EXPTIME**: Description logics like ALC, which add restricted forms of
existential quantification and disjunction. Still decidable, but exponentially
harder.

**At r.e. (undecidable)**: Prolog and full FOL. Turing complete. Semi-decidable
only. No termination guarantee.

## The QBBN's Position

The QBBN sits at the P level — the maximum complexity at which verification is
both decidable and efficient. This is not an accident. It is a consequence of
three design choices:

1. **Horn clauses only** (no disjunction in rule heads) — avoids NP
2. **Finite grounding** (declared entities, no function symbols) — avoids r.e.
3. **Forward fragment** (simple elimination rules only) — avoids exponential
   search

Each restriction rules out a complexity jump. Together they place the QBBN at
exactly P — powerful enough for natural language reasoning, tractable enough for
reliable verification.

## The Gap Between P and NP

The gap between the QBBN (P) and full propositional reasoning (NP) corresponds
to Prawitz's simple/complex distinction. Simple rules (forward chaining through
Horn clauses) give P. Complex rules (case analysis via disjunction) give NP.

If P ≠ NP — as almost all computer scientists believe — then there are reasoning
tasks expressible in full propositional logic that cannot be efficiently solved
by forward chaining through Horn clauses. These tasks involve disjunctive
reasoning: "either A or B is true, and we must consider both cases."

The QBBN paper's sufficiency claim implies that natural language reasoning
rarely requires disjunctive case analysis. When "either A or B" appears in
natural language, it is typically resolvable by evidence (one disjunct is true
and the other is not), which the noisy-OR factor handles within P. True
disjunctive reasoning — where both cases must be explored exhaustively — appears
more in mathematical proofs than in natural language inference.

## Key Works

- Cook, S.A. "The Complexity of Theorem-Proving Procedures." STOC, 1971.
- Dowling, W.F. and Gallier, J.H. "Linear-Time Algorithms for Testing the
  Satisfiability of Propositional Horn Formulae." *J. Logic Programming*,
  1:267-284, 1984.
- Immerman, N. *Descriptive Complexity*. Springer, 1999.
- Papadimitriou, C.H. *Computational Complexity*. Addison-Wesley, 1994.