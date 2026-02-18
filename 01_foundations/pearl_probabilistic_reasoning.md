# Pearl's Probabilistic Reasoning

## The Revolution

Judea Pearl's *Probabilistic Reasoning in Intelligent Systems* (1988) introduced
Bayesian networks and belief propagation, providing the first tractable framework
for probabilistic inference over structured domains. Before Pearl, probabilistic
reasoning meant either full joint distributions (exponential in the number of
variables) or ad hoc approximations. Pearl showed that **structure** — the
conditional independence relationships encoded in a directed graph — makes
inference tractable.

## Bayesian Networks

A Bayesian network is a directed acyclic graph (DAG) where:

- **Nodes** represent random variables
- **Edges** represent direct causal or probabilistic dependencies
- **Conditional probability tables** (CPTs) at each node specify `P(node | parents)`
- The joint distribution factorizes: `P(x₁,...,xₙ) = ∏ P(xᵢ | parents(xᵢ))`

The graph encodes conditional independence: a node is independent of its
non-descendants given its parents. This factorization is what makes inference
tractable — you never need the full joint distribution.

## Belief Propagation

Pearl's belief propagation algorithm passes messages between nodes in the graph:

- **π messages** (forward, causal): flow from parents to children. "Given what I
  know about causes, here's what I believe about effects."
- **λ messages** (backward, evidential): flow from children to parents. "Given what
  I observe about effects, here's what I can infer about causes."
- **Posterior**: `P(x | evidence) = α · π(x) · λ(x)` — the product of forward and
  backward beliefs, normalized.

On trees (singly-connected graphs), belief propagation gives exact answers in
linear time. On loopy graphs (with cycles), it is approximate but empirically
effective — a result demonstrated extensively by Murphy, Weiss, and Jordan (1999).

## From Pearl to the QBBN

The QBBN uses Pearl's belief propagation as its inference engine, but with a
critical twist: the graph structure is not learned from data or specified by hand.
It is **compiled from logical rules**.

The compilation works through the boolean decomposition:

- **Quantified Horn clauses** become AND factors (conjunctive premises) feeding into
  OR factors (disjunctive support for conclusions)
- **Negation** becomes NEG factors linking propositions to their complements
- **Modal quantifiers** (always, usually, sometimes) become weights on OR factor
  edges

The result is a factor graph — a bipartite graph alternating between variable nodes
and factor nodes — which is a generalization of Pearl's Bayesian network. Factor
graphs were formalized by Kschischang, Frey, and Loeliger (2001) and unify
Bayesian networks, Markov random fields, and other graphical models.

## Causal vs. Evidential Reasoning

Pearl's two message directions map directly to logical inference:

- **π messages** implement **modus ponens**: given facts (causes), compute
  conclusions (effects). Forward reasoning.
- **λ messages** implement **modus tollens**: given negative evidence about a
  conclusion, constrain the premises. Backward reasoning.

This mapping — from proof theory to message passing — is the conceptual heart of
the QBBN. Prawitz gives the logic; Pearl gives the algorithm.

## Beyond Pearl: Causal Inference

Pearl's later work on causality (*Causality*, 2000; *The Book of Why*, 2018)
extended Bayesian networks to handle interventions (`do(x)`) and counterfactuals.
The QBBN does not currently implement interventional or counterfactual reasoning,
but the infrastructure is compatible: interventions correspond to clamping nodes
in the factor graph, and counterfactual queries correspond to running belief
propagation under modified evidence.

## Key Works

- Pearl, J. *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann, 1988.
- Murphy, K., Weiss, Y., and Jordan, M.I. "Loopy Belief Propagation for Approximate
  Inference." UAI, 1999.
- Kschischang, F., Frey, B., and Loeliger, H.-A. "Factor Graphs and the Sum-Product
  Algorithm." *IEEE Trans. Information Theory*, 47(2):498-519, 2001.
- Koller, D. and Friedman, N. *Probabilistic Graphical Models*. MIT Press, 2009.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University
  Press, 2000.

## Open Questions

- Can belief propagation on the QBBN's factor graphs be given formal convergence
  guarantees for the specific graph topologies that arise from Horn clause
  compilation?
- How does the QBBN's approximate inference compare to ProbLog's exact weighted
  model counting in terms of accuracy vs. computational cost?
- Can Pearl's `do`-calculus be integrated into the QBBN to support causal and
  counterfactual reasoning?