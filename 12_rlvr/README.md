# Reinforcement Learning with Verifiable Rewards for Reasoning

## The Core Insight

RL needs reward signals. Verifiable reward signals scale. Logic programming verifies things. Therefore: **the characteristica + calculus ratiocinator is a reward signal factory for training LLMs to reason.**

This is the same pattern that made LLMs good at coding:

| Domain | LLM generates | Verifier checks | Reward signal |
|---|---|---|---|
| Code | Python / Rust | Compiler + tests | Pass / fail |
| Math proofs | Lean / Coq | Type checker | Proof checks or doesn't |
| **Reasoning** | **Typed logical forms** | **Calculus ratiocinator** | **Inference succeeds or doesn't** |

Code has a verifier (the compiler). Math has a verifier (the proof assistant). Reasoning hasn't had one — until now. The characteristica is the language. The calculus is the verifier. Together they give reasoning the same RLVR loop that made LLMs good at code.

## The Flywheels

There are several reinforcing loops:

1. [RLVF: Training LLMs to Produce Logical Forms](rlvf.md) — The direct loop: LLM generates logical forms, verifier checks them, reward signal trains the LLM to produce correct reasoning.

2. [The LLM as Thought Externalizer](thought_externalization.md) — The LLM writes its reasoning in the characteristica. The calculus verifies it. This is chain-of-thought but *verifiable* — not English that looks right, but logical forms that are right.

3. [Bootstrapping the Knowledge Base](bootstrapping.md) — The LLM generates not just logical forms but lexicon entries, predicates, rules, entire knowledge bases. The verifier checks consistency. The KB grows with compute.

4. [Bidirectional Training](bidirectional.md) — Train the LLM to go both ways: natural language → logical form (parsing) and logical form → natural language (generation). Both directions have verifiable signals.

## Why This Is Big

RLHF trains models to produce output that *looks* correct to humans. Humans are fooled by fluent, confident nonsense. RLHF optimizes for the appearance of correctness.

RLVF trains models to produce output that *is* correct, verified by the calculus. The model cannot fool the verifier. A logical form either passes inference or it doesn't. RLVF optimizes for actual correctness.

The failure modes tell the story:
- RLHF failure: confident hallucination ("I'm sure this is true" — it isn't)
- RLVF failure: honest inability ("I cannot produce a valid proof" — which is true)

## Why Now

Three things converged:
1. LLMs are good enough to generate plausible logical forms
2. The characteristica is defined and the calculus is implemented
3. The RLVR paradigm (DeepSeek-R1, AlphaProof) has proven the pattern works for code and math

The missing piece was a verification language for *reasoning*. That's what the characteristica is. The RLVR infrastructure already exists. We just need to plug in a new verifier.