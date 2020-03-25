"""
in: test_data
out: prediction
"""


class ModelPredictor:

    def __init__(self, test_data):
        self.test_data = test_data
        # load stored model
        self.model = {}

    def predict(self):

        predictions = self.model.predict(self.test_data)

        return predictions
