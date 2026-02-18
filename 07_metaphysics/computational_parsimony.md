# Computational Parsimony

## The Argument

Among all systems that support verified reasoning, the typed formal language
requires the least computation.

## What Verified Reasoning Costs

Consider the space of systems that can take a knowledge base and a query, perform
inference, and produce a verified conclusion — one that traces back to premises
through explicit steps.

**Neural networks** require billions of parameters, trained over weeks on
thousands of GPUs, consuming megawatt-hours of electricity. At inference time,
each query requires millions of floating-point operations through the parameter
matrix. And after all of that, the output is not verified — it is a statistical
prediction with no proof tree.

**Theorem provers** (resolution-based, tableaux) search through a combinatorial
space of possible proofs. For full first-order logic, the search is undecidable
— it may never terminate. Even for decidable fragments, the worst case is
exponential.

**MCMC sampling** (as in Markov Logic Networks) requires many random samples to
approximate posterior probabilities. The number of samples needed grows with the
size of the model, and convergence is not guaranteed.

**Belief propagation on typed Horn clauses** — the QBBN — requires no training,
no parameters, no search, and no sampling. The forward fragment is linear time.
Grounding is polynomial in the number of entities. Message passing converges in
a small number of iterations (2-3 for most of the 44 test cases). The entire
computation is deterministic given the knowledge base.

## The Minimum

You cannot do verified reasoning with less:

- You need **entities** (things to reason about) — without them there is nothing
  to predicate.
- You need **predicates** (properties and relations) — without them there is
  nothing to say about entities.
- You need **types** (constraints on what fills what role) — without them,
  ill-formed propositions are possible and checking is undefined.
- You need **rules** (implications) — without them, no new conclusions can be
  drawn.
- You need **a propagation mechanism** — without one, rules sit inert.

The QBBN has exactly these components and nothing else. It is the minimal
architecture for verified reasoning. Adding anything (parameters, search,
sampling) increases cost. Removing anything (types, rules, propagation) breaks
verification.

## The Platonic Implication

If there is a uniquely minimal system for verified reasoning — and the typed
formal language is that system — then the typed formal language is not one
option among many. It is the necessary structure. Any system that performs
verified reasoning must either be this system or contain it as a component.

This is the computational argument for Platonic reality: the typed formal
language is not invented. It is discovered. It is the unique minimum of a
well-defined optimization problem (minimize computational cost subject to the
constraint of verified inference). Minima of well-defined problems are objective
features of the problem landscape, not subjective choices.

## Connection to Physics

Physics has a similar principle: the laws of nature minimize action (the
principle of least action). The path a photon takes, the orbit of a planet, the
shape of a soap bubble — all minimize a well-defined functional. Physicists
take this as evidence that the mathematical structure is real, not just
convenient.

The typed formal language minimizes computational action for verified reasoning.
By the same logic, the mathematical structure is real.

## Key Works

- Prawitz, D. *Natural Deduction*. 1965. (The forward fragment and its
  tractability.)
- Pearl, J. *Probabilistic Reasoning in Intelligent Systems*. 1988. (Belief
  propagation as efficient inference.)
- Cooper, G.F. "The Computational Complexity of Probabilistic Inference." 1990.
  (Hardness of general inference.)

## Open Questions

- Is the QBBN provably minimal, or could there exist a cheaper verification
  system that we haven't discovered?
- Does the computational parsimony argument apply only to the forward fragment,
  or does it extend to richer logics?
- Is there a formal sense in which belief propagation is the "least action" path
  through the factor graph?