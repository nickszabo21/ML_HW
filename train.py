import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from joblib import dump
from preprocess import prep_data

df = pd.read_csv("fish_participant.csv")

X, y = prep_data(df)

ttr = ExtraTreesRegressor()
ttr.fit(X, y)

dump(ttr, "reg.joblib")