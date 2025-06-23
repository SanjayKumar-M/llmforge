from llama_index.core import SimpleDirectoryReader
reader = SimpleDirectoryReader('/Users/sanjay/Desktop/llmforge/src/data') 
documents = reader.load_data()
print(documents[0].text)