# Vibe Science: A Methodology for the LLM Era

## The Pattern

Andrej Karpathy coined "vibe coding" in February 2025 to describe a new mode of
software development:

> "There's a new kind of coding I call 'vibe coding', where you fully give in to
> the vibes, embrace exponentials, and forget that the code even exists."

The pattern: describe what you want to the LLM, receive code, run it, observe
results, iterate. The human provides direction; the LLM provides execution. The
speedup is not incremental — it is qualitative. Tasks that took days take minutes.

This paper extends Karpathy's observation across three dimensions:

## Vibe Coding

The software infrastructure for the QBBN — the CLI tools, test harnesses,
development platform, coverage verification, factor graph visualization — was
built in collaboration with LLMs. Earlier iterations with ChatGPT, current
implementation with Claude.

What changed:
- **Before LLMs**: Building a belief propagation engine from scratch would take
  weeks of careful implementation, debugging edge cases in message passing,
  handling convergence issues. Each bug requires reading Pearl's textbook,
  understanding the math, and translating it to code.
- **With LLMs**: Describe the factor types, the message passing equations, the
  convergence criterion. Receive working code. Run tests. Fix failures through
  dialogue. The LLM has read Pearl's textbook (in its training data) and can
  translate the math to code directly.

The human contribution: knowing *what* to build (the boolean decomposition, the
NEG factor, bidirectional graph construction). The LLM contribution: *how* to
build it (the actual code, the data structures, the edge case handling).

## Vibe Science

The coverage tests — 44 inference tests across 22 categories, 33 grammar parses
across 12 categories — were designed through rapid iteration:

1. **Propose** a linguistic phenomenon (e.g., "contrapositive reasoning through
   negated evidence")
2. **Generate** a test case (knowledge base, query, expected answer)
3. **Run** it through the system
4. **Observe** the failure
5. **Diagnose** the cause (missing factor type, incorrect message passing,
   incomplete graph construction)
6. **Fix** the system
7. **Verify** the fix
8. **Repeat**

Each cycle takes minutes. The LLM generates the test case (step 2), often
diagnoses the failure (step 5), and proposes the fix (step 6). The human provides
the scientific judgment: which phenomena matter, whether the test is well-designed,
whether the fix is principled or ad hoc.

This is a new mode of scientific research. Traditional computational linguistics
research requires: (a) identify a phenomenon, (b) design an experiment, (c)
collect or annotate data, (d) implement a system, (e) run the experiment, (f)
analyze results, (g) write up findings. Steps (b) through (f) typically take
months. With vibe science, they take hours.

The quality concern is real: rapid iteration can produce systems that overfit to
test cases rather than capturing genuine linguistic generalizations. The
mitigation is the formal framework itself — the grammar rules and inference
patterns must be principled (type-driven dispatch, belief propagation, natural
deduction) rather than ad hoc patches. The formalism constrains the hypothesis
space.

## Vibe Annotation

The grammar rules, lexicon entries, and gold-standard logical forms were produced
through LLM-assisted authoring:

1. **Describe** a linguistic phenomenon to the LLM ("sentences where a
   prepositional phrase introduces a comparison: 'Alice is taller than Bob'")
2. **Receive** a candidate grammar rule, lexicon entry, and test case
3. **Evaluate** against the formal system
4. **Refine** through dialogue
5. **Commit** the verified output

This is linguistic annotation at a qualitatively different speed. A trained
linguist might produce 5-10 grammar rules per day, each requiring careful
consideration of type signatures, role assignments, and edge cases. An LLM-
assisted process produces 5-10 rules per hour, with the human reviewing and
correcting rather than authoring from scratch.

The quality of LLM-generated annotations is imperfect but systematically
correctable. Common errors include: wrong role labels (agent vs. theme), incorrect
quantifier scope, missing type constraints, and over-general rules that would
produce spurious parses. These errors are caught by the formal system (type
checking, coverage tests) and corrected through dialogue.

## The Bridge

All three dimensions — vibe coding, vibe science, vibe annotation — describe a
**semi-automatic bridge stage** between two endpoints:

**Before LLMs** (Sutton was right): Formal NLP requires human annotation that does
not scale. The bitter lesson applies. Formal approaches lose to statistical
approaches.

**After LLMs** (the steady state): The LLM generates formal representations
directly. The QBBN verifies them. No human in the loop. Both generation and
verification scale with compute.

**The bridge** (now): Humans provide direction and quality judgment. LLMs provide
execution speed and coverage. The formal system provides verification. This is
the stage where the infrastructure is built — the grammar rules, lexicon entries,
and coverage tests that will eventually enable autonomous operation.

The bridge is explicitly temporary. Its purpose is to construct the formal
infrastructure that the autonomous system needs. Once the grammar covers enough
patterns and the lexicon covers enough vocabulary, the LLM can produce logical
forms directly (without human review) and the QBBN can verify them (without human
judgment). The bridge builds itself out of existence.

## Implications for Research Methodology

Vibe science is not just faster traditional science. It is a different mode of
inquiry with different properties:

**Hypothesis generation is cheap.** The bottleneck in traditional research is
generating good hypotheses and designing experiments to test them. With LLMs,
both are cheap. The new bottleneck is evaluating whether the hypotheses are
interesting and the experiments are well-designed — which remains a human judgment.

**Implementation is not a barrier.** In traditional computational linguistics,
a good idea might take months to implement, during which the researcher's
understanding of the problem evolves. With vibe coding, implementation takes
hours, and the researcher can iterate on the idea while the implementation is
fresh.

**Coverage is cumulative and verifiable.** Each test case added to the suite is
permanent. The system either passes all tests or it doesn't. Regressions are
detected immediately. This is the scientific method applied to engineering: every
claim is backed by a test, every test is automated, every failure is a signal.

**Collaboration is between human and LLM.** The traditional model is: one
researcher, one codebase, one paper. The vibe science model is: one researcher
directing multiple LLMs, building code, tests, annotations, and text
simultaneously. The researcher's role shifts from producer to director — from
writing code to evaluating code, from designing experiments to evaluating
experiments, from annotating data to evaluating annotations.

## Acknowledgment

This methodology would not have been possible ten years ago. It would not have
been possible five years ago. It is possible now because LLMs have crossed a
threshold of capability in code generation, linguistic analysis, and scientific
reasoning that makes them productive collaborators rather than unreliable tools.

The threshold is not perfection. LLMs hallucinate, produce inconsistent
annotations, and sometimes fail at tasks they should handle easily. The threshold
is: *the human can review and correct LLM output faster than authoring it from
scratch.* For formal annotation, code generation, and test design, current LLMs
clear that bar decisively.

## Key Sources

- Karpathy, A. "Vibe Coding." Post on X, February 2, 2025.
- Coppola, G. "Statistical Parsing for Logical Information Retrieval." 2026.
  Section 3.3 (The Semi-Automatic Bridge).

## Open Questions

- At what point does vibe science produce results comparable in rigor to
  traditional peer-reviewed research? What are the quality controls?
- Can vibe science be formalized — can we define a protocol for LLM-assisted
  hypothesis generation and testing that is reproducible?
- Does the vibe coding pattern generalize beyond programming to other formal
  domains (mathematics, engineering, law)?
- What happens when LLMs are good enough that the human's review adds no value?
  Is the human still needed, and if so, for what?