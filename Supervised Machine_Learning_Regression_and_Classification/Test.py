import numpy as np
import math

my_list = np.array([1,2,3,4,5])
mylist = np.arange(5)

a = 10

for i in range(5):
    ((-mylist[i]) * math.log(1/2)) - ((1 - mylist[i]) * math.log(1 - 1/2))