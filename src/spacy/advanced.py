import spacy

# Load the pre-trained spaCy model
nlp = spacy.load('en_core_web_lg')

# Example sentence
sentence = "Royal challengers Bangalore won the IPL cup for the first time in 2025"

# Process the sentence
doc = nlp(sentence)

# Part-of-Speech Tagging
print("POS Tagging:")
for token in doc:
    print(f"{token.text}: {token.pos_} ({token.dep_})")

# Dependency Parsing
print("\nDependency Parsing:")
for token in doc:
    print(f"{token.text}: {token.dep_}, Head: {token.head.text}")

# Named Entity Recognition (NER)
print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
    
print("\nLematization")
for lem in doc:
    print(lem.text, " -> ",lem.lemma_)