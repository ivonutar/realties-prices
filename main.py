import pandas
from data_transformator import DataTransformator, DataEngineer
from model_fitting import ModelFitter
from model_predict import ModelPredictor

whole_dataset = pandas.read_csv('flat_info_20200321-152203.csv')

data_transformator = DataTransformator(whole_dataset)
data_transformator.transform()

data_engineer = DataEngineer(data_transformator.whole_dataset)
data_engineer.engineer()

ready_data = data_engineer.whole_dataset

features_for_train = [
                      'discount',
                      'price_of_living',
                      'condition',
                      'living_area',
                      'floor_area',
                      'cellar',
                      'parking',
                      'elevator',
                      'provision_included']

features_to_predict = 'price'

model_fitter = ModelFitter(ready_data, features_for_train, features_to_predict)
model_fitter.fit()


test_data = pandas.read_csv('flat_info-test.csv')
data_transformator = DataTransformator(test_data, test_data=True)
data_transformator.transform()

data_engineer = DataEngineer(data_transformator.whole_dataset, test_data=True)
data_engineer.engineer()


model_predictor = ModelPredictor(data_engineer.whole_dataset[features_for_train], model_fitter.model)

print(model_predictor.predict())
