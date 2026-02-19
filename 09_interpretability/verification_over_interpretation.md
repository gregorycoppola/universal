# Verification Over Interpretation

## The Reframing

The interpretability research program asks: **"What is the AI thinking?"**

We propose a different question: **"Is the AI's conclusion correct?"**

The first question requires access to the AI's internal representations and a
mapping from those representations to human-understandable concepts. As argued
in [The Interpretability Problem](interpretability_problem.md), this mapping
may not exist in a faithful form.

The second question requires only three things:

1. The AI's conclusion is expressed in a formal language
2. The formal language has a defined proof system
3. The proof system has a mechanical checker

If these three conditions are met, the conclusion can be verified without any
understanding of how the AI arrived at it. The AI's internal process is a black
box. The output is checked by a transparent, deterministic, inspectable process.

## The Software Analogy

Software engineering solved this problem decades ago. Compilers are black boxes
— no human reads the compiled binary and "interprets" what the compiler was
"thinking." Instead:

- The source code is the formal specification
- The compiler produces output (compiled binary)
- Testing and formal verification check whether the output satisfies the spec
- If it does, the output is trusted. If not, it is rejected.

Nobody asks "what was GCC thinking when it compiled this function?" The question
is "does the compiled output produce the correct results?" The internal process
is irrelevant to trust.

The QBBN pipeline applies the same pattern to reasoning:

- The knowledge base is the formal specification
- The LLM produces a conclusion
- The QBBN checks whether the conclusion follows from the knowledge base
- If it does, the conclusion is verified. If not, it is rejected.

Nobody needs to ask "what was GPT thinking?" The question is "does the
conclusion follow from the evidence?" The formal language makes this question
answerable.

## What Verification Provides That Interpretation Cannot

**Verification is binary.** A conclusion either follows from the evidence or it
does not. There is no "partially interpretable" or "somewhat explained."
Verification produces a definitive answer.

**Verification is reproducible.** Given the same knowledge base and the same
query, the QBBN always produces the same result. Different interpretability
methods applied to the same neural network produce different explanations.

**Verification is compositional.** If step 1 is verified and step 2 is
verified, the chain is verified. Interpretability explanations do not compose —
explaining step 1 and explaining step 2 does not explain the chain.

**Verification scales.** Checking a proof is cheaper than producing it (in
general, verification is in P while proof search may be NP or worse). As
knowledge bases grow, verification remains tractable. Interpretability methods
generally become harder as models grow — the larger the network, the more there
is to interpret.

## What Verification Does NOT Provide

Verification tells you *whether* a conclusion is correct. It does not tell you:

- Why the LLM proposed that particular conclusion (as opposed to others)
- What the LLM's internal representation looks like
- Whether the knowledge base itself is complete or correct
- Whether the question was well-posed

Verification is not a replacement for all of interpretability. It is a
replacement for the part that matters most: **trust**. You trust a verified
conclusion because the proof checks out, not because you understand the
process that generated it.

## The Proof Tree as Explanation

A side benefit of verification: the proof tree IS an explanation. When the
QBBN verifies a conclusion, the factor graph derivation shows:

- Which evidence nodes contributed
- Which rules were applied
- In what order the inference proceeded
- What the intermediate beliefs were at each step

This is not a post-hoc approximation. It is the actual computation, expressed
in a human-readable formal language. Verification and explanation are the same
thing — because the formal language is both checkable by machine and readable
by human.

This is the real resolution of the interpretability problem: **use a
representation that is simultaneously machine-checkable and human-readable.**
The typed logical language is that representation.

## Key Works

- Leroy, X. "Formal Verification of a Realistic Compiler." *CACM*, 2009.
  (Verification without interpretation in software.)
- De Moura, L. and Ullrich, S. "The Lean 4 Theorem Prover." CADE, 2021.
  (Verified mathematics.)
- Amodei, D. et al. "Concrete Problems in AI Safety." arXiv:1606.06565, 2016.
  (The original framing of interpretability as a safety problem.)