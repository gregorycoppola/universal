# Formal Verification and the Need for Formal Language

## The Central Problem

When an LLM produces a chain of reasoning — "All men are mortal. Socrates is a
man. Therefore Socrates is mortal" — there is no way to check whether the
reasoning is valid by examining the LLM. The reasoning happened inside a neural
network. It is not written down. It is not inspectable. It is not checkable.

This is not a new problem. It is the oldest problem in the philosophy of
knowledge: **how do you distinguish valid reasoning from plausible nonsense?**

The answer, known since Euclid, is: **write the proof down in a formal language
and check each step.**

## What Formal Verification Is

Formal verification is the practice of proving that a system (a program, a
circuit, a protocol, a mathematical theorem) satisfies a specification, using a
proof that can be mechanically checked.

The key components:

1. A **formal language** in which claims can be precisely expressed
2. A **proof system** in which derivations proceed by explicit rules
3. A **checker** that mechanically verifies each step of the proof

If the checker accepts the proof, the claim is verified. If it rejects the
proof, there is an error. If no proof can be constructed, the claim is
unverified. There is no fourth option. There is no "the claim feels right." There
is no "the claim is probably correct." There is only: proved, disproved, or
unknown.

## The Curry-Howard Correspondence

One of the deepest results in the foundations of mathematics and computer science
is the **Curry-Howard correspondence** (Curry, 1934; Howard, 1969): there is a
direct structural isomorphism between proofs and programs.

- A **proposition** corresponds to a **type**
- A **proof** corresponds to a **program** of that type
- **Proof checking** corresponds to **type checking**

If you can write a program that type-checks, you have a proof. If you cannot
write such a program, you do not have a proof. The compiler is the proof checker.

This correspondence is not a metaphor. It is a theorem. It is the foundation of
proof assistants like Lean, Coq, and Agda, where writing a proof literally means
writing a program in a typed language, and verifying the proof literally means
compiling the program.

The QBBN's typed logical language sits in this tradition. Propositions have types
(entity, sentential, predicate). Predicates have typed roles. Rules have typed
variables. The grammar performs type-driven dispatch — which is type checking.
The inference engine performs belief propagation — which is proof execution. The
system does not have a formal Curry-Howard correspondence (belief propagation is
not lambda calculus), but it shares the essential property: **the types constrain
the reasoning, and the constraints are mechanically checkable.**

## Formal Verification in Practice

Formal verification has been applied successfully in several domains:

### Mathematics

The **four-color theorem** (Appel and Haken, 1976) was the first major theorem
proved with computer assistance. The proof was controversial because it relied on
checking thousands of cases by computer — but the checking was formal and
reproducible.

The **Kepler conjecture** (Hales et al., 2017) was formally verified in the
Flyspeck project using the HOL Light and Isabelle proof assistants, after the
original 1998 proof was too complex for human referees to verify with confidence.

More recently, the **Liquid Tensor Experiment** (Scholze, 2022) used Lean to
formally verify a result in condensed mathematics, demonstrating that proof
assistants can handle cutting-edge research mathematics.

### Software

**CompCert** (Leroy, 2009) is a formally verified C compiler — every compilation
step is proved correct in Coq. If CompCert compiles your program, the compiled
code provably implements the source code.

**seL4** (Klein et al., 2009) is a formally verified operating system
microkernel. The implementation is proved to satisfy its specification —
including memory safety, information flow control, and functional correctness.

### Hardware

Intel and AMD use formal verification to check processor designs. The Pentium
FDIV bug (1994) — which cost Intel $475 million — was a motivating example: a
hardware error that testing missed but formal verification would have caught.

## Why Natural Language Needs Formal Verification

In all of these examples, formal verification works because the domain already
has a formal language:

- Mathematics has formal logic and type theory
- Software has programming languages and type systems
- Hardware has HDLs (hardware description languages) and temporal logic

Natural language does not have a standard formal language. This is the gap. When
an LLM reasons in natural language, there is no formal language in which the
reasoning is expressed, no proof system by which the steps can be checked, and no
checker that can verify the result.

The QBBN pipeline fills this gap:

| Formal Verification Component | QBBN Pipeline |
|---|---|
| Formal language | Typed logical language (predicates, roles, types) |
| Specification | Knowledge base (facts and rules) |
| Proof | Factor graph derivation (belief propagation trace) |
| Checker | Inference engine (convergence + posterior) |

The typed logical language is the formal language for natural language reasoning.
The knowledge base is the specification — it defines what is known. The factor
graph derivation is the proof — it traces from evidence through rules to
conclusion. The inference engine is the checker — it verifies that the derivation
is valid and computes the posterior probability.

## Why Translation Is Necessary

The critical question: **why can't we just verify reasoning directly in natural
language?**

Because natural language is:

1. **Ambiguous**: "I saw the man with the telescope" has two readings. A formal
   language has exactly one reading per expression.

2. **Implicit**: "All men are mortal" leaves the quantifier scope, variable
   binding, and logical form implicit. A formal language makes all of these
   explicit.

