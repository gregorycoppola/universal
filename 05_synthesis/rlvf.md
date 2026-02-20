# Reinforcement Learning from Verified Feedback

## The Idea

Large language models are currently trained to reason through two mechanisms:

**RLHF (Reinforcement Learning from Human Feedback)**: Humans rate the quality
of model outputs. The model learns to produce outputs that humans rate highly.
The reward signal is human judgment — subjective, expensive, inconsistent, and
unscalable.

**Code training**: Models generate code, the code is compiled and tested, and
the pass/fail signal is used as reward. The reward signal is mechanical
verification — objective, cheap, consistent, and infinitely scalable. This is
why LLMs are better at coding than at reasoning: code has a verifier (the
compiler + test suite), reasoning does not.

We propose a third mechanism:

**RLVF (Reinforcement Learning from Verified Feedback)**: Models generate
arguments in typed logical form, the QBBN runs inference, and the pass/fail
signal is used as reward. The reward signal is formal verification — the same
kind of objective, mechanical, scalable signal that makes code training work,
but applied to reasoning instead of programming.

## The Analogy

| Domain | Language | Verifier | Reward Signal |
|---|---|---|---|
| Code | Python, JS, Rust | Compiler + test suite | Does it compile and pass tests? |
| Math | Lean, Coq, Agda | Type checker / proof assistant | Does the proof check? |
| Reasoning | Typed logical language | QBBN (spiral reason) | Does inference produce the expected answer? |

In each case, the pattern is the same:

1. The LLM generates output in a formal language
2. A mechanical verifier checks the output
3. The pass/fail signal trains the LLM to produce better output
4. No human is in the loop at verification time

The key insight: **the typed logical language gives reasoning the same kind of
verifier that programming languages give code.** Without a formal language,
there is no mechanical verifier. Without a mechanical verifier, there is no
scalable reward signal. Without a scalable reward signal, LLMs cannot learn to
reason reliably. The formal language is the bottleneck, and the QBBN removes
it.

## What Already Happened

This pattern is not hypothetical. It occurred in the conversation that produced
this document:

1. Claude (an LLM) generated lexicon entries and gold.logic files — arguments
   for the universal language thesis, expressed in typed logical form
2. A human ran `spiral reason --data-dir .`
3. The inference engine returned: 3 passed, 0 failed, 0 errors
4. The pass signal confirmed that the formalization was correct
5. More examples were generated and tested

The human's role was minimal: copy-paste the files, run the command, report the
result. This is exactly the role that would be eliminated in a fully automated
training loop. The LLM generates the logical forms, the verifier checks them,
the signal flows back. The human sets up the lexicon and defines the predicates
— the same role a software architect plays when defining APIs and writing test
specifications.

## The Training Loop

### Phase 1: Supervised (Current)
- Human + LLM collaboratively author lexicon, gold.logic files, expected.txt
- `spiral reason` verifies each argument
- Human reviews and corrects failures
- This is "vibe annotation" — the semi-automatic bridge stage

### Phase 2: Semi-Automated
- LLM generates candidate gold.logic files from natural language arguments
- `spiral reason` automatically verifies
- Passing examples are accepted; failing examples are fed back to the LLM
  for revision
- Human reviews periodically for quality
- This is the verify-and-revise loop from the QBBN paper

### Phase 3: Fully Automated (RLVF)
- LLM generates logical forms directly from text
- `spiral reason` provides reward signal
- Standard RL training loop (PPO, DPO, or similar) optimizes the LLM to
  produce logical forms that pass verification
- No human in the loop
- The LLM learns to reason by learning to produce verifiable arguments

## Why RLVF Is Stronger Than RLHF for Reasoning

**RLHF** trains models to produce outputs that *look* correct to humans.
Humans are fooled by confident, fluent, plausible-sounding arguments. The
model learns to produce plausible-sounding arguments, not correct ones. This
is why RLHF-trained models hallucinate fluently — they have been optimized for
the appearance of correctness, not correctness itself.

**RLVF** trains models to produce outputs that *are* correct, as verified by a
formal system. The model cannot fool the verifier with fluent nonsense. A
logical form either passes inference or it does not. There is no "plausible
but wrong" in formal verification. The model learns to produce correct
arguments because that is the only way to get reward.

