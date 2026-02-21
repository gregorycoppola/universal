# The Logic Programming Connection

## Prolog and the QBBN

The QBBN is a probabilistic Datalog. Understanding where it sits in
the logic programming family clarifies what it can and cannot do.

## The Family Tree

### Prolog (Colmerauer, 1972)
- Horn clauses as a programming language
- Unification + backtracking as execution
- Turing-complete (function symbols create infinite terms)
- No probabilistic reasoning
- Depth-first search (incomplete — can loop forever)

### Datalog (Ceri, Gottlob, Tanca, 1986)
- Prolog minus function symbols
- Only constants, no computed values
- Guaranteed termination (finite grounding)
- Polynomial time data complexity
- Used in databases, static analysis, networking

### The QBBN (Coppola, 2024)
- Datalog plus probabilistic weights
- Horn clauses compiled to factor graphs
- Belief propagation instead of backtracking
- Modal quantifiers (always/usually/sometimes) map to weights
- Guaranteed termination (finite grounding, like Datalog)
- Returns probabilities, not just yes/no

### Constraint Logic Programming (Jaffar & Lassez, 1987)
- Prolog plus constraint solvers over domains (integers, reals, etc.)
- Can handle arithmetic: X > 18, Y = X + 1
- This is the direction needed for computed values

### ProbLog (De Raedt et al., 2007)
- Prolog plus probabilistic facts
- Exact inference via weighted model counting
- More expressive than QBBN (full Prolog) but slower inference

### Markov Logic Networks (Richardson & Domingos, 2006)
- Full first-order logic plus Markov random fields
- MCMC inference (slower than belief propagation)
- More expressive than QBBN but less efficient

## The Design Space