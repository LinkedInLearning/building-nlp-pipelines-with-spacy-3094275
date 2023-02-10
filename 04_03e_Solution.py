# Executing a Training Loop from scratch

# Importing the blank English model

nlp = spacy.blank('en')

# Creating a new entity recogniser and adding it to the pipeline

ner = nlp.create_pipe('ner')

nlp.add_pipe(ner)

# Adding the label Gadget to the entity recogniser

ner.add_label('GADGET')

nlp.begin_training() # Starting the training

# Implementing Batch processing with batch size of 2

for itn in range(10): # Looping for 10 iterations

  random.shuffle(TRAINING_DATA) # shuffling

  losses = {} # Implementing batch processing

  # Extracting text & annotations from respective entities

  for batch in spacy.util.minibatch(TRAINING_DATA, size=2):

    texts = [text for text, entities in batch]

    annotations = [entities for text, entities in batch]

    # Updating & saving the model after each iteration & printing the iteration loss

    nlp.update(texts, annotations, losses=losses) # updating the model

    print(losses)
