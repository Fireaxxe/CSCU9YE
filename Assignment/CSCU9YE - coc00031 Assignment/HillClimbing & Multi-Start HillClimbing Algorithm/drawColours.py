import time
import math
import tkinter
from tkinter import messagebox
import statistics
import matplotlib.pyplot as plt
import numpy
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
# plot_colours(test_colours, permutation)
# print(permutation)



def list_of_colours():
    """
    :return: The inventory of colours from colours.txt
    """
    num_of_colours, inventory_of_colours = read_file('colours.txt')
    inventory_of_colours = list(numpy.float_(inventory_of_colours))  # Changing the inventory_of_colours from strings to floats
    return inventory_of_colours

inventory_of_colours = list_of_colours()

def statistic_calculations(values: list):
    """
    This function prints the, Lowest, Highest, Mean, Median and Standard Deviation
    :param values: A list with all the time values
    """
    # print("List of all the values:", values)
    print("Lowest value of the list:" , min(values))
    print("Highest value of the list:", max(values))
    print("Mean:", statistics.mean(values))
    print("Median:", statistics.median(values))
    print("Standard Deviation:", statistics.stdev(values))

def euclidean_distance_calculation(first_colour, second_colour):
    """
    :param first_colour: The first colour
    :param second_colour: The second colour
    :return: The euclidean distance between two colours.
    """
    return math.sqrt((second_colour[0] - first_colour[0])**2 + (second_colour[1] - first_colour[1])**2 + (second_colour[2] - first_colour[2])**2)

def run(repetition: int, colour_list_size: int):
    """
    This function runs the algorithm of hill climbing as many times as the variable of repetition defines e.g. run(x,100) which x is the number of repeats.
    If x = 1 then it will be a single run and two plots will be made.
    If x = >1 then the multi-start hill climbing algorithm will run and will produce the best solution plot as well as the mean, median and standard deviation.
    :param repetition: No. of times the algorithm will run
    :param colour_list_size: The colour list size
    """
    if repetition > 1:
        multi_start_hill_climbing_algorithm(repetition, colour_list_size)
    else:
        single_run_hill_climbing_algorithm(colour_list_size)

def random_metathesis(size):
    """
    This function Returns a size-based random metathesis.
    :param size: The size of the metathesis
    :return: A random metathesis
    """
    return random.sample(range(size), size)

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

def random_neighbour_metathesis(metathesis):
    """
    This function uses the inverse procedure to return a random neighbor metathesis.
    :param metathesis: The original metathesis
    :return: A neighbour of the original metathesis
    """
    new_metathesis = metathesis.copy() #metathesis.copy() to make a copy of the list of metathesis so that the original list does not change
    has_operation_finished = False
    indicator_a = random.randint(0, len(metathesis) - 1) #random position
    indicator_b = random.randint(0, len(metathesis) - 1) #random position

    while indicator_a == indicator_b: #to avoid same random positions
        indicator_b = random.randint(0, len(metathesis) - 1)
    while not has_operation_finished: #inverse Operator
        value_a = metathesis[indicator_a]       #swaping the values
        value_b = metathesis[indicator_b]       #swaping the values
        new_metathesis[indicator_a] = value_b   #swaping the values
        new_metathesis[indicator_b] = value_a   #swaping the values
        if indicator_a < indicator_b: #changes the indices depending on their location
            indicator_a += 1
            indicator_b -= 1
            if indicator_a >= indicator_b:
                has_operation_finished = True
                continue
        else:
            indicator_b += 1
            indicator_a -= 1
            if indicator_a <= indicator_b:
                has_operation_finished = True
                continue
    return new_metathesis

def hill_climbing_algorithm(starting_metathesis):
    """
    This function use a nearest neighbor with an inverse operator for the hill climbing algorithm.
    :param starting_metathesis: The starting metathesis
    :return: The final and best metathesis
    """
    total_time_1 = time.time() #time() used for testing
    final_metathesis = starting_metathesis
    top_results = [] #top_results used for plotting and keeps record of total_values
    for i in range(10000): #the higher the range number the better the calculation of the final metathesis (also it will take more time)
        total_value = calculate_metathesis(final_metathesis)
        neighbour_metathesis = random_neighbour_metathesis(final_metathesis)
        neighbour_total_value = calculate_metathesis(neighbour_metathesis)
        if neighbour_total_value < total_value: #if the neighbor's total_value is less then the neighbor's result is better
            final_metathesis.clear()
            top_results.append(neighbour_total_value)
            final_metathesis = neighbour_metathesis.copy()
            neighbour_metathesis.clear()
    total_time_2 = time.time() #time() used for test the running time of the algorithm
    root = tkinter.Tk()
    root.withdraw() #hide main window
    time_elapsed = ((total_time_2 - total_time_1)) #calculate to total time it took the algorithm to finish its run
    # messagebox.showinfo("Best time:", time_elapsed) #COMMENT THIS OUT if it becomes annoying --- message box display
    print("Best time for this run:", time_elapsed , "seconds.")
    return top_results, final_metathesis

def single_run_hill_climbing_algorithm(colour_list_size):
    """
    A single run of the climbing algorithm generates a plot showing that iteration's progress as well as a color plot showing the final result.
    :param colour_list_size: The colour list size
    """
    test_colours = inventory_of_colours[0:colour_list_size]  #list of colours for testing
    top_results, best_metathesis = hill_climbing_algorithm(random_metathesis(colour_list_size))
    plot(top_results)
    plot_colours(test_colours, best_metathesis)

def multi_start_hill_climbing_algorithm(repetition: int, colour_list_size: int):
    """
    This function runs for a number of repeats and seeks the best solution for hill climbing
    :param repetition: The number of repeats of the function
    :param colour_list_size: The colour list size
    :return: A summary of the best solution with best distance and a list of all the solutions found
    """
    top_result = []
    best_distance = 0
    value_list = []
    plot_value_list = []
    for i in range(repetition):
        bs, metathesis = hill_climbing_algorithm(random_metathesis(colour_list_size))
        new_distance = calculate_metathesis(metathesis)
        plot_value_list.append(new_distance)
        current_run = i+1
        print("Updated list of all values:", plot_value_list)
        print("Best distance for the current iteration:", new_distance)
        print("Current run:", current_run)
        print()
        if new_distance < best_distance or i == 0:
            top_result = metathesis.copy()
            best_distance = new_distance
            value_list.append(new_distance)
    statistic_calculations(value_list)
    plot(plot_value_list)
    print("The best operational value: ", best_distance)
    print("List of ALL values: ", plot_value_list)
    test_colours = inventory_of_colours[0:colour_list_size]  # list of colours for testing
    plot_colours(test_colours, top_result)
    return value_list

def plot(top_results):
    """
    Creates a plot based on the top_results list.
    :param top_results: The list to create a plot from
    """
    plt.plot(top_results)
    plt.ylabel('Value (Total Distance)')
    plt.xlabel("Iterations")
    plt.grid(True)

run(30, 100)
#run(1, 100)
#run(10,100) !# WARNING: COMMENT OUT --- messagebox.showinfo("Best time: ", time_elapsed) line:157
#run(30,100) !# WARNING: COMMENT OUT --- messagebox.showinfo("Best time: ", time_elapsed) line:157

#run(1, 500)
#run(10,500) !# WARNING: COMMENT OUT --- messagebox.showinfo("Best time: ", time_elapsed) line:157
#run(30,500) !# WARNING: COMMENT OUT --- messagebox.showinfo("Best time: ", time_elapsed) line:157
