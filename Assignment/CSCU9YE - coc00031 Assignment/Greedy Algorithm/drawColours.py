import time
import math
import numpy
import matplotlib.pyplot as plt
import random
import os

# Reads the file  of colours
# Returns the number of colours in the file and a list with the colours (RGB) values

def read_file(fname):
    with open(fname, 'r') as afile:
        lines = afile.readlines()
    n = int(lines[3])    # number of colours  in the file
    col = []
    lines = lines[4:]    # colors as rgb values
    for l in lines:
        rgb = l.split()
        col.append(rgb)
    return n, col

# Display the colours in the order of the permutation in a pyplot window
# Input, list of colours, and ordering  of colours.
# They need to be of the same length

def plot_colours(col, perm):

	assert len(col) == len(perm)

	ratio = 10 # ratio of line height/width, e.g. colour lines will have height 10 and width 1
	img = numpy.zeros((ratio, len(col), 3))
	for i in range(0, len(col)):
		img[:, i, :] = colours[perm[i]]

	fig, axes = plt.subplots(1, figsize=(8,4)) # figsize=(width,height) handles window dimensions
	axes.imshow(img, interpolation='nearest')
	axes.axis('off')
	plt.show()


#####_______main_____######

# Get the directory where the file is located
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path) # Change the working directory so we can read the file


ncolors, colours = read_file('colours.txt')  # Total number of colours and list of colours

test_size = 100  # Size of the subset of colours for testing
test_colours = colours[0:test_size]  # list of colours for testing

permutation = random.sample(range(test_size), test_size) # produces random pemutation of lenght test_size, from the numbers 0 to test_size -1
plot_colours(test_colours, permutation)
# print(permutation)


def list_of_colours():
    """
    :return: The inventory of colours from colours.txt
    """
    num_of_colours, inventory_of_colours = read_file('colours.txt')
    inventory_of_colours = list(numpy.float_(inventory_of_colours))  # Changing the inventory_of_colours from strings to floats
    return inventory_of_colours

inventory_of_colours = list_of_colours()

def run(color_list_size: int):
    test_colour_list_size = color_list_size  # Size of the subset of colours for testing
    test_colour_list = inventory_of_colours[0:test_colour_list_size]  # list of colours for testing
    test, values = greedy_algorithm(colour_initialize_original(), test_colour_list_size)
    plot_colours(test_colour_list, test)

def euclidean_distance_calculation(first_colour, second_colour):
    """
    :param first_colour: The first colour
    :param second_colour: The second colour
    :return: The euclidean distance between two colours.
    """
    return math.sqrt((second_colour[0] - first_colour[0])**2 + (second_colour[1] - first_colour[1])**2 + (second_colour[2] - first_colour[2])**2)

def calculate_metathesis(metathesis):
    """
    This function uses euclidean distance to Return the distances between all pairs of the metathesis provided.
    :param metathesis: The metathesis (permutation)
    :return: The total sum of all the distances
    """
    total_value = 0
    for i in range(len(metathesis) - 1):
        first_colour = inventory_of_colours[metathesis[i]]
        second_colour = inventory_of_colours[metathesis[i+1]]
        distance = euclidean_distance_calculation(first_colour, second_colour)
        total_value += distance
    return total_value

def colour_initialize_original():
    """
    This function returns from the original 1000 color list a random index
    :return: The random number from the colour list
    """
    return random.randint(0, len(inventory_of_colours) - 1)

def greedy_algorithm(start_index: int, color_list_size: int):
    """
    This function begins with a random color from the original list and uses the closest point to each color it identifies to perform a greedy search.
    :param start_index: The random color index to begin the search
    :param color_list_size: The number of colours to group
    :return: The sorded list of colours
    """
    sorted_colours = []
    value_list = []
    sorted_colours.append(start_index)
    start_time = time.time()
    for i in range(color_list_size - 1):
        current_colour = sorted_colours[i]
        best_distance = 1000
        for k in range(len(inventory_of_colours)):
            colour_a = inventory_of_colours[current_colour]
            print(k)
            if k != current_colour and sorted_colours.__contains__(k) is False:
                colour_b = inventory_of_colours[k]
            else:
                continue
            distance_new = euclidean_distance_calculation(colour_a, colour_b)
            if distance_new < best_distance:
                best_colour = k
                best_distance = distance_new
                value_list.append(distance_new)
        sorted_colours.append(best_colour)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Duration of " + str(elapsed_time) + " seconds. List size of testing colours: " + str(color_list_size))
    print("The best operational value: " + str(calculate_metathesis(sorted_colours)))
    # plt.plot(sorted_colours)
    return sorted_colours, value_list

run(100)
#run(500)
