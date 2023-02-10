text_1 = 'Linkedin is the best place to expand one’s network.'

# Tokenising text without using complete NLP pipeline. Thus, printing each token’s corresponding text

nlp = _________

doc = _________(text_1) # Tokenising the text

# Using NLP pipeline for tokenising text without using tagger and parser

print(_________)

text_2 = 'Linkedin is the best place to expand one’s network.'

# Printing the entities from the final doc

# Disable the tagger and parser
with _________(_________):

  _________ = _________(text_2) # Processing the text

  print(doc._________) # Printing the entities
