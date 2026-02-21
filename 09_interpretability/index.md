# Interpretability, Verification, and Human-Computer Interface

## The Field

"Interpretability" (also called "explainability" or XAI) emerged as a major
subfield of AI research roughly around 2016-2018, as deep neural networks
became dominant in high-stakes applications — medical diagnosis, criminal
sentencing, loan approval, autonomous driving. The core concern: if a neural
network makes a decision that affects someone's life, we should be able to
explain why.

The field has produced techniques like attention visualization, saliency maps,
LIME, SHAP values, feature attribution, circuit analysis (Anthropic's own work
on mechanistic interpretability), probing classifiers, and concept activation
vectors. These techniques ask: **what is the network doing internally?**

We argue this is the wrong question — or at least an incomplete one.

## The Problem with Interpretability

Interpretability tries to make neural network internals human-readable. But
neural networks do not represent knowledge in a human-readable format. Their
"knowledge" is distributed across billions of floating-point parameters in
high-dimensional spaces. Making this readable is not just technically hard — it
may be category error, like asking "what color is the number seven?"

The fundamental issues:

1. **No shared representation.** The network's internal states are vectors in
   R^n. Human understanding operates over discrete concepts, propositions,
   and arguments. There is no natural mapping between them.

2. **Post-hoc rationalization.** Most interpretability methods generate
   explanations *after* the network has made its decision. The explanation
   is not the network's actual reasoning process — it is a human-readable
   approximation constructed after the fact. This is rationalization, not
   interpretation.

3. **No verification.** Even if you produce an explanation ("the network
   classified this as a cat because of these pixels"), you cannot verify that
   the explanation is correct. The explanation is another model's output, not
   a proof. You have replaced one unverifiable claim with another.

4. **The field has no convergent answer.** After nearly a decade of intensive
   research, there is no consensus on what interpretability even means, let
   alone how to achieve it. Different methods give different explanations for
   the same decision. This is not a sign of a field converging on truth.

## From Interpretation to Verification

We propose a reframing: **the goal is not to interpret the AI's reasoning but
to verify it.**

Interpretation asks: "What is the AI thinking?"
Verification asks: "Is the AI's conclusion correct?"

These are fundamentally different questions. The first requires access to the
AI's internal representations (which may be uninterpretable by design). The
second requires only that the AI's conclusion be expressed in a language that
supports proof checking.

The QBBN pipeline achieves verification without interpretation:

1. The LLM produces a conclusion (opaque internal process — we don't interpret
   it)
2. The grammar translates it to a formal representation (typed logical form)
3. The QBBN checks whether the conclusion follows from the evidence (belief
   propagation over the factor graph)
4. If it checks out, the conclusion is verified. If not, it is rejected.

At no point do we need to know what the LLM was "thinking." We only need to
know whether its output is correct. This is the same principle as software
testing: you don't need to understand the compiler's internals to verify that
the compiled program is correct. You run it and check the output.

## The Shared Language

But verification alone is not enough for human-computer collaboration. The
human also needs to understand the verified conclusion and its justification.
This is where the universal grammar becomes critical.

The typed logical language serves as the **shared representational medium**
between human and machine:

- The **human** can read `always [x:e]: man(theme: x) -> mortal(theme: x)` and
  understand it immediately — it maps directly to "all men are mortal."
- The **machine** can process the same representation — ground it, build a
  factor graph, run belief propagation, produce a posterior probability.
- The **verification engine** can check it — trace from evidence through rules
  to conclusion, verify each step.

All three — human, machine, verifier — operate on the same formal object. This
is not interpretation (making the machine's internals readable). It is
**interface** — a shared language in which both human and machine can express,
check, and discuss reasoning.

## The Deeper Insight: Transformers Already Implement the Calculus

Recent analysis of the transformer architecture reveals a striking
correspondence: the components of a trained transformer map systematically onto
the components of formal inference. Attention heads learn typed relations.
Feedforward layers function as knowledge stores. Layer stacking implements
proof-tree-depth reasoning. The transformer has learned a distributed,
continuous approximation of the characteristica and calculus — not by design,
but because language encodes logical structure and the model learned to
recapitulate it.

This means that parsing LLM output into typed logical forms is not imposing
external structure. It is decompressing the structure the model already has.
And it reframes the relationship between our approach and mechanistic
interpretability: they identify features and circuits in the continuous
substrate; we provide the formal language those features and circuits implement.
The two programs are complementary.

## Documents

1. [The Interpretability Problem](interpretability_problem.md) — Why
   interpretability as currently framed may be a category error.

2. [Verification Over Interpretation](verification_over_interpretation.md) —
   The reframing: you don't need to read the AI's mind, you need to check its
   work.

3. [The Transformer as Distributed Calculus](transformer_as_calculus.md) —
   How transformer components map onto the characteristica and calculus
   ratiocinator: attention as predicate evaluation, feedforward as KB,
   layers as proof depth.

4. [The Universal Grammar as Interface](ug_as_interface.md) — The typed logical
   language as the shared medium between human and machine reasoning.

5. [Human-Computer Fusion](human_computer_fusion.md) — The deeper vision: human
   and AI reasoning converging on the same formal language, with the human in
   control.