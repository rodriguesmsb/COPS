import pandas as pd
import joblib
import sklearn
from sklearn.ensemble import RandomForestClassifier

def prediction_prob(data):

    model = joblib.load("app/cops_model.joblib")
    return(model.predict_proba(data))


