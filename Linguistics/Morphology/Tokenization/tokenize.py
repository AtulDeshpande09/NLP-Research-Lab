

def word_tokenize(text :str)->list:

    text = text.lower()

    tokens = text.split(" ")

    tokens.remove(".") #Removing full-stop as we generally dont need it
    return tokens



if __name__ == '__main__':

    text = "In tokenization we divide a large chunch of text into smaller units . for example a paragraph can be broken down into bunch of sentences or a sentence into bunch of words ."

    tokens = word_tokenize(text)

    print(text)
    print("\nAfter Tokenization : \n")

    print(tokens)
