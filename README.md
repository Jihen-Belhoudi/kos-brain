# KOS – Knowledge Operating System

## Overview

KOS (Knowledge Operating System) is a local, modular Retrieval-Augmented Generation (RAG) system designed to ingest documents, store them as semantic embeddings, retrieve relevant knowledge, and generate grounded answers using a local Large Language Model (LLM).

The project emphasizes clarity, modularity, and privacy, making it suitable for private data, experimentation, and extensible AI systems.

## Motivation

Large Language Models are powerful, but they suffer from key limitations:

- They do not have access to private or domain-specific documents
- They may hallucinate when answering without grounded context
- They are often tightly coupled to external APIs

KOS addresses these limitations by:

- Separating knowledge retrieval from answer generation
- Grounding responses in real documents
- Running entirely locally, without external APIs or cloud dependencies

## High-Level Architecture

Documents (PDF / TXT / MD) -> Document Loader -> Text Chunking -> Embeddings (Sentence Transformers) -> Vector Database (ChromaDB) -> Relevant Context Retrieval -> Local LLM (Ollama + Mistral)
-> Final Answer


## Installation

### Prerequisites

- Python 3.10 or 3.11
- Ollama installed locally

### Pull Model

ollama pull mistral


### Python Setup



python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## Usage

python main.py


## Current Limitations

- Single-agent execution
- No source citation
- CLI-based interface

## Future Improvements

- Source citations
- Multi-agent orchestration
- API interface

