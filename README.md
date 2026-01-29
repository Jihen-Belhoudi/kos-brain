# KOS – Knowledge Operating System
## Overview

KOS (Knowledge Operating System) is a local, modular Retrieval-Augmented Generation (RAG) system designed to ingest documents, store them as semantic embeddings, retrieve relevant knowledge, and generate grounded answers using a local Large Language Model (LLM).

The project emphasizes clarity, modularity, and privacy, making it suitable for private data, experimentation, and extensible AI systems.

## Motivation

Large Language Models are powerful, but they suffer from key limitations:

They do not have access to private or domain-specific documents

They may hallucinate when answering without grounded context

They are often tightly coupled to external APIs

KOS addresses these limitations by:

Separating knowledge retrieval from answer generation

Grounding responses in real documents

Running entirely locally, without external APIs or cloud dependencies

High-Level Architecture
Documents (PDF / TXT / MD)
        ↓
Document Loader
        ↓
Text Chunking
        ↓
Embeddings (Sentence Transformers)
        ↓
Vector Database (ChromaDB)
        ↓
Relevant Context Retrieval
        ↓
Local LLM (Ollama + Mistral)
        ↓
Final Answer


This architecture follows standard RAG principles while remaining simple, transparent, and extensible.

## Core Components
Document Loader (rag/doc_loader.py)

Reads documents from the data/ directory

Supports PDF, TXT, and Markdown formats

Extracts raw text for further processing

Text Chunking (rag/chunker.py)

Splits large documents into smaller overlapping chunks

Improves retrieval precision

Reduces noise in LLM prompts

Ensures better grounding during answer generation

Vector Store (rag/vector_store.py)

Uses Sentence Transformers to compute embeddings

Stores embeddings in ChromaDB

Acts as the system’s long-term semantic memory

RAG Engine (rag/rag_engine.py)

Orchestrates the full RAG pipeline

Retrieves the most relevant chunks for a query

Builds a context-aware prompt

Calls the LLM to generate a grounded answer

LLM Client (core/llm_client.py)

Interfaces with a local LLM through Ollama

Uses Mistral by default

Ensures non-interactive, one-shot execution for reliability on Windows and Linux

Why Local LLMs (Ollama)

Full control over data and execution

No API keys or usage limits

Suitable for private or sensitive documents

Easy to swap models (Mistral, LLaMA, etc.)

## Project Structure
KOS_BRAIN/
├── agents/                # Future agent orchestration
├── core/
│   └── llm_client.py      # Local LLM interface
├── rag/
│   ├── chunker.py         # Text chunking logic
│   ├── doc_loader.py      # Document ingestion
│   ├── vector_store.py   # Embeddings + vector DB
│   └── rag_engine.py     # Retrieval + generation
├── data/                 # Documents to ingest
├── main.py               # Entry point
├── requirements.txt
└── README.md

## Installation
Prerequisites

Python 3.10 or 3.11

Ollama installed locally

Install Ollama:

https://ollama.com


## Pull the model:

ollama pull mistral

Python Setup
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt

## Usage

Place your documents in the data/ folder

Run the system:

python main.py


The system will:

Load and chunk documents

Generate embeddings and store them in ChromaDB

Retrieve relevant context for a query

Generate a grounded answer using the local LLM

Design Principles

Modular and replaceable components

Local-first and privacy-oriented

Clear separation of concerns

Minimal abstractions

Designed for extensibility (agents, tools, APIs)

Current Limitations

Single-agent question answering

No source citation in responses

No metadata-based filtering

CLI-based execution only

These limitations are intentional to keep the core system simple and understandable.

Future Improvements

Source citations

Multi-agent orchestration

FastAPI interface

Streaming LLM responses

Advanced chunking strategies

Evaluation and logging pipelines
