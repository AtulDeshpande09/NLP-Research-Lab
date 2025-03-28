
DET = ['a' , 'an' , 'the' ]
NN = ['cat' ,'mouse' , 'cow']
VBZ = ['catches', 'sees' , 'chases']
VBD = ['caught','saw','chased']
VBG = ['catching','seeing','chasing']
VBN = ['caught' , 'seen','chased']
VB = ['catch','see','chase']
MD = ['shall','will']
auxV = ['is','am','are','was','have','has','had','be','been','being']


# converts str into list
def tokenize(sentence:str):
    return sentence.lower().split()


def match(remaining_tokens):
    # consumes first token
    return  remaining_tokens[1:]


def v(remaining_tokens:list):

    # Simple present
    if remaining_tokens and remaining_tokens[0] in VBZ:
        #print("Word to parse ---> ",remaining_tokens[0])
        remaining_tokens = match(remaining_tokens)
        return True , remaining_tokens
    
    # simple past
    elif remaining_tokens and remaining_tokens[0] in VBD:
        #print("Word to parse ---> ",remaining_tokens[0])
        remaining_tokens = match(remaining_tokens)
        return True , remaining_tokens
    
    # MD + VB
    elif remaining_tokens and remaining_tokens[0] in MD:
        #print("Word to parse ---> ",remaining_tokens[0])
        remaining_tokens = match(remaining_tokens)

        if remaining_tokens and remaining_tokens[0] in VB:
           # print("Word to parse ---> ",remaining_tokens[0])
            remaining_tokens = match(remaining_tokens)
            return True , remaining_tokens 
        
        elif remaining_tokens:
            return v(remaining_tokens)

        else:
            return False, remaining_tokens


    #  auxV + VB
    if remaining_tokens and remaining_tokens[0] in auxV:
        remaining_tokens = match(remaining_tokens)

        if remaining_tokens[0] in VBG:
            remaining_tokens = match(remaining_tokens)
            return True , remaining_tokens
        
        elif remaining_tokens[0] in VBN:
            remaining_tokens = match(remaining_tokens)
            return True , remaining_tokens
        
        # simple cluase
        elif remaining_tokens[0] in DET :
            return True , remaining_tokens
        
        # simple clause A be B 
        else:
            return v(remaining_tokens)




def ar(remaining_tokens:list):
    
    if remaining_tokens and remaining_tokens[0] in DET:
        #print("Word to parse ---> ",remaining_tokens[0])

        remaining_tokens = match(remaining_tokens)
        return True , remaining_tokens

    else :
        print("Parsing Error!!")
        return False , remaining_tokens

def n(remaining_tokens:list):

    if remaining_tokens and remaining_tokens[0] in NN:
        #print("Word to parse ---> " , remaining_tokens[0])
        remaining_tokens = match(remaining_tokens)
        return True , remaining_tokens

    else:
        print("Parsing Error!!")
        return False , remaining_tokens


def np(remaining_tokens):

    if remaining_tokens:
        p1, remaining_tokens = ar(remaining_tokens)
        p2,remaining_tokens = n(remaining_tokens)

        print("Parsed noun part!!")

        if p1 and p2 :
            return True , remaining_tokens
        else :
            return False,remaining_tokens


def vp(remaining_tokens:list):

    if remaining_tokens:

        p1 , remaining_tokens = v(remaining_tokens)

        if not remaining_tokens:
            return False , remaining_tokens
        p2, remaining_tokens = np(remaining_tokens)

        print("parsed verb part!!")
        if p1 and p2 :
            return True , remaining_tokens
        else :
            return False , remaining_tokens

def s(tokens:list):

    current_index = 0
    if tokens:
        p1,remaining_tokens = np(tokens)

        if not p1 :
            #print("Parsing Failed at Noun Phrase")
            return False
            
        if not remaining_tokens:
            #print("Parsing failed becuase of incomplete sentence")
            return False
        p2,remaining_tokens = vp(remaining_tokens)
        if not p2 :
            #print("Prsing Failed at Verb Phrase!!")
            return False

        if remaining_tokens:
            #print("Parsing Failed because of extra words!!!")
            return False

        print("Sentence Parsed Successfully!!")
        return True
        
        
    else:
        print("Please enter a valid sentence!!")
        return False


sentences = ["a cat sees a mouse",
             "a cat is seeing a mouse",
             "a cat has seen a mouse",
             "a cat has been seeing a mouse",
             "a cat saw a mouse",
             "a cat was seeing a mouse",
             "a cat had seen a mouse",
             "a cat had been seeing a mouse",
             "a cat will see a mouse",
             "a cat will be seeing a mouse",
             "a cat will have seen a mouse",
             "a cat will have been seeing a mouse"
             ]

#print(tokenize(sentence))

for sentence in sentences :
    print(f"Sentence to parse ------->{sentence}")
    tokens = tokenize(sentence)
    s(tokens)
    print("")

