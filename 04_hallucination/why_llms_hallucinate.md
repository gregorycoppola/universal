# Why LLMs Hallucinate

## The Phenomenon

Large language models produce fluent, confident, detailed text that is factually
wrong. They invent citations that do not exist. They attribute quotes to people
who never said them. They describe events that never happened. They solve math
problems with plausible-looking steps that arrive at wrong answers. They do all
of this with the same tone and confidence as when they are correct.

This is not a bug that will be fixed with more data or better training. It is a
structural consequence of what LLMs are.

## The Architecture

An LLM is a function from token sequences to probability distributions over next
tokens:

    P(token_n+1 | token_1, token_2, ..., token_n)

At each step, the model selects the next token based on statistical patterns
learned from training data. The selection is conditioned on the preceding context,
not on any model of truth, consistency, or the world.

This architecture has no mechanism for:

1. **Checking whether a claim is true**. The model does not maintain a knowledge
   base of facts against which outputs are verified. It does not "know" things —
   it has learned statistical associations between tokens.

2. **Tracing how a conclusion was reached**. There is no derivation, no proof
   tree, no chain of inference. The output is a sample from a probability
   distribution, not the conclusion of an argument.

3. **Detecting contradictions**. The model can assert P in one sentence and ¬P
   in the next. There is no consistency-checking mechanism. Each token prediction
   is locally conditioned; global coherence is not enforced.

4. **Distinguishing knowledge from ignorance**. The model produces output for
   every input. It cannot say "I don't know" in a principled way — it can only
   generate tokens that look like "I don't know," which is a very different thing.

## Three Kinds of Hallucination

### Factual Hallucination
The model states something false with confidence.

"The Eiffel Tower was designed by Gustave Eiffel and completed in 1889 for the
World's Fair in Berlin."

Everything is correct except "Berlin" — it was Paris. The model has learned strong
associations between "Eiffel Tower," "Gustave Eiffel," "1889," and "World's Fair,"
but the association between "World's Fair" and "Paris" competed with "Berlin" (which
hosted a different World's Fair) and the wrong token won.

This is not a reasoning error. It is a **sampling error** — the model sampled from
a distribution that assigns nonzero probability to a false completion. No amount of
scaling eliminates this possibility, because the distribution is learned from finite
data and any finite sample can produce arbitrarily rare but nonzero-probability
errors.

### Inferential Hallucination
The model produces a reasoning chain that looks valid but isn't.

"All birds can fly. Penguins are birds. Therefore, penguins can fly."

The syllogism is valid. The major premise is false. The model cannot distinguish
valid inference from invalid inference, or true premises from false premises,
because it has no inference engine — it has a next-token predictor that has learned
what reasoning *looks like*.

This is the deepest problem. An LLM that produces correct-looking reasoning is
more dangerous than one that produces obviously wrong text, because the error is
hidden inside an apparently valid structure.

### Confabulatory Hallucination
The model invents detailed, specific, entirely fictional content.

"According to Smith and Jones (2019), published in the Journal of Computational
Linguistics, the BERT model achieved 94.7% accuracy on the PP attachment task
using a novel attention mechanism they called 'structural gating.'"

Every detail is fictional — the authors, the year, the journal, the result, the
method name. The model has learned the *form* of academic citation and filled it
with plausible content. This is not a mistake; it is the model doing exactly what
it was trained to do — predict plausible continuations — in a domain where
plausibility and truth diverge.

## The Root Cause: No Language of Thought

Fodor's Language of Thought hypothesis says that reasoning requires a compositional
representational medium — Mentalese — over which logical operations are defined.
LLMs do not have this.

LLMs have:
- **Embeddings**: continuous vector representations of tokens
- **Attention**: a mechanism for relating tokens to each other based on learned
  patterns
- **Parameters**: billions of weights encoding statistical associations from
  training data

LLMs do not have:
- **Propositions**: discrete, typed, truth-evaluable representations
- **Inference rules**: explicit operations that derive conclusions from premises
- **A knowledge base**: a structured store of facts that can be queried, updated,
  and checked for consistency
- **Proof trees**: traceable derivations from evidence to conclusion

Without a Language of Thought, an LLM cannot **think** — it can only **generate
text that looks like the output of thinking**. The distinction is invisible to a
casual reader but fatal for any application that requires verifiable reasoning.

## Why Scaling Doesn't Help

A common response to hallucination is: bigger models hallucinate less. This is
empirically true on benchmarks — GPT-4 hallucinates less than GPT-3.5, which
hallucinates less than GPT-3. But the improvement is asymptotic, not eliminative.

Scaling reduces the *frequency* of hallucination but cannot eliminate it, because:

1. The architecture has no truth-checking mechanism at any scale. A trillion-
   parameter model still selects tokens from a probability distribution, not from
   a verified knowledge base.

2. Hallucination rate is bounded below by the noise in training data. If 0.1% of
   training data contains false claims, the model will reproduce false claims at
   some nonzero rate regardless of scale.

3. The harder the reasoning, the more likely the hallucination. Simple factual
   recall improves with scale. Multi-step inference does not improve at the same
   rate, because each step compounds the error probability.

4. Novel combinations — questions that require combining facts in ways not present
   in training data — are precisely where hallucination is most likely, and where
   reasoning is most needed.

The scaling hypothesis says: given enough data and compute, LLMs will eventually
reason correctly. The structural argument says: no amount of data and compute can
make a next-token predictor into a theorem prover. These are fundamentally
different architectures solving fundamentally different problems.

## The Plato Connection

Plato's allegory of the cave describes prisoners who see only shadows on the wall
and take them for reality. An LLM sees only token sequences — shadows of thoughts —
and produces more token sequences. It has never seen the objects casting the
shadows (the logical forms, the facts, the inference rules). It cannot, because
its architecture has no representation for them.

Ascending from the cave requires a different kind of seeing — not more shadows, but
direct apprehension of the Forms (logical structure). The QBBN provides this: typed
predicates are the Forms, the knowledge base is the realm of Forms, and belief
propagation is the dialectic that ascends from particular facts to general
conclusions.

## Key Sources

- Ji, Z. et al. "Survey of Hallucination in Natural Language Generation." *ACM
  Computing Surveys*, 55(12):1-38, 2023.
- Maynez, J. et al. "On Faithfulness and Factuality in Abstractive Summarization."
  ACL, 2020.
- Huang, L. et al. "A Survey on Hallucination in Large Language Models." arXiv:
  2311.05232, 2023.
- Fodor, J. *The Language of Thought*. Harvard University Press, 1975.

## Open Questions

- Is there a theoretical lower bound on hallucination rate for autoregressive
  language models, analogous to the Bayes error rate in classification?
- Can retrieval-augmented generation (RAG) eliminate hallucination, or does it
  merely shift the problem from generation to retrieval?
- Are multimodal models (vision + language) less prone to hallucination because
  grounding in perception constrains generation? Or do they hallucinate in new
  modalities?