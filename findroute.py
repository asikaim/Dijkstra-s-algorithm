# List and dictionaries needed for Dijkstra's algorithm
nodes=[]			# list where passed nodes are stored
currload={}			# dictionary where largest possible load is stored
travelled={}		# dictionary for travelled routes


def readfile():
	'''
	Asks user for filename and reads the file if possible
	Returns a list which contains all nodes and cargo limits between routes
	'''

	list1 = []

	while True:
		file = input("Input file name: ")

		try:
			with open(file, "r") as dest:
				for row in dest:
					list1.append((row.rstrip()).split())

				return list1	
												
		except IOError:
			print("Can't open file. Try again. ")


def findroute(graph, start, end):
	'''
	Recursive function which finds the best possible route using Dijkstra's algorithm
	
	graph = dictionary where routes between nodes are stored
	start = point where function starts looking for adjacent nodes
	end = last node
	'''

	route = [] 				# list for best possible route
	left = {} 				# dictionary for nodes that haven't been visited

	if start == end:		# tests if we are at the end of graph
		previous = end

		while previous != None:		# travels passed routes back to beginning
			route.append(previous)
			previous = travelled.get(previous, None)

		load = currload[end] - 8 # last possible cargo load
		if load < 8:			 # tests if possible load is smaller than 8
			print("No possible route")
		else:					 # reverses the route and prints it
			route.reverse()
			print("Best possible route: " + str(route) + "\nMaximum cargo load: " + str(load))

	else:
		if not nodes:
			currload[start] = float('inf')	# there are no routes at the beginning of function so cargo load can be infinite
		for route in graph[start]:			# searches adjacent nodes
			if route not in nodes:			# if nodes haven't been passed already
				maxload = min(currload[start], graph[start][route]) 
				if maxload > currload.get(route, 0):	# chooses the route with largest possible cargo load
					currload[route] = maxload
					travelled[route] = start

		nodes.append(start)		# adds node into passed

		for i in graph:			# finds rest of the nodes
			if i not in nodes:
				left[i] = currload.get(i, 0)

		try:					# iterates through the dictionary and picks the largest value for next
			nextn = str(max(left, key=left.get))
		except ValueError:		# if dictionary is empty we know that there are no more nodes
			nextn = end
	
		findroute(graph, nextn, end)	# calls for itself with next nodes value


def main():
	'''
	Main function which creates a graph for Dijkstra's algorithm
	'''
	
	graph = {}
	list1 = readfile()
	start = '1'
	end = list1.pop()	# pops last value in list and assigns it as ending point
	list1.pop(0)		# pops unneeded values in list

	for dest in list1:			# loop which adds all routes and nodes from list into graph
		if dest[0] in graph:
			graph[dest[0]][dest[1]] = int(dest[2])
			if dest[1] in graph:
				graph[dest[1]][dest[0]] = int(dest[2])

		else:
			graph[dest[0]] = {dest[1]: int(dest[2])}
			graph[dest[1]] = {dest[0]: int(dest[2])}

	findroute(graph, start, end[0])


if __name__ == "__main__":
	main()