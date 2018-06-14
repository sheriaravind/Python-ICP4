import numpy as np
no=np.random.randint(0,1000,(10,10)) # Creating the array of 10*10 size with random number using random.randint method
print(no)
min,max = no.min(axis=1),no.max(axis=1) # Finding the minimum and maximum in each row using min and max methods
print("Minimum elements of 10 size Array is",min)
print("Maximum elements of 10 size Array is",max)