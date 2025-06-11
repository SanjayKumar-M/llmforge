import spacy
from spacy import displacy # this is for visually appealing ui on cli

nlp = spacy.load("en_core_web_sm")

with open('../data/data.txt','r',encoding='utf-8') as file:
    data = file.read()
    
rcb_data =  nlp(data[:199])

for sent in rcb_data.sents:
    print("Whole Sentence: ",sent)
    for word in sent:
        print("Word by word: ",word)  # first level of tokenization i.e raw text into sentence into words
       

for ner in rcb_data.ents:
    print("Entities: ",ner.text) # not word by word, but an entity. for example Saveetha engineering college (noun), not word by word

for ner in rcb_data.noun_chunks:
    print("Noun chunks",ner.text_with_ws) # with white space at the end "Sanjay " example


# displacy.serve(rcb_data, style="ent") 
displacy.serve(rcb_data, style="dep", port=5000)