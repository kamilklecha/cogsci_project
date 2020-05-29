## based on: https://towardsdatascience.com/google-news-and-leo-tolstoy-visualizing-word2vec-word-embeddings-with-t-sne-11558d8bd4d ##
import gensim
from sklearn.manifold import TSNE
import numpy as np

model = gensim.models.Word2Vec.load("model/ your model name")

## chosen keywords
keys = [ "representation", "learning", "cognition", "perception", "processing", "computational", "encode", "conceptual", "network", "model", "judgement", "heuristic", "framework", "embody", "knowledge", "information", "concept", "modality", "preposition", "attention" ]

import matplotlib.pyplot as plt
import matplotlib.cm as cm

## plotting graph function
def tsne_plot_similar_words(title, embedding_clusters, word_clusters, a, filename=None):
    plt.figure(figsize=(16, 9))
    colors = cm.rainbow(np.linspace(0, 1))
    for embeddings, words, color in zip(embedding_clusters, word_clusters, colors):
        x = embeddings[:, 0]
        y = embeddings[:, 1]
        plt.scatter(x, y, c=color, alpha=a)
        for i, word in enumerate(words):
            plt.annotate(word, alpha=0.5, xy=(x[i], y[i]), xytext=(5, 2),
                         textcoords='offset points', ha='right', va='bottom', size=8)
    #plt.legend(loc=4) # adds legend to the graph
    plt.title(title)
    plt.grid(True)
    if filename:
        plt.savefig(filename, format='png', dpi=150, bbox_inches='tight')
    plt.show()

## preparation of vectors for graphs and drawing for each keyword individually
word_clusters = []
for word in keys:
    embedding_clusters = []
    embeddings = []
    words = []
    for similar_word, _ in model.most_similar(word, topn=30):
        if similar_word == 'iss':
            pass
        else:
            words.append(similar_word)
            embeddings.append(model[similar_word])
    embedding_clusters.append(embeddings)
    word_clusters.append(words)

    embedding_clusters = np.array(embedding_clusters)
    n, m, k = embedding_clusters.shape
    tsne_model_en_2d = TSNE(perplexity=15, n_components=2, init='pca', n_iter=3500, random_state=32)
    embeddings_en_2d = np.array(tsne_model_en_2d.fit_transform(embedding_clusters.reshape(n * m, k))).reshape(n, m, 2)

    filename = word + "_brit_acad.png"
    tsne_plot_similar_words(word, embeddings_en_2d, word_clusters, 0.7, filename)
