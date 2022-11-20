# %%

import spacy
from spacy.matcher import Matcher
from spacy import displacy


# %%

texts = ...  # texts loaded in a list

# Tranforms texts into docs (involves steps like tokenizer, tagger, parser, ner, etc)) 
nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello little cat, you are my friend!")

pattern = [
    {"POS": "NOUN"}
]

matcher = Matcher(nlp.vocab)
matcher.add("HelloPattern", [pattern])

matcher(doc)
# Match ID | Token Start | Token End
# [(10496072603676489703, 0, 1)]

# %%

doc = nlp("You should definitely buy Bitcoin")

pattern = [
    {"LEMMA": {"IN": ["buy", "sell"]}},
    {"LOWER": {"IN": ["bitcoin", "dogecoin"]}},
]

matcher = Matcher(nlp.vocab)
matcher.add("HelloWorld", [pattern])

matcher(doc)

# %%

nlp = spacy.load("en_core_web_sm")

doc_before = nlp("John lives in Atlanta")

# No entities are detected
print(doc_before.ents)


# Create an entity ruler and add it some patterns
entity_ruler = nlp.add_pipe("entity_ruler")

patterns = [
    {
        "label": "PERSON",
        "pattern": "John",
        "id": "john",
    },
    {
        "label": "GPE",
        "pattern": [{"LOWER": "atlanta"}],
        "id": "atlanta",
    },
]

entity_ruler.add_patterns(patterns)
doc_after = nlp("Jonh lives in Atlanta.")

for ent in doc.ents:
    print(ent.text, ":", ent.label_)

# %%

nlp = spacy.load("en_core_web_sm")

doc = nlp("John lives in France and works at Apple Inc.")

print(doc.ents)

displacy.render(doc, style="ent")
