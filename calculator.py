import math

def total_squared_distance(centroid, lst):
	""" calculator for total_squared_distance
	>>> centroid_1 = [3.0, 9.5]
	>>> cluster_1 = [(2, 10), (4, 9), (5, 8)]
	>>> total_squared_distance(centroid_1, cluster_1)

	>>> centroid_2 = [6.5, 5,25]
	>>> cluster_2 = [(6, 4), (7, 5), (8, 4)]
	>>> total_squared_distance(centroid_2, cluster_2)

	>>> centroid_3 = [1.5, 3.5]
	>>> cluster_3 = [(1, 2), (2, 5)]
	>>> total_squared_distance(centroid_3, cluster_3)
	"""
	total_distance = 0
	for i in lst:
		total_distance += (math.sqrt((centroid[0] - i[0])**2 + (centroid[1] - i[1])**2))**2

	return total_distance

def centroid_calculator(centroid, cluster):
	""" calculator for total_squared_distance
	>>> centroid_1 = [3.0, 9.5]
	>>> cluster_1 = [(2, 10), (4, 9), (5, 8)]
	>>> centroid_calculator(centroid_1, cluster_1)

	>>> centroid_2 = [6.5, 5,25]
	>>> cluster_2 = [(6, 4), (7, 5), (8, 4)]
	>>> centroid_calculator(centroid_2, cluster_2)

	>>> centroid_3 = [1.5, 3.5]
	>>> cluster_3 = [(1, 2), (2, 5)]
	>>> centroid_calculator(centroid_3, cluster_3)
	"""
	x = centroid[0]
	y = centroid[1]

	for i in cluster:
		x += i[0]
	for i in cluster:
		y += i[1]

	x = x/(len(cluster) + 1)
	y = y/(len(cluster) + 1)
	
	return (x, y)


lst_y = [12, 5, 2, -3, -5, -8, -13]
lst_x = [-3, -2, -1, 0, 1, 2, 3]

"""
The following functions are used to calculate h(x)
in degrees 0 to 4
"""
def degree_0(x):
	c0 = -1.4286
	h = [c0 for i in x]
	return h

def degree_1(x):
	c0 = -1.4286
	c1 = -3.8571
	h = [(c0 + c1*i) for i in x]
	return h

def degree_2(x):
	c0 = -2.1905
	c1 = -3.8521
	c2 = 0.1905
	h = [(c0 + c1*i + c2*(i**2)) for i in x]
	return h

def degree_3(x):
	c0 = -2.1905
	c1 = -2.884 
	c2 = 0.1903
	c3 = -0.1389
	h = [(c0 + c1*i + c2*(i**2) + c3*(i**3)) for i in x]
	return h

def degree_4(x):
	c0 = -2.324
	c1 = -2.8849
	c2 = 0.2992
	c3 = -0.1389
	c4 = -0.0114
	h =[(c0 + c1*i + c2*(i**2) + c3*(i**3) + c4*(i**4)) for i in x]
	return h 

"""
The following function is used to calculate the MSE of each hypothesis
""" 
def mean_squared_error(y, x, func):
	"""
	>>> mean_squared_error(lst_y, lst_x, degree_0)
	>>> mean_squared_error(lst_y, lst_x, degree_1)
	>>> mean_squared_error(lst_y, lst_x, degree_2)
	>>> mean_squared_error(lst_y, lst_x, degree_3)
	>>> mean_squared_error(lst_y, lst_x, degree_4)
	"""
	lst_gen = func(x)
	total = 0
	for i in range(len(y)):
		total += (y[i] - lst_gen[i])**2
	mean = total/len(y)

	return mean

