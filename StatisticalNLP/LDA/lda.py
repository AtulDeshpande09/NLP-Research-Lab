import random

class LDA:

    def __init__(self , no_topics:int , corpus):
        
        self.word_topic_table = None
        self.doc_topic_table = None

        self.no_topics = no_topics
        self.topic_list = [ i for i in range(no_topics)]

        self.no_docs = len(corpus)

        self.vocab = list(set([word for doc in corpus for word in doc ]))
        
        self.probability_table = { word : [0]*no_topics for word in self.vocab}

        self.corpus = corpus

        self.assignment = [ [ 0 for word in doc] for doc in corpus]

        self.probability_table = { word : [0]*self.no_topics for word in self.vocab}

        self.show_table = None


    def doc_topic(self):
        table = {f"doc{i}" : [0]*self.no_topics for i in range(self.no_docs)}
        return table

    def word_topic(self):
        table = {f"{word}" : [0]*self.no_topics for word in self.vocab}
        return table

    def initialize(self):
        
        self.word_topic_table = self.word_topic()
        self.doc_topic_table = self.doc_topic()
        
        for i,doc in enumerate(self.corpus):
            for j ,word in enumerate(doc) :
                self.assignment[i][j] = random.choice(self.topic_list)

    def fill_tables(self):
        for i , doc in enumerate(self.corpus):
            for j ,word in enumerate(doc) :
                topic = self.assignment[i][j]
                self.word_topic_table[word][topic] += 1
                self.doc_topic_table[f"doc{i}"][topic] += 1


    def normalize(self , prob : list):
        total = sum(prob)
        prob_list = [ i/total for i in prob]
        return prob_list

    def sample(self , choice:list , weight:list):
        weight = self.normalize(weight)
        choice = random.choices(choice , weights = weight)
        return int(choice[0]) , weight


    def iteration(self , alpha = 0.1 , beta=0.01):
    
        for i , doc in enumerate(self.corpus):
            for j , word in enumerate(doc):
    
                current_topic = self.assignment[i][j]
    
                # Decreament step
                self.word_topic_table[word][current_topic] -= 1
    
                self.doc_topic_table[f"doc{i}"][current_topic]-= 1
    
                # temporary list to store probability of word getting reassigned a topic
                probability_list = []
                # Re-assigning word to topic
                for topic in range(self.no_topics):
                    
                    # Values
                    # count of word 'w' in topic 'k'
                    n_wk = self.word_topic_table[word][topic]
                    
                    #total number of words in topic k
                    n_k = sum([self.doc_topic_table[document][topic] for document in self.doc_topic_table]) 
                    
                    # count of topic k in document d
                    n_kd = self.doc_topic_table[f"doc{i}"][topic]
                    
                    # total words in document d
                    n_d = len(doc)
                    
                    # total number of words in corpus
                    v = len(self.vocab)
                    
                    # formula
                    probability = (n_wk + beta)/(n_k + v * beta) * (n_kd + alpha)/(n_d + self.no_topics *alpha)
                    probability_list.append(probability)
                    
                # Normalization and sampling
                sampled_topic , prob = self.sample(self.topic_list , weight=probability_list)
    
                # adding
                self.word_topic_table[word][sampled_topic] += 1
                self.doc_topic_table[f"doc{i}"][sampled_topic] += 1
    
                # re-assigning
                self.assignment[i][j] = sampled_topic
    
                # fill the probability table
                self.probability_table[word] = prob


    def model_topics(self , iterations = 500):
            
        self.initialize()
        self.fill_tables()
        for _ in range(iterations):
            self.iteration()

        self.create_prob_table()
        print("Completed Topic Modeling!!! \nYou can see by using 'show_topics()' function.")

    def create_prob_table(self):
        new_table = {f"topic{i}" : [0]*len(self.vocab) for i in range(self.no_topics)}
        for i , word in enumerate(self.probability_table):
            for j , prob in enumerate(self.probability_table[word]):
                    new_table[f"topic{j}"][i] = f"{prob}*{word}"

        self.show_table = new_table

    def show_topics(self):
            
        for topic in self.show_table:
            print("Topic \n : ")
            print(self.show_table[topic])
            print("\n")
            print("------------+------------")
            
    def help(self):
        print("This is help function created to guide you to use LDA class\n")
        print("\n")
        print('Functions : \n')
        text = """
        lda.model_topic() --> takes one parameter epoches , works even left blank.
        lda.show_topic() ---> Shows probability of a word with respect to topic .
                                  Note : It does not give sorted probabilities!!!

        How to use :

            
        no_topics = 2 ( or any number you want )
        #tokenized data
        corpus = [
                ["apple", "banana", "apple", "fruit", "fruit", "banana"],
                ["dog", "cat", "dog", "animal", "pet", "cat"],
                ["banana", "fruit", "apple", "orange", "fruit", "banana"]
                ]

        lda = LDA(no_topics=no_topics , corpus=corpus)
        lda.model_topics()
        lda.show_topics()
        """
        print(text)
            
            
            