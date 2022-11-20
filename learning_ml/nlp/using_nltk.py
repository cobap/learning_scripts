# %%
from matplotlib import pyplot
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# %%

filename = 'lorem.txt'
with open(filename, 'rt') as file:
    text = file.read()
print(text)
print(type(text))

# %%

# Tokenization
tokens = word_tokenize(text)
tokens

# %%

# Bag of words
# Score based on word occurrence in the document and the inverse occurrence across all documents called TfidfVectorizer.
vectorizer = TfidfVectorizer()
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer.fit(corpus)

print(vectorizer.vocabulary_)
print(vectorizer.idf_)

# %%

vector = vectorizer.transform([corpus[0]])
# summarize encoded vector
print(vector.shape)
print(vector.toarray())

# %%

# Word2Vec model

# define training data
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
             ['this', 'is', 'the', 'second', 'sentence'],
             ['yet', 'another', 'sentence'],
             ['one', 'more', 'sentence'],
             ['and', 'the', 'final', 'sentence']]

# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.key_to_index.keys())
print(words)
# access vector for one word
# print(model['sentence'])

# %%

# define training data
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
             ['this', 'is', 'the', 'second', 'sentence'],
             ['yet', 'another', 'sentence'],
             ['one', 'more', 'sentence'],
             ['and', 'the', 'final', 'sentence']]
# train model
model = Word2Vec(sentences, min_count=1)
# fit a 2D PCA model to the vectors
X = model.wv.key_to_index.keys()
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()

# %%

# Classifying text

# Embeddings + CNN

# define problem
vocab_size = 100
max_length = 200
# define model CNN
model = Sequential()
model.add(Embedding(vocab_size, 100, input_length=max_length))
model.add(Conv1D(filters=32, kernel_size=8, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

# %%

# Sentiment Analysis
