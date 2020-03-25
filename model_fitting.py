"""
in: train_data
out: stored trained model
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor


class ModelFitter:
    features = ['price', 'price_note', 'discount', 'original_price', 'price_of_living', 'ID', 'date_of_update',
                'type_of_building', 'condition', 'ownership', 'location', 'floor', 'living_area', 'floor_area',
                'cellar',
                'reconstruction_year', 'water', 'gas', 'waste', 'heat', 'telecomunication', 'electricity', 'commute',
                'communication', 'parking', 'energy_efficiency_1', 'energy_efficiency_2', 'energy_efficiency_3',
                'furniture', 'elevator', 'type_of_flat']

    model = RandomForestRegressor(n_estimators=100, min_samples_leaf=1)

    def __init__(self, train_data, features_to_train, feature_to_predict):
        self.train_data = train_data
        self.features_to_train = features_to_train
        self.feature_to_predict = feature_to_predict

    def fit(self):
        # self.__standardize()
        self.__split_test()
        self.model.fit(self.X_train, self.Y_train)

    def __split_test(self):
        self.X = self.train_data[self.features_to_train]
        self.Y = self.train_data[self.feature_to_predict].astype(int)
        self.X_train, self.X_test, self.Y_train, self.Y_test = \
            train_test_split(self.X, self.Y, test_size=0.2, random_state=42)

    def __standardize(self):
        scaler = StandardScaler()
        data_to_transform = self.train_data[self.feature_to_predict]
        data_to_transform = [[x] for x in data_to_transform]
        self.train_data[self.feature_to_predict] = scaler.fit_transform(data_to_transform)

