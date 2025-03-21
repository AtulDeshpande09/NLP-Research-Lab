
t1 = "I love NLP"
t2 = "NLP is amazing"

docs:dict = {
        'd1' = t1,
        'd2' = t2
        }

def count_frequency(tokens:list)->list:
    """
    Input -> Tokens List of words
    Return -> List of tuple ( word , frequency)
    """
    freq = {}

    for word in tokens:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    return freq


def bow(docs:dict)->dict:
    ...


