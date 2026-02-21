# The Transformer as Distributed Calculus

## The Claim

A trained transformer has learned a distributed, continuous approximation of
the characteristica universalis and calculus ratiocinator. The components of
the transformer architecture map systematically onto the components of formal
inference. Parsing LLM output into typed logical forms is not imposing external
structure — it is decompressing the structure the model already learned.

## The Mapping

### Token Embeddings ≈ The Lexicon

Before any processing, each token is mapped to a vector encoding its identity,
type, and semantic neighborhood. In the characteristica, the lexicon maps words
to typed entries — "jack" is an entity of type person, "trust" is a predicate
taking agent and patient roles. The embedding encodes the same information —
type, typical roles, semantic neighborhood — implicitly in the geometry of
high-dimensional space.

### One Attention Head ≈ One Typed Predicate

An attention head learns three weight matrices (W_Q, W_K, W_V) that define a
relation: what to look for, how to be found, and what to return when found.
After training, a head might learn "when processing a pronoun, find the most
recent animate noun and return its semantic features."

Write that as a typed predicate:

    referent(pronoun: X, antecedent: Y) :- animate(Y), precedes(Y, X)

The structure is identical. The Query is the left-hand side of a lookup. The
Key is the matching condition. The Value is what gets returned when the match
succeeds. The difference is substrate — three matrices of continuous weights
versus discrete symbols with explicit types.

Critically, a single head computes a bilinear function: Q and K interact
through a dot product, which is a similarity measure in a learned space. This
constrains what a single head can represent to relations based on matching —
which is exactly what predicate unification does in logic. One head learns one
matching pattern. One predicate defines one matching pattern. Same operation,
different medium.

A single head also learns what to *ignore*. The softmax over attention weights
pushes most weights near zero. The head filters the entire sequence down to the
signal it cares about. A typed predicate does the same —
`trust(agent: X, patient: Y)` implicitly excludes location, time, color, size.
The type signature is the discrete version of what learned attention weights do
continuously.

### Multiple Heads per Layer ≈ Parallel Rule Application

A single layer has 32 or 128 heads, each performing independent Q/K/V lookup
over the same input. Head 1 might match pronouns to antecedents. Head 2 might
match verbs to subjects. Head 17 might learn an abstract pattern that resists
human naming but that the training signal found useful.

In a forward-chaining inference engine, you take the current set of facts and
apply all matching rules in parallel. Every rule whose left-hand side matches
fires, producing new derived facts.

Multi-head attention is exactly this. Each head is an independent rule,
pattern-matching against the same representations, producing its own output.
The concatenation of all head outputs is the union of all derived facts from
one round of parallel rule application. The number of heads is the number of
rules the system can apply simultaneously.

### Feedforward Layers ≈ The Knowledge Base

