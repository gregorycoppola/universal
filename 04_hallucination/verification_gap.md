# The Verification Gap

## The Problem

When an LLM tells you "Socrates is mortal," you cannot determine from the model
itself whether this is:

1. A correct inference from known facts
2. A statistical pattern reproduced from training data
3. A hallucination that happens to be true
4. A hallucination that is false

All four cases produce the same output: a confident, fluent English sentence. The
model provides no metadata, no derivation, no confidence calibration, no proof.
The output is a string of tokens. Its relationship to truth is opaque.

This is the **verification gap**: the distance between what a system asserts and
what a system can justify.

## Verification in Other Domains

The verification gap is not unique to AI. It appears wherever assertions are made
without accompanying justification. What is unique to AI is that the gap is
**structural** — built into the architecture — rather than contingent.

### Mathematics
A mathematical claim can be verified by checking the proof. The proof is a finite
sequence of steps, each following from the previous by an accepted rule of
inference. If the proof is valid, the claim is true (within the axiomatic system).
If no proof is provided, the claim is unverified — not necessarily false, but not
established.

### Software
A program can be verified by running it. The program takes input, performs
operations, produces output. If the output is correct for all inputs, the program
is correct. More practically, tests verify specific input-output pairs, and formal
verification techniques can prove correctness for all inputs.

The paper makes an analogy: **the QBBN is a runtime for natural language reasoning,
in the same way that a Python interpreter is a runtime for code.** One does not
trust code because the programmer is reliable; one trusts it because one can
execute it and observe the results. One should not trust a reasoning system because
the model is large; one should trust it because the inference is traceable.

### Science
A scientific claim is verified by reproducing the experiment. The paper describes
the method; the reader follows the method; if the results match, the claim is
supported. Replication is verification.

### Law
A legal conclusion is verified by tracing it through statute, precedent, and
argument. A court opinion lays out its reasoning: these are the facts, this is
the applicable law, this is how the law applies to the facts, therefore this is
the conclusion. The reasoning is public and challengeable.

## What Verification Requires

All verification systems share three properties:

1. **Explicit representation**: The claim must be expressed in a form that can be
   inspected. A mathematical proof is written down. A program is source code. A
   scientific method is a protocol. An LLM's "reasoning" is hidden in billions
   of parameters — it is not inspectable.

2. **Traceable derivation**: The path from premises to conclusion must be
   followable step by step. Each step must be an application of a recognized rule
   to recognized inputs. An LLM has no steps — it has a single forward pass
   through a neural network, producing a probability distribution over tokens.

3. **Reproducibility**: Given the same inputs and rules, the same conclusion must
   follow. A mathematical proof is deterministic. A program is deterministic (for
   the same input). An LLM is stochastic — the same prompt can produce different
   outputs, and small changes in the prompt can produce radically different outputs.

## The QBBN Closes the Gap

The QBBN provides all three properties:

### Explicit Representation
Every fact is a typed proposition: mortal(theme: socrates). Every rule is a
quantified Horn clause: always [x:e]: man(theme: x) -> mortal(theme: x). Every
entity is declared with a type: socrates : e. The knowledge base is a text file
that a human (or an LLM) can read, inspect, and critique.

### Traceable Derivation
Every conclusion comes with a proof tree — a path through the factor graph from
evidence nodes through named rules to the query:

    man(theme: socrates)  [evidence, P=0.99]
      → AND factor: man(theme: socrates) forms group g1
        → OR factor: g1 supports mortal(theme: socrates) with weight 0.99
          → mortal(theme: socrates)  [posterior, P=0.98]

If the derivation cannot be constructed, the system returns P = 0.5 — "unknown."
There is no mechanism to produce an answer without a proof, so there is no
mechanism to hallucinate.

### Reproducibility
Given the same knowledge base and the same query, belief propagation produces the
same posterior probability every time. The system is deterministic (given fixed
evidence and rules). Different knowledge bases produce different answers — but the
relationship between knowledge base and answer is transparent and inspectable.

## Degrees of Verification

Not all verification is binary. The QBBN provides **graded** verification through
its probabilistic framework:

- **P = 0.99**: Strong evidence via deterministic rules (always)
- **P = 0.90**: Strong evidence via soft rules (usually)
- **P = 0.50**: No evidence either way — the system's "I don't know"
- **P = 0.10**: Strong evidence against via soft rules
- **P = 0.01**: Strong evidence against via deterministic rules

The probability is not a confidence score (which would be opaque). It is a
**computed posterior** with a known derivation: you can trace which rules fired,
with what weights, through what chains, to produce the final number. The
probability is transparent.

## The Generator-Verifier Architecture

The verification gap suggests a general architectural pattern:

    Generator (produces candidates) → Verifier (checks candidates)

In different domains:

| Domain | Generator | Verifier |
|---|---|---|
| Mathematics | Mathematician / LLM | Proof assistant (Lean, Coq) |
| Software | Programmer / LLM | Compiler + test suite |
| Science | Researcher / LLM | Experiment + replication |
| Natural language reasoning | LLM | QBBN |

The LLM is a powerful generator. It produces plausible candidates — code, proofs,
logical forms, reasoning chains. But plausibility is not truth. The verifier checks
truth. The generator and verifier are fundamentally different systems with
fundamentally different architectures, because generation and verification are
fundamentally different tasks.

The insight: **you do not need a trustworthy generator if you have a reliable
verifier.** The generator can hallucinate freely, as long as the verifier catches
every error. This is why the QBBN + LLM architecture works: the LLM generates
candidate logical forms (possibly with errors), the grammar compiles them (catching
structural errors), and the QBBN reasons over them (catching logical errors). The
pipeline tolerates an imperfect generator because the verifier is exact.

## Key Sources

- Coppola, G. "Statistical Parsing for Logical Information Retrieval." 2026.
  Section 2 (Motivation) and Section 3.2 (The LLM as Annotator).
- De Moura, L. and Ullrich, S. "The Lean 4 Theorem Prover and Programming
  Language." CADE, 2021.
- Chen, M. et al. "Evaluating Large Language Models Trained on Code." arXiv:
  2107.03374, 2021.

## Open Questions

- Is the generator-verifier architecture the *only* way to achieve hallucination-
  free reasoning, or could a future architecture combine generation and
  verification in a single system?
- Can the QBBN verifier be fast enough for real-time applications (e.g., verifying
  each sentence of an LLM response as it is generated)?
- Is there a formal relationship between the verification gap and Gödel's
  incompleteness — are there true claims that no verifier can verify?