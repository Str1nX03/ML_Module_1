# %%
# Importing all required python libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# %%
# Importing our data csv file into a pandas dataframe

sonar_data = pd.read_csv('sonar data.csv' , header = None)

# %%
# Display top 10 entries in the dataset

sonar_data.head(10)

# %%
# Lets check the shape of the dataset

sonar_data.shape

# %%
# Lets check the statistical measures of the dataset

sonar_data.describe()

# %%
# Lets see how many rock and mine's example are there in the dataset

sonar_data[60].value_counts()

# %%
# Separating data and labels

x = sonar_data.drop(columns = 60 , axis = 1)
y = sonar_data[60]

# %%
# Grouping the data based on number of rocks and mines example

sonar_data.groupby(60).mean()

# %%
# Lets see value of x

print(x)

# %%
# Lets see value of y

print(y)

# %%
# Spliting the dataset into training and testing data

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.1 , stratify = y ,  random_state = 1)

# %%
# Lets see if we have splitted the data in correct ratio

print(x.shape , ',' , x_test.shape , 'and' , x_train.shape)

# %%
# Loading Logistic Regression model

model = LogisticRegression()

# %%
# Training the Logistic Regression model with training data

model.fit(x_train , y_train)

# %%
# Lets calculate the accuracy of our model on training data

x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction , y_train)

# %%
# Lets see the accuracy of our model on training data

print('Accuracy on the training data is:- ' , training_data_accuracy * 100 , '%')

# %%
# Lets calculate the accuracy of our model on testing data

x_test_prediction = model.predict(x_test)
testing_data_accuracy = accuracy_score(x_test_prediction , y_test)

# %%
# Lets see the accuracy of our model on testing data

print('Accuracy on the testing data is:- ' , testing_data_accuracy * 100 , '%')

# %%
# Now that the model is already trained and ready
# We should make it a predictive system so that we can predict the results on specific data as well

input_data = (0.0114,0.0222,0.0269,0.0384,0.1217,0.2062,0.1489,0.0929,0.1350,0.1799,0.2486,0.2973,0.3672,0.4394,0.5258,0.6755,0.7402,0.8284,0.9033,0.9584,1.0000,0.9982,0.8899,0.7493,0.6367,0.6744,0.7207,0.6821,0.5512,0.4789,0.3924,0.2533,0.1089,0.1390,0.2551,0.3301,0.2818,0.2142,0.2266,0.2142,0.2354,0.2871,0.2596,0.1925,0.1256,0.1003,0.0951,0.1210,0.0728,0.0174,0.0213,0.0269,0.0152,0.0257,0.0097,0.0041,0.0050,0.0145,0.0103,0.0025)
input_data_as_array = np.array(input_data)
input_data_reshaped = input_data_as_array.reshape(1 , -1)
prediction =model.predict(input_data_reshaped)

if prediction[0] == 'R':

    print('Its a Rock.')

else:

    print('Its a Mine.')
