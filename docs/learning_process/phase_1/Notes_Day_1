# Notes Day 1 #

Answer to the Question:

## How does Attention work, and what problem does it solve? ##


Starting of with the basics:

1. A Transformer takes in a input, often times structured as a human redable text.
2. This Text gets then broken down into a unit for LLMs - the so called Tokens.
    Every token has a distinct Token_ID, which is unique. In GPT 3 it was composed of about 50k Token_IDs.
3. Afterwards every token gets embedded. That means every token is transformed into a embedding.
    A Emedding is a high demensional Vector, that tries to express the meaning of the token.
    The useful property is that semantically similar tokens end up close to each other in the high-dimensional space, not that each axis has a human-readable name.
4. Now that we have the vector translation of every token, we try to change the meanings of these   tokens, that mean something differently in the destinct context that they are currently in. 
    We get this done with attention. Every word gets a strongness from 0 - 1, whith which its meaning is tansposed onto every other token. Since the token sequence isnt recorded automatically, this is also done by position embedding.
5. If token 1 has a strong attention to token 2, it means that that *vector 1's* meaning gets shifted, by contributing vector 2s to it. The *attention* of *token 1 to token 2*, controls *how much* the *vector* representation of *token 1* gets *shifted by token 2*
That way vector 1 getts a new meaning, which is in respect to the context of the meaning of token 2. 
The attention weight of 1 regarding 2 decides how much 2 shifts the meaning of 1. 

* **Query:** What is this Token looking for
* **Key:** What does this Token have to offer
* **Value:** The actual content, which gets passed furter, if attention is high.
* The actual Attention is derived by comparing the Query with the Key, (Dot product, and Softmax) The output is then the Weighted Sum of Value Vectors

**This solves the Problem:**

That Words can have different meaning based on the context they come up in. Fore example the sentances: "It is useful to live by the approach of eating the frog", and "We dont eat the frog", have 2 completely different meanings, eventhough they use similar words. 


