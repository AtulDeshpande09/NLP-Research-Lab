import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess(text:str)->list:

    # Tokenize
    tokens = word_tokenize(text)

    # lowercase
    tokens = [ word.lower() for word in tokens ]

    # removing stopwords
    sw = set(stopwords.words('english'))
    tokens = [ word for word in tokens if word not in sw ]

    # lemmatization 
    wnl = WordNetLemmatizer()
    tokens = [ wnl.lemmatize(word) for word in tokens]

    return tokens


if __name__ == '__main__':

    text = "The quick brown fox jumps over the lazy dog."
    print("This is sample text : \n",text)
    print("Applying text Normalization ... ")
    tokens = preprocess(text)
    print("Text Normalization Completed!!!")
    print("\n")
    print(tokens)