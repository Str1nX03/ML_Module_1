# %%
# Importing pandas library

import pandas as pd

# %%
# Creating a pandas Dataframe from an imported csv file

dataset = pd.read_csv('iris_data.csv')
df = pd.DataFrame(dataset)
print(df)

# %%
# Displaying only top 10 results of the dataframe

print(df.head(10))

# %%
# Display only bottom 10 results of the dataframe

print(df.tail(10))

# %%
# Description of the dataframe

print(df.describe())

# %%
# Max value of the dataframe in every aspect

print(df.max())

# %%
# Creating a Series from a user data

dict = {'Name':[1,2,3,4,5,6]}
series = pd.Series(dict)
print(series)

# %%
# Creating a dataframe on user data and default indexes

dict = {'Name':['Dravin' , 'Kumar' , 'Sharma'] , 'Roll':[1,2,3]}
df1 = pd.DataFrame(dict)
print(df1)


# %%
# Creating a dataframe on user data and custom made indexes

dict = {'Name':['Dravin' , 'Kumar' , 'Sharma'] , 'Roll':[3,5,7]}
df2 = pd.DataFrame(dict , index = ['First Name' , 'Middle Name' , 'Last Name'])
print(df2)

# %%
# Adding a column into the dataframe

df2['Priority'] = [1,2,3]
print(df2)

# %%
# Removing a row from a dataframe (To remove a row, we need to give axis as 0)

df3 = df2.drop(index = 'Middle Name' , axis = 0)
print(df3)

# %%
# Removing a column from a dataframe (To remove a column, we need to give axis as 1)

df4 = df2.drop(columns = 'Roll' , axis = 1)
print(df4)

# %%
# Locating a row using the index value

print(df1.iloc[1])

# %%
# Selecting whole column

print(df2.iloc[: , 0])
print(df2.iloc[: , 1])
print(df2.iloc[: , 2])

# %%
# Selecting whole row

print(df2.iloc[0 , :])
print(df2.iloc[1 , :])
print(df2.iloc[2 , :])

# %%
# Accessing a group of rows and columns using loc() function

print(df2.loc[['First Name' , 'Last Name']])
print(df2.loc[df2['Priority'] > 1])
