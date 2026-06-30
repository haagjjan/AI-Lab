# Phase 1 — Orientation
**Duration:** 4 Days - Mo 29.6.26 - Do  
**Overall Deadline:** End of Day 4  
**Overall Milestone:** Project README committed to GitHub. 37 Anki cards created and reviewed once. I can explain the transformer → RAG → agent stack without notes.

---

## Day 1 — Transformers & Embeddings
**Assignment: Transformer Architecture Review**  
**Deadline: End of Day 1**

### Resources
1. 3b1b — Deep Learning, Chapters 5 & 6 *(~50 min)*
2. Jay Alammar — *The Illustrated Transformer* — `jalammar.github.io/illustrated-transformer` *(~45 min read)*
3. Andrej Karpathy — *Let's build GPT from scratch* — first 35 min only *(orientation, not learning)*

### Deliverables
**D1.1 — Anki Deck: Transformers** *(15 cards minimum)*  
Create one card per concept below, written in my own phrasing — no copy-pasting definitions:
- Token / tokenization
- Embedding — what it represents geometrically
- Attention — what problem it solves
- Query, Key, Value — what each represents
- Self-attention vs cross-attention
- Encoder-only / decoder-only / encoder-decoder — one example model each
- Context window — what it is and why it is a hard constraint
- Why transformers replaced RNNs *(one-sentence answer)*

**D1.2 — Written Explanation in Repository** *(150 words minimum)*  
Answer the following question in my own words, without looking at the resources:
> *"How does attention work and what problem does it solve?"*

Save to: `docs/learning_process/phase_1/Notes_Day_1.md`

### Day 1 Checkpoint
Before closing my laptop I must be able to answer this out loud without notes:
- What is an embedding?
- What does the attention mechanism actually compute?

---

## Day 2 — RAG Pipelines + Framework Decision
**Assignment: RAG Pipeline Mapping & Framework Commitment**  
**Deadline: End of Day 2**

### Resources
1. LangChain — *RAG from Scratch* YouTube series — first 5 videos *(search: "RAG from Scratch LangChain YouTube")*
2. LangChain RAG quickstart — `python.langchain.com/docs/tutorials/rag` *(skim)*
3. LlamaIndex starter example — `docs.llamaindex.ai/en/stable/getting_started/starter_example` *(skim)*

### Deliverables
**D2.1 — Anki Deck: RAG** *(12 cards minimum)*  
One card per concept, own phrasing:
- The 5 stages of a RAG pipeline in sequence
- Chunking — what it is and why chunk size matters
- Vector store — what it stores, how similarity search works
- Embedding model vs LLM — what each does in the pipeline
- Dense retrieval vs sparse/keyword retrieval *(awareness level only)*
- RAG vs fine-tuning — when to use which *(this is a classic interview question)*
- Hallucination — what it is and why RAG reduces it

**D2.2 — RAG Pipeline Diagram**  
Draw the full RAG pipeline (all 5 stages, labeled, with arrows showing data flow). Digital or hand-drawn — both are valid.  
Save to: `docs/learning_process/phase_1/Day2_RAG_Pipeline_Diagram.md` *(or attach image in the repository)*

**D2.3 — Framework Decision Record** *(1 paragraph)*  
State which framework I chose (LangChain or LlamaIndex) and why in one paragraph. This decision is final — no revisiting after today.  
Save to: `docs/learning_process/phase_1/Day2_Framework_Decision.md`

### Day 2 Checkpoint
Before closing my laptop:
- My framework is chosen and written down
- I can walk through all 5 RAG pipeline stages from memory

---

## Day 3 — Agents & Tool Use
**Assignment: Agent Architecture Introduction**  
**Deadline: End of Day 3**

### Resources
1. DeepLearning.ai — *AI Agents in LangGraph* (free short course) — first 3–4 lessons only *(~1.5–2h)*  
   `deeplearning.ai/short-courses/ai-agents-in-langgraph`
2. LangGraph conceptual docs — *"Why LangGraph"* and *"Agents"* sections only *(~20 min)*  
   `langchain-ai.github.io/langgraph/concepts`

### Deliverables
**D3.1 — Anki Deck: Agents** *(10 cards minimum)*  
One card per concept, own phrasing:
- Agent vs chain — the key difference
- Tool use — what a tool is and how it gets called
- ReAct loop — Reason → Act → Observe → repeat
- When to use an agent vs a simple RAG pipeline
- Short-term vs long-term memory in agents
- LangGraph: what a node is
- LangGraph: what an edge is

**D3.2 — RAG vs Agent Comparison Note** *(100 words minimum)*  
Answer the following in my own words:
> *"When do I use a RAG pipeline and when do I use an agent instead? What is the deciding factor?"*

Save to: `docs/learning_process/phase_1/Day3_RAG_vs_Agent.md`

**D3.3 — ReAct Loop Diagram**  
Draw or write out the ReAct loop as a cycle. Label each stage. Must be produceable from memory.  
Save to: `docs/learning_process/phase_1/Day3_ReAct_Diagram.md`

### Day 3 Checkpoint
Before closing my laptop:
- I can explain what a tool is in the agent context
- I can explain why a ReAct loop is more flexible than a fixed pipeline
- I can name one situation where an agent is overkill

---

## Day 4 — Project Definition + Buffer
**Assignment: Project Specification Document**  
**Deadline: End of Day 4 — this is the Phase A milestone**

No new learning resources today. This day converts orientation into a concrete commitment.

### Deliverables
**D4.1 — Project README pushed to GitHub**  
The README must answer all four of the following — if I cannot answer one, that is where the buffer time goes:

- **Problem statement:** What specific SMB problem does this solve? *(Not "automation" — a named, concrete problem. e.g. "a small law firm's client intake document Q&A" or "an accountancy firm's internal policy search")*
- **Demo description:** What does the user actually do and see in the working version?
- **Technical stack:** LLM provider, vector store, orchestration framework, interface layer
- **Architecture sketch:** A rough diagram or bullet-point breakdown of the system components

Repo must be pushed with this README before I close my laptop.

**D4.2 — Full Anki Review Session**  
Review all 37 cards from Days 1–3 in one sitting. Mark any cards I fail — these are my known gaps entering Phase B.

**D4.3 — Gap Note** *(1 paragraph)*  
Identify the one concept I am still most uncertain about after Phase A. Write what it is and how I resolved it (or plan to resolve it in Phase B).  
Save to: `docs/learning_process/phase_1/Day4_Known_Gap.md`

### Phase A Final Milestone Checkpoint
I do not move to Phase B until I can answer all four of the following out loud, without notes:

- [ ] What does a transformer do?
- [ ] How does a RAG pipeline work, step by step?
- [ ] What is an agent and how does it differ from a RAG pipeline?
- [ ] What is my project going to build?

---

## Phase A Summary

| Day | Theme | Key Deliverable | Cards |
|-----|-------|-----------------|-------|
| 1 | Transformers & Embeddings | Written attention explanation | 15 |
| 2 | RAG Pipelines | Pipeline diagram + framework decision | 12 |
| 3 | Agents & Tool Use | RAG vs Agent comparison + ReAct diagram | 10 |
| 4 | Project Definition | README pushed to GitHub + full card review | — |

**Total cards after Phase A: 37**  
**GitHub status after Phase A: Repo initialised, README committed**  
**Repository status after Phase A: 5 notes created under `docs/learning_process/phase_1/`**