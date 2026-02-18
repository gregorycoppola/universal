# Montague's Formal Semantics

## The Radical Claim

Richard Montague's work, particularly "The Proper Treatment of Quantification in
Ordinary English" (1973), made a claim that was radical for its time: **natural
language can be treated with the same formal rigor as mathematical logic.**

Montague rejected the prevailing view (shared by many logicians and even Chomsky)
that natural language was too messy, too ambiguous, too context-dependent for formal
treatment. His response was to build a complete formal semantics for a fragment of
English, demonstrating that every sentence could be assigned a precise logical
interpretation through compositional rules.

## The Architecture

Montague Grammar has three layers:

1. **Syntax**: A categorial grammar generating English sentences. Categories are
   typed: `e` for entities, `t` for truth values, `e → t` for properties, etc.
2. **Translation**: Each syntactic rule has a corresponding semantic rule that
   translates English expressions into Intensional Logic (IL).
3. **Model theory**: IL expressions are interpreted in a model — a set of possible
   worlds with domains of entities — yielding truth values.

The compositionality principle (**Frege's principle**): the meaning of a complex
expression is a function of the meanings of its parts and the way they are combined.
This is not just a guideline — in Montague Grammar, it is a theorem: the syntax-
semantics mapping is a homomorphism.

## Why It Mattered

Before Montague, formal logic and natural language semantics were separate fields.
Logicians worked with artificial languages; linguists worked with natural languages;
neither group had a systematic bridge between the two.

Montague provided the bridge. After his work, it was possible to say precisely what
"Every man loves a woman" means — and to distinguish its two readings (wide-scope
vs. narrow-scope quantification) using formal machinery.

## Why It Failed to Scale

Montague Grammar worked brilliantly on fragments — carefully chosen subsets of
English where every word was in the lexicon and every construction was covered by a
rule. But extending coverage to open-domain text required:

- Writing grammar rules for every syntactic pattern (thousands)
- Creating lexicon entries for every word sense (tens of thousands)
- Resolving ambiguity at every level (combinatorial explosion)

All of this required human linguists. The formal machinery was sound; the
construction process was unscalable. This is exactly the bitter lesson in action.

## Relevance to This Project

The QBBN's typed logical language is a direct descendant of Montague's approach:

- **Typed predicates** descend from Montague's typed lambda calculus
- **Role-labeled arguments** replace positional arguments (an improvement — natural
  language uses roles, not positions)
- **Quantified rules** with modal weights replace Montague's deterministic
  quantification (an improvement — natural language is probabilistic)
- **Three tiers of expressiveness** from Prawitz correspond to Montague's type
  hierarchy

The critical difference is the construction process. Montague needed linguists to
write every rule and lexicon entry. The QBBN uses LLMs as annotators — generating
grammar rules, lexicon entries, and logical forms at scale. Same formal rigor,
different construction economics.

Montague showed it was possible. The QBBN shows it can scale.

## Key Works

- Montague, R. "Universal Grammar." *Theoria*, 36:373-398, 1970.
- Montague, R. "The Proper Treatment of Quantification in Ordinary English." In
  *Approaches to Natural Language*, pages 221-242, 1973.
- Dowty, D., Wall, R., and Peters, S. *Introduction to Montague Semantics*. Reidel,
  1981.
- Partee, B. "Montague Grammar." In *Handbook of Logic and Language*, 1997.

## Open Questions

- Is Montague's intensional logic (with possible worlds) necessary for natural
  language, or can the QBBN's extensional approach (with probabilistic weights)
  capture the same phenomena?
- Does the role-labeled predicate language lose anything by abandoning Montague's
  positional lambda calculus?
- Can LLM-generated Montague-style translations serve as training data for the
  typed slot grammar?