from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def document_processing(pdf):
# load the pdf, we can also use pdfplumber (already used)
    resume_loader = PyPDFLoader(pdf)
    docs = resume_loader.load()

# now chunking it
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    return chunks