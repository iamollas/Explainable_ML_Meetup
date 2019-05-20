from keras.preprocessing.text import Tokenizer
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
class MyTextsToSequences(Tokenizer, BaseEstimator, TransformerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def fit(self,texts,y=None):
        self.fit_on_texts(texts)
        return self

    def transform(self,texts,y=None):
        return np.array(self.texts_to_sequences(texts))