# Data standardization is a data processing workflow that converts the structure of different datasets into one common format of data
#%%
# Importing all required libraries

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# %%
# Loading the dataset

dataset = sklearn.datasets.load_breast_cancer()

# %%
# Display the whole dataset

print(dataset)

# %%
# Loading the data into a pandas Dataframe

df = pd.DataFrame(dataset.data , columns = dataset.feature_names)

# %%
# Display top entries of the dataset

df.head(10)

# %%
# Checking the shape of the dataframe

df.shape

# %%
# Splitting target and other data into 2 different variables
# When we printed the whole dataset, we found that it contains a variable named 'feature_names' that contains names of all required columns so we can use it to get capture all the data using 'feature_names' into one variable

x = df
y = dataset.target

# %%
# Checking the values of 'x' variable

print(x)

# %%
# Checking the values of 'y' variable

print(y)

# %%
# Splitting training data and testing data
# The random state hyperparameter in the train_test_split() function controls the shuffling process, I used 3 so if you will use 3 you will get the same type of shuffling as mine but its your choice you can have any type of shuffling as you want

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 , random_state = 3)

# %%
# Checking shape of our variables

print(x.shape , x_train.shape , x_test.shape)
print(y.shape , y_train.shape , y_test.shape)

# %%
# Checking Standard deviation of the data
# Standardization entails scaling data to fit a standard normal distribution
# If value of standard deviation is 1 then it means that all the data are in somewhat similar range and it doesn't change the nature of the data

print(dataset.data.std())

# %%
# Using Standard Scaler to standardize data

scaler = StandardScaler()
scaler.fit(x_train)

# %%
# Transforming the data into standard scaler format

x_train_standardized = scaler.transform(x_train)

# %%
# Lets see the standardized data in x_train
# Now the difference in different data points will not be too large

print(x_train_standardized)

# %%
# Standardizing x_test variable

x_test_standardized = scaler.transform(x_test)

# %%
# Lets check standard deviation of x_train_standardized and x_test_standardized now
# x_test_standardized is not 1 as it was standardized based on x_train_standardized but it is much better than 228.29740508276657 which we got previously
# Now we can say that our 'x' data is completely standardized

print(x_train_standardized.std())
print(x_test_standardized.std())
