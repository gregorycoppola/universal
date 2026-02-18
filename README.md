# Universal Grammar and the Language of Concepts

A collection of notes exploring the connection between Chomsky's Universal Grammar,
Fodor's Language of Thought, and the typed logical language developed in
[Statistical Parsing for Logical Information Retrieval](https://github.com/gregorycoppola/world) (Coppola, 2026).

## Thesis

The typed logical language of the QBBN — role-labeled predicates, quantified Horn clauses,
three tiers of expressiveness from Prawitz — is a *language of concepts*: a formal
Mentalese in which every thought is compositional, every inference is traceable, and every
conclusion is verifiable. LLMs lack this language, which is why they hallucinate. The
QBBN provides it, which is why it doesn't.

## Reading Order

### 0. Philosophy
The deep history — from Plato's Forms to Frege's concept-script:

1. [Plato: Theory of Forms](00_philosophy/plato_forms.md) — Abstract universals and the allegory of the cave
2. [Aristotle: Categories and Syllogisms](00_philosophy/aristotle_categories.md) — Predication, substance, and the first formal logic
3. [The Medieval Universals Debate](00_philosophy/medieval_universals.md) — Do abstract concepts really exist?
4. [From Leibniz to Frege](00_philosophy/leibniz_to_frege.md) — The dream of a universal language, through Kant, Russell, Wittgenstein, and Carnap

### 1. Foundations
The five intellectual ancestors of the QBBN:

1. [Chomsky: Universal Grammar](01_foundations/chomsky_universal_grammar.md) — The claim that language has innate structure
2. [Fodor: Language of Thought](01_foundations/fodor_language_of_thought.md) — The claim that thought itself is language-like
3. [Montague: Formal Semantics](01_foundations/montague_formal_semantics.md) — The math that connects language to logic
4. [Prawitz: Natural Deduction](01_foundations/prawitz_natural_deduction.md) — The proof theory that constrains inference
5. [Pearl: Probabilistic Reasoning](01_foundations/pearl_probabilistic_reasoning.md) — The machinery that makes it run

### 2. The Bitter Lesson
Why formal NLP failed historically and why LLMs change the equation:

1. [Sutton's Bitter Lesson](02_the_bitter_lesson/sutton_bitter_lesson.md) — General methods that scale with compute always win
2. [Why Formal NLP Failed](02_the_bitter_lesson/formal_nlp_failure.md) — The annotation bottleneck
3. [The LLM as Annotator](02_the_bitter_lesson/llm_as_annotator.md) — Why LLMs change the equation

### 3. Language of Concepts
The novel synthesis — connecting the QBBN's logical language to Fodor's LOT and Chomsky's UG:

1. [What Is a Language of Thought?](03_language_of_concepts/what_is_lot.md) — Fodor's requirements and the QBBN as LOT
2. [Typed Predicates as Concepts](03_language_of_concepts/typed_predicates_as_concepts.md) — Role-labeled predicates = structured concepts
3. [The Three Tiers](03_language_of_concepts/three_tiers.md) — Prawitz's tiers as levels of conceptual complexity
4. [UG as Interface Specification](03_language_of_concepts/ug_as_interface.md) — Grammar rules as the universal mapping

### 4. Hallucination
*(Coming soon)* Why this matters: LLMs have no language of thought, and that's why they hallucinate.

### 5. Synthesis
*(Coming soon)* The full argument and architecture.

## Related Work
- [The QBBN Paper (2024)](https://arxiv.org/abs/2402.06557)
- [Statistical Parsing for Logical Information Retrieval (2026)](https://github.com/gregorycoppola/world)
- [Super Sonic Vibes](https://supersonicvibes.club)