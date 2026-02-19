# The Datalog Boundary

## The Key Distinction

The difference between decidable and undecidable Horn clause reasoning is
exactly one thing: **whether grounding is finite or unbounded**.

| System | Rules | Grounding | Complexity |
|---|---|---|---|
| Datalog | Horn clauses, no function symbols | Finite | P-complete |
| Prolog | Horn clauses with function symbols | Unbounded | Turing complete (r.e.) |
| QBBN | Weighted Horn clauses, no function symbols | Finite (declared entities) | P (decidable) |

**Datalog** restricts to Horn clauses over a finite set of constants (the
"extensional database"). No function symbols are allowed, so no new terms can
be created during inference. The set of derivable ground facts is bounded by the
number of predicates times the number of tuples of constants — a finite,
computable quantity. Forward chaining (bottom-up evaluation) terminates in
polynomial time.

**Prolog** allows function symbols like successor(X), which generate an infinite
set of terms: 0, successor(0), successor(successor(0)), ... This means
grounding is unbounded, forward chaining may never terminate, and the system is
Turing complete.

**The QBBN** is Datalog-like: entities are declared explicitly (socrates : e,
jack : e, jill : e), and grounding substitutes only declared entities for
variables. No function symbols, no term generation, no infinite domains.
Verification always terminates.

## The Immerman-Vardi Theorem

Immerman (1986) and Vardi (1982) independently showed that over ordered finite
structures, the queries expressible in least fixed-point logic (which
corresponds to Datalog with stratified negation) are exactly the polynomial-time
computable queries. Datalog captures P.

This means the QBBN's forward fragment, with finite grounding, is exactly as
powerful as polynomial-time computation. It cannot solve NP-hard problems (unless
P = NP), but it can express any reasoning task that is solvable in polynomial
time.

## Why This Is the Right Boundary for Verification

A verifier must terminate. A verifier that might run forever is not a verifier —
it is a semi-decision procedure, and you can never be sure it won't loop.

Turing-complete systems (Prolog, full FOL) are semi-decision procedures: they
confirm valid conclusions but may loop on invalid ones. You cannot use them as
reliable verifiers because you cannot distinguish "still thinking" from "will
never finish."

Datalog-level systems (the QBBN) always terminate. Every query gets an answer
in bounded time. This is the maximum expressiveness consistent with reliable
verification.

The question is: is Datalog-level expressiveness sufficient for natural language
reasoning? The QBBN paper's evidence (44 inference tests, 33 parsing tests,
covering 22 reasoning categories) says yes. Natural language reasoning over
finite domains lives within P.

## The Role of Finite Domains in Natural Language

Natural language texts always involve a finite number of entities. A document
mentions specific people, places, things, events. The domain of discourse is
bounded by the text.

This is unlike mathematics, where reasoning over infinite domains (natural
numbers, real numbers, sets) is fundamental. Mathematical reasoning often
requires unbounded grounding — which is why mathematical theorem proving is
undecidable.

The QBBN exploits this difference. Natural language reasoning is about finite
worlds — and Datalog is exactly right for finite worlds.

## Key Works

- Ceri, S., Gottlob, G., and Tanca, L. *Logic Programming and Databases*.
  Springer, 1990.
- Immerman, N. "Relational Queries Computable in Polynomial Time." *Information
  and Control*, 68:86-104, 1986.
- Vardi, M.Y. "The Complexity of Relational Query Languages." STOC, 1982.
- Abiteboul, S., Hull, R., and Vianu, V. *Foundations of Databases*.
  Addison-Wesley, 1995.