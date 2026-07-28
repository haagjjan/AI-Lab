# ML/AI Project Context

> Codex handoff document  
> Last consolidated: 27 July 2026  
> Project: **ML/AI — AI Engineering skill-building sprint**

---

## 1. Project purpose

This project is an **11-week, project-driven AI Engineering sprint** intended to improve both:

1. **Actual engineering ability**
2. **Hireability and visible proof of work**

The selected focus is:

> **AI Engineering for automating real processes in small and medium-sized businesses (SMEs).**

The objective is not to become a frontier ML researcher within 11 weeks. The objective is to become capable of designing, implementing, evaluating, documenting, and presenting a credible end-to-end AI automation system.

The final work should demonstrate:

- solid software-engineering fundamentals;
- practical understanding of modern LLM systems;
- the ability to select between deterministic software, RAG, tools, workflows, and agents;
- responsible use of model APIs and local models;
- evaluation and debugging of AI behavior;
- clear technical documentation;
- a polished GitHub project that can support internship or junior software/AI engineering applications.

---

## 2. User background

The user is **Jan Valentin Haag**.

Relevant background:

- BSc Computer Science student at the University of Basel
- Degree started in 2025
- Currently around the transition into the third semester
- Completed the fundamental university programming courses
- Strongest prior language/project experience is in Java
- Has built side projects beyond coursework
- Career direction includes:
  - software engineering;
  - backend engineering;
  - full-stack engineering;
  - AI engineering;
  - internships or junior roles in Switzerland or Europe.
- Has prior leadership experience as a Swiss Armed Forces officer
- Has prior ML exposure from a Matura thesis:
  - handwritten digit recognition using MNIST;
  - implemented and explained a neural network/backpropagation;
  - thesis grade: 6.0.

The user is not a complete programming beginner. However, he is still building systematic knowledge of LLM application engineering, retrieval, agents, model APIs, evaluation, and production AI workflows.

---

## 3. Strategic goal

By the end of the sprint, the project should produce evidence in several dimensions.

### 3.1 Technical ability

The user should be able to:

- explain the important components of an LLM application;
- build a basic model integration;
- build and evaluate a RAG pipeline;
- use tools and structured outputs;
- distinguish a fixed chain/workflow from an agent;
- understand the ReAct loop;
- use LangChain and LangGraph deliberately rather than mechanically;
- decide when not to use an agent;
- reason about short-term and long-term state;
- compare cloud-hosted and local models;
- understand where system costs originate;
- implement a real automation pipeline around an SME process;
- test the system with realistic cases;
- identify failure modes, limitations, and operational risks.

### 3.2 Portfolio and hireability

The sprint should produce:

- a strong GitHub repository;
- readable project documentation;
- architecture diagrams;
- a clear README;
- setup and usage instructions;
- evaluation results;
- design decisions and trade-offs;
- visible progress updates where useful;
- material that can later support LinkedIn and CV entries;
- a technical or paper-style write-up.

### 3.3 Learning evidence

Learning is reinforced through:

- concise notes;
- Anki cards in the user’s own phrasing;
- implementation immediately after concepts are introduced;
- written explanations of important design decisions;
- small verified experiments before larger abstractions.

---

## 4. Learning philosophy and working method

The project follows **just-in-time learning**, not broad just-in-case study.

The intended loop is:

1. Obtain enough orientation to understand the problem space.
2. Learn one concept.
3. Explain it in the user’s own words.
4. Correct conceptual errors.
5. Convert the stable understanding into Anki cards.
6. Apply the concept in code.
7. Verify the result.
8. Document what was learned.
9. Continue to the next concept only when it becomes useful.

Important principles:

- Do not spend weeks studying theory before building.
- Do not prematurely lock the final SME project before sufficient reconnaissance.
- Orientation videos and documentation are inputs, not the final product.
- Prefer the simplest architecture that solves the actual problem.
- RAG, agents, LangChain, and LangGraph are tools, not project requirements.
- Avoid adding agentic behavior merely because it is fashionable.
- A fixed deterministic workflow is preferable when the task can be specified reliably.
- Explanations should separate:
  - exact technical definitions;
  - useful intuition;
  - simplifications;
  - implementation details.

---

## 5. Overall project shape

The sprint has two related but distinct build tracks.

### 5.1 Learning builds

Small projects are used to understand individual concepts.

The current learning build is:

> **`01_mini_rag` — a minimal RAG application built step by step**

