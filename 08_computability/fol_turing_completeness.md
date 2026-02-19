# FOL and Turing Completeness: The Bidirectional Equivalence

## The Result

First-order logic and Turing machines are computationally equivalent. Each can
simulate the other, and neither can do more than the other.

**Direction 1: Turing machine → FOL prover.** A Turing machine can implement a
complete first-order theorem prover. This follows from Gödel's completeness
theorem (1929): every valid first-order sentence has a finite proof. A Turing
machine can systematically enumerate all possible proofs (by length, or by
applying all rules in all combinations) and will eventually find one for any
valid sentence. This is a semi-decision procedure — it says "yes" when the
answer is yes, and may search forever when the answer is no.

**Direction 2: FOL prover → Turing machine.** A first-order theorem prover can
simulate any Turing machine. Given a Turing machine M and input w, you can
construct a first-order theory T(M,w) such that "M halts on w" if and only if
T(M,w) proves a particular sentence. The prover's search for a proof
reconstructs the machine's execution trace. (The encoding is detailed in
[The Turing Machine Encoding](turing_encoding.md).)

**The equivalence.** Both are semi-decision procedures for the same class of
problems (the recursively enumerable sets, Σ₁⁰ in the arithmetical hierarchy).
The undecidability of FOL validity (Church-Turing, 1936) and the undecidability
of the halting problem (Turing, 1936) are the same theorem viewed from two
sides.

## What This Means

First-order logic is not just a notation for writing down mathematical
statements. It is a complete model of computation — as powerful as any
programming language, any Turing machine, any lambda calculus. The Church-Turing
thesis says this is the maximum: no physically realizable system can compute
more than a Turing machine, and therefore no physically realizable system can
compute more than first-order logic.

This means the typed logical language used in the QBBN is a *restriction* of a
computationally universal system. The QBBN uses universally quantified Horn
clauses with finite grounding — a strict subset of FOL. This restriction is
deliberate: it trades Turing completeness for decidability, ensuring that
verification always terminates.

## Historical Context

The equivalence was established in 1936 through three independent results:

- **Turing** showed that no machine can decide the halting problem.
- **Church** showed that no procedure can decide validity in the lambda calculus
  (which is equivalent to FOL).
- **Church** independently showed that FOL validity is undecidable.

These results, together with the equivalence of Turing machines, lambda
calculus, recursive functions (Gödel-Herbrand), and Post production systems,
form the basis of the Church-Turing thesis.

The convergence of five independent formalisms on the same computational
boundary is itself an instance of the historical convergence argument (Section
7): when every path leads to the same destination, the destination is real.

## Key Works

- Gödel, K. "Die Vollständigkeit der Axiome des logischen Funktionenkalküls."
  1929.
- Turing, A.M. "On Computable Numbers, with an Application to the
  Entscheidungsproblem." 1936.
- Church, A. "An Unsolvable Problem of Elementary Number Theory." 1936.
- Enderton, H.B. *A Mathematical Introduction to Logic*. 2001.
- Boolos, G., Burgess, J., and Jeffrey, R. *Computability and Logic*. 2007.