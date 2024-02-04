# %%
# Importing numpy library

import numpy as np

# %%

from time import process_time

# %%

python_list = [i for i in range(100000000)]

start_time = process_time()

python_list = [i+5 for i in python_list]

end_time = process_time()

print(end_time - start_time)

# %%

np_array = np.array([i for i in range(100000000)])

start_time = process_time()

np_array += 5   #Same as adding 5 to all the elements in the numpy array, this concept is also know as broadcasting

end_time = process_time()

print(end_time - start_time)

# %%

list1 = [1,2,3,4,5]
print(list1 , type(list1))

# %%

np_array = np.array([1,2,3,4,5])
print(np_array , type(np_array))

# %%
#Creating a 1D array

one_dimensional_array = np.array([1,2,3,4])
print("\nOne Dimensional Array : \n", one_dimensional_array)
print('Dimension: ' , one_dimensional_array.ndim)
print('Size: ' , one_dimensional_array.size)
print('Shape: ' , one_dimensional_array.shape)

# %%
#Creating a 2D array

two_dimensional_array = np.array([[1,2,3,4],[5,6,7,8]])
print("\nTwo Dimensional Array : \n", two_dimensional_array)
print('Dimension: ' , two_dimensional_array.ndim)
print('Size: ' , two_dimensional_array.size)
print('Shape: ' , two_dimensional_array.shape)

# %%
#Creating a 3D array

three_dimensional_array = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print('\nThree Dimensional Array : \n', three_dimensional_array)
print('Dimension: ' , three_dimensional_array.ndim)
print('Size: ' , three_dimensional_array.size)
print('Shape: ' , three_dimensional_array.shape)

# %%
#Creating an ndarray of Zeros

x = np.zeros((3,4,5))
print(x)

# %%
#Creating an ndarray of any number let's say 7 in a 3 x 3 matrix

n = int(input('Enter any number: '))
z = np.full((3,3) , n)
print('3 x 3 Matrix of value {0}: \n '.format(n) , z)

# %%
# Creating an identity Matrix

a = np.eye(5)  # Identity matrix can only be form within a square matrix
print(a)

# %%
# Creating an ndarray of random values

b = np.random.random((3,3))
print('Matrix of random values: \n' , b)

# %%
# Creating an ndarray of random integer values within a specific range

c = np.random.randint(10 , 100 , (3,3))    # 10 is the lower limit and 100 is the upper limit
print('Mtarix of random integer values: \n' , c)

# %%
# Creating an ndarray of evenly spaced values

d = np.linspace(10 , 30 , 5)   # 10 is the starting element, 30 is the ending element and 5 is the number of elements in the matrix
print('Array with evenly spaced values: \n' , d)

# %%
# Creating an ndarray of evenly spaced values which will depend on the given steps

e = np.arange(10 , 30 , 5)     # 10 is the starting element, 30 is the (ending element + 1) and 5 is the step number in the matrix
print('Matrix of values made up of step number: \n' , e)

# %%
# Conversion of a list into ndarray

list2 = [1,2,4,5]
np_array = np.array(list2)
print('Converted list into ndarray is:\n' , np_array)

# %%
# Reshaping an ndarray

a = np.array([[1,2,3,4],[5,6,7,8]])
print("Original array:\n" , a)
b = a.reshape(4,2)   # It means we are changing the shape to 4 rows and 2 columns
print('Reshaped array: \n' , b)

# %%
# Performing vectorization (Algorithm to perform mathematical operations without performing loops)

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.add(a, b)

print(c)