Its purpose is to make retrieval, embeddings, model calls, LangChain integration, and environment setup concrete.

It is intentionally small and should not be mistaken for the final portfolio project.

### 5.2 Main portfolio project

The eventual main project should be:

> A well-built, end-to-end AI automation pipeline for a real SME process.

It should solve a concrete business problem rather than merely demonstrate API calls.

The exact use case has not yet been permanently selected. Reconnaissance should precede that decision.

Possible characteristics of the final system:

- real documents or business data;
- retrieval over business knowledge;
- deterministic workflow steps;
- selective model reasoning;
- structured outputs;
- external tool or service calls;
- human review where necessary;
- auditability;
- evaluation;
- failure handling;
- deployment;
- security and privacy considerations.

The system may contain an agent, but only if dynamic tool selection or iterative reasoning is genuinely required.

---

## 6. Timeline and completed learning

### 26–27 June 2026 — project direction

The initial broad goal was an 11-week CS skill-building phase.

The focus was refined to:

> AI Engineering for automating processes for SMEs.

Success was defined as both:

- real technical competence;
- visible proof of competence.

A key decision was made not to immediately choose a superficial “big project” without first understanding the AI application landscape.

---

### 28 June 2026 — Day 1: Transformers, tokens, embeddings, and attention

A draft Anki deck of approximately **22 cards** was created.

Topics included:

- tokenization;
- tokens;
- token IDs;
- the difference between a word and a token;
- embeddings;
- embedding dimensions;
- positional information;
- positional encoding;
- attention;
- attention weights;
- queries, keys, and values;
- intuition for the distinction between Q, K, and V.

Current conceptual understanding:

1. Input text is tokenized.
2. Tokens are mapped to token IDs.
3. Token IDs are converted into vectors.
4. Positional information is added because the transformer does not inherently know sequence order.
5. Attention lets each token representation incorporate information from other relevant tokens.
6. Queries and keys determine relevance.
7. Values provide the information that is aggregated.
8. The resulting token representation becomes contextual rather than static.

Important correction to preserve:

- Attention does not simply “transpose the meaning” of one word onto another.
- Attention computes weighted combinations of value vectors based on query-key compatibility.
- Attention weights describe relevance within a particular attention head and layer; they are not a universal semantic-strength score.
- Embedding dimensions should not be assumed to map cleanly to human-interpretable properties such as “mass” or “sex.” Meaning is generally distributed across dimensions.

Anki preference:

- Definitions should become stable and fairly final.
- Intuition cards may evolve.
- Cards should be based on concepts the user has actually worked through.
- Do not generate large unseen decks detached from the learning session.

---

### 29 June 2026 — Day 2: RAG

A RAG Anki deck of approximately **29 cards** was prepared.

Deck name:

> `AI Engineering::Phase A::RAG`

Core concepts covered:

- what RAG is;
- the RAG pipeline;
- document ingestion;
- text splitting;
- chunking;
- embeddings;
- vector stores;
- retrieval;
- passing retrieved context to an LLM;
- generation;
- embedding model versus generation model;
- dense retrieval;
- sparse retrieval;
- RAG versus fine-tuning;
- hallucinations and grounding.

Working definition:

> Retrieval-Augmented Generation retrieves relevant external information and supplies it to a generation model as context for answering a request.

Important nuances:

- RAG does not change the model’s trained weights.
- RAG does not inherently make the model more intelligent.
- It gives the model access to information not reliably contained in its parameters.
- It can improve freshness, domain grounding, and traceability.
- It can reduce hallucination risk, but it does not eliminate hallucinations.
- Bad retrieval can create confidently wrong answers.
- Evaluation must consider retrieval quality separately from generation quality.

Typical RAG pipeline:

1. Load documents.
2. Clean or normalize content.
3. Split documents into chunks.
4. Generate embeddings for chunks.
5. Store vectors and metadata.
6. Embed the user query.
7. Retrieve relevant chunks.
8. Optionally rerank or filter.
9. Build the model prompt/context.
10. Generate an answer.
11. Return sources or citations where possible.
12. Evaluate both retrieval and final answer quality.

Local LLM clarification:

- Running a local model is not automatically RAG.
- A local model becomes part of a RAG system only when an external retrieval pipeline supplies relevant context.
- “Local model” describes where inference runs.
- “RAG” describes an application architecture.

---

### 3 July 2026 — LangChain, LangGraph, agents, and ecosystem understanding

The user read parts of the LangChain and LangGraph documentation.

