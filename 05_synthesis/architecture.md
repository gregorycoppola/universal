# The Architecture

## Overview

The complete system has four stages:

    Natural Language → LLM Preprocesses → Grammar Parses → LLM Reranks → QBBN Infers

Each stage has a precise function, a precise input/output contract, and a precise
relationship to the intellectual tradition described in this collection.

## Stage 1: Natural Language Input

**Input**: Raw text — sentences, paragraphs, documents.

**Properties**: Ambiguous, unstructured, unverified. Words have multiple senses.
Prepositional phrases attach ambiguously. Quantifier scope is underspecified.
Pronouns are unresolved. This is the cave — the world of shadows.

**Relevant tradition**: The later Wittgenstein (meaning is use), the statistical
NLP revolution (language is data).

## Stage 2: LLM Preprocessing

**Input**: Raw text.
**Output**: Disambiguated text — each word tagged with its part of speech, sense,
and intended attachment.

**Operations**:
1. Spelling correction and normalization
2. Tokenization and segmentation
3. Lemmatization (reducing to canonical forms)
4. Word sense disambiguation
5. Part-of-speech tagging
6. PP attachment resolution

**Properties**: The LLM uses world knowledge and semantic context to resolve
ambiguities that are irresolvable by structural means alone. "I saw the man with
the telescope" is ambiguous in isolation but clear in context. The LLM provides
the context.

**Performance**: 95% accuracy on PP attachment (vs. 50% for the Stanford parser).
89-91% on POS tagging (with most "errors" reflecting annotation conventions).
These numbers are for zero-shot prompting — no fine-tuning required.

**What it is**: The annotator. Leibniz's scribe. The mechanism by which raw
language is prepared for formal treatment.

**What it is not**: A reasoner. The LLM does not perform inference at this stage.
It disambiguates — it selects from among possible readings. This is pattern
matching, not logical reasoning, and LLMs are excellent at it.

**Relevant tradition**: The statistical NLP revolution (amortize annotation over
training), the bitter lesson (scale with compute), Karpathy's vibe annotation
(LLMs as linguistic annotators).

## Stage 3: Grammar Parsing

**Input**: Disambiguated text + lexicon.
**Output**: Typed logical forms — ground facts and quantified rules in the QBBN's
logical language.

**Operations**:
1. Tokenize the sentence
2. Look up each content word in the lexicon (binding to typed predicates/entities)
3. Skip function words
4. Dispatch to a grammar rule based on the pattern of matched types
5. Emit the logical form

**Properties**: Deterministic. Zero ambiguity on disambiguated input (33/33
sentences, 0 ambiguous parses). Type-driven dispatch ensures exactly one rule
fires. The grammar is the compiler — it translates from natural language to the
universal language.

**Key guarantee**: If the grammar produces output, the output is a well-formed
logical form. The grammar never guesses, never approximates, never hallucinates.
It either compiles correctly or fails explicitly.

**What it is**: The compiler. Montague's syntax-semantics homomorphism, realized
computationally. Chomsky's Universal Grammar, implemented as a finite set of
type-driven rules.

**What it is not**: A parser in the traditional sense. Traditional parsers handle
ambiguity (producing multiple parses, ranked by probability). This grammar does
not handle ambiguity — that is the LLM's job. The grammar handles compilation —
the deterministic mapping from disambiguated input to logical form.

**Relevant tradition**: Montague Grammar (compositional semantics), categorial
grammar (type-driven parsing), Chomsky's UG (universal structural patterns),
compiler theory (deterministic translation).

## Stage 4: LLM Reranking (When Needed)

**Input**: Multiple candidate parses from the grammar.
**Output**: The best parse, selected by semantic plausibility.

**When it fires**: Only when preprocessing fails to fully disambiguate — when the
grammar produces multiple parses for the same input. In our evaluation, this
never happened (0 ambiguous parses), but it will happen at scale.

**Properties**: 95% accuracy when directed to evaluate a specific ambiguous
construction. 50% accuracy on general critique (no better than chance). The
grammar identifies *where* ambiguity exists; the LLM resolves *which* reading
is correct.

**What it is**: The quality gate. The post-compilation optimizer. The mechanism
that handles the residual ambiguity that preprocessing missed.

**Relevant tradition**: Parse reranking (Collins, 2000; Charniak and Johnson,
2005), LLMs as linguistic judges.

## Stage 5: QBBN Inference

**Input**: Knowledge base (typed predicates, ground facts, quantified rules) +
query.
**Output**: Posterior probability with proof tree.

**Operations**:
1. Parse the logical language
2. Ground all quantified rules (substitute entities for variables)
3. Build factor graph via bidirectional expansion from query
4. Run belief propagation with damping
5. Classify result: yes (P > 0.5), no (P < 0.5), unknown (P ≈ 0.5)

**Properties**: 44/44 test cases pass. All converge within 20 iterations. Every
conclusion traces back through explicit derivation. No hallucination possible by
construction.

**What it is**: The runtime. Leibniz's calculus ratiocinator. Pearl's belief
propagation, applied to Prawitz's natural deduction. Plato's dialectic,
mechanized.

**What it is not**: A theorem prover (it does not search for proofs — it
propagates beliefs). A neural network (it does not learn — it computes). An
LLM (it does not generate — it derives).

**Relevant tradition**: Pearl (belief propagation), Prawitz (natural deduction),
Gentzen (sequent calculus), Aristotle (syllogistic logic).

## The Division of Labor

The architecture embodies a clean separation of concerns:

| Concern | Component | Tradition |
|---|---|---|
| Ambiguity resolution | LLM | Statistical NLP |
| Structural compilation | Grammar | Formal linguistics |
| Quality control | LLM reranking | Parse reranking |
| Logical inference | QBBN | Proof theory + graphical models |

Each component does what it is best at. The LLM handles soft, context-dependent,
knowledge-intensive tasks (disambiguation, annotation, reranking). The formal
components handle hard, structure-dependent, correctness-critical tasks
(compilation, type-checking, inference).

This division is not an engineering convenience. It is a reflection of a deep
asymmetry between two kinds of intelligence: the ability to understand context
(which LLMs have and formal systems lack) and the ability to guarantee correctness
(which formal systems have and LLMs lack). The architecture combines both.

## Scalability

Each component scales with computation:

- **LLM preprocessing** scales with model size and inference compute. Bigger
  models disambiguate better.
- **Grammar parsing** scales with lexicon size and rule count. More rules cover
  more patterns.
- **LLM reranking** scales with model size. Bigger models make better judgments.
- **QBBN inference** scales with graph size and iteration count. Larger knowledge
  bases support more comprehensive inference.

Nothing scales with human effort. The LLM replaces the human annotator. The
grammar rules are authored with LLM assistance. The lexicon is populated by LLM
generation. The coverage tests are designed through LLM-assisted iteration. The
bitter lesson is satisfied.

## Key Sources

- Coppola, G. "Statistical Parsing for Logical Information Retrieval." 2026.
  Section 8.6 (The Synthesis).

## Open Questions

- Can the four stages be collapsed into fewer stages without losing correctness
  guarantees?
- What is the latency budget for each stage in a real-time system?
- Can the grammar and QBBN be compiled to GPU-accelerated code for parallel
  execution?
- At what scale does the architecture break — thousands of facts? Millions?
  Billions?