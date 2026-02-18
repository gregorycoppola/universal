# Universal Grammar as Interface Specification

## The Reframing

Chomsky's Universal Grammar is usually presented as a claim about biology — there
exists an innate faculty in the human brain that constrains the space of possible
grammars. This is a strong empirical claim that has been debated for sixty years
without resolution.

We propose a different reading: **UG is an interface specification.** It defines
the structural contract between surface language and the language of thought.

This reframing is not a weakening of Chomsky's claim. It is a sharpening. Instead
of asking "what is innate in the brain?" we ask "what structural mapping is
necessary for language to connect to thought?" The answer turns out to be a finite,
specifiable set of patterns — which is exactly what the typed slot grammar provides.

## The Interface

Every natural language sentence must be converted into a thought — a structured
representation over which inference can operate. This conversion requires:

1. **Identifying entities**: which noun phrases refer to things in the world
2. **Identifying predicates**: which words denote properties or relations
3. **Assigning roles**: who does what to whom
4. **Determining scope**: which quantifiers bind which variables
5. **Resolving embedding**: which clauses are arguments to which predicates

These five tasks are **universal** — they must be performed for every sentence in
every human language. The specific mechanisms vary (word order, case marking,
agreement, particles), but the tasks are the same. This is what UG is: the
specification of the mapping from surface form to conceptual form.

## The Grammar as UG

The typed slot grammar in the QBBN paper implements this specification:

| UG Task | Grammar Implementation |
|---|---|
| Identify entities | Lexicon lookup: `socrates : e` |
| Identify predicates | Lexicon lookup: `predicate mortal {theme: e}` |
| Assign roles | Type-driven dispatch: subject → agent, object → patient |
| Determine scope | Rule patterns: "All X are Y" → `always [x:e]: X(x) -> Y(x)` |
| Resolve embedding | Sentential type: `believe {experiencer: e, content: s}` |

The grammar rules are the **universal patterns**:

- Copular fact ("X is a Y")
- Transitive fact ("X verbs Y")
- Copular universal ("All X are Y")
- Conditional ("If X then Y")
- Negation ("X is not Y")

These patterns recur across languages. English uses word order and function words.
Japanese uses particles. Latin uses case endings. But the underlying structural
patterns — predication, quantification, negation, conditionality, embedding —
are the same.

## Principles and Parameters, Revisited

Chomsky's Principles and Parameters framework distinguished:

- **Principles**: Universal structural constraints (present in all languages)
- **Parameters**: Binary switches that vary across languages

In the QBBN framework:

- **Principles** = the grammar rules (the structural patterns that map surface
  form to logical form)
- **Parameters** = the lexicon entries (which words map to which predicates and
  roles, which vary by language)

A new language requires new lexicon entries but the same grammar rules. The
universal part is the structural mapping; the parametric part is the vocabulary.

This is a testable prediction: if you build a lexicon for a typologically
different language (say, Japanese or Turkish) and feed it through the same grammar
rules (suitably adapted for word order), you should get correct logical forms.
The grammar rules may need surface-level adaptation (head-final vs. head-initial
ordering), but the underlying type-driven dispatch should be the same.

## UG Without Biology

The reframing avoids the biological debate entirely. We do not need to claim that
UG is innate, that there is a "language organ," or that children have a Universal
Grammar module in their brains. We need only claim that:

1. Thought has structure (Fodor's LOT).
2. Language expresses thought.
3. Therefore, there must be a systematic mapping from language to thought.
4. That mapping has universal structural properties.

This is a logical argument, not an empirical one. It holds regardless of whether
the mapping is innate or learned, whether it is a biological module or a
statistical regularity, whether it is in the brain or in a computer.

The typed slot grammar is a **computational proof** that such a mapping exists and
can be specified finitely. Sixteen grammar rules cover the structural patterns
found in the QBBN's test suite. The claim is that a bounded extension of these
rules (perhaps 50-100 total) would cover the structural patterns of any natural
language.

## The LLM Connection

If UG is an interface specification, then:

- The **grammar** implements the specification (universal structural patterns)
- The **lexicon** parameterizes it (language-specific vocabulary)
- The **LLM** populates both (proposing rules and entries at scale)
- The **QBBN** validates the output (verifying that logical forms are well-typed
  and inference-ready)

The LLM has implicitly learned UG — it knows the structural patterns of language
from training data. The grammar makes these patterns explicit and exact. The LLM
provides coverage; the grammar provides correctness. Together, they realize UG
as a working system.

## Key Works

- Chomsky, N. *Lectures on Government and Binding*. Foris, 1981.
- Chomsky, N. "Principles and Parameters in Syntactic Theory." In *Explanation in
  Linguistics*, 1981.
- Baker, M. *The Atoms of Language*. Basic Books, 2001.
- Newmeyer, F. *Language Form and Language Function*. MIT Press, 1998.
- Evans, N. and Levinson, S. "The Myth of Language Universals." *Behavioral and
  Brain Sciences*, 32(5):429-448, 2009.

## Open Questions

- How many grammar rules are needed for full coverage of English? Of any language?
  Is the number bounded, and if so, what is the bound?
- Does the UG-as-interface-specification view make predictions that differ from
  Chomsky's biological UG? If so, are they testable?
- Can the grammar rules be *derived* from the type system alone, or do they require
  language-specific engineering? If derivable, UG truly is the type system.
- What happens at the boundaries — pidgins, creoles, sign languages, constructed
  languages? Do they obey the same interface specification?