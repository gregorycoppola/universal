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

### 4. Hallucination and Verification
Why this matters — LLMs hallucinate because they lack formal language, and formal verification is the solution:

1. [Why LLMs Hallucinate](04_hallucination/why_llms_hallucinate.md) — No LOT, no verification, no grounding
2. [The Verification Gap](04_hallucination/verification_gap.md) — The runtime analogy — you trust code because you run it
3. [The QBBN as Runtime](04_hallucination/qbbn_as_runtime.md) — The QBBN as a "Python interpreter" for thought
4. [Formal Verification](04_hallucination/formal_verification.md) — Why natural language must be translated to formal language to be checked

### 5. Synthesis
The full argument and architecture:

1. [The Universal Language Thesis](05_synthesis/universal_language_thesis.md) — The big claim: typed logical language = universal language
2. [The Architecture](05_synthesis/architecture.md) — LLM preprocesses → grammar parses → QBBN infers
3. [Vibe Science Methodology](05_synthesis/vibe_science_methodology.md) — How this was built, the bridge stage

### 6. References

1. [Bibliography](06_references/bibliography.md) — Full reference list
2. [Reading List](06_references/reading_list.md) — Recommended reading order for newcomers

### 7. Metaphysics
The Platonic argument — four independent convergences on the reality of formal structure:

1. [Index: The Four Convergences](07_metaphysics/index.md) — Overview and the self-application argument
2. [Computational Parsimony](07_metaphysics/computational_parsimony.md) — Cheapest to run
3. [Information-Theoretic Parsimony](07_metaphysics/information_theoretic_parsimony.md) — Shortest to encode
4. [Conceptual Parsimony](07_metaphysics/conceptual_parsimony.md) — Simplest to understand
5. [Historical Convergence](07_metaphysics/historical_convergence.md) — Independently rediscovered by everyone who tries

### 8. Computability
The QBBN's position in the computability landscape — why the forward fragment is the sweet spot:

1. [Index: Computability and the Forward Fragment](08_computability/index.md) — Overview and the key insight
2. [FOL and Turing Completeness](08_computability/fol_turing_completeness.md) — The bidirectional equivalence
3. [The Turing Machine Encoding](08_computability/turing_encoding.md) — How to encode a TM in Horn clauses
4. [Prawitz's Rules and Computability](08_computability/prawitz_computability.md) — The minimal Turing-complete fragment of natural deduction
5. [The Datalog Boundary](08_computability/datalog_boundary.md) — Finite grounding = decidability
6. [The Complexity Landscape](08_computability/complexity_landscape.md) — Where every fragment sits
7. [Why Sub-Turing Is a Feature](08_computability/sub_turing_feature.md) — Termination as a prerequisite for trust

### 9. Interpretability
The QBBN as a solution to the interpretability problem:

1. [Index](09_interpretability/index.md) — Overview
2. [The Interpretability Problem](09_interpretability/interpretability_problem.md) — Why neural networks are opaque
3. [Verification over Interpretation](09_interpretability/verification_over_interpretation.md) — Don't interpret the model, verify the output
4. [UG as Interface](09_interpretability/ug_as_interface.md) — The typed language as the human-machine boundary
5. [Human-Computer Fusion](09_interpretability/human_computer_fusion.md) — LLM generates, QBBN verifies, human directs

### 10. Applications
The universal language beyond natural language — software engineering as the first application:

1. [Index: Applications](10_applications/index.md) — Why software architecture is the most immediate application
2. [Software Architecture as Logic](10_applications/software_architecture.md) — Components are entities, dependencies are Horn clauses, the architecture diagram is a factor graph
3. [Functions as Relations](10_applications/functions_as_relations.md) — Data flow through shared variables, functions as predicates with output roles
4. [Workflow Verification](10_applications/workflow_verification.md) — DAG-shaped workflows, failure propagation via backward inference, soft dependencies via modal quantifiers
5. [The Formal Verification Landscape](10_applications/formal_verification_landscape.md) — Testing → static analysis → model checking → theorem proving, and where the QBBN sits (Level 2: model checking with probability)
6. [The Verification Bottleneck and LLMs](10_applications/verification_bottleneck.md) — The annotation bottleneck in verification mirrors NLP; LLMs solve both the same way
7. [The Logic Programming Connection](10_applications/logic_programming_connection.md) — Prolog, Datalog, CLP, ProbLog, MLNs — the family tree and where the QBBN sits
8. [The Vibe Coding Connection](10_applications/vibe_coding.md) — LLM generates code, QBBN holds the spec, same architecture as natural language verification
9. [Prolog Examples](prolog/) — Runnable logic programming examples demonstrating the concepts

## Key Open Questions

- **Functions and values**: The calculus handles truth values but not computed values. The logic programming tradition (Prolog, Datalog, CLP) maps the design space. The QBBN sits at Datalog (decidable, no function symbols). Extending to computed values requires careful design to preserve decidability. See [Functions as Relations](10_applications/functions_as_relations.md).

- **Testing as verification**: Two levels mirror Rust's compilation pipeline. Level 1 (compilation): does the logical form type-check? Level 2 (inference): does the factor graph produce the expected posterior? The growing test suite is both a grammar coverage test and an inference test.

- **The verification bottleneck**: Writing formal specifications is as expensive as writing formal linguistic annotations. LLMs solve both bottlenecks the same way — generate candidates, verify formally, repair iteratively. See [The Verification Bottleneck and LLMs](10_applications/verification_bottleneck.md).

## Related Work
- [The QBBN Paper (2024)](https://arxiv.org/abs/2402.06557)
- [Statistical Parsing for Logical Information Retrieval (2026)](https://github.com/gregorycoppola/world)
- [Super Sonic Vibes](https://supersonicvibes.club)