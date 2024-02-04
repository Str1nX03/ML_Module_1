# %%
# Import all required python libraries

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# %%
# Covert csv data files into pandas DataFrame

diabetes_dataset = pd.read_csv('diabetes.csv')

# %%
# Display top 10 entries of the dataset

diabetes_dataset.head(10)

# %%
# Check the shape of the dataset

diabetes_dataset.shape

# %%
# Evaluate the statistical measures of the dataset

diabetes_dataset.describe()

# %%
# Check the data points for each target value

diabetes_dataset['Outcome'].value_counts()

# %%
# Group by the dataset on the basis of the target column

diabetes_dataset.groupby('Outcome').mean()

# %%
# Split the dataset into features x and target variable y

x = diabetes_dataset.drop(columns = 'Outcome' , axis = 1)
y = diabetes_dataset['Outcome']

# %%
# Display the value of x

print(x)

# %%
# Display the value of y

print(y)

# %%
# Loading Standard Scaler function in order to standardized the data

scaler = StandardScaler()
scaler.fit(x)

# %%
# Standardized the data

standardized_data = scaler.transform(x)

# %%
# Updating the values of x and y

x = standardized_data
y = diabetes_dataset['Outcome']

# %%
# Lets check the new values of x and y

print(x)
print(y)

# %%
# Spliting the training and testing data

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 , stratify = y , random_state = 1)

# %%
# Lets see the shape of our training and testing data when compared with the actual data to see if the spliting was done properly

print(x.shape , ',' , x_train.shape , 'and' , x_test.shape)

# %%
# Initializing the Support Vector Machine model and fitting it with the training data

classifier =svm.SVC(kernel = 'linear')
classifier.fit(x_train , y_train)

# %%
# Evaluating the model on training data

x_train_prediction = classifier.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction , y_train)

# %%
#  Printing the Accuracy score for Training Data

print('Accuracy score of the training data: ' , training_data_accuracy)

# %%
# Evaluating the model on training data

x_test_prediction = classifier.predict(x_test)
testing_data_accuracy = accuracy_score(x_test_prediction , y_test)

# %%
#  Printing the Accuracy score for Testing Data

print('Accuracy score of the testing data: ' , testing_data_accuracy)

# %%
# Making a predictive model in order to predict outcomes on new data

input_data = (0,100,88,60,110,46.8,0.962,31)
input_data_as_array = np.asarray(input_data)
input_data_reshaped = input_data_as_array.reshape(1 , -1)
std_data = scaler.transform(input_data_reshaped)
prediction = classifier.predict(std_data)

print(std_data)
print(prediction)

if prediction == 0:

    print('Person is non-diabetic.')

else:

    print('Person is diabetic.')
    
# %%
