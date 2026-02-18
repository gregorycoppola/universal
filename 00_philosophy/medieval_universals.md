# The Medieval Universals Debate

## The Problem

The medieval universals debate — one of the longest-running disputes in the
history of philosophy — is directly relevant to the QBBN because it asks the
fundamental question: **do abstract concepts really exist, and if so, how?**

When we write `predicate man {theme: e}` in the QBBN's lexicon, what is the
ontological status of `man`? Is it:

- A real thing that exists independently of any particular man? (**Realism**)
- A mental concept that exists only in minds? (**Conceptualism**)
- A mere name — a useful label with no existence beyond the word? (**Nominalism**)

The answer matters for the QBBN's claims about verification and hallucination.
If predicates are merely names, the QBBN is just manipulating symbols. If they
are real structures, the QBBN is reasoning about the world.

## The Three Positions

### Realism (Plato, Augustine, Scotus)

**Universals exist independently of particulars and minds.**

Plato's Forms are the paradigm case: the Form of Man exists in a separate realm,
and particular men participate in it. Medieval realists (following Augustine and
later Duns Scotus) softened this to: universals exist in the mind of God, or in
the natures of things themselves.

In QBBN terms: when we write `predicate man {theme: e}`, we are naming something
real — a genuine structure in the world that Socrates and Plato share. The
predicate is not just a label; it picks out a real universal.

**Implication for the QBBN**: If realism is correct, then the QBBN's knowledge
base is a (partial, approximate) map of the real structure of the world. Inference
over this map produces genuine knowledge. Hallucination is impossible by
construction because every conclusion traces back to real universals.

### Conceptualism (Abelard, Aquinas, Kant)

**Universals exist as concepts in the mind, abstracted from experience with
particulars.**

Peter Abelard (12th century) argued that universals are mental acts of
abstraction: you perceive particular men, notice what they have in common, and
form the concept MAN. The concept is real (it exists in the mind) but it does not
exist independently of minds.

Thomas Aquinas refined this: universals exist in three ways — in the mind of God
(ante rem), in particular things (in re), and in the human mind as abstractions
(post rem).

In QBBN terms: `predicate man {theme: e}` is a mental construct — a useful
abstraction that the system (or its human designer, or the LLM annotator) formed
by observing patterns in language and world. It does not name a Platonic Form;
it names a concept.

**Implication for the QBBN**: The knowledge base is a model of concepts, not of
the world directly. Inference is valid relative to the conceptual scheme, but
different conceptual schemes (different lexicons, different predicate
decompositions) might be equally valid. The QBBN does not hallucinate *within
its conceptual scheme*, but the scheme itself might not carve the world at its
joints.

### Nominalism (Ockham, Hobbes, Goodman)

**Universals are just names. Only particular things exist.**

William of Ockham (14th century) argued that universals are *nomina* — words that
we apply to groups of similar things for convenience. There is no "manness" shared
by Socrates and Plato; there are just Socrates and Plato, and we happen to call
them both "man."

Ockham's Razor — "entities should not be multiplied beyond necessity" — was
originally directed against realist ontologies that postulated unnecessary
abstract entities.

In QBBN terms: `predicate man {theme: e}` is just a string. It has no referent
beyond its use in the system. The system manipulates symbols according to rules;
the symbols do not "mean" anything in a metaphysical sense.

**Implication for the QBBN**: The system is a formal calculus, not a model of
reality. Inference is symbol manipulation. The absence of hallucination means only
that every output is derivable from the inputs — not that the outputs are "true"
in any deeper sense. This is actually the most defensible philosophical position
for a computational system: the QBBN provides formal guarantees about derivability,
not metaphysical guarantees about truth.

## The QBBN's Position

The QBBN is most naturally read as a **moderate conceptualist** system:

1. Predicates are **concepts** — structured mental representations (or their
   computational analogs) that organize experience.
2. Concepts have **real structure** — typed roles, argument positions, relations
   to other concepts — that is not arbitrary.
3. Inference over concepts produces **warranted belief** — conclusions that follow
   from premises via explicit, inspectable derivations.
4. The warrant is **formal** (derivability) not **metaphysical** (correspondence
   to Platonic Forms).

This is a practical position: the QBBN does not need to resolve the universals
debate to be useful. It needs only to provide formal guarantees about what follows
from what — which it does, regardless of whether predicates are real universals,
mental concepts, or mere names.

## Relevance to LLMs and Hallucination

The nominalist position is, implicitly, the position of modern deep learning:
words are tokens, embeddings are vectors, meaning is statistical co-occurrence.
There are no universals, no concepts, no logical structure — just patterns.

The problem with nominalism for AI is that it provides no basis for
**verification**. If words are just names and meaning is just statistics, there
is no way to check whether an output is correct. You can check whether it is
*likely* (the model assigns high probability), but likelihood is not truth.
Hallucinations are likely.

The conceptualist position — which the QBBN occupies — provides a verification
mechanism: conclusions must be derivable from premises through explicit rules.
This does not guarantee metaphysical truth, but it guarantees **logical
consistency** — which is exactly what hallucination-free reasoning requires.

## Key Works

- Abelard, P. *Logica Ingredientibus*. c. 1120.
- Aquinas, T. *Summa Theologica*. 1265-1274. Especially I, Q. 85.
- Ockham, W. *Summa Logicae*. c. 1323.
- Spade, P.V. "The Problem of Universals." *Stanford Encyclopedia of Philosophy*,
  2020.
- Klima, G. "The Medieval Problem of Universals." *Stanford Encyclopedia of
  Philosophy*, 2017.

## Open Questions

- Does the success or failure of the QBBN have implications for the universals
  debate, or is it neutral between the positions?
- If two QBBN systems with different lexicons (different predicate decompositions)
  produce different inferences from the same text, which is correct? The
  conceptualist says both can be; the realist says at most one is.
- Is Ockham's Razor an argument against the QBBN (which postulates a rich
  ontology of types, roles, and predicates) or for it (which eliminates the
  hidden, unverifiable "knowledge" in neural network weights)?