# Bootstrapping the Knowledge Base

## The Problem

RLVF needs a knowledge base to verify against. Where does the KB come from?

## The Solution: LLMs Build the KB

The same LLM that generates logical forms can generate the KB itself:

1. **Lexicon generation**: LLM proposes predicate declarations with typed roles
   ```
   predicate trust {agent: e, patient: e}
   predicate mortal {theme: e}
   ```
   Verifier checks: are the types well-formed? Are the roles consistent?

2. **Entity generation**: LLM proposes entities
   ```
   entity socrates : e
   entity plato : e
   ```
   Verifier checks: no duplicate declarations, types are valid.

3. **Fact generation**: LLM proposes ground facts
   ```
   man(theme: socrates)
   teacher(agent: socrates, student: plato)
   ```
   Verifier checks: predicates exist, roles match, entities exist.

4. **Rule generation**: LLM proposes Horn clauses
   ```
   always [x:e]: man(theme: x) -> mortal(theme: x)
   ```
   Verifier checks: types check, variables are safe (Datalog restriction), no inconsistencies with existing KB.

5. **Consistency checking**: After each addition, run the calculus. Flag any contradictions. Feed contradictions back to the LLM for repair.

## The Flywheel