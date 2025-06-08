# read text from file

with open('../data/data.txt','r',encoding='utf-8') as file:
    data = file.read()
    
partialdata = data[:1000]  # taking only the first 1000 characters for testing

# now using spacy

import spacy
nlp = spacy.load('en_core_web_sm')
print(nlp.add_pipe)  # checking the available pipelines
rcb_doc = nlp(partialdata)
for sentence in rcb_doc.sents:
    print(sentence.text)  # extracting sentences from the document
    for word in sentence:
       print(word)  # extracting words from the document approach: 1
        

# extracting words from the document approach: 2
datas = [word.text for word in rcb_doc]  
print(datas)

for ent in rcb_doc.ents:
    print(ent.text, ent.label)
    

def spacy_large_ner(document):
  return {(ent.text.strip(), ent.label_) for ent in nlp(document).ents}
print(spacy_large_ner(data))