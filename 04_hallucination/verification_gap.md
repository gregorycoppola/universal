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
Every fact is a typed proposition: `mortal(theme: socrates)`. Every rule is a
quantified Horn clause: `always [x:e]: man(theme: x) -> mortal(theme: x)`. Every
entity is declared with a type: `socrates : e`. The knowledge base is a text file
that a human (or an LLM) can read, inspect, and critique.

### Traceable Derivation
Every conclusion comes with a proof tree — a path through the factor graph from
evidence nodes through named rules to the query: