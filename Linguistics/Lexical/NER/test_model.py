import pickle
from helper import sent2features

with open('crf_model.pkl' , 'rb' ) as f:
    crf =pickle.load(f)

sent = "Google was founded by Larry Page"
new_sentence = ['Google','was','founded','by','Larry','Page']
features = sent2features(new_sentence)
predicted = crf.predict_single(features)

print(f"Sentence : \n\t{sent}")
l = list(zip(new_sentence , predicted ))

print("")
for word , tag in l:
    print(f"{word} : {tag}")


