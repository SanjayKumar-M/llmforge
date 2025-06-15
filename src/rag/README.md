Building simple RAG application to understand the end to end workflow
# RAG for Resume Analyzer and Reviewer

## Overview
This project is a simple Retrieval-Augmented Generation (RAG) system designed to analyze and review resumes. Users can submit their resumes and receive role-specific advice on whether the resume fits the desired role and suggestions for improvement.

## Tech Stack
1. **Programming Language**: Python
2. **LLM API**: Groq - `llama-4-scout-17b-16e-instruct`
3. **Vector Database**: Chroma DB for storing vector embeddings
4. **Embedding Model**: `BAAI/bge-base-en-v1.5`

## Workflow
1. **Data Ingestion**: Extract data from the submitted resume.
2. **Embedding Creation**: Generate embeddings using the embedding model and store them as vectors in Chroma DB.
3. **Querying LLM**: Use a predefined prompt and context derived from the resume data to query the LLM API.
4. **Response Generation**: The LLM generates a response with role-specific advice and improvement suggestions.

## Features
- Role-specific resume analysis
- Suggestions for resume improvement
- Efficient data processing with embeddings and vector storage

## Usage
1. Submit a resume.
2. Specify the desired role.
3. Receive feedback and actionable insights.
