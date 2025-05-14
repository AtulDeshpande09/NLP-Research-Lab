import re
import nltk
nltk.download("punkt")

from nltk.tokenize import word_tokenize

class Vocabulary:
    def __init__(self):
        self.word2index = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2, "<UNK>": 3}
        self.index2word = {0: "<PAD>", 1: "<SOS>", 2: "<EOS>", 3: "<UNK>"}
        self.word_count = {}
        self.n_words = 4

    def add_sentence(self, sentence):
        for word in sentence:
            self.add_word(word)

    def add_word(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.index2word[self.n_words] = word
            self.n_words += 1

    def sentence_to_indexes(self, sentence):
        indexes = [self.word2index.get(word, self.word2index["<UNK>"]) for word in sentence]
        indexes.append(self.word2index["<EOS>"])
        return indexes

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    tokens = word_tokenize(text)
    return tokens
