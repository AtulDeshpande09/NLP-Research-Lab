class BagofWords:

    def __init__(self):

        self.matrix = False
        self.df = False

    def tokenize(self,text):
        return text.lower().split()

    def count_frequency(self , tokens:list)->list:
        """
        Input -> Tokens List of words
        Return -> dictionary - {word:freq}

        Note : No Need to Call this method directly
              --> This method is called in create_docs()
        """
        freq = {}

        for word in tokens:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        return freq

    def create_doc(self , text:list)->dict:
        """
        Input --> list of lists
        returns -> dict of dict
        """
        docs = {}

        # enumerate -> add counter to each token
        for i , tokens in enumerate(text):
        
            freq = self.count_frequency(tokens)
            docs[i] = freq
    
        return docs

    def represent(self ,docs:dict)->dict:
        '''
        Input --> dict of dict
        return -> dict of list
        '''

        matrix = {"index" : [] 
                 }
        # docs - dictionary of dictionary
        # doc - dictionary { word : frequency }
        for doc in docs :
            for word in docs[doc]:
                if word not in matrix["index"]:
                    matrix["index"].append(word)
    
        for doc in docs :
            # Creates List of Zeros for all documents
            # We will modify this list later
            matrix[f'doc{doc}'] = [0]*(len(matrix['index']))
            for word , frequency in docs[doc].items():
                # Get index of Word
                # We can replace Frequency of word at that index - In matrix
                index = matrix['index'].index(word)
                # Replace
                matrix[f'doc{doc}'][index] = frequency
        return matrix

    def to_df(self):
        '''
        Converts Dict into pandas df
        '''
        if self.df != False:
            return self.df
        if self.matrix == False:
            print("No Data!!!")
            return None
        
        import pandas as pd
        self.df = pd.DataFrame(self.matrix)
        self.df.set_index("index")

        return self.df

    def bow(self , text_list):
        """
        This is All in one method
        Like combination of all of the above methods
        """

        text = []
        for t in text_list :
            text.append(self.tokenize(t))

        docs = self.create_doc(text)

        # Create Matrix
        self.matrix = self.represent(docs)

    def show_bag(self):
        if self.matrix == False:
            print("No representation!!")
            return None
        return self.matrix