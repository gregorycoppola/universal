# The LLM as Annotator

## The Thesis

Large language models change the equation described in the bitter lesson — not by
replacing formal representations, but by replacing the human annotator.

The bottleneck that killed formal NLP was never the representation. The typed
logical languages, the compositional grammars, the inference engines — these were
sound. What was unsound was the construction process: every grammar rule, lexicon
entry, and coverage test required a trained linguist working by hand.

LLMs eliminate that bottleneck. They serve as the annotator.

## What LLMs Can Do

An LLM can perform the tasks that previously required a human linguist:

**Grammar rule authoring**: Describe a syntactic pattern ("sentences where a
prepositional phrase modifies the subject"), and the LLM proposes a grammar rule
with the correct type signature and compilation logic. The human reviews and
corrects — faster than authoring from scratch.

**Lexicon construction**: Given a lexicon format (predicate name, typed roles,
natural language gloss), the LLM generates entries for unseen words. For common
words, accuracy is high. For rare or technical words, accuracy is lower but the
output is a useful starting point.

**Coverage test generation**: Given existing tests, the LLM generates new tests
exercising different linguistic phenomena. It understands what "a test for relative
clause attachment" means and can produce both the input sentence and the expected
logical form.

**Logical form production**: Given a sentence and a lexicon, the LLM produces a
candidate logical form. It gets the predicate names and role labels right most of
the time. When it doesn't, the errors are systematic and correctable.

**Parse disambiguation**: Given an ambiguous sentence, the LLM resolves PP
attachment, word sense ambiguity, and scope ambiguity with high accuracy (95% on
PP attachment in our experiments), leveraging world knowledge that no grammar
can encode.

## What LLMs Cannot Do

LLMs cannot replace the formal layer. The evidence is clear:

**Direct structured parsing fails**: When asked to produce dependency parses in
standard format, LLMs achieve only 12.4% unlabeled attachment score — essentially
random. They understand structure but cannot produce exact formal representations
over combinatorially large spaces.

**Inference is unreliable**: LLMs can answer "Is Socrates mortal?" correctly, but
you cannot distinguish a correct answer from a confident hallucination. There is
no proof tree, no derivation, no verification. The answer is a statistical
prediction, not a logical conclusion.

**Consistency is not guaranteed**: An LLM can assert P and ¬P in the same
conversation. There is no mechanism to detect or prevent contradictions. A formal
system with a knowledge base and inference engine catches contradictions by
construction.

## The Division of Labor

The architecture that emerges is:

| Task | Who Does It | Why |
|---|---|---|
| Disambiguation | LLM | Requires world knowledge, context, semantics |
| Annotation | LLM | Requires understanding of linguistic structure |
| Exact parsing | Grammar | Requires guaranteed structure, zero ambiguity |
| Inference | QBBN | Requires verifiable, traceable reasoning |
| Verification | QBBN | Requires formal proof trees |

The LLM is the **generator**. The formal system is the **verifier**. This is the
same generator-verifier pattern that appears in:

- Code generation (LLM writes code, compiler/tests verify)
- Mathematical proof (LLM proposes steps, proof assistant verifies)
- Scientific hypothesis (LLM generates hypotheses, experiment verifies)

## Alignment with the Bitter Lesson

This division aligns with Sutton's prescription. Both components scale with
computation:

- The **LLM** (annotator/generator) scales with model size, training data, and
  inference compute. Bigger models produce better annotations.
- The **QBBN** (verifier/reasoner) scales with graph size and iteration count.
  Larger knowledge bases produce more comprehensive inference.

What no longer scales with human effort is the construction of the formal
infrastructure. The LLM replaces the human in that role. The bitter lesson is
satisfied: the system scales with compute, not with linguist-hours.

## The Vibe Annotation Pattern

The semi-automatic bridge stage uses what we call "vibe annotation" — an extension
of Karpathy's "vibe coding" pattern to linguistic annotation:

1. **Describe** a linguistic phenomenon to the LLM
2. **Receive** a candidate grammar rule, lexicon entry, and test case
3. **Evaluate** against the formal system (grammar parse, inference engine)
4. **Refine** through dialogue until the formal system accepts the output
5. **Commit** the verified rule/entry/test to the knowledge base

Each cycle takes minutes. The equivalent process with human annotation took days
or weeks. The speedup is not incremental — it is qualitative. Phenomena that were
too expensive to cover (rare syntactic constructions, domain-specific vocabulary,
edge cases in quantifier scope) become feasible.

## The Steady State

The bridge is temporary. In the fully automated steady state:

1. Raw text arrives
2. LLM produces candidate logical forms
3. QBBN verifies for consistency
4. Inconsistencies are fed back to the LLM for revision
5. Verified logical forms enter the knowledge base
6. Inference runs over the knowledge base

No human is in the loop. The LLM generates; the QBBN verifies. Both scale with
compute. The formal infrastructure that once required a research institute to
build is now constructed and maintained autonomously.

## Key Sources

- Karpathy, A. "Vibe Coding." Post on X, February 2, 2025.
- Coppola, G. "Statistical Parsing for Logical Information Retrieval." 2026.
  Sections 3.2-3.3.

## Open Questions

- How good does the LLM annotator need to be for the system to be self-improving?
  Is there a quality threshold below which the verify-and-revise loop diverges?
- Can the QBBN's verification signal be used to fine-tune the LLM, creating a
  closed feedback loop?
- At what point does the vibe annotation bridge become unnecessary — when grammar
  coverage reaches 80%? 95%? 99%?
- Does the generator-verifier architecture generalize beyond NLP to other domains
  where formal verification is possible (mathematics, program synthesis, circuit
  design)?