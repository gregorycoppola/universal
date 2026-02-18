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
| Substance | man(theme: socrates) — unary predicate |
| Quality | wise(theme: socrates) — unary predicate |
| Relation | taller_than(theme: socrates, reference: plato) — binary predicate |
| Place | in(theme: socrates, location: athens) — role-labeled relation |
| Time | before(theme: event1, reference: event2) — temporal relation |
| Action | teach(agent: socrates, patient: students) — agent-patient structure |
| Passion | judge(agent: court, patient: socrates) — reversed agency |

The Categories are, in effect, a proto-ontology for semantic roles. Aristotle
noticed twenty-four centuries ago that predication has structure — that "Socrates
is wise" and "Socrates teaches Plato" are fundamentally different kinds of claims,
requiring different argument structures.

## The Syllogism

Aristotle's *Prior Analytics* introduced the **syllogism** — the first formal
system of logical inference:

    All men are mortal.          (Major premise)
    Socrates is a man.           (Minor premise)
    Therefore, Socrates is mortal.  (Conclusion)

This is **modus ponens** — the same inference rule implemented by the QBBN's
AND + OR factors with forward π messages. Aristotle's syllogism is, quite
literally, the first example of the inference pattern that belief propagation
computes.

Aristotle identified 256 possible syllogistic forms and proved that exactly 24
are valid. This was the first **completeness result** in logic — a bounded
enumeration of all valid inference patterns in a formal system. It stood for
two thousand years until Frege generalized it.

## Substance and Predication

Aristotle's distinction between **substance** (what a thing is) and **accident**
(what can be said of it) maps to the QBBN's distinction between **entities**
and **predicates**:

- socrates : e is a substance — a particular, independently existing thing
- man {theme: e} is a predicate — something said of substances
- man(theme: socrates) is a predication — a substance falling under a predicate

This distinction is not just philosophical. It is the foundation of the type
system. Entities and predicates are different types precisely because Aristotle
was right: there is a fundamental asymmetry between things and what is said of
them. You can predicate "man" of Socrates, but you cannot predicate Socrates of
"man." The type system enforces this: e fills roles in predicates, but
predicates do not fill roles in entities.

## From Aristotle to Frege

Aristotle's system was limited to categorical syllogisms — a fragment of what we
now call monadic first-order logic. It could not handle:

- **Relations**: "Socrates is taller than Plato" (binary predicates)
- **Nested quantification**: "Every person loves someone" (mixed quantifiers)
- **Propositional connectives**: "If it rains, then the ground is wet" (material
  conditional beyond categorical form)

These limitations persisted for over two thousand years. Medieval logicians
(Ockham, Buridan, Scotus) extended the system but could not break free of the
syllogistic framework. The breakthrough came with Frege's *Begriffsschrift*
(1879), which generalized Aristotle's categories into a full predicate calculus
with quantifiers, variables, and truth-functional connectives.

The QBBN's logical language is a direct descendant of Frege's generalization of
Aristotle — but with role labels (from Fillmore and the dependency grammar
tradition) replacing positional arguments, and probabilistic weights (from Pearl)
replacing deterministic truth values.

## Key Works

- Aristotle. *Categories*. c. 350 BC.
- Aristotle. *Prior Analytics*. c. 350 BC.
- Aristotle. *Metaphysics*. c. 340 BC.
- Ackrill, J.L. *Aristotle's Categories and De Interpretatione*. Oxford, 1963.
- Smith, R. "Aristotle's Logic." *Stanford Encyclopedia of Philosophy*, 2020.

## Open Questions

- Are Aristotle's ten categories the right ontology for a knowledge
  representation system, or is a simpler set (entity, property, relation)
  sufficient?
- Does the QBBN's treatment of all predicates as the same kind of object
  (differing only in role signatures) lose something that Aristotle's categorical
  distinctions captured?
- Is the syllogism truly the historical ancestor of belief propagation, or is
  this an anachronistic reading?