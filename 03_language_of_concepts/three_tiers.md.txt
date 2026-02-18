# The Three Tiers of Conceptual Complexity

## Overview

Prawitz's *Natural Deduction* (1965) organizes logic into levels of increasing
expressiveness. The QBBN paper maps these levels to three tiers of the typed
logical language and claims they are **sufficient for natural language semantics**.

This document unpacks that claim. What does each tier handle? What phenomena
require which tier? And why should three tiers be enough?

## Tier 1: First-Order Quantification Over Entities

**Prawitz Chapters I-IV. The workhorse.**

Tier 1 handles everything that can be expressed with entities, predicates, and
universally quantified Horn clauses with negation.

### What It Covers

**Simple predication**: Socrates is a man.

    man(theme: socrates)

**Classification and taxonomy**: All men are mortal.

    always [x:e]: man(theme: x) -> mortal(theme: x)

**Relations**: Jack trusts Jill.

    trust(agent: jack, patient: jill)

**Transitive chains**: If A is taller than B and B is taller than C, then A is
taller than C.

    always [x:e, y:e, z:e]:
      taller_than(theme: x, reference: y)
      & taller_than(theme: y, reference: z)
      -> taller_than(theme: x, reference: z)

**Negation and contrapositive**: Zeus is not mortal, therefore Zeus is not a man.

    not mortal(theme: zeus)

Combined with the rule above, belief propagation infers not man(theme: zeus).

**Conjunction in premises**: If someone is a man and is king, they are powerful.

    always [x:e]:
      man(theme: x) & king(theme: x) -> powerful(theme: x)

**Causation**: Rain causes flooding.

    always [x:e]: rain(location: x) -> flooding(location: x)

**Spatial reasoning**: Paris is in France. France is in Europe. Therefore Paris
is in Europe. Handled by transitivity of in(theme: x, location: y).

**Temporal reasoning**: Event A is before B. B is before C. Therefore A is before
C. Handled by transitivity of before(theme: x, reference: y).

### What It Cannot Cover

- Sentences about beliefs, desires, or obligations ("John believes it will rain")
- Sentences where a verb takes a whole clause as argument ("I want you to leave")
- Definitions that quantify over properties ("A bachelor is an unmarried man")

These require Tiers 2 and 3.

## Tier 2: Propositions as Arguments

**Prawitz Chapters V-VI. The modal tier.**

Tier 2 allows a predicate to take a **full proposition** as an argument, via the
sentential type s:

    predicate should {content: s}
    predicate believe {experiencer: e, content: s}
    predicate want {experiencer: e, content: s}
    predicate know {experiencer: e, content: s}
    predicate say {agent: e, content: s}

### What It Covers

**Modal verbs**: Mary should be careful.

    should(content: careful(theme: mary))

**Propositional attitudes**: John believes Socrates is mortal.

    believe(experiencer: john, content: mortal(theme: socrates))

**Desires and intentions**: Mary wants John to apologize.

    want(experiencer: mary, content: apologize(agent: john))

**Reported speech**: John said that it will rain.

    say(agent: john, content: rain(location: here))

**Epistemic modals**: It is possible that Socrates was wrong.

    possible(content: wrong(theme: socrates))

### The Key Technical Achievement

Variables can cross into embedded propositions. In:

    always [o:e]: offend(agent: o) -> should(content: apologize(agent: o))

The variable o is bound by the outer quantifier but appears inside the embedded
proposition apologize(agent: o). The grounding engine handles this correctly —
when o is instantiated to john, the result is:

    should(content: apologize(agent: john))

This is what makes Tier 2 genuinely expressive rather than a notational trick.
Propositions are first-class values that participate in quantification.

### What It Cannot Cover

- Quantification over properties ("Every positive trait is admirable")
- Compound predicates built by abstraction ("a tall, funny man")
- Definitions that involve predicate variables

These require Tier 3.

## Tier 3: Predicate Quantification and Lambda Abstraction

**Prawitz Chapter V. The theoretical frontier.**

Tier 3 allows variables that range over **predicates** rather than entities, and
**lambda abstraction** for building compound predicates:

    ∀P: positive_trait(P) → admirable(P)
    λx. man(x) ∧ tall(x)     -- the compound predicate "tall man"

### What It Would Cover

**Quantification over properties**: Everything fun is worth trying.

    always [P:p]: fun(P) -> worth_trying(P)

**Compound predicates**: A tall man entered.

    (λx. man(theme: x) ∧ tall(theme: x))(theme: stranger1)

**Definitions**: A bachelor is an unmarried man.

    always [x:e]: bachelor(theme: x) ↔ man(theme: x) ∧ unmarried(theme: x)

### Current Status

Tier 3 is **designed but not yet tested** in the inference engine. For common
cases, Tier 1's conjunction in rule premises handles the same phenomena:

    always [x:e]: man(theme: x) & tall(theme: x) -> impressive(theme: x)

This avoids lambda abstraction for the most frequent use case (intersective
adjectives). Full predicate quantification is needed only for genuinely
higher-order phenomena, which are relatively rare in everyday language.

## The Sufficiency Argument

The claim is that these three tiers are **sufficient** for natural language
semantics. The argument:

1. Every natural language sentence describes a situation involving **entities**
   (people, objects, places), **properties** (tall, mortal, funny), and
   **relations** (trusts, taller than, in).

2. These descriptions are structured by **quantification** (all, some, no),
   **negation** (not), **conjunction** (and), **implication** (if-then), and
   **embedding** (believes that, wants to, should).

3. Tier 1 handles entities, properties, relations, quantification, negation,
   conjunction, and implication.

4. Tier 2 handles embedding — propositions as arguments to modal, attitudinal,
   and communicative predicates.

5. Tier 3 handles quantification over properties and compound predicate
   construction.

6. There is nothing left. Every natural language sentence decomposes into some
   combination of these elements.

The remaining work is **lexical** — determining which words map to which predicates,
which roles they take, and what types their arguments have. This is vocabulary,
not logic. And vocabulary is exactly what LLMs can provide at scale.

## Key Works

- Prawitz, D. *Natural Deduction*. 1965. Especially Chapters I-VI.
- Montague, R. "The Proper Treatment of Quantification in Ordinary English." 1973.
- Partee, B. "Compositionality." In *Varieties of Formal Semantics*, 1984.
- Chierchia, G. and McConnell-Ginet, S. *Meaning and Grammar*. MIT Press, 2000.

## Open Questions

- Are three tiers truly sufficient, or are there natural language phenomena
  (generics, habituals, mass nouns, degree modification) that require a fourth?
- Can Tier 3 be eliminated entirely in favor of Tier 1 conjunction, or are there
  irreducibly higher-order constructions in common language?
- Does the sufficiency of three tiers tell us something about cognition — that
  human thought operates over exactly these three levels of abstraction?