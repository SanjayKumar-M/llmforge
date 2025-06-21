from transformers import AutoTokenizer, AutoModel
import torch
from document_processing import document_processing
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"


model_name = "BAAI/bge-base-en-v1.5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to convert any text into a vector (embedding)
def embed_text(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():  # No training, just inference
        outputs = model(**inputs)
        # We take the vector of the [CLS] token (first one) as the summary of the text
        embeddings = outputs.last_hidden_state[:, 0]
        return embeddings[0].numpy()


# Function to create a vector DB and store all the resume chunks inside
def store_in_vector_db(chunks, collection):
    for i, chunk in enumerate(chunks):
        text = chunk.page_content
        embedding = embed_text(text)

        # Save the text, its vector, and some metadata
        collection.add(
            documents=[text],
            embeddings=[embedding.tolist()],
            ids=[f"chunk_{i}"],
            metadatas=[chunk.metadata]
        )
    print(f"Stored {len(chunks)} chunks in ChromaDB")

# Function to search for relevant chunks using a natural language query
def retrieve_relevant_chunks(query, collection, top_k=3):
    query_embedding = embed_text(query)
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )
    return results['documents'][0]  # List of top-k matching chunks
