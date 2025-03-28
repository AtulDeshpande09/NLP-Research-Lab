import random


pcfg = {
    "S": [("NP VP", 0.85) , ("S conj S" , 0.15) ],
    "NP": [("Det N", 0.3), ("Name", 0.3) , ("Det JJ N",0.4) ],
   
    "VP": [("V NP", 0.15), ("V", 0.01) ,
           ("VBD NP",0.13), ("VBZ VBG NP",0.13),("PP VBN NP",0.13),
           ("MD RT NP", 0.16), ("MD be VBG NP" , 0.15),
           ("PP been VBG NP" , 0.07) , ("MD have been VBG NP",0.07)],
   
    "Det": [("the", 0.3), ("a", 0.7)],
    "N": [("cat", 0.3), ("dog", 0.3), ("mouse", 0.4)],
   
    "V": [("sees", 0.5), ("chases", 0.5)],
    "VBD": [("saw", 0.5), ("chased", 0.5)],
    "VBZ": [("was", 0.5), ("is", 0.5)],
    "VBG": [("seeing", 0.5), ("chasing", 0.5)],
    "Name": [("Alice", 0.5), ("Bob", 0.5)],
   
    "VBN": [("seen", 0.5), ("chased", 0.5)],
    "PP": [("has", 0.5), ("had", 0.5)],
   
    "MD": [("will", 0.95), ("shall", 0.05)],
    "RT": [("see", 0.5), ("chase", 0.5)],
   
    "conj" : [("and", 0.5), ("but", 0.5)],
    "JJ" : [("big",0.25),("little",0.25) , ("white",0.25) ,("black",0.25) ]
}

def generate(symbol:str):
    
    if symbol not in pcfg:
        return symbol

    #Here we expand the production rule
    #IT chooses based on probability
    rule_expanded = random.choices(
            [sym[0] for sym in pcfg[symbol]],
            weights = [sym[1] for sym in pcfg[symbol]]
            )[0]

    return " ".join(generate(sym) for sym in rule_expanded.split())


# testing
# Lets generate 10 sentences to check the result
for _ in range(10):
    print(generate("S"))
    print("-----+----- ")
