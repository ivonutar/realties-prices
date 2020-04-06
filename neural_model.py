from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd

from data_transformator import DataTransformator, DataEngineer


# read in training data
train_df = pd.read_csv('flat_info_20200321-152203.csv')


data_transformator = DataTransformator(train_df)
data_transformator.transform()

data_engineer = DataEngineer(data_transformator.whole_dataset)
data_engineer.engineer()

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
train_df = data_engineer.whole_dataset[features_for_train]

model = Sequential()

model.add(Dense(50, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

X = train_df.drop(target, axis=1).values
Y = train_df[[target]].values

# Train the model
model.fit(
    X,
    Y,
    epochs=1100,
    shuffle=True,
    verbose=2
)

prediction = model.predict(X[:5])

print(train_df.head(5)['price'])
print(prediction[:5])
print(prediction.min())
print(prediction.max())
