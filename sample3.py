#What is the number of non-negative integers with atmost four digits at least one of which is equal to 7
from itertools import product

count=0
for d in product(range(10),repeat=4):
    if 7 in d:
        count+=1
print(count)
print(10**4-9**4)
