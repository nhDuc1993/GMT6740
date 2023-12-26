import pandas as pd
import numpy as np

from sklearn.impute import MissingIndicator
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from scipy.sparse import csr_matrix, save_npz
import joblib

# Import data
file_path = r".\data\clean_df.csv"
df = pd.read_csv(file_path)

# Create man_period, stk_period
df['date_created'] = pd.to_datetime(df['date_created'], format = "ISO8601")
df['year_created'] = df['date_created'].dt.year

df['man_period'] = df['year_created'] - df['manufacture_year']
df['stk_period'] = df['year_created'] - df['stk_year']

# Drop and impute column for faster one hot encoding
num_cols = [2,3,4,7,8,10,11]
cat_cols = [0,1,5,6,9]

df = df.drop(['manufacture_year', 'stk_year', 'date_created', 'date_last_seen', 'year_created'], axis=1)
df.iloc[:,cat_cols] = df.iloc[:,cat_cols].fillna('unknown')

# Split
X = df.drop('price_eur', axis=1).to_numpy()
y = df['price_eur'].to_numpy()

# Feature processing
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
    

# one_hot_encoder = OneHotEncoder(handle_unknown='ignore')
# indicator = Indicator()

full_pipeline = ColumnTransformer([
    ("num", OneHotEncoder(handle_unknown='ignore'), num_cols),
    ("cat", Indicator() , cat_cols),
])

# Transform
full_pipeline.fit(X)

if __name__ == "__main__":
    joblib.dump(full_pipeline, './FastAPI/model/preprocessing.joblib')

    X_trans = full_pipeline.transform(X)
    file_path = ".\data\X_trans.npz"
    save_npz(file_path, X_trans)

    file_path = ".\data\y.txt"
    np.savetxt(file_path, y)
