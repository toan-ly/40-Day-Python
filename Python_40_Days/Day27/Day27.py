from underthesea import pos_tag, classify, sentiment, sent_tokenize, word_tokenize

with open('text.txt', 'r') as f:
    sentence = f.read()
    print('+ POS Tagging: ', pos_tag(sentence))
    print('+ Text Classification: ', classify(sentence))
    print('+ Sentiment Analysis: ', sentiment(sentence))
    print('+ Sentence Segmentation: ', sent_tokenize(sentence))
    print('+ Word Segmentation: ', word_tokenize(sentence))
