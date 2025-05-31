from sklearn_crfsuite import CRF
from helper import read_conll_data , sent2labels , sent2features
import pickle

X_raw , y_raw = read_conll_data('data.txt')

X = [sent2features(s) for s in X_raw]
y = [sent2labels(t) for t in y_raw]


crf = CRF(algorithm='lbfgs', max_iterations = 100)

print(f"X :  {len(X)}")
print("")
print(f'y : {len(y)}')
crf.fit(X,y)

with open('crf_model.pkl','wb') as f:
    pickle.dump(crf,f)

print("Model trained and saved!")

