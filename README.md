# Dijkstra's algorithm

# NOTE
While implementing this algorithm, I didn't take into account that roads are supposed to be two-way instead of one-way.

# 811312A Data Structures and Algorithms 2017-2018, Python Assignment 
This assignment shall be implemented in Python. There exists a country with many roads containing weight restricted bridges. K. is a truck owner in a country’s city and he transports cargo from his home city to country’s other cities. His only truck weighs 8 tons and there is no maximum weight for its cargo. When he takes a transport task, he wants to know, how many tons of cargo he can take to the destination with one trip. For this, all route options are formulated as an undirected graph, whose nodes are cities and edges are roads connecting them. The weight of an edge will be the maximum weight that can be transported using the corresponding road. There is necessarily no direct road connecting a pair of cities. Weights are tons in integers. The cities are numbered with consecutive integers starting from 1, where 1 is always K’s home city and thus the origin of the route. 
  
In this assignment you shall help K by implementing a program that takes as an input the road network and its restrictions as a text file as follows: First line of the file will contain two integers: the number of cities and the number of road segments. The next lines will each contain three integers: first two are city numbers and the third is the maximum weight that can be transported on the road between these cities. Last line will contain one integer representing the destination city. 

First line tells that there are 7 cities and 9 roads. Thus, the following 9 lines define the roads and their maximum weights. The last line tells that we want to know the best route from city 1 to city 7. The name of the input text file can be given as a user input to the program. The program shall print the maximum weight of the cargo or announce that there is no possible route. This latter can happen, if there are no routes from origin to destination or if every route has a maximum weight less than truck’s weight (8 tons). 
