# Vocabulary
vocab = ['Banana' , 'Apple' , 'Orange' ,
         'Tiger' , 'Lion' , 'Elephant' , 'Fox', 'Wolf',
         'Earth' , 'Sun' , 'Moon' , 'Pluto' , 'Mars' , 'Jupyter' ,'Neptune']
# Total 15 words

# Topic Probability
# lets consider document is made up of three topics
# thier probabilities are as follows

theta = [0.45 , 0.15 , 0.4]

#Word probability for topics
t1 = [0.25 , 0.15 , 0.1 , 
      0.03 , 0.03 , 0.05 , 0.04 , 0.05 ,
      0.04 ,0.04 , 0.04 ,0.04 , 0.04 , 0.05 , 0.05]

t2 = [0.03 , 0.03 , 0.04 , 
      0.1 , 0.15 , 0.15 , 0.1 , 0.1 ,
      0.04 ,0.04 , 0.04 ,0.04 , 0.04 , 0.05 , 0.05]

t3 = [0.03 , 0.03 , 0.04 , 
      0.03 , 0.03 , 0.03 , 0.03 , 0.03 ,
      0.13 ,0.12 , 0.11 ,0.09 , 0.1 , 0.1 , 0.1]

topics = [t1 , t2 , t3 ]
import random

# Document generation
document = []

# Let's assume that our document is made of 10 words
for i in range(10):
    #Choosing a topic
    topic = random.choices(
            topics ,
            weights = theta
            )
    # Choosing a word
    word = random.choices(
        vocab , 
        weights = topic[0]
        )

    document.append(word[0])

print(" ".join(document))
