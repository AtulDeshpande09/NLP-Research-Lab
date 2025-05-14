from flask import Flask, request, jsonify
import torch
import torch.nn as nn
import pickle
#from vocab import Vocab  # or wherever the class is defined
from flask_cors import CORS

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


vocab=Vocabulary()


from model import EncoderRNN, DecoderRNN
from utils import normalize_text, Vocabulary

# ----------------- Setup Flask App -----------------
app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----------------- Load Vocabularies -----------------
with open("input_vocab.pkl", "rb") as f:
    input_vocab = pickle.load(f)

with open("output_vocab.pkl", "rb") as f:
    output_vocab = pickle.load(f)

# ----------------- Load Models -----------------
hidden_size = 256  # should match your training setup

encoder = EncoderRNN(input_vocab.n_words, hidden_size).to(device)
decoder = DecoderRNN(hidden_size, output_vocab.n_words).to(device)

encoder.load_state_dict(torch.load("encoder.pth", map_location=device))
decoder.load_state_dict(torch.load("decoder.pth", map_location=device))

encoder.eval()
decoder.eval()





CORS(app) 
# ----------------- Evaluate Function -----------------
def evaluate(sentence):
    with torch.no_grad():
        tokens = normalize_text(sentence)
        indexes = vocab.sentence_to_indexes(tokens)
        input_tensor = torch.tensor(indexes, dtype=torch.long, device=device).view(-1, 1)

        encoder_hidden = encoder.init_hidden().to(device)
        for ei in range(input_tensor.size(0)):
            _, encoder_hidden = encoder(input_tensor[ei], encoder_hidden)

        decoder_input = torch.tensor([[output_vocab.word2index["<SOS>"]]], device=device)
        decoder_hidden = encoder_hidden

        decoded_words = []
        for _ in range(15):  # max output length
            decoder_output, decoder_hidden = decoder(decoder_input, decoder_hidden)
            topv, topi = decoder_output.topk(1)
            next_index = topi.item()

            if next_index == output_vocab.word2index["<EOS>"]:
                break
            decoded_words.append(output_vocab.index2word.get(next_index, "<UNK>"))

            decoder_input = topi.detach()

        return ' '.join(decoded_words)

# ----------------- Routes -----------------
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Farming Chatbot API is running."})



@app.route("/chat", methods=["POST"])
def chat():
    try:
        print("hi")
        data = request.get_json()
        user_input = data.get("message", "")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        response = evaluate(user_input)
        return jsonify({"reply": response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

# ----------------- Run App -----------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
