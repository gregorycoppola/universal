# The Interpretability Problem

## What the Field Is Trying to Do

The interpretability research program, broadly construed, attempts to answer:
"Why did the neural network produce this output?" The field emerged from a
legitimate concern: neural networks making consequential decisions —
medical diagnoses, criminal risk assessments, loan approvals — should be
explainable to the humans affected by those decisions.

The major approaches:

**Feature attribution** (LIME, SHAP, saliency maps): Which input features
contributed most to the output? These methods perturb inputs and observe
changes in output, producing heatmaps or feature importance scores.

**Attention visualization**: For transformer models, visualize which tokens
attend to which other tokens. The implicit claim is that attention patterns
reveal the model's "reasoning."

**Probing classifiers**: Train small models to predict linguistic or semantic
properties from a network's internal representations. If a probing classifier
can extract part-of-speech tags from layer 6, then layer 6 "represents"
part-of-speech information.

**Mechanistic interpretability**: Anthropic's research program to reverse-
engineer the circuits inside neural networks — identifying specific features,
neurons, and circuits that implement recognizable computations.

**Concept activation vectors** (TCAV): Find directions in the network's
representation space that correspond to human-interpretable concepts (e.g.,
"striped," "male," "formal").

## Why It Has Not Converged

After nearly a decade of intensive research, the field lacks consensus on
fundamental questions:

**What counts as an explanation?** Feature attribution gives a different answer
than attention visualization, which gives a different answer than probing,
which gives a different answer than circuit analysis. These are not different
measurements of the same thing — they are measurements of different things,
each claiming to be "the" explanation.

**Faithfulness vs. plausibility.** An explanation can be plausible to a human
without being faithful to the network's actual computation. Attention patterns
are intuitive but do not reliably indicate which inputs the model depends on
(Jain and Wallace, 2019). Saliency maps are visually compelling but
inconsistent across methods. The explanations that humans find most
understandable may be the least accurate.

**The representation gap.** Neural networks represent knowledge as continuous
vectors in high-dimensional spaces. Human understanding operates over discrete
concepts and propositions. Mapping between these requires lossy compression —
any human-readable explanation is necessarily a simplification of what the
network actually computed. The explanation is not the computation. It is a
story about the computation.

**Superposition.** Anthropic's mechanistic interpretability research has found
that individual neurons often represent multiple unrelated concepts
simultaneously (superposition), making it impossible to assign clean semantic
meanings to individual computational units. The basic assumption that network
components map to concepts appears to be false.

## The Deeper Problem

All interpretability methods share a common structure: take an opaque
computation, produce a human-readable approximation, and hope the approximation
is faithful. This is post-hoc rationalization — constructing a story after the
fact that may or may not reflect the actual process.

The problem is not that current methods are insufficiently sophisticated. The
problem is structural. A neural network's computation is a sequence of matrix
multiplications in R^n. A human explanation is a sequence of propositions in
natural language. These are fundamentally different kinds of objects. No amount
of methodological sophistication will make one into the other, any more than a
sufficiently sophisticated thermometer will measure color.

## What Would Actually Work

If the goal is to understand *why* a system produced a conclusion, the
conclusion must be expressed in a language that supports "why" questions. This
means: a language with explicit premises, explicit rules, and explicit
derivations. In other words, a formal language.

In the QBBN, every conclusion has a proof tree: a derivation through the factor
graph from evidence nodes through named rules to the conclusion. The "why" is
the proof. It is not a post-hoc approximation — it is the actual computation.
The representation is the explanation.

This is not interpretability in the neural network sense. It is transparency in
the formal verification sense. The system does not need to be interpreted
because its reasoning is already written in a language the human can read.

## Key Works

- Ribeiro, M.T., Singh, S., and Guestrin, C. "Why Should I Trust You?
  Explaining the Predictions of Any Classifier." KDD, 2016. (LIME.)
- Lundberg, S.M. and Lee, S-I. "A Unified Approach to Interpreting Model
  Predictions." NeurIPS, 2017. (SHAP.)
- Jain, S. and Wallace, B.C. "Attention Is Not Explanation." NAACL, 2019.
- Elhage, N. et al. "Toy Models of Superposition." Anthropic, 2022.
- Olah, C. et al. "Zoom In: An Introduction to Circuits." Distill, 2020.
- Kim, B. et al. "Interpretability Beyond Feature Attribution." ICML, 2018.
  (TCAV.)