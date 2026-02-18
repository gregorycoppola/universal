# Chomsky's Universal Grammar

## The Core Claim

Noam Chomsky's central insight, developed from *Syntactic Structures* (1957) through
*Aspects of the Theory of Syntax* (1965) and the Principles and Parameters framework
(1981), is that human languages share a common structural foundation that is innate
to the species.

The argument proceeds from the **poverty of the stimulus**: children acquire language
from limited, noisy input, yet converge on grammars of extraordinary complexity and
regularity. The input underdetermines the grammar. Therefore, something must constrain
the hypothesis space — and that something is Universal Grammar (UG), an innate
faculty that specifies the structural possibilities of human language.

## Principles and Parameters

UG is not a single grammar but a framework. It consists of:

- **Principles**: invariant structural constraints shared by all languages (e.g.,
  every sentence has a subject, structure is hierarchical not linear, dependencies
  are bounded).
- **Parameters**: binary switches that vary across languages (e.g., head-initial vs.
  head-final, pro-drop vs. non-pro-drop). Language acquisition is the process of
  setting parameters based on input.

This gives a combinatorial account of linguistic diversity: a small number of binary
parameters generates a large space of possible grammars, all sharing the same
structural core.

## What UG Is *Not*

UG is not a claim about specific words, meanings, or concepts. It is a claim about
**structure** — about the kinds of relationships that can hold between elements in a
sentence. It says nothing about what those elements mean.

This is precisely the gap that Montague's formal semantics and Fodor's Language of
Thought attempt to fill: UG gives you the syntax, but you need a theory of meaning
to connect it to the world.

## Relevance to This Project

The typed slot grammar in *Statistical Parsing for Logical Information Retrieval*
(Coppola, 2026) is, in a sense, a computational realization of UG — a finite set of
structural patterns that map natural language sentences to a universal logical form.
The grammar rules (copular fact, transitive fact, conditional, etc.) are the
"principles"; the lexicon entries that determine which rule fires are the "parameters."

The key difference: Chomsky's UG maps surface structure to deep structure (both
syntactic). Our grammar maps surface structure to **logical form** — a typed,
role-labeled, quantified representation in which inference can actually be performed.
This is the step Chomsky never took, because his program was about syntax, not
semantics.

## Key Works

- Chomsky, N. *Syntactic Structures*. Mouton, 1957.
- Chomsky, N. *Aspects of the Theory of Syntax*. MIT Press, 1965.
- Chomsky, N. *Lectures on Government and Binding*. Foris, 1981.
- Chomsky, N. *The Minimalist Program*. MIT Press, 1995.

## Open Questions

- Is UG best understood as a biological endowment (Chomsky's view), a statistical
  regularity of language input (the connectionist view), or a logical necessity of
  compositional systems (the mathematical view)?
- Does the success of LLMs at syntactic tasks without explicit UG refute Chomsky,
  or confirm him (since the structure must be in the training data)?
- If a formal grammar + LLM disambiguation achieves UG-like coverage, does the
  locus of universality shift from the brain to the grammar?