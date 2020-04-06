from sklearn.preprocessing import StandardScaler
"""
in: test_data
out: prediction
"""


class ModelPredictor:

    def __init__(self, model):
        self.model = model

    def predict(self, test_data):
        self.test_data = test_data
        self.__standardize()
        predictions = self.model.predict(self.test_data)

        return predictions

    def __standardize(self):
        scaler = StandardScaler()
        self.test_data = scaler.fit_transform(self.test_data)
        pass

