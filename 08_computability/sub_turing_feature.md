# Why Sub-Turing Is a Feature

## The Problem with Turing-Complete Verifiers

A verifier must answer: "Is this conclusion justified by this evidence and
these rules?" If the verifier is Turing complete, this question is undecidable.
The verifier might run forever without producing an answer. And you cannot, in
general, determine whether it will ever finish — that is the halting problem.

A verifier that might not halt is not a verifier. It is a hope.

## The Infinite Regress

If your verifier is Turing complete, you need a meta-verifier to check that the
verifier will terminate. But if the meta-verifier is also Turing complete, you
need a meta-meta-verifier. This is an infinite regress with no foundation.

The only way to ground the regress is to have a verifier that provably
terminates — one whose halting is guaranteed by its design, not by an external
check. This requires the verifier to be sub-Turing.

The QBBN is sub-Turing by design:
- Finite grounding: only declared entities are substituted
- No function symbols: no new terms are generated
- Forward fragment: no unbounded search
- Belief propagation: fixed number of iterations with convergence check

These properties are statically verifiable. You do not need to run the system
to know it will terminate. The termination guarantee is structural, not
empirical.

## The Analogy to Type Systems

In programming languages, a type system is a static verifier that checks
properties of programs without running them. Type systems are deliberately
sub-Turing — if type checking were undecidable, the compiler might loop forever
on valid programs. Languages like Haskell, Rust, and Lean have carefully
designed type systems that are expressive enough to catch real bugs but
restricted enough to always terminate.

The QBBN's finite grounding plays the same role as a type system's termination
guarantee. It restricts expressiveness just enough to ensure that verification
always completes.

## What You Give Up

The QBBN cannot reason about infinite domains (natural numbers, real numbers,
infinite sets). It cannot perform mathematical induction. It cannot prove
theorems that require existential witnesses from an infinite domain.

These are real limitations — but they are limitations of natural language
reasoning, not just of the QBBN. When a human reads "All men are mortal" and
"Socrates is a man," they reason over a finite domain (the mentioned entities).
They do not perform induction over the natural numbers. They do not search
infinite sets for witnesses. Natural language reasoning is inherently
finite-domain reasoning, and the QBBN captures exactly that.

## The Trust Argument

The ultimate purpose of verification is trust. You trust a verified conclusion
because:

1. The knowledge base is explicit and inspectable
2. The inference rules are defined and finite
3. The derivation traces from evidence to conclusion
4. **The verification process provably terminates**

Without (4), you cannot trust the verifier. With (4), you can.

Sub-Turing is not a limitation. It is the price of trust. And for natural
language reasoning over finite domains, it costs nothing in expressiveness.

## Key Works

- Turing, A.M. "On Computable Numbers." 1936. (The halting problem.)
- Pierce, B.C. *Types and Programming Languages*. MIT Press, 2002. (Type
  systems as decidable verifiers.)
- Barendregt, H. "Lambda Calculi with Types." *Handbook of Logic in Computer
  Science*, 1992.