# The knapsack problem
# Gabriela Ochoa

import os 
import random as rnd

# Single knapsack problem

# Read the instance  data given a file name. Returns: n = no. items, 
# c = capacity, vs: list of itmen vamies, ws: list of item weigths

def read_kfile(fname):
    with open(fname, 'r') as kfile:
        lines = kfile.readlines()     # reads the whole file
    n = int(lines[0])   # fist line is the number of items, need to transform to int
    c = int(lines[n+1]) # last line is the capacity, need to transform to int 
    vs = []
    ws = []
    lines = lines[1:n+1]   # Removes the first and last line
    for l in lines:
        numbers = l.split()   # Converts the string into a list
        vs.append(int(numbers[1]))  # Appends value, need to convert to int
        ws.append(int(numbers[2]))  # Appends weigth, need to convert to int
    return n, c, vs, ws

dir_path = os.path.dirname(os.path.realpath(__file__))  # Get the directory where the file is located
os.chdir(dir_path)  # Change the working directory so we can read the file

knapfile = 'knap20.txt'
nitems, cap, values, weights = read_kfile(knapfile)



# Evaluates a solution.
# input: solution binary string
# ouptut: value and weight of the input solution

def evaluate(sol):
    totv = 0
    totw = 0
    for i in range(nitems):
        totv = totv + sol[i]*values[i]
        totw = totw + sol[i]*weights[i]
    return totv, totw

# Generates a random solution (binary string)
# input: number of items
# output: binary string with solutions 

def random_sol(n):
    sol = []
    for i in range (n):
        sol.append(rnd.randint(0,1))   # Random binary string len = nitems
    return sol
    
# Generates a valid random solution (binary string)
# input:  number of items
# output: sol, binary string with solutions 

def random_sol_valid(n):
    binvalid = True
    while binvalid:
        s = random_sol(n)
        v, w = evaluate(s)
        binvalid = (w > cap)
    return s, v, w


# Multiple iterations of generating valid random solutions
# input:  number of repetitions
# output: Set of values obtained, binary string with solutions 

def random_search_valid(tries):
    values = []
    best_sol = []
    best_val = 0
    best_wei = 0
    print("Multi Random")
    for i in range (tries):
        sol, v, w = random_sol_valid(nitems)
        values.append(v)
        if (v > best_val):
            best_val = v
            best_wei = w
            best_sol = sol[:]
    return best_sol, best_val, best_wei
    


# Implements a greedy constructive heuristic
# Returns: solution, value and weight

def constructive():
    sol_wei = 0
    sol_val = 0
    solution = []
    tvalues = values[:]         # A copy of the list of values,to remove items 
    for k in range(nitems):     # the maximun possible itmes to include
        best = max(tvalues)     # determine the best item in the temp variable
        i = values.index(best)  # determine index of best item in the original
        ti = tvalues.index(best) # determine index of best item in the temporal
        tmp_wei = sol_wei + weights[i]
        if (tmp_wei <= cap):     # if new best item fits add it
            solution.append(i)   # Add item to solution, index from original 
            sol_wei= tmp_wei     # Increase weight of solution
            sol_val = sol_val + values[i]  # Increase value of solution
            del tvalues[ti]      # delete added item from temp values,              
    return solution, sol_val, sol_wei   

    
solc, valc, weic = constructive()

print("Solution for constructuve heuristic")
print("Value: ", valc, " Weight: ", weic)
print("Solution: ",solc) 


solr, valr, weir = random_search_valid(50)

print("Solution for random search")
print("Value: ", valr, " Weight: ", weir)
print("Solution: ",solr) 
  

