# Fodor's Language of Thought

## The Hypothesis

Jerry Fodor's Language of Thought (LOT) hypothesis, introduced in *The Language of
Thought* (1975), claims that cognitive processes operate over a compositional
representational system — a "Mentalese" — that has the structural properties of a
language but is not identical to any natural language.

The core properties of Mentalese:

- **Compositionality**: Complex thoughts are built from simpler ones by systematic
  rules. The thought JOHN LOVES MARY is composed from JOHN, LOVES, and MARY in a
  way that determines its meaning from the meanings of its parts.
- **Productivity**: A finite set of concepts and rules generates an infinite set of
  possible thoughts.
- **Systematicity**: If you can think JOHN LOVES MARY, you can also think MARY
  LOVES JOHN. The capacity to entertain one thought entails the capacity to
  entertain structurally related thoughts.

## The Argument

Fodor's argument is structural, not empirical. It proceeds:

1. Thought is computational (the computational theory of mind).
2. Computation requires representations to operate over.
3. These representations must be compositional to explain productivity and
   systematicity.
4. Therefore, thought operates over a compositional representational system — a
   language.

This is not a claim that we think "in English" or "in Chinese." Mentalese is
*pre-linguistic* — it's the medium in which meanings are represented before they are
expressed in any natural language. Translation between natural languages is possible
precisely because both map onto the same underlying Mentalese.

## LOT vs. Connectionism

The LOT hypothesis was the central battleground in the "classical vs. connectionist"
debate of the 1980s-90s. Connectionists (Rumelhart, McClelland, Smolensky) argued
that cognition operates over distributed representations — patterns of activation
across networks — not discrete symbols.

Fodor and Pylyshyn's famous reply (1988) argued that distributed representations
cannot explain systematicity without implementing a compositional structure — in
which case they are just an implementation of LOT, not an alternative to it.

This debate is directly relevant to LLMs. LLMs are the most powerful connectionist
systems ever built. They demonstrate remarkable linguistic competence. But they
cannot verify their own reasoning, cannot trace their inferences, and hallucinate
confidently. Fodor would say: they lack a Language of Thought.

## Relevance to This Project

The typed logical language of the QBBN is a candidate Language of Thought — a formal
Mentalese with the properties Fodor identified:

- **Compositionality**: `trust(agent: jack, patient: jill)` is composed from
  typed predicates and role-labeled arguments in a way that determines its meaning.
- **Productivity**: A finite lexicon and grammar generates an unbounded set of
  logical forms.
- **Systematicity**: If the system can represent `trust(agent: jack, patient: jill)`,
  it can represent `trust(agent: jill, patient: jack)` — the roles are explicit.

The QBBN adds something Fodor's LOT lacked: a **computational semantics**. Fodor
said thought was compositional but never specified the inference mechanism. The QBBN
provides one: belief propagation over factor graphs with AND, OR, and NEG factors.
Mentalese now has a runtime.

## The LLM Connection

LLMs map natural language to distributed representations (embeddings) and back.
The QBBN maps natural language to discrete logical forms and reasons over them.

The synthesis is: LLMs handle the *mapping* (natural language ↔ Mentalese), while
the QBBN handles the *reasoning* (inference within Mentalese). This is exactly
the architecture in the paper: LLM preprocesses → grammar parses → QBBN infers.

The LLM is the encoder/decoder. The QBBN is the Language of Thought.

## Key Works

- Fodor, J. *The Language of Thought*. Harvard University Press, 1975.
- Fodor, J. and Pylyshyn, Z. "Connectionism and Cognitive Architecture: A Critical
  Analysis." *Cognition*, 28:3-71, 1988.
- Fodor, J. *LOT 2: The Language of Thought Revisited*. Oxford University Press, 2008.
- Pinker, S. *The Language Instinct*. William Morrow, 1994.

## Open Questions

- If LLMs can approximate systematic reasoning without explicit LOT, does that
  weaken Fodor's argument or confirm it (since the training data encodes LOT-like
  structure)?
- Is the QBBN's logical language *the* LOT, or *a* LOT — one of many possible
  formal Mentaleses?
- Does the three-tier structure (entities, propositions-as-arguments, predicate
  quantification) correspond to levels of cognitive complexity in human thought?