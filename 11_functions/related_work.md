# Related Work: Functions in Logic Programming and Verification

## The Landscape

The question of how to combine functions with logical inference has been explored for fifty years across multiple traditions. No existing system makes the exact design choice we propose — a lexicon-level type distinction between predicates (search the KB) and functions (call an implementation), unified in a single proof tree. But many systems address overlapping concerns.

## Prolog: Arithmetic as Special Case

Prolog (Colmerauer, 1972; Kowalski, 1974) is pure Horn clause inference — everything is a predicate, resolved by unification and search. But arithmetic was immediately a problem. The solution was `is/2`, a built-in that evaluates the right-hand side:

```prolog
energy(X, E) :- mass(X, M), E is M * 299792458 * 299792458.