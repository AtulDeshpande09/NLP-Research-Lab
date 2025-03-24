import math

class TFIDF:

    def __init__(self):
        self.matrix = None
        self.tfidf = None
        self.number_of_documents = None

    def get_words(self , bag_of_words):

        # Matrix will be used for further referecing
        self.matrix = bag_of_words

        # Total Number of documents
        self.number_of_documents = len(bag_of_words) - 1

        # tfidf => bag_of_words (copy) -> It will get updated later in tf_idf()
        self.tfidf = bag_of_words.copy()

        print("Matrix Created!!!")

        
    def TF(self , term:str , document : str ):

        # Number of documents in that document
        N = sum(self.matrix[document])

        i = self.matrix["index"].index(term)

        number_term = self.matrix[document][i]
    
        return number_term / N


    def IDF(self ,term):

        term_index = self.matrix["index"].index(term)
        d_with_t = 0
        for doc in self.matrix:
        # Checking if word is present in that list
            if self.matrix[doc][term_index] != 0:
                d_with_t += 1

        # Due to above condition - if will consider matrix[index] also
        d_with_t = d_with_t-1

        return math.log(self.number_of_documents/(d_with_t))

    def tf_idf(self):

        # Loop over all the words
        for i , word in enumerate(self.matrix["index"]) :
            # Loop over all the documents 
            for doc in self.matrix:
                if doc == "index":
                    continue

                #here
                print("word and doc : " , word,doc)

                # tf of word and document doc
                tf = self.TF(term=word , document=doc)
                idf = self.IDF(word)

                tfidf = tf*idf

                self.tfidf[doc][i] = tfidf

        return self.tfidf

    def to_df(self):
        if self.tfidf == False:
            print("No representation!!")
            return None
        import pandas as pd
        df = pd.DataFrame(self.tfidf)
        return df