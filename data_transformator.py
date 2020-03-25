import pandas
"""
in: data
out: transformed data
"""


class DataEngineer:

    def __init__(self, whole_dataset):
        self.whole_dataset = whole_dataset


class DataTransformator:

    def __init__(self, whole_dataset):
        self.whole_dataset = whole_dataset

    def transform(self):

        self.__fill_na('price', self.whole_dataset['discount'])
        self.__fill_na('price', self.whole_dataset['price_note'])
        self.__str_to_int('price')
        self.__fill_na('price', self.whole_dataset['price'].median())
        self.__na_to_bool('discount')

        pass

    def __fill_na(self, feature, fill_with):
        self.whole_dataset[feature] = self.whole_dataset[feature].fillna(fill_with)

    def __str_to_int(self, feature):
        self.whole_dataset[feature] = pandas.to_numeric(self.whole_dataset[feature].str.replace(r'[^0-9]+', ''))

    def __na_to_bool(self, feature):
        self.whole_dataset[feature] = self.whole_dataset[feature].notna()

    # def __change_type(self, feature, to_type):
