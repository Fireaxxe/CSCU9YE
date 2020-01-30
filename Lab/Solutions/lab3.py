# The knapsack problem
# Gabriela Ochoa

import os 
import matplotlib.pyplot as plt
import random as rnd

# Single knapsack problem

# Read the instance  data given a file name. Returns: n = no. items, 
# c = capacity, vs: list of itmen values, ws: list of item weigths

def read_kfile(fname):
    with open(fname, 'rU') as kfile:
        lines = kfile.readlines()     # reads the whole file
    n = int(lines[0])
    c = int(lines[n+1])
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
    return values, best_sol, best_val, best_wei
    

# Return a random 1-bit flip neigbour 
# input: solution as binary vector
# output: random solution in the 1-bit flip neighbourhood

def random_valid_neig(sol):
    binvalid = True
    while binvalid:
        neig = sol[:]                 # copy solution
        i = rnd.randint(0,nitems-1)
        neig[i] = 0 if sol[i] else 1  # alter position i
        v, w = evaluate(neig)
        binvalid = (w > cap)
    return neig, v, w



# First improvement random mutation, hill-climbing

def hill_climbing(maxiter):
    trace = []
    s, v, w = random_sol_valid(nitems)
    trace.append(v)
    for i in range (maxiter):
        s1, v1, w1 = random_valid_neig(s)  
        if v1 > v:
            v = v1
            w = w1
            s = s1[:]
            trace.append(v)       
    return s, v, w, trace
  
# multiple tries, hill-climbig   
 
def multi_hc(tries, hc_iter):
    values = []
    best_sol = []
    best_trace =[]
    best_val = 0 
    best_wei = 0
    print("Multi hill climbing")
    for i in range (tries):
        sol, v, w, trace = hill_climbing(hc_iter) 
        values.append(v)
        if (v > best_val):
            best_val = v
            best_wei = w
            best_sol = sol[:]
            best_trace = trace[:]
    return best_trace, values, best_sol, best_val, best_wei
                            
# Calling functions
s, v, w, trace = hill_climbing(10)    # single run of hill-climbing
print('After hill-climibing')
print ('Sol.:' , s, 'V:', v, 'W:', w)
print ('Trace:', trace)
plt.figure()
plt.plot(trace,'ro')  # 'ro' indicates to plot as dots (circles) of red color
plt.title('Trace ' + knapfile)
plt.ylabel('Value')
plt.show()


times = 30  # number of tries by the random search and the multi HC
# random search
values_rnd, sol_rnd, val_rnd, wei_rnd = random_search_valid(times)
print('Best Solution after Random Search:')
print('Sol.:' , sol_rnd, 'V:', val_rnd, 'W:', wei_rnd)


# Multi hill climbing
hc_maxiter = 10 # set the maximun iterations for the hill-climebr 
b_trace, values_mhc, sol_mhc, val_mhc, wei_mhc = multi_hc(times, hc_maxiter)
print('Best Solution after Multi-start hill-climbing:')
print('Sol.:' , sol_mhc, 'V:', val_mhc, 'W:', wei_mhc)
plt.figure()
plt.plot(b_trace,'bo')  # 'ro' indicates to plot as dots (circles) blue color
plt.title('Best Trace ' + knapfile)
plt.ylabel('Value')
plt.show()

#  Comparing the performances of randon search against multiple hill-climbing
results = [values_rnd, values_mhc]  # combine solutions of two algorithms
plt.figure()
plt.boxplot(results,labels = ['random','hill-climbing'])
plt.title('Comparison ' + knapfile)
plt.ylabel('Value')
plt.show()