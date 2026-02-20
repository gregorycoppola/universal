# Functions as Relations

## The Problem

The QBBN's root concept is the predicate — a map to truth values.
But software is built from functions — maps from values to values.
How do you represent "the output of A is the input to B"?

## The Logic Programming Answer

A function is a relation with a distinguished output role.
This is the core insight of logic programming (Kowalski, 1974):

    Algorithm = Logic + Control

The logic declares relationships between inputs and outputs.
The control determines how to search for solutions.

In Prolog:

    parse_int("42", 42).
    parent(frank, sue).
    grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

In the QBBN:

    always [s:string, n:int]:
      is_digit_string(value: s)
      & represents_number(string: s, number: n)
      -> parse_int(input: s, result: n)

The shared variable mediates data flow: `n` appears as the
output of `represents_number` and the result of `parse_int`.
This is the same mechanism that handles "her father" in
natural language — the variable `f` in:

    always [b:e, g:e, f:e]:
      disrespect(agent: b, patient: g)
      & father_of(parent: f, child: g)
      -> upset(agent: b, patient: f)

## Data Flow Through Shared Variables

"The output of A feeds into B" is just a shared variable:

    always [r:e, d:data]:
      fetch(request: r, result: d)
      & validate(input: d)
      -> process(request: r, data: d)

The variable `d` IS the data flow. It connects fetch's output
to validate's input. No function types needed — just variables
and predicates, the same primitives used for everything else.

## The Boundary

This representation captures the *structure* of data flow —
what connects to what, what types are expected, what can fail.
It does not capture *computation* — what the actual values are.

The QBBN is a specification language, not an execution engine.
It verifies that the architecture is sound, not that the
program computes the right answer. This is the same role that
type systems play: Rust's borrow checker doesn't know what
your integers are, but it guarantees memory safety.