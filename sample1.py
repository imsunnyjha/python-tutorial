count=0
for a in range(1,1001):
    if (a%2==0) | (a%3==0):
        count+=1
print(count)

counti=0
for a in range(1,1001):
    if (a%2!=0) & (a%3!=0):
        counti+=1
print(counti)
#Here is the code printing all 3-permutations of letters a, b, c, d, e, f. 
#Run the code and observe the result for better understanding of permutations.
from itertools import permutations
for p in permutations("abcdef", 3):
    print("".join(p))