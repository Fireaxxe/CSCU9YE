import random as rnd
import matplotlib.pyplot as plt


def test_function(a, b):
    val_sum = a+b
    val_dif = a-b
    return val_sum, val_dif

#call the test function
val1, val2 = test_function(45, 20)

print ("Sum:", val1)
print ("Diff:", val2)


def ages_function(asize):
    ages = []
    sum_ages = 0
    for i in range(asize):
        ages.append(rnd.randint(1,120))
        sum_ages = sum_ages + ages[i]
    return ages, sum_ages/asize
    
    
ages, avg = ages_function(50)
avg2 = sum(ages)/50

print("Ages:", ages)
print("Average of Ages:", avg)


plt.figure()
plt.plot(ages)
plt.show()
 
plt.figure()
plt.boxplot(ages)
plt.show()