After attention derives relational structure, the feedforward network enriches
representations with stored factual knowledge. Research in mechanistic
interpretability (Geva et al., 2021; Anthropic's work on features) has found
that feedforward layers function as key-value memories — the first layer's
weights are keys, the second layer's weights are values.

This is KB lookup. After applying inference rules (attention) and deriving new
facts, the system grounds those facts against stored knowledge (feedforward).
Attention establishes structure ("there is an agent here in a trust relation").
The feedforward layer fills in content ("here is what we know about agents in
trust relations").

### One Transformer Block ≈ One Cycle of Inference + Grounding

Each transformer block (attention followed by feedforward) implements one
complete step: apply typed rules to derive relational facts, then ground those
facts against stored knowledge. This is one cycle of the calculus ratiocinator
operating over the characteristica with KB lookup.

### Layer Stacking ≈ Proof Tree Depth

Layer 1 applies rules to raw token representations and derives surface
relations. Layer 5 derives clause structure. Layer 20 derives discourse-level
meaning. Layer 60 derives abstract inferences over deeply composed
representations. Each layer takes the output of the previous layer and applies
another round of rules and grounding.

In Prawitz's forward fragment, each level of the proof tree is one round of
inference. The depth of the tree is the number of chaining steps required.
Layer depth in a transformer *is* proof tree depth. Deeper models are smarter
not because they know more facts (that is the feedforward layers' job) but
because they can chain more steps of inference.

Critically, by the deep layers, the representations are no longer "about"
tokens. They are about abstract patterns derived through dozens of rounds of
inference — exactly the kind of structured representations that decompress
naturally into typed predicates rather than surface words.

### The Residual Stream ≈ Working Memory

The residual connection means each layer adds to the running representation
rather than replacing it. The vector flowing through the network accumulates
derived facts. Layer 1 adds its derivations. Layer 2 adds its on top. The
residual stream is the working memory of a forward-chaining system —
monotonically accumulating everything derived through all rounds of processing.

### Softmax Attention Weights ≈ Probabilistic Predicate Evaluation

Attention weights are not binary — they are graded. "70% likely this pronoun
refers to jack, 20% to jill, 10% ambiguous." This is not classical logic.
This is probabilistic inference over typed bindings.

The QBBN formalizes exactly this: weighted Horn clauses with belief propagation
over factor graphs. The soft attention mechanism is already computing what the
QBBN expresses symbolically — graded belief over possible groundings of a
predicate.

### Positional Encodings ≈ Discourse Indexing

The model needs to distinguish "jack" at position 3 from "jack" at position 47.
In the characteristica, this is handled by explicit indices or discourse
referents. Positional encodings serve the same function — tagging each
representation with its location so identical tokens in different positions
remain distinguishable.

### The Final Projection ≈ Generation from Logical Form

The last layer's representation is projected through a matrix to vocabulary-
sized logits, producing a probability distribution over tokens. This is
translation from the internal derived representation back into natural
language — the inverse of parsing. Generation from logical form to surface
string.

### KV Cache ≈ Memoization of Derived Facts

During generation, previously computed Keys and Values are stored and reused.
In a logic system, you would not re-derive something already proven. The KV
cache is memoization of intermediate inference results — a store of previously
derived facts that persist and can be looked up by future queries without
re-derivation.

## The Summary Table

| Transformer Component | Formal Reasoning Analog |
|---|---|
| Token embeddings | Lexicon (words → typed entries) |
| One attention head | One typed predicate / inference rule |
| Multiple heads per layer | Parallel rule application |
| Feedforward layer | Knowledge base lookup |
| Transformer block | One cycle of inference + grounding |
| Layer stacking | Proof tree depth / forward chaining |
| Residual stream | Working memory (accumulated derived facts) |
| Softmax weights | Probabilistic predicate evaluation (QBBN) |
| Positional encodings | Discourse indexing |
| Final projection | Generation from logical form |
| KV cache | Memoization of derived facts |

## The Structural Echo

The transformer architecture embodies a separation between inference and
knowledge — attention for relational reasoning, feedforward for factual
storage — that mirrors the characteristica/calculus distinction. This
separation was not designed by analogy to logic. It emerged from optimizing
next-token prediction on language data. That it converges on the same
separation is evidence that the structure is fundamental.

## Evidence from Architecture Evolution

Modern architectures (Nemotron 3, hybrid Mamba-Transformer models) are moving
toward sparse attention — using full K/V lookup at only a few strategic layers,
with cheaper sequential processing (Mamba state-space layers) handling the bulk
of computation. Nemotron 3 Nano uses only 6 attention layers out of 52 total.

This suggests the field is discovering empirically that full relational lookup
is expensive and should be applied surgically, while the majority of processing
can be cheaper forward propagation. The convergence toward structured, modular
processing — with explicit separation between relational inference and
sequential state maintenance — is a move toward something more like the
explicit KB/calculus separation, not less.

## What This Means for Interpretability

If the transformer has learned a distributed encoding of the characteristica
and calculus, then interpretability is translation between substrates:

- The model's internal representations correspond to typed predicates, role
  labels, and inference rules — encoded as directions in high-dimensional
  vector spaces via superposition
- Parsing LLM output into logical forms is decompressing these distributed
  representations into the discrete symbols humans read
- The characteristica provides mechanistic interpretability with a *target
  vocabulary* — instead of asking "what is this neuron doing?" we can ask
  "which predicate does this direction in activation space correspond to?"

This reframes the relationship between our approach and Anthropic's mechanistic
interpretability program. They are identifying features and circuits in the
continuous substrate. We are providing the formal language those features and
circuits implement. The two programs are complementary — one finds the
distributed encoding, the other names what is encoded.

## What This Means for RLVF

If the transformer already computes something like the characteristica
internally, then RLVF is not teaching the model something foreign. It is
training the model to do explicitly and verifiably what it already does
implicitly and approximately. The reward signal teaches the model to sharpen
its distributed reasoning into clean discrete logical forms.

This is a much easier learning problem than learning reasoning from scratch —
and explains why LLMs can learn to produce logical forms from relatively few
examples.

## What This Means for Hallucination

The transformer has something *like* the characteristica internally, but in a
lossy continuous approximation. The soft bindings, the superposition, the
compressed state — these allow graceful degradation into plausible-sounding
nonsense. Hallucination is what happens when the distributed approximation
diverges from what the discrete calculus would derive. Making the
characteristica explicit catches what the distributed version misses.

## What This Does Not Claim

- That we can currently decompress transformer weights into explicit predicates
  (this is a project for mechanistic interpretability)
- That the mapping is exact (continuous systems are lossy relative to discrete
  ones — this is why hallucination exists)
- That the transformer "intends" to implement logic (it optimizes for next-
  token prediction; logical structure emerges because language encodes it)

The claim is structural: the transformer architecture, trained on human
language, converges on computational patterns that correspond to the components
of formal reasoning. This convergence is evidence for the universality thesis.

## Key Works

- Geva, M. et al. "Transformer Feed-Forward Layers Are Key-Value Memories."
  EMNLP, 2021.
- Elhage, N. et al. "Toy Models of Superposition." Anthropic, 2022.
- Olah, C. et al. "Zoom In: An Introduction to Circuits." Distill, 2020.
- Vaswani, A. et al. "Attention Is All You Need." NeurIPS, 2017.
- Gu, A. and Dao, T. "Mamba: Linear-Time Sequence Modeling with Selective
  State Spaces." arXiv:2312.00752, 2023.