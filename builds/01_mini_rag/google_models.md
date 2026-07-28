# Google Models to choose from 

## Models and their usage: ##
*gemini-3.1-flash-lite* - default for cheap, fast and less complexity.
 - RPM: 15
 - TPM: 250k
 - RPD: 500

*gemini-2.5-flash-lite* - fallback cheap model.
 - RPM: 10
 - TPM: 250k
 - RPD: 20

*gemini-2.5-flash* - default for mor complex questions.
 - RPM: 5
 - TPM: 250k
 - RPD: 20

*gemini-3.5-flash* - when 2.5's answers aren't good enough.
 - RPM: 5
 - TPM: 250k
 - RPD: 20

*gemma-4-31b-it* - additional for openweights categories.
 - RPM: 15
 - TPM: inf
 - RPD: 1.5k

*gemma-4-26b-a4b-it* - additional for openweights categories.
 - RPM: 15
 - TPM: inf
 - RPD: 1.5k

*gemini-embedding-001* - use for embeddings in the RAG pipeline; this creates the vectors for document chunks and queries.