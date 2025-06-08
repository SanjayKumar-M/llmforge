# Span: Not a method, used internally to represent a slice of tokens
# Example: a span could represent a part of the text, like "New York"

# Noun Chunks / ents / sents: Span is used internally by spaCy for these
# Example: "New York" could be recognized as a noun chunk (ent) by spaCy

# pos_: Grammatical role of word (e.g., noun, verb, adjective)
# Example: 'dog' -> 'NOUN', 'running' -> 'VERB'

# NER (Named Entity Recognition): Labels chunks/words to give them meaning
# Example: "Royal Challengers Bangalore" might be labeled as an 'ORG' (organization)

# ents: Complete entities like "Royal Challengers Bangalore" (not half chunks)
# Example: spaCy would recognize "Barack Obama" as a single named entity

# Lexeme: spaCy’s internal dictionary/vocab mapping for word knowledge
# Example: 'run' -> represents the word 'run' in spaCy's internal system

# Doc: The full input to nlp() which contains the processed text
# Example: A document would be the entire text you pass to the nlp() function
