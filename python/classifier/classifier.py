import pickle
import pandas as pd
import joblib
import time
from pathlib import Path
from keras.models import load_model


class Classifier:
    def __init__(self, path):
        cur_path = Path(path).resolve()
        model_path = Path.joinpath(cur_path, 'model.h5')
        scaler_path = Path.joinpath(cur_path, 'scaler.pkl')

        self.classifier = load_model(model_path)
        self.scaler = joblib.load(scaler_path)

    def classify(self, values: list):
        values = pd.DataFrame(values)
        values = values[0:7].values
        values = values.reshape(1, -1)
        values = self.scaler.transform(values)

        prediction = self.classifier.predict(values)

        return int(prediction[0][0])
