# Label encoding is a technique used in machine learning and data analysis to convert categorical variables into numerical format
#%%
# Importing required python libraries

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# %%
# Loading the data from csv file to pandas Dataframe

cancer_data = pd.read_csv('breast_cancer_data.csv')

# %%
# Display top 10 entries of the dataset

cancer_data.head(10)

# %%
# Finding the count of different labels

cancer_data['diagnosis'].value_counts()

# %%
# Load the label encoder function

label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(cancer_data.diagnosis)

# %%
# Appending the labels to the dataframe

cancer_data['target'] = labels

# %%
# Check the dataframe for column named 'target'

cancer_data.head(10)

# %%
# Lets drop the diagnosis column as now we have target column to conduct our testing
# Now the dataset is completely label encoded and ready to conduct analysis and testing

cancer_data.drop('diagnosis' , axis = 1)
