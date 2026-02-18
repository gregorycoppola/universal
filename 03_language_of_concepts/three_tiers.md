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
`man(theme: socrates)`

**Classification and taxonomy**: All men are mortal.
`always [x:e]: man(theme: x) -> mortal(theme: x)`

**Relations**: Jack trusts Jill.
`trust(agent: jack, patient: jill)`

**Transitive chains**: If A is taller than B and B is taller than C, then A is
taller than C.