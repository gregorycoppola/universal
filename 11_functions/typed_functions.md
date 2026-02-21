# Approach 5: Typed Functions in the Lexicon

## The Idea

The type system already distinguishes entities (`e`), propositions (`s`), and predicates (`p`). Extend it with a new lexicon declaration: `function`. A function has typed inputs and a typed output, and an implementation that the interpreter *calls* rather than looks up.