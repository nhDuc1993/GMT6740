from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import MissingIndicator
import numpy as np

class Indicator(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        nonnull_X = np.nan_to_num(X.astype(float), nan=0).astype(int)

        missing_indicator = MissingIndicator(features='all')
        indicator_values = missing_indicator.fit_transform(X).astype(int)

        return np.c_[nonnull_X, indicator_values]