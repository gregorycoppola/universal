# Typed Predicates as Concepts

## The Idea

A concept, in the formal tradition from Frege (1879) onward, is a structured
unit of thought that can combine with other concepts to form complex thoughts.
Frege defined concepts as functions from objects to truth values: `man(·)` takes
an entity and returns true or false. "Dog" is a concept. "Red" is a concept.
"RED DOG" is a complex thought composed from two concepts by a combinatorial rule.

In the QBBN's logical language, concepts are **typed predicates with role-labeled
arguments**:

    predicate dog {theme: e}
    predicate red {theme: e}
    predicate chase {agent: e, patient: e}
    predicate give {agent: e, patient: e, recipient: e}

Each predicate defines a concept. The roles define the concept's **argument
structure** — the slots that must be filled to produce a complete thought.
chase is not a thought by itself; chase(agent: rex, patient: felix) is.

## Why Roles Matter

Traditional first-order logic uses **positional** arguments:

    chase(rex, felix)       -- who chases whom? depends on convention
    chase(felix, rex)       -- reversed meaning, same function name

The QBBN uses **labeled** arguments:

    chase(agent: rex, patient: felix)     -- rex chases felix
    chase(agent: felix, patient: rex)     -- felix chases rex

This is not a cosmetic difference. Labeled roles make concepts **self-documenting**:
you can read the logical form and understand the meaning without knowing an
arbitrary positional convention. More importantly, roles make concepts
**compositionally transparent**: the grammar can map from natural language directly
to role-filled predicates because dependency parses already identify grammatical
relations (subject, object, oblique) that map systematically to semantic roles
(agent, patient, theme).

This connection between grammatical relations and semantic roles is one of the
oldest insights in linguistics — Fillmore's Case Grammar (1968), Dowty's
proto-roles (1991), and the entire FrameNet/PropBank tradition. The QBBN's
role-labeled predicates make this connection explicit and computable.

## Types as Ontological Categories

Each role has a **type** that constrains what can fill it:

    predicate trust {agent: e, patient: e}          -- entities trust entities
    predicate believe {experiencer: e, content: s}   -- entities believe propositions
    predicate taller_than {theme: e, reference: e}   -- entities compared to entities

The type system defines the ontological categories of the language:

- **e** (entity): objects, people, places — things that exist
- **s** (sentential/propositional): complete thoughts — things that can be true or false
- **p** (predicate): properties and relations — things that can be said of entities

These three types correspond to the three tiers of expressiveness from Prawitz:

| Type | Prawitz Tier | Example |
|---|---|---|
| e | Tier 1: First-order | mortal(theme: socrates) |
| s | Tier 2: Propositional arguments | believe(experiencer: john, content: mortal(theme: socrates)) |
| p | Tier 3: Predicate quantification | ∀P: P(theme: x) → notable(theme: x) |

Types are not just a technical convenience. They are the **categories of thought**:
entities, propositions, and properties are the fundamental kinds of things that
formal reasoning represents. This is the same ontology found in Montague's type
theory (e, t, and functions over them), in Frege's distinction between objects and
concepts, and in Aristotle's categories.

## Concepts as Lexicon Entries

In the QBBN system, a concept is formally defined by a **lexicon entry**:

    predicate trust {agent: e, patient: e}
      "to have confidence or faith in someone"

    predicate mortal {theme: e}
      "subject to death"

    entity socrates : e
      "Greek philosopher, 470-399 BC"

The lexicon is the **vocabulary of the characteristica**. Each entry defines:

1. A predicate name (the concept's identity)
2. Typed roles (the concept's argument structure)
3. A natural language gloss (the bridge to surface language)

This is where the LLM-as-annotator thesis becomes concrete. Populating the lexicon
— defining every concept in a domain with its argument structure and natural
language description — is exactly the task that LLMs can automate. A linguist
might define 50 lexicon entries per day. An LLM can propose 500 per hour, with
a human reviewing and correcting.

## Composition

Concepts compose into thoughts through the grammar rules:

**Predication**: Filling a concept's roles with entities.
dog(theme: rex) — Rex is a dog.

**Conjunction**: Multiple concepts sharing a variable.
dog(theme: rex) & red(theme: rex) — Rex is a red dog.
(This is how Tier 1 handles compound concepts without lambda abstraction.)

**Implication**: One thought entailing another.
always [x:e]: dog(theme: x) -> animal(theme: x) — All dogs are animals.

**Embedding**: A thought as an argument to another thought.
believe(experiencer: john, content: dog(theme: rex)) — John believes Rex is a dog.

These four operations — predication, conjunction, implication, embedding — generate
the full space of expressible thoughts. This is productivity: a finite set of
concepts and four composition operations yield an infinite set of thoughts.

## Key Works

- Frege, G. *Begriffsschrift*. 1879.
- Fillmore, C.J. "The Case for Case." In *Universals in Linguistic Theory*, 1968.
- Dowty, D. "Thematic Proto-Roles and Argument Selection." *Language*, 67(3):547-619,
  1991.
- Jackendoff, R. *Semantic Structures*. MIT Press, 1990.
- Levin, B. *English Verb Classes and Alternations*. University of Chicago Press, 1993.

## Open Questions

- Is the set of semantic roles finite and universal, or language/domain-specific?
  FrameNet uses hundreds of frame-specific roles; the QBBN uses a smaller set of
  general roles (agent, patient, theme, experiencer, etc.). Which is correct?
- Can the type system be extended to handle gradable concepts (more/less, degree
  modification) without abandoning Boolean propositions?
- How do abstract concepts (justice, freedom, beauty) decompose into typed
  predicates? Are they primitive, or do they reduce to combinations of simpler
  concepts?