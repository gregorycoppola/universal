# The LLM as Thought Externalizer

## The Idea

Chain-of-thought prompting (Wei et al., 2022) showed that LLMs reason better when they "think out loud" in English. But English chain-of-thought is unverifiable — it looks like reasoning but you can't check it mechanically.

The characteristica gives chain-of-thought a verifiable medium. Instead of:

> "All men are mortal. Socrates is a man. Therefore, since all men are mortal and Socrates is a man, Socrates must be mortal."

The LLM produces: