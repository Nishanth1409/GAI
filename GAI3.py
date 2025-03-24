from gensim.models import Word2Vec
def cw(corpus):
    model = Word2Vec(
        sentences=corpus, 
        vector_size=50,
        window=5, 
        min_count=1, 
        workers=4,
        epochs=10,
        )
    return model
def anal(model, word):
    sw = model.wv.most_similar(word, topn=5)
    for w, s in sw:
        print(w,s)
corpus = [
    "The patient was prescribed antibiotics to treat the infection.".split(), 
    "The court ruled in favor of the defendant after reviewing theevidence.".split(),
    "Diagnosis of diabetes mellitus requires specific blood tests.".split(), 
    "The legal contract must be signed in the presence of a witness.".split(), 
    "Symptoms of the disease include fever, cough, and fatigue.".split(),
    ]
model = cw(corpus)
print("\n Analysing for word patient")
anal(model, "patient")
print("\n Analysing for word court")
anal(model, "court")