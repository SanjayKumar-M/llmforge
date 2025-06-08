## My undersntandings

## Span
A `Span` is not a method but an internal representation of a slice of tokens.  
**Example:** A span could represent a part of the text, like `"New York"`.

## Noun Chunks / Entities / Sentences
`Span` is used internally by spaCy to identify noun chunks, entities, and sentences.  
**Example:** `"New York"` could be recognized as a noun chunk (entity) by spaCy.

## `pos_`
Represents the grammatical role of a word (e.g., noun, verb, adjective).  
**Example:** `'dog' -> 'NOUN'`, `'running' -> 'VERB'`.

## Named Entity Recognition (NER)
Labels chunks or words to assign them meaning.  
**Example:** `"Royal Challengers Bangalore"` might be labeled as an `'ORG'` (organization).

## Entities (`ents`)
Represents complete entities, not partial chunks.  
**Example:** spaCy would recognize `"Barack Obama"` as a single named entity.

## Lexeme
spaCy’s internal dictionary/vocabulary mapping for word knowledge.  
**Example:** `'run'` represents the word `'run'` in spaCy's internal system.

## Document (`Doc`)
The full input processed by the `nlp()` function, containing the entire text.  
**Example:** A document would be the entire text you pass to the `nlp()` function.

