"""
in: train_data
out: stored trained model
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt


class ModelFitter:
    features = ['price', 'price_note', 'discount', 'original_price', 'price_of_living', 'ID', 'date_of_update',
                'type_of_building', 'condition', 'ownership', 'location', 'floor', 'living_area', 'floor_area',
                'cellar',
                'reconstruction_year', 'water', 'gas', 'waste', 'heat', 'telecomunication', 'electricity', 'commute',
                'communication', 'parking', 'energy_efficiency_1', 'energy_efficiency_2', 'energy_efficiency_3',
                'furniture', 'elevator', 'type_of_flat']
    model = RandomForestRegressor()

    def __init__(self, train_data, features_to_train, feature_to_predict):
        self.train_data = train_data
        self.features_to_train = features_to_train
        self.feature_to_predict = feature_to_predict
        target = 'price'
        features_for_train = [
            'discount',
            'price_of_living',
            'condition',
            'living_area',
            'floor_area',
            'cellar',
            'parking',
            'elevator',
            'provision_included',
            'price']
        self.train_df = self.train_data[features_for_train]
        self.X = self.train_df.drop(target, axis=1).values
        self.Y = self.train_df[[target]].values

    def fit(self):
        self.__standardize()
        self.__split_test()
        self.model.fit(
            self.X_train,
            self.Y_train
        )

    def __split_test(self):

        self.X_train, self.X_test, self.Y_train, self.Y_test = \
            train_test_split(self.X, self.Y, test_size=0.2, random_state=42)

    def __standardize(self):
        scaler = StandardScaler()
        data_to_transform = self.train_data[self.feature_to_predict]
        data_to_transform = [[x] for x in data_to_transform]
        self.train_data[self.feature_to_predict] = scaler.fit_transform(data_to_transform)

    def plot(self):
        preds = self.model.predict(self.X_test)
        plt.xlabel("Predicted value")
        plt.ylabel("Actual value")
        plt.title("Predicted vs. Actual values for\nnLinear Regression model")
        x = 1000000
        y = 8000000
        plt.xlim([x, y])
        plt.ylim([x, y])
        plt.scatter(preds, self.Y_test)
        plt.plot([x, y], [x, y])
        plt.show()
