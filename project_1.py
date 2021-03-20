# -*- coding: utf-8 -*-
"""Project 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17PpkWuCEVKYxCOoXsVJxRaL5yiGR_d3c
"""

'''
This project involves creating a randomized vector field, plotting the vector field,
creating a random walk based off of the vector field, and plotting this random walk. 
I hereby attest that I have adhered to the rules for quizzes and projects as well as UICâ€™s
Academic Integrity standards. Signed: [[Saketh Mahesh].
'''
import random
import numpy as np
import matplotlib.pyplot as plt

'''
This function creates a random vector field of size 10 by 10. Variables grid_x and grid_y refer to the grid size on the plot and variables rise and run refer to the randomized vector field created for each point on that graph. The end result is a returned vector field array using numpy. For the purposes of this project, the function creates a 10 by 10 random vector field every time.
'''
def create_vectors():
  x = np.arange(10) #Generates values for the x coordinate in the range of 10
  y = np.arange(10) #Generates values for the y coordinate in the range of 10

  grid_x, grid_y = np.meshgrid(x, y) #Values for x and y are meshgrided in order to create a 10 by 10 array

  rise = np.zeros(shape = (10,10)) #Filling a 10 by 10 array with temporary zeros
  run = np.zeros(shape = (10,10))  #Filling a 10 by 10 array with temporary zeros

  '''For loop for creating the randomized rise and run values withing the range of 10. The end result is a 10 by 10 array consisting of randomized values.'''
  for x in range(0,10):
    temp = [np.random.randint(10), np.random.randint(10),np.random.randint(10),
            np.random.randint(10),np.random.randint(10),np.random.randint(10),
            np.random.randint(10),np.random.randint(10),np.random.randint(10),np.random.randint(10)]
    temp2 = [np.random.randint(10), np.random.randint(10),np.random.randint(10),
            np.random.randint(10),np.random.randint(10),np.random.randint(10),
            np.random.randint(10),np.random.randint(10),np.random.randint(10),np.random.randint(10)]
    rise[x] = temp #All 10 of the random temp values are assigned to the variable rise
    run[x] = temp2 #All 10 of the random temp values are assigned to the variable run
  return (rise,run,grid_x,grid_y) #Returns the random vector field

'''
This function plots the given vector field input using matplotlib.
'''
def vec_plot(rise,run,grid_x,grid_y):
  rise,run,grid_x,grid_y = create_vectors() #Variables that are taken as input are defined in this function
  fig, ax = plt.subplots() #Creating positions of this plot using the figure and axes
  plt.plot(grid_x,grid_y, "ro") #Plots the grid_x and grid_y as red circles
  q = ax.quiver(rise,run) #Quiverplots the rise and runs for each coordinate point
  plt.show() #Displays the plot

'''
This function generates the random walk based off the given vector field input.
'''
def random_walk(rise,run,grid_x,grid_y):
  rise,run,grid_x,grid_y = create_vectors() #Previous function variables are called.
  size_lim = len(grid_x) #Sets the size boundary of the random walk to be the boundaries of the grid_x array 
  grid_x = [item for sublist in grid_x for item in sublist] #Flattens the grid_x 10 by 10 array into 1 array
  grid_y = [item for sublist in grid_y for item in sublist] #Flattens the grid_y 10 by 10 array into 1 array

  x_y = list(zip(grid_x,grid_y)) #Zip the grid_x and grid_y array into 1 list of tuples

  rise = [item for sublist in rise for item in sublist] #Flattens the rise 10 by 10 array into 1 array
  run = [item for sublist in run for item in sublist] #Flattens the run 10 by 10 array into 1 array

  vec1 = list(zip(rise,run)) #Zip the rise and run arrays into 1 list of tuples

  step = list() #Creates an empty list
  for x in range(0,10): #For loop to create 10 random x and y coordinates within a certain bounds
    random_number = random.randint(0,size_lim) #Creates a random int within the bounds of grid_x(which is the starting point)
    x1 = [int(x_y[random_number][0]), int(vec1[random_number][0])]#Sets the random number to be the x coordinate of the first tuple in the x_y list and same process for the vector list
    y1 = [int(x_y[random_number][1]), int(vec1[random_number][1])]#Sets the random number to be the y coordinate of the first tuple in the x_y list and same process for the vector list
    new_start = (random.randint(min(x1), max(x1)), random.randint(min(y1), max(y1)))#Generates a coordinate that lies between the min and max of x1 and the same for y1
    step.append(new_start) #Appends all the values of new_start into the empty list step
  return step #The 10 steps or "walks" are returned

'''
This function plots the given random walk
'''
def walk_plot(rise,run,grid_x,grid_y):
  rise,run,grid_x,grid_y = create_vectors() #x,y,rise,and run coordinates are called to be used.
  step = random_walk(rise,run,grid_x,grid_y) #The step list containing the random walks is called
  out = [item for x in step for item in x] #The step list of tuples is turned into a list only.
  x_list = out[::2] #This is the x coordinates of the step(every other number in the out list)
  y_list = out[1::2] #This is the y coordinates of the step(every odd number in the outlist)
  plt.plot(x_list,y_list) #The 2 lists containing the random walk are plotted
  plt.plot(grid_x, grid_y, "go") #The x and y coordinates of each point on the plot are plotted
  plt.savefig("newfigure") #Saves the figure in a new file 
  plt.show() #Displays the random walk plot along with a green circle for each point on the graph





'''
  How To Call Functions:
  In order to call the first function, the grader needs to type in "create_vectors()"
  into the console and the result will be 4 arrays(the x grid, the y grid, the rise,
  and the run)
  2. In order to call the second function, the grader needs to type in "vec_plot(10,10,10,10)"
  because the plot is set to be a 10 by 10 grid with one random vector generated for each point.
  3. In order to call the third function, the grader needs to type in "random_walk(10,10,10,10)"
  because yet again, the parameters of the rise,run,grid_x,and grid_y are set(as the directions
  allow it to be).
  4. In order to call the 4th function, the grader needs to type in "walk_plot(10,10,10,10)"
  into the console.
'''