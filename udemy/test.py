import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Tesla is looking at buying U.S. Startup for $6 million')

for token in doc:
    print(token.text,token.pos_, token.dep_)


print(nlp.pipeline)
print(nlp.pipe_names)