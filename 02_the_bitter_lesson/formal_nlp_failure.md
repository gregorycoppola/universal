# Why Formal NLP Failed to Scale

## The Promise

The formal semantics tradition in NLP — from Montague Grammar (1973) through
Categorial Grammar, HPSG, LFG, and Definite Clause Grammars — promised something
remarkable: a complete, compositional, formally verified mapping from natural
language to logical representation. If you could parse a sentence, you could reason
about it. If you could reason about it, you could verify it. No hallucination,
no ambiguity, no hand-waving.

The promise was real. The systems worked. On fragments.

## The Bottleneck

The bottleneck was always the same: **human annotation**.

Every grammar rule had to be written by a linguist who understood both the
syntactic pattern and the target logical formalism. Every lexicon entry required
a trained annotator who could assign the correct types, roles, and semantic
features. Every coverage test required someone who could read both the input
sentence and the output logical form and verify correctness.

The numbers were brutal:

- The **Penn Treebank** (Marcus et al., 1993) took years to construct, covered
  only Wall Street Journal text, and provided syntactic annotation only — no
  formal semantics.
- **FrameNet** (Baker et al., 1998) took over a decade to annotate ~200,000
  sentences across ~1,200 frames. Coverage of English remains incomplete.
- **PropBank** (Palmer et al., 2005) added predicate-argument structure to the
  Penn Treebank, but each verb required manual annotation of its argument roles.
- The **Abstract Meaning Representation** project (Banarescu et al., 2013)
  aimed at full semantic representation but achieved coverage of only ~60,000
  sentences after years of annotation effort.

Each of these projects required trained linguists working full-time for years.
The rate of progress was linear in human-hours. There was no exponential.

## The Statistical Revolution

The statistical NLP revolution — from HMMs in the 1980s through maximum entropy
models in the 1990s to deep learning after 2012 — succeeded precisely because it
**amortized** human annotation over training sets. You annotated a corpus once,
trained a model, and the model generalized to unseen data. The cost at inference
time was pure computation.

The formal approach could not compete. A statistical POS tagger trained on the
Penn Treebank achieved 97% accuracy in seconds. A hand-written grammar covering
the same phenomena would take months to build and still have gaps. The statistical
approach was worse in theory (no formal guarantees, no compositionality, no
inference) but overwhelmingly better in practice (coverage, robustness, speed).

The bitter lesson played out exactly as Sutton described.

## What Was Lost

When formal NLP lost to statistical NLP, something real was lost:

- **Verifiability**: A statistical parser gives you a tree, but you can't reason
  over it. A formal parser gives you a logical form you can feed to a theorem
  prover.
- **Compositionality**: Statistical models treat sentences as bags of features.
  Formal models preserve the compositional structure that makes inference possible.
- **Transparency**: A formal derivation is inspectable at every step. A neural
  network is a black box.
- **Consistency**: Formal systems are monotonic — adding a fact never invalidates
  an existing conclusion (in the relevant fragment). Neural networks have no such
  guarantee.

The field gained coverage and lost verifiability. For most NLP applications
(translation, summarization, question answering), this tradeoff was acceptable.
For high-stakes reasoning (medical diagnosis, legal reasoning, scientific
inference), it was not.

## The Impasse

By the mid-2010s, the field was stuck:

- **Statistical/neural NLP** could process any text but could not reason formally.
- **Formal NLP** could reason formally but could not process real text.

Neither approach alone was sufficient. The formal approach had the right
representation but the wrong construction process. The statistical approach had
the right construction process but the wrong representation.

The resolution requires a system that combines formal representations with
scalable construction. That is what LLMs make possible.

## Key Works

- Marcus, M., Santorini, B., and Marcinkiewicz, M.A. "Building a Large Annotated
  Corpus of English: The Penn Treebank." *Computational Linguistics*, 19(2):313-330,
  1993.
- Baker, C.F., Fillmore, C.J., and Lowe, J.B. "The Berkeley FrameNet Project."
  COLING, 1998.
- Palmer, M., Gildea, D., and Kingsbury, P. "The Proposition Bank: An Annotated
  Corpus of Semantic Roles." *Computational Linguistics*, 31(1):71-106, 2005.
- Banarescu, L. et al. "Abstract Meaning Representation for Sembanking." LAW, 2013.

## Open Questions

- Was the failure of formal NLP inevitable, or could it have succeeded with
  better tooling and more funding for annotation?
- Is the statistical/formal divide a false dichotomy, or does it reflect a
  genuine architectural difference that cannot be bridged within a single system?
- Could active learning (where the system identifies the most informative
  sentences to annotate) have closed the annotation gap without LLMs?