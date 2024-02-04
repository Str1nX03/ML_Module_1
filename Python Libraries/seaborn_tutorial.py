# %%
# Importing Seaborn library

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
# We are going to import one of the toy dataset that is available within seaborn library which is 'tips' dataset

tips = sns.load_dataset('tips')

# %%
# Display first 5 results of the dataset

tips.head()

# %%
# Display last 5 results of the dataset

tips.tail()

# %%
# Visualize the tip dataset

sns.relplot(data = tips , x = 'total_bill' , y = 'tip' , col = 'time' , hue = 'smoker' , style = 'smoker' , size = 'size')

# %%
# Setting a theme for the plots

sns.set_theme()

# %%
# Visualize the tip dataset after setting up the theme

sns.relplot(data = tips , x = 'total_bill' , y = 'tip' , col = 'time' , hue = 'smoker' , style = 'smoker' , size = 'size')

# %%
# Importing Iris dataset (manually)

data = pd.read_csv('iris_data.csv')
print(data)
df = pd.DataFrame(data)
print(df.describe())

# %%
# Importing Iris dataset from seaborn library

iris =sns.load_dataset('iris')

# %%
# Display first 5 results of iris dataset

iris.head()

# %%
# Display last 5 results of iris dataset

iris.tail()

# %%
# Visualizing iris dataset using scatter plot

sns.scatterplot(x = 'sepal_length' , y = 'petal_length' , hue = 'species' , data = iris)

# %%
# Importing Titanic dataset from seaborn library

titanic = sns.load_dataset('titanic')

# %%
# Display first 5 results in titanic dataset

titanic.head()

# %%
# Display last 5 results in titanic dataset

titanic.tail()

# %%
# Plotting a Count Plot

sns.countplot(x = 'class' , data = titanic)
sns.countplot(x = 'survived' , data = titanic)

# %%
# Plotting a bar chart

sns.barplot(x = 'sex' , y = 'survived' , hue = 'class' , data = titanic)