#### LangChain ecosystem understanding

Current working model:

- **LangChain** is an open-source application framework/library.
- **LangGraph** is an open-source graph-based orchestration framework for stateful workflows and agents.
- These open-source components can be used under their applicable open-source licenses.
- **LangSmith** is the main commercial product for tracing, observability, evaluation, deployment-related workflows, and team/production functionality.

Typical costs in an AI application do not primarily come from importing LangChain.

Costs usually come from:

- model API calls;
- embedding API calls;
- vector databases or search systems;
- cloud compute;
- storage;
- observability;
- external APIs;
- production hosting;
- engineering and operations.

Local alternatives can reduce direct API spending but shift cost and complexity toward:

- hardware;
- power;
- deployment;
- inference optimization;
- maintenance;
- model serving;
- lower model quality or throughput in some cases.

Do not describe LangChain’s business model as primarily based on model-provider contracts unless verified. The safer distinction is:

- LangChain/LangGraph: open-source frameworks;
- LangSmith and enterprise services: commercial offering;
- model-provider charges: paid directly to the relevant providers unless another platform is explicitly intermediating them.

---

## 7. Agent concepts covered

A Day 3 Anki sequence was planned around:

1. Agent versus chain
2. Tool use
3. ReAct loop
4. Agent versus simple RAG pipeline
5. Short-term versus long-term memory
6. LangGraph node
7. LangGraph edge

Concepts 1–5 were worked through. LangGraph nodes and edges were planned as the next concepts.

### 7.1 Agent versus chain

A **chain or fixed workflow** follows a predefined sequence of operations.

An **agent** dynamically decides which action to take next based on:

- the current goal;
- current state;
- available tools;
- previous observations;
- termination conditions.

Key distinction:

> A workflow designer chooses the next step in a chain. The model may choose the next step in an agent.

A system can use LLM calls without being an agent.

A graph can also contain both deterministic and agentic nodes.

Prefer a chain/workflow when:

- the steps are known in advance;
- predictable behavior is important;
- reliability matters more than flexibility;
- the task can be expressed deterministically;
- cost and latency should be controlled.

Prefer an agent when:

- the correct sequence cannot be fully predetermined;
- tool selection depends on intermediate results;
- the system must adapt after observations;
- iterative exploration is necessary;
- failures can be bounded and evaluated.

The deciding principle is usually:

> Use the simplest system that can reliably solve the task.

---

### 7.2 Tools

A tool is a callable capability exposed to a model or orchestrator.

Examples:

- search;
- database query;
- calculator;
- file retrieval;
- email action;
- calendar action;
- API request;
- code execution;
- business-system operation.

A tool normally has:

- a name;
- a description;
- an input schema;
- implementation code;
- an output.

The model does not directly perform the external action merely by producing natural language. It selects or requests a tool call in a structured form. The application validates and executes it, then returns the result.

Important concerns:

- clear tool descriptions;
- strict schemas;
- input validation;
- permissions;
- idempotency where relevant;
- timeouts;
- retries;
- safe error handling;
- logging;
- confirmation before destructive actions.

---

### 7.3 ReAct loop

ReAct means:

> **Reason → Act → Observe → repeat**

Operationally:

1. Inspect the goal and current state.
2. Decide what information or action is needed.
3. Select a tool or action.
4. Execute it.
5. Observe the result.
6. Update the state.
7. Decide whether to continue or return the final answer.

The loop stops when:

- the goal is satisfied;
- a terminal state is reached;
- a maximum-step limit is reached;
- the process fails safely;
- human input is required.

Important implementation note:

- Internal model reasoning does not need to be exposed.
- The application should retain observable state, tool calls, outputs, errors, and decisions needed for debugging.

---

### 7.4 Agent versus RAG

RAG and agents address different dimensions.

RAG primarily addresses:

> How does the model obtain relevant external knowledge?

Agents primarily address:

> How does the system dynamically choose and sequence actions?

They are not mutually exclusive.

Possible systems include:

- simple LLM without retrieval;
- fixed RAG pipeline;
- deterministic workflow with tools;
- agent without RAG;
- agent that uses retrieval as one tool;
- graph containing retrieval, deterministic logic, and agentic decisions.

Use simple RAG when:

- the main requirement is answering from a known knowledge base;
- retrieval and answer generation are sufficient;
- the sequence is stable;
- no dynamic planning is needed.

Use an agent when:

- multiple tools may be needed;
- the system must decide which tool to use;
- intermediate observations change the next step;
- the number or order of steps is not fixed.

---

### 7.5 Short-term versus long-term memory

Short-term memory is state relevant to the current execution or conversation.

Examples:

- current messages;
- retrieved context;
- intermediate tool outputs;
- current plan;
- variables in the active graph state.

Long-term memory persists beyond a single run or conversation.

Examples:

- durable user preferences;
- previously learned facts;
- historical outcomes;
- stored summaries;
- business entities;
- persistent task state.

Important distinction:

- A model context window is not automatically durable memory.
- Persistence requires an external storage mechanism.
- Memory should be selective; storing everything creates noise, privacy risk, and retrieval problems.
- Long-term memory needs:
  - a write policy;
  - a retrieval policy;
  - update and deletion behavior;
  - provenance;
  - privacy controls.

---

### 7.6 LangGraph concepts still to formalize

#### Node

A node is a unit of computation in a graph.

A node can:

- call a model;
- call a tool;
- retrieve data;
- transform state;
- validate output;
- request human input;
- decide routing information.

#### Edge

An edge determines how execution moves between nodes.

Edges may be:

- unconditional;
- conditional;
- looping;
- terminal.

In LangGraph, graph state is passed through nodes and updated over time. The primary value is explicit orchestration, inspectable state transitions, cycles, persistence, and controlled branching.

These concepts should still be converted into final Anki cards and applied in a small graph implementation.

---

## 8. Current practical build: `01_mini_rag`

### 8.1 Purpose

The current code project is a small toy RAG application.

Primary objective:

> Get a complete minimal RAG pipeline running while understanding each component.

This is an educational build, not yet a production application.

### 8.2 Known repository context

Observed working path:

```text
~/proj/AI-Lab/builds/01_mini_rag
```

Observed branch:

```text
main
```

A Python virtual environment is used:

```text
.venv
```

A local `.env` file is used for API credentials.

The relevant environment variable is:

```text
GOOGLE_API_KEY
```

A command used to verify the `.env` file and key loading was:

```bash
python -c "from pathlib import Path; from dotenv import dotenv_values; p=Path.cwd()/'.env'; print(p); print(p.exists()); print('GOOGLE_API_KEY' in dotenv_values(p)); print(bool(dotenv_values(p).get('GOOGLE_API_KEY')))"
```

The verification checks:

1. the resolved `.env` path;
2. whether the file exists;
3. whether `GOOGLE_API_KEY` is present;
4. whether the value is non-empty.

Secrets must never be committed.

Recommended `.gitignore` coverage includes:

```gitignore
.env
.env.*
!.env.example
.venv/
__pycache__/
*.py[cod]
```

An `.env.example` may document the variable name without containing a real key:

```dotenv
GOOGLE_API_KEY=
```

---

## 9. Model and API strategy

The first API integration uses Google-hosted models.

The user wants to understand model selection rather than always using the strongest model.

Selection criteria:

- task difficulty;
- latency;
- token limits;
- requests-per-minute;
- requests-per-day;
- cost;
- free-tier availability;
- model availability;
- context size;
- output quality;
- embedding compatibility.

The user explicitly prefers compact model guidance in this style:

```text
model-name — when to choose it
```

General model strategy:

- use a small/cheap model for:
  - ingestion experiments;
  - prompt wiring;
  - retrieval debugging;
  - repeated local development;
  - simple classification or extraction;
- use a stronger model for:
  - difficult synthesis;
  - ambiguous reasoning;
  - complex agent decisions;
  - final quality comparisons;
- use a dedicated embedding model for document and query embeddings;
- do not use an expensive generation model for embeddings;
- make model IDs configurable rather than scattered through the code.

Previously discussed candidate IDs included Gemini Flash/Flash-Lite variants and `gemini-embedding-001`. These identifiers and their quotas can change and must be checked against current Google documentation before hardcoding them.

The user also mentioned potentially experimenting with Gemma 4 variants such as 26B or 31B if their availability and quotas are favorable. Exact model names and availability were not finalized and must be verified before use.

### 9.1 Quota understanding

The user initially found values such as hundreds of thousands of tokens per minute surprisingly high compared with interactive coding sessions.

Important quota concepts:

- **RPM**: requests per minute
- **TPM**: tokens per minute
- **RPD**: requests per day
- input and output tokens may both count depending on provider rules
- minute-level limits may appear generous while daily request limits become the actual bottleneck
- embeddings and generation models may have separate quotas
- quotas are shared by project/account according to provider rules
- hitting a quota can produce rate-limit errors even when billing credit remains

A long coding session does not necessarily consume extreme token volume. Token usage depends on:

- prompt length;
- retrieved context;
- output length;
- repeated retries;
- number of parallel calls;
- agent loop length;
- conversation history sent on every request.

The code should log or otherwise expose token usage when the SDK provides it.

---

## 10. Cloud versus local models

The project should include exposure to both approaches.

### Cloud models

Advantages:

- easiest setup;
- strong model quality;
- managed infrastructure;
- scalable;
- no local inference engineering.

Disadvantages:

- recurring API cost;
- quotas;
- network dependency;
- data-governance concerns;
- provider-specific behavior;
- possible model deprecation.

### Local models

Advantages:

- more control;
- no per-call provider bill;
- offline use;
- data can remain local;
- useful for experimentation with open models.

Disadvantages:

- hardware requirements;
- slower inference on insufficient hardware;
- setup complexity;
- serving and monitoring work;
- memory constraints;
- potentially weaker quality;
- operational responsibility.

The architecture should avoid unnecessary provider lock-in, but provider abstraction must not become premature overengineering.

A practical approach:

1. get the pipeline working with one cloud model;
2. isolate the model interface;
3. add a local model experiment later;
4. compare quality, latency, memory use, and operational complexity.

---

## 11. Expected architecture for the mini-RAG

A minimal but clear structure may include:

```text
01_mini_rag/
├── README.md
├── pyproject.toml or requirements.txt
├── .env.example
├── .gitignore
├── data/
├── src/
│   ├── config.py
│   ├── ingest.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieve.py
│   ├── generate.py
│   └── main.py
└── tests/
```

This is a suggested logical separation, not a requirement to refactor immediately.

The first complete vertical slice should be:

1. load one small document;
2. split it into chunks;
3. create embeddings;
4. store them;
5. embed a query;
6. retrieve relevant chunks;
7. call the generation model with those chunks;
8. print the answer and retrieved sources.

Only after the vertical slice works should the project add:

- persistence;
- multiple documents;
- metadata filters;
- alternative chunking;
- reranking;
- evaluation sets;
- UI;
- agents.

---

## 12. Evaluation requirements

The project should not evaluate only whether an answer “looks good.”

RAG evaluation should separate:

### 12.1 Retrieval evaluation

Questions:

- Was the necessary chunk retrieved?
- Was it ranked highly enough?
- Were irrelevant chunks included?
- Did chunking separate information badly?
- Did metadata filtering help?
- Did the query need rewriting?

Possible metrics:

- hit rate;
- recall@k;
- precision@k;
- mean reciprocal rank;
- manually labeled relevance.

### 12.2 Generation evaluation

Questions:

- Is the answer correct?
- Is it supported by retrieved context?
- Does it cite the correct source?
- Does it invent unsupported details?
- Does it admit when context is insufficient?
- Is it concise and useful?

### 12.3 System evaluation

Measure:

- latency;
- token usage;
- API calls;
- estimated cost;
- failure rate;
- reproducibility;
- behavior with empty or conflicting retrieval;
- robustness to malformed documents.

A small manually created evaluation dataset is preferable to no evaluation.

---

## 13. Documentation expectations

Every meaningful build should explain:

- the problem;
- the intended user;
- the architecture;
- setup;
- environment variables;
- how to run it;
- sample inputs and outputs;
- design decisions;
- alternatives considered;
- known limitations;
- evaluation method;
- results;
- next steps.

The final project should support a recruiter or engineer who opens the repository and wants to understand it quickly.

Avoid marketing language that overstates capability.

For example:

- do not call a fixed scripted workflow an autonomous agent;
- do not claim hallucinations are eliminated;
- do not call a toy demo production-ready;
- do not imply fine-tuning when only prompt engineering or RAG is used.

---

## 14. Instructions for Codex

### 14.1 General collaboration style

Codex should:

- work in small, inspectable increments;
- explain what a change does and why it is needed;
- prefer a working vertical slice over broad scaffolding;
- verify each stage before adding complexity;
- preserve the user’s opportunity to understand the implementation;
- point out conceptual mistakes directly;
- distinguish required work from optional improvements;
- provide compact answers when a compact answer is requested;
- avoid repeating information the user has already supplied;
- assume the user knows fundamental programming but is learning AI application engineering.

Do not turn every learning step into a large framework abstraction.

Do not introduce an agent before a fixed workflow has been considered.

Do not introduce a vector database service if an in-memory or local option is sufficient for the current learning objective.

### 14.2 Repository safety

The user wants direct control over Git history.

Codex must not automatically:

- stage files;
- commit changes;
- amend commits;
- rebase;
- squash;
- stash;
- reset;
- clean;
- discard changes;
- include unrelated uncommitted files.

These actions require explicit user approval.

Before editing:

- inspect the current repository state;
- avoid touching unrelated files;
- preserve existing uncommitted work;
- describe which files will be changed.

When suggesting a commit:

- show the exact files that belong to it;
- let the user perform or explicitly approve the commit;
- do not add `Co-Authored-By` metadata unless explicitly requested.

### 14.3 Secrets and configuration

Never:

- print a real API key;
- commit `.env`;
- hardcode credentials;
- put secrets in screenshots, logs, fixtures, or documentation.

Prefer:

- `.env`;
- `.env.example`;
- centralized configuration;
- startup validation with clear errors.

### 14.4 Dependency choices

Before adding a dependency:

- explain what problem it solves;
- check whether the standard library or an existing dependency is sufficient;
- avoid adding large frameworks for a trivial function;
- pin or constrain versions appropriately;
- update the dependency file and documentation together.

### 14.5 Testing style

At each step, provide a direct verification method.

Examples:

- environment key loads;
- model call succeeds;
- embeddings have expected shape;
- vector store contains expected chunks;
- retrieval returns the known relevant chunk;
- generated answer uses the retrieved context;
- missing-key behavior fails clearly;
- invalid input does not crash unclearly.

---

## 15. Near-term next steps

The immediate sequence should remain compact and practical.

### Step 1 — stabilize the minimal model call

Confirm:

- virtual environment is active;
- dependencies are installed;
- `.env` loads;
- `GOOGLE_API_KEY` is available;
- selected model ID is current;
- one simple request succeeds;
- errors are readable.

### Step 2 — create the smallest RAG vertical slice

Use a tiny known document and one question with an obvious answer.

Implement:

- loader;
- chunker;
- embeddings;
- local vector storage;
- retrieval;
- prompt assembly;
- generation;
- source display.

### Step 3 — inspect retrieval before generation

Print or log:

- query;
- retrieved chunks;
- similarity scores where available;
- source metadata.

Do not debug generation before confirming retrieval.

### Step 4 — add a minimal evaluation set

Create approximately 5–10 questions containing:

- direct answer;
- answer spread across chunks;
- irrelevant question;
- missing information;
- ambiguous wording.

Record expected sources and expected answer behavior.

### Step 5 — document the learning build

Add a README explaining:

- why the project exists;
- architecture;
- how to configure it;
- how to run ingestion;
- how to ask a question;
- limitations;
- next experiments.

### Step 6 — complete Day 3 concepts

Finalize Anki cards for:

- short-term versus long-term memory;
- LangGraph node;
- LangGraph edge.

Then create a minimal LangGraph example only when it adds a useful learning contrast to the fixed RAG pipeline.

### Step 7 — begin SME use-case reconnaissance

Investigate candidate processes based on:

- real pain;
- access to representative data;
- clear user;
- repetitive knowledge work;
- measurable success;
- feasible integration scope;
- privacy and risk;
- whether AI is actually useful.

Do not select a use case merely because it looks impressive.

---

## 16. Open decisions

The following are not finalized:

- exact final SME use case;
- exact final portfolio architecture;
- whether the final project needs an agent;
- cloud model provider for the final system;
- whether a local model will be part of the final deployed system or only an experiment;
- vector store choice;
- UI framework;
- deployment target;
- evaluation framework;
- long-term memory requirements;
- exact Gemini/Gemma model IDs.

Treat these as decisions to be made from evidence, not defaults.

---

## 17. Definition of success

The sprint is successful when the user can credibly show and explain:

1. a working AI automation system;
2. why its architecture was chosen;
3. why simpler alternatives were rejected or accepted;
4. how retrieval and generation were evaluated;
5. how errors and unsafe actions are controlled;
6. what the system costs;
7. how it could be deployed and monitored;
8. its limitations;
9. what was learned;
10. what the user personally implemented.

The strongest final result is not the system with the most AI components.

It is the system that:

- solves a real problem;
- uses the correct amount of AI;
- is engineered clearly;
- is tested;
- is documented honestly;
- can be demonstrated;
- can be defended in a technical interview.
