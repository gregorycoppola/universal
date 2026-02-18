# Why LLMs Hallucinate

## The Phenomenon

Large language models produce fluent, confident, detailed text that is factually
wrong. They invent citations that do not exist. They attribute quotes to people
who never said them. They describe events that never happened. They solve math
problems with plausible-looking steps that arrive at wrong answers. They do all
of this with the same tone and confidence as when they are correct.

This is not a bug that will be fixed with more data or better training. It is a
structural consequence of what LLMs are.

## The Architecture

An LLM is a function from token sequences to probability distributions over next
tokens: