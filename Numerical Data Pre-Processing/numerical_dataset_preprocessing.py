# %%
# Importing required python libraries

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# %%
# Loading the diabetes csv file into a pandas dataframe

diabetes_data = pd.read_csv('diabetes.csv')

# %%
# Displaying the first 10 rows of the dataset

diabetes_data.head(10)

# %%
# Shape of the dataset

diabetes_data.shape

# %%
# Lets see the statistical features of the dataset

diabetes_data.describe()

# %%
# Separating features and target from the dataset

x = diabetes_data.drop(columns = 'Outcome' , axis = 1)
y = diabetes_data['Outcome']

# %%
# Lets check the feature value

print(x)

# %%
# Lets check the target value

print(y)

# %%
# Lets build a standard scaler for standardization of our data

scaler = StandardScaler()
standardized_data = scaler.fit_transform(x)

# %%
# Display our standardized data

print(standardized_data)

# %%
# Splitting the dataset into training and testing data
# Now our data is already pre-processed and is ready for training , testing and analysis part

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 , random_state = 2)
