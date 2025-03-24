import matplotlib
matplotlib.use('TkAgg')
from sklearn.decomposition import PCA  # Corrected import statement
import matplotlib.pyplot as plt
import numpy as np
words = ['football', 'basketball', 'cricket', 'technology', 'computer', 'robot', 'AI', 'cloud', 'python', 'data']
np.random.seed(42)
word_vectors = {word: np.random.rand(100) for word in words}
pca = PCA(n_components=2)
pca_result = pca.fit_transform([word_vectors[word] for word in words])
plt.figure(figsize=(8, 8))
plt.scatter(pca_result[:, 0], pca_result[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, (pca_result[i, 0], pca_result[i, 1]))
plt.title('Word Embedding Visualization with PCA')
plt.savefig(r'D:\PESITM\Studies\6 sem\LAB\GAI\word_embedding_visualization.png')
plt.show()


