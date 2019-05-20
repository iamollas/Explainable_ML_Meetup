from sklearn.base import BaseEstimator, TransformerMixin
from keras.preprocessing.sequence import pad_sequences

class MyPadder(BaseEstimator,TransformerMixin):
    def __init__(self,maxlen=5000):
        self.maxlen = maxlen
        self.max_index = None

    def fit(self,X,y=None):
        self.max_index = pad_sequences(X,maxlen=self.maxlen).max()
        return self

    def transform(self,X,y=None):
        X = pad_sequences(X,maxlen=self.maxlen)
        X[X>self.max_index] = 0
        return X