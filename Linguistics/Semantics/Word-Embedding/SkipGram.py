import torch
import torch.nn as nn
import torch.optim as optim


class Word2VecSkipGram(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()

        self.embedding_dim = embedding_dim
        self.vocab_size = vocab_size
        self.input_embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.output_embeddings = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, center_word_index):
        v_c = self.input_embeddings(center_word_index)  # (batch_size, embedding_dim)
        u = self.output_embeddings.weight.T             # (embedding_dim, vocab_size)
        scores = torch.matmul(v_c, u)                   # (batch_size, vocab_size)
        return scores

    def get_embeddings(self, word_idx):
        return self.input_embeddings(torch.tensor([word_idx]))

    def get_weights(self):
        return self.input_embeddings.weight.data  # Returns entire embedding matrix

    def save(self, path="word2vec.pt"):
        torch.save(self.state_dict(), path)

    def load(self, path):
        self.load_state_dict(torch.load(path))




class SkipGrams:

    def __init__(self , corpus_tokens ,window , embedding_dim):

        
        self.corpus_tokens = corpus_tokens
        self.vocab = sorted(set(corpus_tokens))

        self.window = window
        self.word2idx = {word: i for i, word in enumerate(self.vocab)}
        self.idx2word = {i: word for word, i in self.word2idx.items()}
        
        self.model = Word2VecSkipGram(vocab_size=len(self.vocab), embedding_dim=50)

        self.epochs = 1000

    def build_skipgram_pairs(self):
        pairs = []
        for i in range(len(self.corpus_tokens)):
            target_word = self.corpus_tokens[i]
            for j in range(-self.window, self.window + 1):
                if j == 0:
                    continue 
                context_index = i + j
                if context_index < 0 or context_index >= len(self.corpus_tokens):
                    continue
                context_word = self.corpus_tokens[context_index]
                pairs.append((self.word2idx[target_word], self.word2idx[context_word]))
        return pairs
        


    def fit(self):
        
        loss_fn = nn.CrossEntropyLoss()

        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01)

        pairs = self.build_skipgram_pairs()
        
        for _ in range(self.epochs):
            total_loss = 0
            for center_idx, context_idx in pairs:
                center_tensor = torch.tensor([center_idx])
                context_tensor = torch.tensor([context_idx])

                # Forward pass
                scores = self.model(center_tensor)  # shape: (1, vocab_size)

                # Compute loss
                loss = criterion(scores, context_tensor)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()


    def vectors(self):
        self.fit()
        return self.model.get_weights()
