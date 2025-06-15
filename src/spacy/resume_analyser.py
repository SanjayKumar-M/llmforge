from langchain_community.document_loaders import PDFPlumberLoader
import spacy
loader = PDFPlumberLoader('../data/resume.pdf')
docs = loader.load()
full_text = "\n".join(doc.page_content for doc in docs)
for doc in docs:
    full_text.join(doc.page_content)

      
# preprocessing the input for Spacy

# def resume_analyser(resume_text):
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(resume_text)
    
#     for ent in doc.ents:
#         print(ent.text, ent.label_)

# resume_analyser(full_text)