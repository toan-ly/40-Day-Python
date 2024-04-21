corpus = ['Tôi thích môn Toán', 
          'Tôi thích AI',
          'Tôi thích âm nhạc']

vocab = set()
for doc in corpus:
    for word in doc.split():
        vocab.add(word)

sample = 'Tôi thích AI thích Toán'
sample_words = sample.split()
sample_vector = [0] * len(vocab)
for i, word in enumerate(vocab):
    sample_vector[i] = sample_words.count(word)

print(sample_words)
print(vocab)
print(sample_vector)