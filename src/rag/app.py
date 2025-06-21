import steamlit as st
from document_processing import document_processing
from embedding import store_in_vector_db, retrieve_relevant_chunks
from llm import get_response
import chromadb
import os
import tempfile

st.set_page_config(page_title="AI Resume Reviewer", layout="centered")

st.title("📄 AI-Powered Resume Reviewer")
st.markdown("Upload your resume and get detailed feedback for a specific role.")

# Upload PDF
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
query = st.text_input("Job Description or Role Requirement", placeholder="e.g. Backend engineer with 1 year Node.js experience")

if uploaded_file and query:
    if st.button("🧠 Analyze Resume"):
        with st.spinner("Processing..."):

            # Save file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            # Process and embed
            chunks = document_processing(tmp_path)
            chroma_client = chromadb.Client()
            collection = chroma_client.get_or_create_collection(name="resume")

            store_in_vector_db(chunks, collection)
            top_chunks = retrieve_relevant_chunks(query, collection, top_k=3)

            response = get_response(query, top_chunks)

        st.success("✅ Analysis complete!")
        st.subheader("LLM Feedback:")
        st.markdown(response.content.strip())
