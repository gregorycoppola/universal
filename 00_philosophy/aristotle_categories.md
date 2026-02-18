# Aristotle's Categories and Syllogistic Logic

## From Forms to Categories

Aristotle studied under Plato but rejected the separate realm of Forms. His
response, developed in the *Categories*, the *Metaphysics*, and the *Prior
Analytics*, was to bring the Forms down to earth: universals exist, but they
exist **in** particulars, not apart from them.

Where Plato asked "what is the Form of Man?", Aristotle asked "what can be
**said of** a particular man?" The answer is a structured set of **categories**
— fundamental ways of predicating things of subjects.

## The Ten Categories

Aristotle identified ten categories of predication:

1. **Substance** (*ousia*): what a thing is — "Socrates is a man"
2. **Quantity**: how much — "Socrates is five feet tall"
3. **Quality**: what kind — "Socrates is wise"
4. **Relation**: in relation to what — "Socrates is taller than Plato"
5. **Place**: where — "Socrates is in Athens"
6. **Time**: when — "Socrates lived in the 5th century"
7. **Position**: in what posture — "Socrates is sitting"
8. **State**: in what condition — "Socrates is armed"
9. **Action**: what doing — "Socrates is teaching"
10. **Passion**: what undergoing — "Socrates is being judged"

These categories are **not arbitrary**. They represent the fundamental ways
concepts can relate to entities. And they map directly to the QBBN's type system:

| Aristotle's Category | QBBN Representation |
|---|---|
| Substance | `man(theme: socrates)` — unary predicate |
| Quality | `wise(theme: socrates)` — unary predicate |
| Relation | `taller_than(theme: socrates, reference: plato)` — binary predicate |
| Place | `in(theme: socrates, location: athens)` — role-labeled relation |
| Time | `before(theme: event1, reference: event2)` — temporal relation |
| Action | `teach(agent: socrates, patient: students)` — agent-patient structure |
| Passion | `judge(agent: court, patient: socrates)` — reversed agency |

The Categories are, in effect, a proto-ontology for semantic roles. Aristotle
noticed twenty-four centuries ago that predication has structure — that "Socrates
is wise" and "Socrates teaches Plato" are fundamentally different kinds of claims,
requiring different argument structures.

## The Syllogism

Aristotle's *Prior Analytics* introduced the **syllogism** — the first formal
system of logical inference: