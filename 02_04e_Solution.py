# Importing Phrase Matcher & initialise it.

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

# Creating pattern doc objects

patterns = list(nlp.pipe(COUNTRIES))

matcher.add('COUNTRY', None, *patterns) # Adding to matcher

# Calling the matcher on the doc & printing the result.

matches = matcher(doc)

print([doc[start:end] for match_id, start, end in matches])