| Property | RLHF | RLVF |
|---|---|---|
| Reward signal | Human judgment | Formal verification |
| Foolable? | Yes (fluent nonsense) | No (proof checks or it doesn't) |
| Scalable? | No (requires human raters) | Yes (fully mechanical) |
| Consistent? | No (inter-rater disagreement) | Yes (deterministic) |
| What it optimizes | Appearance of correctness | Actual correctness |
| Failure mode | Confident hallucination | Refusal to generate (no proof found) |

The failure mode is revealing. An RLHF-trained model fails by hallucinating
confidently. An RLVF-trained model fails by being unable to generate a
verifiable argument — which is honest failure. "I cannot prove this" is
infinitely better than "I am confident this is true (but it isn't)."

## The Bitter Lesson Connection

Sutton's bitter lesson says: scale with compute, not with human effort. RLHF
scales with human effort (more raters = better signal). RLVF scales with
compute (more verification runs = better signal). RLVF is aligned with the
bitter lesson. RLHF is not.

The QBBN paper's central argument — that LLMs change the equation for formal
semantics by replacing the human annotator — applies equally to training. The
formal language provides the verifier. The LLM provides the generator. The
training loop provides the optimization. All three scale with compute. No
human is in the loop.

## What the Formal Language Must Provide

For RLVF to work, the formal language must have four properties:

1. **Expressiveness**: The language must be able to represent the target
   reasoning tasks. (The QBBN's sufficiency claim: three tiers cover natural
   language semantics.)

2. **Decidability**: Verification must always terminate. (The QBBN's finite
   grounding: Datalog-level, polynomial time.)

3. **Compositionality**: Complex arguments must be built from simpler ones, so
   the LLM can learn incrementally. (The QBBN's typed predicates with roles.)

4. **Learnability**: The language must have enough structure that an LLM can
   learn to produce valid expressions from examples. (The QBBN's regular
   syntax: predicates, roles, quantifiers, arrows — a small grammar.)

The typed logical language satisfies all four. It is not the only possible
verification language for RLVF — Lean, Coq, and Isabelle could also serve —
but it is arguably the simplest one that covers natural language reasoning,
which makes it the most learnable.

## The Existing Evidence

Code training already demonstrates that RLVF works in principle:

- **AlphaCode** (DeepMind): Trained on competitive programming problems with
  test-case verification as reward signal
- **CodeRL** (Salesforce): RL fine-tuning of code models using unit test
  pass rates
- **AlphaProof** (DeepMind): Trained to produce Lean proofs of math olympiad
  problems, with the Lean type checker as verifier

These systems demonstrate that LLMs can learn to produce formally verified
output through RL training with mechanical verification. RLVF for reasoning
is the same pattern applied to a new domain — natural language arguments
instead of code or mathematical proofs — using the QBBN instead of a compiler
or proof assistant.

## The Recursive Implication

If RLVF works — if LLMs can be trained to produce verified logical forms
through reinforcement learning with the QBBN as reward model — then the
system improves itself:

1. Better LLM → better logical forms → more coverage
2. More coverage → more training data → better LLM
3. Better LLM → can generate new lexicon entries, new predicates, new rules
4. New rules → expanded verification capability → even more training data

This is the virtuous cycle that the bitter lesson predicts: once both
generation (LLM) and verification (QBBN) scale with compute, the system
improves with more compute. The human's role diminishes to defining the
initial predicates and reviewing the expanding knowledge base — quality
control, not construction.

The formal language is what makes the cycle possible. Without it, there is
no verifier. Without a verifier, there is no reward signal. Without a reward
signal, there is no learning loop. The typed logical language is the
foundation on which autonomous reasoning improvement is built.

## Key Works

- Christiano, P. et al. "Deep Reinforcement Learning from Human Preferences."
  NeurIPS, 2017. (RLHF.)
- Ouyang, L. et al. "Training Language Models to Follow Instructions with
  Human Feedback." NeurIPS, 2022. (InstructGPT / RLHF at scale.)
- Le, H. et al. "CodeRL: Mastering Code Generation through Pretrained Models
  and Deep Reinforcement Learning." NeurIPS, 2022.
- Li, Y. et al. "Competition-Level Code Generation with AlphaCode." Science,
  2022.
- Silver, D. et al. "AlphaProof." DeepMind, 2024. (RL + Lean for math.)
- Sutton, R. "The Bitter Lesson." 2019.

## Open Questions

- What is the minimum amount of supervised data (Phase 1) needed before
  Phase 2 and Phase 3 become effective?
- Can RLVF train models to generate entire knowledge bases (lexicons + rules),
  or only individual logical forms within a fixed knowledge base?
- How does the choice of modal quantifier (always/usually/sometimes) affect
  learnability? Are probabilistic rules harder for LLMs to get right than
  deterministic ones?
- Can RLVF and RLHF be combined — using RLVF for the reasoning component and
  RLHF for the natural language interface?
- What happens when the LLM discovers that the knowledge base is inconsistent?
  Can the verify-and-revise loop be used to debug knowledge bases, not just
  individual arguments?