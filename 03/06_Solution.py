text_1 = “Linkedin is the best place to expand one’s network.”

nlp = spacy.load(‘en_core_web_sm’)

doc = nlp.make_doc(text_1) # Tokenising the text

print([token.text for token in doc])

text_2 = “Linkedin is the best place to expand one’s network.”

# Disable the tagger and parser
with nlp.disable_pipes('tagger', 'parser'):

  doc = nlp(text_2) # Processing the text

  print(doc.ents) # Printing the entities
