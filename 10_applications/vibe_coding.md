# The Vibe Coding Connection

## The Problem with Vibe Coding

Karpathy (2025) identified "vibe coding" — building software by
describing intent to an LLM and accepting the output. This works
remarkably well for generating code, but has no formal guarantee
that the generated code satisfies architectural constraints.

The LLM writes functions. But who verifies the architecture?

## The QBBN as Architectural Spec

The architecture — components, dependencies, data flow, failure
modes — can be expressed as a QBBN knowledge base. This knowledge
base is the *specification* of the system.

The LLM generates code. The QBBN holds the spec. Verification is:

1. **Compilation**: Do the logical forms type-check? Are all
   dependencies declared? Are all data flows well-typed?

2. **Inference**: Given the declared architecture, can all
   required endpoints be reached? If a service fails, what
   breaks? Are there circular dependencies?

This is the same two-level verification from natural language:
compilation checks well-formedness, inference checks consequences.

## The Architecture

    LLM generates code
    → Grammar extracts architectural claims
    → QBBN verifies against spec
    → Violations fed back to LLM for repair

This mirrors the natural language pipeline:

    LLM preprocesses → Grammar parses → QBBN infers

The same machinery. The same verification. Different domain.

## Why This Matters

Vibe coding scales code generation. The QBBN scales code
verification. Together they close the loop: the LLM is the
generator, the formal system is the verifier. This is the
bitter lesson applied to software engineering — both generation
and verification scale with compute, not human effort.