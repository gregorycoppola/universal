# Computability and the Forward Fragment

## Why This Section Exists

The QBBN's design — universally quantified Horn clauses with finite grounding
and belief propagation — sits at a very specific point in the computability
landscape. Understanding that point explains why the system works, why it
terminates, why it is expressive enough for natural language, and why going
further would break verification.

This section maps the QBBN onto the classical results of computability theory
and connects them to Prawitz's proof-theoretic classification.

## Documents

1. [FOL and Turing Completeness](fol_turing_completeness.md) — The
   bidirectional equivalence: FOL can simulate Turing machines, Turing machines
   can implement FOL provers. They are the same computational object.

2. [The Turing Machine Encoding](turing_encoding.md) — The explicit
   construction: how to encode a Turing machine's execution trace as
   universally quantified Horn clauses, and why only modus ponens, conjunction,
   and universal instantiation are needed.

3. [Prawitz's Rules and Computability](prawitz_computability.md) — The novel
   connection: Prawitz's three simple elimination rules with unbounded grounding
   are Turing complete. This is the minimal Turing-complete fragment of natural
   deduction.

4. [The Datalog Boundary](datalog_boundary.md) — Finite grounding makes Horn
   clauses decidable (Datalog = P-complete). The QBBN lives here. This is the
   design choice that makes verification terminate.

5. [The Complexity Landscape](complexity_landscape.md) — Where different
   logical fragments sit: propositional (coNP), Datalog (P), Horn clauses with
   function symbols (r.e.), full FOL (r.e.), SOL (beyond r.e.). The QBBN's
   position and why it is the sweet spot.

6. [Why Sub-Turing Is a Feature](sub_turing_feature.md) — A Turing-complete
   verifier could run forever. Verification of verification would be
   undecidable. The QBBN guarantees termination precisely because it stays
   below the Turing boundary. You cannot trust a verifier that might not halt.

## The Key Insight

The forward fragment of natural deduction is the **maximum expressiveness
consistent with decidable verification**. Go further (add function symbols,
existential search, proof by contradiction) and you gain expressiveness but lose
the guarantee that verification terminates. Stay here (modus ponens,
conjunction, universal instantiation over finite domains) and verification
always terminates in polynomial time.

The sufficiency claim from the QBBN paper — that these three tiers handle all
of natural language semantics — means that natural language reasoning lives
below the Turing boundary. You do not need Turing completeness to reason about
the things humans reason about in language. This is a strong empirical claim,
and if true, it explains why the QBBN works.