#What is the number of non-negative integers with atmost 4 digits are increasing
from itertools import product

count=0
for d in product(range(10), repeat=4):
    if d[0]<d[1] and d[1]<d[2] and d[2]<d[3]:
        count+=1
        print(d)
print(count)