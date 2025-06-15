from llm import get_response
from document_processing import document_processing
from embedding import store_in_vector_db, retrieve_relevant_chunks
import chromadb

chunks  =  document_processing('../data/resume.pdf')
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="resume")


storage = store_in_vector_db(chunks,collection)
query = "I want to hire for Javascript Backend engineer who has 1 year of experience atleast"
fetch_chunks = retrieve_relevant_chunks(query,collection,top_k=3)

response = get_response(query,fetch_chunks)
print(response.content.strip())
