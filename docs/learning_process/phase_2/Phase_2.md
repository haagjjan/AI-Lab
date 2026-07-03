# Phase 2 - Mini Projects and Experience 

The Idea of this phase, is to build up first hands on expereices with building Agents and RAG pipelines. And doing market research.

## Day 1 - Sa 4.7.26
*Start off:*
Get-in line (your literal first action): open AI-Lab, create builds/01_min_rag/, and get your LLM provider to answer a single hello-world call before you write anything else. Nothing else matters until that one call returns.


**Building Goal**

1. Provider — API key (OpenAI/Anthropic) or local via Ollama on your 24GB Mac. Whichever you can get responding fastest today; don't deliberate.
2. Data — drop 5–10 small text files in data/ (your own diary entries, some articles, anything). The data doesn't matter, the pipeline does.
3. Indexing flow — load → split into chunks → embed → store. Use a simple vector lib (Chroma or FAISS) for storage/search, using the LangChain frame work. 
4. Understand - Get intuition for: the moving parts:
    - Query flow — embed question → retrieve top-k → stuff into prompt → LLM call → print answer.
    - Verify — ask 3 real questions about your docs, and print the retrieved chunks to confirm retrieval is actually pulling relevant ones, not just that the answer sounds plausible.

*Done when:* you get a grounded answer AND you've eyeballed the retrieved chunks to confirm retrieval works. That's the bar — not pretty, just working and understood.
*Diary:* log what broke (it'll be env/API/setup, always is), what clicked, what's still fuzzy.
*Prereq check:* RAG theory ✓, agents ✓, Python ✓ — no forward dependencies. The only thing that can eat your morning is provider setup, so that's why it's step 0.