3. **Inconsistent**: Natural language tolerates contradictions, vagueness, and
   context-dependence. A formal language enforces consistency by construction.

4. **Untyped**: In natural language, "Socrates" and "justice" are both nouns,
   but one is an entity and one is an abstract property. A typed language
   distinguishes them and prevents category errors.

5. **Non-compositional in practice**: The meaning of "kick the bucket" is not
   the meaning of "kick" plus the meaning of "the bucket." Formal languages are
   compositional by construction.

You cannot check a proof written in natural language because you cannot parse it
unambiguously, you cannot identify the inference steps, and you cannot verify
that each step follows from the previous by a recognized rule. The translation
from natural language to formal language is not an optional nicety. It is a
**prerequisite for verification**.

This is the same reason mathematicians write proofs in formal notation rather
than English. It is the same reason programmers write code in programming
languages rather than natural language specifications. It is the same reason
hardware designers use HDLs rather than English descriptions. Formal language is
the price of verification. There is no shortcut.

## The LLM's Role

The LLM cannot verify. But it can **translate**. This is the key insight of the
QBBN pipeline:

1. The LLM reads natural language and produces candidate formal representations
2. The grammar compiles these to typed logical forms (catching structural errors)
3. The QBBN reasons over the logical forms (performing verified inference)
4. If the reasoning fails, the error is fed back to the LLM for correction

The LLM is the **translator** from informal to formal. The QBBN is the
**verifier** of the formal representation. Neither can do the other's job:

- The LLM cannot verify because it has no formal proof system
- The QBBN cannot translate because it has no understanding of natural language

Together, they constitute a complete system: translation + verification =
verified reasoning from natural language input.

## The Analogy to Proof Assistants

The architecture mirrors the modern workflow with proof assistants like Lean:

| Lean Workflow | QBBN Workflow |
|---|---|
| Mathematician has an informal proof idea | LLM produces natural language reasoning |
| Mathematician translates to Lean's formal language | Grammar + LLM translate to typed logical forms |
| Lean's type checker verifies each step | QBBN's belief propagation verifies inference |
| If verification fails, mathematician revises | If verification fails, LLM revises |
| Verified proof is trustworthy | Verified conclusion is trustworthy |

In the Lean world, the human mathematician is the translator and Lean is the
verifier. In the QBBN world, the LLM is the translator and the QBBN is the
verifier. The human mathematician is being replaced by the LLM — which is
exactly the bitter lesson in action, applied to formal verification.

## From Verification to Trust

The ultimate goal is **trust**. Not trust in the LLM (which hallucinates), not
trust in the formal system (which is only as good as its knowledge base), but
trust in the **pipeline**: if the input is correct and the inference is verified,
the output is correct.

This is the same kind of trust we place in:

- A compiler: if the source code is correct and the compiler is verified
  (CompCert), the binary is correct
- A proof assistant: if the axioms are sound and the proof checks, the theorem
  is true
- A calculator: if the input is right and the arithmetic is correct, the answer
  is right

The QBBN aspires to the same status for natural language reasoning: if the
knowledge base is correct and the inference is verified, the conclusion is
correct. The formal language is what makes this possible. Without it, there is
no verification, and without verification, there is no trust — only hope that the
LLM got it right.

## Key Works

- Curry, H.B. "Functionality in Combinatory Logic." *Proceedings of the National
  Academy of Sciences*, 20(11):584-590, 1934.
- Howard, W.A. "The Formulae-as-Types Notion of Construction." 1969. Published
  in *To H.B. Curry: Essays on Combinatory Logic*, 1980.
- Appel, K. and Haken, W. "Every Planar Map is Four Colorable." *Bulletin of the
  AMS*, 82(5):711-712, 1976.
- Leroy, X. "Formal Verification of a Realistic Compiler." *Communications of the
  ACM*, 52(7):107-115, 2009.
- Klein, G. et al. "seL4: Formal Verification of an OS Kernel." SOSP, 2009.
- Hales, T. et al. "A Formal Proof of the Kepler Conjecture." *Forum of
  Mathematics, Pi*, 5, 2017.
- De Moura, L. and Ullrich, S. "The Lean 4 Theorem Prover and Programming
  Language." CADE, 2021.
- The Mathlib Community. "The Lean Mathematical Library." CPP, 2020.

## Open Questions

- Can the QBBN's inference be given a formal Curry-Howard interpretation, where
  factor graph derivations correspond to programs in a typed language?
- Is belief propagation "verification" in the same strong sense as type checking
  in Lean, or is it a weaker form of assurance?
- Can the verify-and-revise loop (LLM generates, QBBN verifies, errors fed back)
  converge to correct representations, or can it get stuck in cycles?
- What is the right formal relationship between the QBBN's probabilistic
  verification (P > 0.5) and the deterministic verification (proof checks or it
  doesn't) used in proof assistants?
- Could the QBBN be implemented *inside* a proof assistant like Lean, giving it
  the strongest possible verification guarantees?