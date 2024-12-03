import pandas as pd
import joblib

model = joblib.load('model.pkl') 

def predict_collision(data):

    prediction = model.predict(data)
    return prediction