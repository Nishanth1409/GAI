import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.downloader import load

# Dimensionality reduction using PCA
def rd(ems):
    pca = PCA(n_components=2)
    r = pca.fit_transform(ems)
    return r

# Visualize word embeddings
def visualize(words, ems):
    plt.figure(figsize=(10, 6))
    for i, word in enumerate(words):
        x, y = ems[i]
        plt.scatter(x, y)
        plt.text(x + 0.02, y + 0.02, word, fontsize=12)
    plt.title("2D PCA Projection of Word Embeddings")
    plt.grid(True)
    plt.show()

# Generate semantically similar words
def gsm(word):
    print(f"\nTop 5 words similar to '{word}':")
    sw = model.most_similar(word, topn=5)
    for word, s in sw:
        print(word, s)

# Load pre-trained GloVe model from Gensim API
print("Loading pre-trained GloVe model (50 dimensions)...")
model = load("glove-wiki-gigaword-50")

# Define a list of sports-related words
words = ['football', 'basketball', 'soccer', 'tennis', 'cricket']
ems = [model[word] for word in words]

# Reduce dimensions and visualize
e = rd(ems)
visualize(words, e)

# Show similar words for 'programming'
gsm("programming")
