# %%
# Importing matplotlib library

import matplotlib.pyplot as plt
import numpy as np

# %%
# Generating values for our plot

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)

print('Values of Sine function: ' , y)
print('Values of Cosine function: ' , z)

# %%
# Plotting Sine wave using matplotlib

plt.plot(x , y)
plt.show()

# %%
# Plotting Cosine wave using matplotlib

plt.plot(x , z)
plt.show()

# %%
# Labeling x and y axis in Sine wave plot

plt.plot(x , y)
plt.title('Sine Graph')
plt.xlabel('Angle')
plt.ylabel('Sine Values')
plt.show()

# %%
# Lableling x and y axis in Cosine wave plot

plt.plot(x, z)
plt.title('Cosine Graph')
plt.xlabel('Angle')
plt.ylabel('Cosine Values')
plt.show()

# %%
# Plotting a Parabola in matplotlib

x1 = np.linspace(-10 , 10 , 20)
y1 = x1 ** 2
plt.plot(x1 , y1)
plt.xlabel('Value of X')
plt.ylabel('Value of Y')
plt.title('Parabola')
plt.show()

# %%
# Plotting the Parabola in different type of lines or symbols

plt.plot(x1 , y1 , 'r')
plt.show()
plt.plot(x1 , y1 , 'r+')
plt.show()
plt.plot(x1 , y1 , 'g.')
plt.show()
plt.plot(x1 , y1 , 'rx')
plt.show()

# %%
# Making multiple lines in single graph

x2 = np.linspace(-5 , 5 , 50)
y2 = np.sin(x2)
z2 = np.cos(x2)
plt.plot(x2 , y2 , 'g-')
plt.plot(x2 , z2 , 'r')
plt.show()

# %%
# Plotting Bar graph

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = ['Hindi' , 'English' , 'French' , 'Spanish' , 'Japanese']
people = [100 ,50 , 150 , 40 , 70]
ax.bar(languages , people)
plt.xlabel('Languages')
plt.ylabel('Number of people')
plt.title('Bar Graph')
plt.show()

# %%
# Plotting a pie chart

fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
languages = ['Hindi' , 'English' , 'French' , 'Spanish' , 'Japanese']
people = [100 ,50 , 150 , 40 , 70]
plt.title('Pie Chart')
ax1.pie(people , labels = languages , autopct = '%1.1f%%')
plt.show()

# %%
# Plotting a scatter plot

x3 = np.linspace(0 , 10 , 30)
y3 = np.sin(x3)
z3 = np.cos(x3)
fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
ax2.scatter(x3 , y3 , color = 'g')
ax2.scatter(x3 , z3 , color = 'b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot')
plt.show()


# %%
# Plotting a 3D scatter plot

fig3 = plt.figure()
ax3 = plt.axes(projection = '3d')
x4 = 20 * np.random.random(100)
y4 = np.sin(x4)
z4 = np.cos(x4)
ax3.scatter(x4 ,y4 , z4 , c = z4 , cmap = 'Blues')
plt.show()

# %%
# Same scatter plot in 2D

fig3 = plt.figure()
ax3 = plt.axes()
x4 = 20 * np.random.random(100)
y4 = np.sin(x4)
z4 = np.cos(x4)
ax3.scatter(x4 ,y4 , z4 , c = z4 , cmap = 'Blues')
plt.show()
