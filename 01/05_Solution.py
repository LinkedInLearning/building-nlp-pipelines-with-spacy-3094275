# Part - 1

text = “Ram goes to college everyday by car.”
# Importing spacy and getting all attributes.

nlp = spacy.load(‘en_core_web_sm’)
doc = nlp(text)

for token in doc:
  token_text = token.text # Getting the corresponding text
  token_dep = token.dep_ # Getting the Dependency label
  token_pos = token.pos_ # Getting the POS Tag
  print(token_text, token_dep, token_pos)


# Part - 2

text = “Ram goes to college everyday by car.”
# Importing spacy and getting all attributes.

nlp = spacy.load(‘en_core_web_sm’)
doc = nlp(text)

for ent in doc.ents:
  # Printing the entity text and label
  print(ent.text, ent.label_)
