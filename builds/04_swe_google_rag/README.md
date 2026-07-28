# Software Engineering at Google RAG

This mini-project will implement a small retrieval-augmented generation (RAG)
system over user-provided PDF material related to *Software Engineering at Google*. 
It is a learning build intended to make indexing, embeddings,
similarity retrieval, grounding, and evaluation visible before introducing
larger frameworks or a user interface.

The repository currently contains **only a scaffold**. PDF extraction,
chunking, embeddings, vector persistence, retrieval, generation, and the CLI
are not implemented yet.

## Intended model stack

- Google-hosted Gemma instruction model for answer generation
- Google embedding model, initially expected to be `gemini-embedding-001`
- Local file-backed vector storage

Exact model identifiers are deliberately not configured in source code. They
must be selected and verified through environment variables before the
integration is implemented.

## High-level architecture

The system is divided into two execution phases.

### Indexing time

Indexing runs when source PDFs are added or changed:

1. Discover PDFs in `data/pdfs/`.
2. Extract text and page metadata.
3. Split text into overlapping, token-based chunks.
4. Embed each chunk with the configured embedding model.
5. Store vectors, chunk text, source filename, page number, chunk ID, detected
   section information, and index metadata in `data/vector_store/`.

Document embeddings should be created once and reused for later questions.

### Query time

Query processing runs for each user question:

1. Embed the complete question with the same model and dimensionality used
   during indexing.
2. Search the local vector store using similarity.
3. Retrieve the nearest chunks (`TOP_K=3` initially).
4. Format their text and source metadata into grounded model context.
5. Ask the configured Gemma model to answer only from that context.
6. Return the answer with source references, or state that the supplied
   documents do not contain enough information.

The query itself will not be split in the first version because questions are
expected to be short.

## Planned project structure

```text
04_swe_google_rag/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   ├── pdfs/
│   │   └── .gitkeep
│   └── vector_store/
│       └── .gitkeep
├── src/
│   └── swe_google_rag/
│       ├── __init__.py
│       ├── chunking.py
│       ├── config.py
│       ├── documents.py
│       ├── embeddings.py
│       ├── generation.py
│       ├── indexing.py
│       ├── main.py
│       ├── rag.py
│       ├── schemas.py
│       └── vector_store.py
└── tests/
    ├── test_chunking.py
    ├── test_config.py
    └── test_retrieval.py
```

Input PDFs and generated vector-store files are intentionally ignored by Git.
Only their placeholder files are tracked.

## Planned environment variables

| Variable | Purpose |
| --- | --- |
| `GOOGLE_API_KEY` | Credential used for Google model API calls |
| `GENERATION_MODEL` | Verified Google-hosted Gemma model ID |
| `EMBEDDING_MODEL` | Verified Google embedding model ID |
| `EMBEDDING_DIMENSION` | Embedding dimension shared by indexing and querying |
| `PDF_STORAGE_PATH` | Folder scanned for input PDFs |
| `VECTOR_STORE_PATH` | Folder used for persisted vector data |
| `CHUNK_SIZE_TOKENS` | Maximum token count for each document chunk |
| `CHUNK_OVERLAP_TOKENS` | Token overlap between adjacent chunks |
| `TOP_K` | Number of nearest chunks retrieved per question |

Copy `.env.example` to `.env` only when implementation begins, then insert the
real API key locally. Never commit `.env`.

## Dependency plan

`requirements.txt` records the small initial dependency set without installing
it. The project plans to use:

- the official Google Gen AI SDK for model APIs;
- `pypdf` for PDF extraction;
- NumPy for vector representation and similarity;
- `python-dotenv` for local environment loading;
- pytest for later verification.

No tokenizer dependency has been selected yet. The first chunking implementation
should choose a tokenization method that is appropriate for the selected
embedding model instead of silently using an unrelated tokenizer.

No LangChain, LangGraph, hosted vector database, or provider abstraction is
part of this scaffold.

## Next implementation step

Implement and test configuration loading first. It should:

1. load `.env` relative to this project;
2. validate required values without printing secrets;
3. parse numeric RAG settings;
4. resolve the configured data paths;
5. fail with clear messages for missing or invalid configuration.

After that works, implement PDF discovery and extraction as the first indexing
increment. Do not proceed to generation before inspecting and verifying
retrieval results.
