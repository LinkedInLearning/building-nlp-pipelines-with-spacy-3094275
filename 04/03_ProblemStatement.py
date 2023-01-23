# Importing the blank English model

nlp = spacy.blank('en')

# Creating a new entity recogniser and adding it to the pipeline

ner = nlp.create_pipe('ner')

nlp.add_pipe(ner)

# Adding the label Gadget to the entity recogniser

ner.add_label('GADGET')

nlp._________ # Starting the training

for _________ in range(_________): # Looping for 10 iterations

  random._________(TRAINING_DATA) # shuffling

  _________ = _________ # Implementing batch processing

  for _________ in _________(TRAINING_DATA, size=_________):

    texts = [text for text, entities in batch]

    _________ = _________

    nlp.update(_________, _________, losses=_________) # updating the model

    print(_________)
