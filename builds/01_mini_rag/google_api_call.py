import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


PROJECT_DIR = Path(__file__).parent
load_dotenv(PROJECT_DIR / ".env")

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError(
        "Missing GOOGLE_API_KEY. Must be in AI-Lab/builds/01_mini_rag/.env, and saved afterwards."
    )

model = ChatGoogleGenerativeAI(
    model="gemma-4-31b-it",
)

"""Models to choose from:
gemini-3.1-flash-lite - default for cheap, fast and less complexity.
gemini-2.5-flash-lite - fallback cheap model.

gemini-2.5-flash - default for mor complex questions.
gemini-3.5-flash - when 2.5's answers aren't good enough.

gemma-4-31b-it - additional for openweights categories.
gemma-4-26b-a4b-it - additional for openweights categories.

gemini-embedding-001 - for embeddings in RAG pipeline.
"""

response = model.invoke(
    [
        ("system","You are an expert in answering QA questions."),
        ("human","hello"),
    ]
)

print(response.content)