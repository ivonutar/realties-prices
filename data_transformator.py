import pandas

"""
in: data
out: transformed data
"""


class DataEngineer:
    bool_mapping = {
        True: 1,
        False: 0
    }

    def __init__(self, whole_dataset, test_data=False):
        self.whole_dataset = whole_dataset
        self.test_data = test_data

    def engineer(self):
        self.whole_dataset['provision_included'] = self.whole_dataset['price_note'].str.contains('včetně provize')
        self.whole_dataset['provision_included'] = self.whole_dataset['provision_included'].fillna(False)
        self.__replace('provision_included', self.bool_mapping)
        self.whole_dataset['street'] = self.whole_dataset['street'].str.split(pat=',').str[-1].str.split(' - ').str[-1]

    def __replace(self, feature, replace_with):
        self.whole_dataset[feature] = self.whole_dataset[feature].replace(replace_with)


class DataTransformator:
    condition_mapping = {'undefined': 0,
                         'Ve výstavbě': 1,
                         'Před rekonstrukcí': 2,
                         'Dobrý': 3,
                         'Po rekonstrukci': 4,
                         'Velmi dobrý': 5,
                         'Novostavba': 6,
                         'Projekt': 7
                         }

    bool_mapping = {
        True: 1,
        False: 0
    }

    def __init__(self, whole_dataset, test_data=False):
        self.whole_dataset = whole_dataset
        self.test_data = test_data

    def transform(self):
        if not self.test_data:
            self.__fill_na('price', self.whole_dataset['discount'])
            self.__fill_na('price', self.whole_dataset['price_note'])
            self.__str_to_int('price')
            self.__fill_na('price', self.whole_dataset['price'].median())
        self.__na_to_bool('discount')

        self.__fill_na('cellar', '0 m2')
        self.__fill_na('living_area', '0 m2')
        self.__fill_na('floor_area', '0 m2')
        self.__fill_na('parking', 0)
        self.__fill_na('elevator', False)
        self.__fill_na('price_of_living', '0')

        self.__str_to_int_replace('cellar', ' m2', '')
        self.__str_to_int_replace('living_area', ' m2', '')
        self.__str_to_int_replace('floor_area', ' m2', '')

        self.__fill_na('living_area', self.whole_dataset['living_area'].median())
        self.__fill_na('floor_area', self.whole_dataset['floor_area'].median())

        self.__fill_na('condition', 'undefined')
        self.__replace('condition', self.condition_mapping)

        self.__replace('elevator', self.bool_mapping)
        self.__replace('discount', self.bool_mapping)

        self.__str_to_int('price_of_living')
        self.__fill_na('price_of_living', self.whole_dataset['price_of_living'].mean())

        pass

    def __fill_na(self, feature, fill_with):
        self.whole_dataset[feature] = self.whole_dataset[feature].fillna(fill_with)

    def __str_to_int(self, feature):
        self.__str_to_int_replace(feature, r'[^0-9]+', '')

    def __str_to_int_replace(self, feature, replace_what, replace_with):
        self.whole_dataset[feature] = pandas.to_numeric(self.whole_dataset[feature].str.replace(replace_what,
                                                                                                replace_with))

    def __na_to_bool(self, feature):
        self.whole_dataset[feature] = self.whole_dataset[feature].notna()

    def __replace(self, feature, replace_with):
        self.whole_dataset[feature] = self.whole_dataset[feature].replace(replace_with)

    # def __change_type(self, feature, to_type):
