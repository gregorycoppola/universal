# Bidirectional Training

## Two Directions, Both Verifiable

The characteristica enables training in both directions:

### Direction 1: Understanding (NL → Logic)
Input: "Socrates is a man"
Output: `man(theme: socrates)`
Verification: does the logical form type-check and ground correctly?

### Direction 2: Generation (Logic → NL)
Input: `man(theme: socrates)`
Output: "Socrates is a man"
Verification: parse the output back to logical form. Does it match the input? (Round-trip consistency)

### Direction 3: Inference (Logic → Logic)
Input: KB + query
Output: proof tree
Verification: does the proof tree use only valid rules? Does each step follow?

### Direction 4: Formalization (NL argument → Logic proof)
Input: "All men are mortal. Socrates is a man. Therefore Socrates is mortal."
Output: KB + rules + proof tree
Verification: does the entire chain check out?

## Why Bidirectional Matters

Each direction provides a different RLVR reward signal. An LLM trained on all four can:

1. Parse natural language into verified logical forms (understanding)
2. Explain logical forms in natural language (generation / interpretability)
3. Perform verified inference (reasoning)
4. Formalize informal arguments (the killer app)

Direction 4 is the most powerful: take an English paragraph of reasoning and produce a fully verified logical proof. This is what "solving hallucination" looks like in practice — the LLM doesn't just *claim* something is true, it produces a checkable proof.

## The Round-Trip Test

The strongest verification signal combines directions 1 and 2:

1. Start with natural language S
2. Parse to logical form L (direction 1)
3. Generate natural language S' from L (direction 2)
4. Parse S' back to logical form L' (direction 1 again)
5. Check: does L = L'?

If yes, the round trip is consistent — the LLM's understanding and generation are aligned. If no, the discrepancy is a training signal. This is a self-supervised reward signal that requires no human annotation at all.