# From Leibniz to Frege: The Dream of a Universal Language

## Leibniz's Vision

Gottfried Wilhelm Leibniz (1646-1716) dreamed of two things that together
constitute the earliest clear articulation of what the QBBN attempts:

1. A **characteristica universalis** — a universal formal language in which all
   human knowledge could be expressed unambiguously.
2. A **calculus ratiocinator** — a mechanical procedure for reasoning in that
   language, such that disputes could be settled by computation.

Leibniz wrote in 1685:

> "If we had it [the characteristica universalis], we should be able to reason in
> metaphysics and morals in much the same way as in geometry and analysis."

And more boldly:

> "If controversies were to arise, there would be no more need of disputation
> between two philosophers than between two accountants. For it would suffice to
> take their pencils in hand, to sit down to their slates, and to say to each
> other: *Calculemus!* — Let us calculate."

This is precisely the QBBN's value proposition: express knowledge in a typed
logical language (characteristica), run belief propagation (calculus ratiocinator),
and read off the answer. No hallucination, no disputation, no ambiguity — just
calculation.

## Why Leibniz Failed

Leibniz never built either system. The obstacles were:

1. **No formal logic**: Aristotle's syllogistic was too weak. Leibniz needed
   predicate logic with quantifiers and relations, which would not exist for
   another two centuries.
2. **No computation**: Leibniz built mechanical calculators for arithmetic, but
   had no way to mechanize logical inference.
3. **No ontology**: Leibniz could not specify the "alphabet of human thought" —
   the atomic concepts from which all knowledge would be composed. This is the
   same problem Fodor faced with Mentalese.

The dream was correct. The technology was three centuries away.

## The British Empiricists and the Problem of Abstraction

Between Leibniz and Frege, the British empiricists — Locke, Berkeley, Hume —
raised a fundamental challenge to the entire project of universal concepts.

**Locke** (1690) argued that abstract ideas are formed by stripping away
particulars: you see many triangles, abstract away the specific angles and sizes,
and arrive at the "abstract idea" of Triangle. This is essentially concept
formation by generalization — not unlike how LLMs form representations from
training data.

**Berkeley** (1710) objected that you cannot form a mental image of "triangle in
general" — any triangle you imagine has specific angles. Abstract ideas, he
argued, are impossible. What we have instead are particular ideas that serve as
**representatives** of their class.

**Hume** (1739) sided with Berkeley but added that our concept of causation — the
most important relation for reasoning — is not a logical necessity but a **habit
of mind** formed by repeated experience.

The empiricist challenge matters because it questions whether the "universal
language" can have a fixed vocabulary. If concepts are abstractions from
experience, they vary across individuals and cultures. There is no "alphabet of
human thought" — just statistical regularities.

The QBBN's response: the vocabulary (lexicon) is not universal, but the
**structure** (typed predicates, role labels, quantified rules) is. Different
domains have different predicates, but all predicates have typed roles, and all
rules have the same logical form. The universality is structural, not lexical.

## Kant's Synthesis

Immanuel Kant (1781) attempted to resolve the empiricist challenge by arguing that
the mind imposes **categories** on experience — not Aristotle's ten categories,
but twelve categories of the understanding organized by quantity, quality,
relation, and modality.

Kant's categories are the conditions for the possibility of experience itself.
You cannot perceive anything without categorizing it as a substance with
properties, standing in causal relations, existing at a time and place.

The Kantian view maps to the QBBN's type system:

- **Categories of quantity** → quantifiers (always, usually, sometimes)
- **Categories of quality** → truth values (positive, negative)
- **Categories of relation** → predicate roles (agent, patient, cause, effect)
- **Categories of modality** → Tier 2 modal predicates (possible, necessary, should)

Kant argued these categories are **a priori** — known prior to experience. In
the QBBN, the type system is prior to any particular knowledge base. You define
the types before you define the predicates. The structure precedes the content.

## Frege's Revolution

Gottlob Frege's *Begriffsschrift* ("Concept-Script," 1879) finally delivered
what Leibniz had dreamed of: a formal language expressive enough to capture
mathematical and logical reasoning, with a mechanical procedure for deriving
conclusions.

Frege's contributions:

1. **Predicate logic**: Generalized Aristotle's subject-predicate structure to
   arbitrary predicates with multiple arguments. `loves(john, mary)` rather than
   just "John is mortal."
2. **Quantifiers**: Universal (∀) and existential (∃) quantification, binding
   variables in predicates. `∀x: man(x) → mortal(x)`.
3. **Compositionality**: The meaning of a complex expression is a function of the
   meanings of its parts — now called **Frege's Principle**, the foundation of all
   formal semantics.
4. **Function-argument structure**: Concepts are functions from objects to truth
   values. `man(·)` is a function that takes an entity and returns true or false.

Frege's system is the direct ancestor of the QBBN's logical language. The QBBN
adds three things Frege lacked: role labels (from 20th century linguistics),
probabilistic weights (from Pearl), and a connection to natural language (from
Montague and the parsing tradition).

## Russell and Logical Atomism

Bertrand Russell extended Frege's logic and developed **logical atomism** (1918):
the view that the world consists of atomic facts, and language is meaningful
insofar as it pictures these facts.

Russell's atomic facts are the QBBN's ground facts: