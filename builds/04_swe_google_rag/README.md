# Software Engineering at Google RAG

This project is a small, transparent retrieval-augmented generation (RAG)
pipeline over PDF chapters from *Software Engineering at Google*. It uses the
Google Gen AI SDK for embeddings and grounded answer generation, while keeping
document extraction, chunking, vector persistence, and cosine retrieval local.

The pipeline is implemented, tested, and runnable from the command line.

## What it does

Indexing:

1. Finds PDFs recursively in `data/pdfs/`.
2. Extracts page-aware text with `pypdf`.
3. Splits each page into deterministic overlapping lexical-token chunks.
4. Embeds the chunks with `gemini-embedding-001`.
5. Saves vectors and source metadata in
   `data/vector_store/index.npz`.

Question answering:

1. Embeds the complete question with the same embedding configuration.
2. Ranks stored chunks by cosine similarity.
3. Sends the nearest chunks to the configured Google generation model.
4. Returns a grounded answer with source labels and page references.
5. Explicitly says when the retrieved evidence is insufficient.

No LangChain, hosted vector database, or provider abstraction is used.

## Quick start

```bash
cd builds/04_swe_google_rag
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
cp .env.example .env
```

Add a valid Google AI Studio key to `GOOGLE_API_KEY` in `.env`, place one or
more PDFs in `data/pdfs/`, then run:

```bash
swe-google-rag index
swe-google-rag ask "What are the main differences between programming and software engineering?"
```

The API key, input PDFs, and generated vector index are ignored by Git.

For the full setup, operating workflow, configuration reference, and
troubleshooting guide, read [USER_MANUAL.md](USER_MANUAL.md).

## Default model configuration

```dotenv
GENERATION_MODEL=gemma-4-26b-a4b-it
EMBEDDING_MODEL=gemini-embedding-001
EMBEDDING_DIMENSION=768
```

The generation model can be changed to another model available to the Google
API key. Changing the embedding model or dimension requires rebuilding the
index.

Current model contracts were checked against the
[Google Gen AI Python SDK](https://googleapis.github.io/python-genai/),
[Gemini embedding API](https://ai.google.dev/api/embeddings), and
[Gemma on the Gemini API](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api).

## Development verification

Run the local test suite without making external API calls:

```bash
python -m pytest -q
```

The completed implementation has 42 passing tests. It was also verified live
with the included local chapter PDFs:

- 2 PDFs discovered;
- 37 pages extracted;
- 59 chunks indexed;
- 768-dimensional vectors stored;
- a relevant question answered with correct page citations;
- an unrelated question rejected as insufficiently supported.

See [JAN_DEVELOPMENT_LOG.md](JAN_DEVELOPMENT_LOG.md) for the first-person
repair record, decisions, and verification evidence.

## Project structure

```text
04_swe_google_rag/
├── .env.example
├── JAN_DEVELOPMENT_LOG.md
├── README.md
├── USER_MANUAL.md
├── pyproject.toml
├── requirements.txt
├── data/
│   ├── pdfs/
│   └── vector_store/
├── src/swe_google_rag/
│   ├── chunking.py
│   ├── config.py
│   ├── documents.py
│   ├── embeddings.py
│   ├── generation.py
│   ├── indexing.py
│   ├── main.py
│   ├── rag.py
│   ├── schemas.py
│   └── vector_store.py
└── tests/
```

## Deliberate limitations

- Text must already be extractable from the PDF; there is no OCR.
- Chunk sizes use deterministic lexical tokens rather than Google billing
  tokens because Google does not expose a local tokenizer for
  `gemini-embedding-001`.
- Indexing performs a full rebuild instead of incremental document updates.
- Retrieval is dense cosine similarity only; there is no reranker or lexical
  fallback.
- The vector index is a local file intended for this learning-scale project,
  not concurrent multi-user workloads.
