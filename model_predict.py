from sklearn.preprocessing import StandardScaler
"""
in: test_data
out: prediction
"""


class ModelPredictor:

    def __init__(self, test_data, model):
        self.test_data = test_data
        self.model = model

    def predict(self):

        self.__standardize()
        predictions = self.model.predict(self.test_data)

        return predictions

    def __standardize(self):
        scaler = StandardScaler()
        self.test_data = scaler.fit_transform(self.test_data)
        pass

