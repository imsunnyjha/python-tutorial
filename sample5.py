#We have an unlimited supply of tomatoes, bell peppers and lettuce. We want to make a salad out of 4 units among these three ingredients (we do not have to use all ingredients). The order in which we use the ingredients does not matter. How many different salads we can make? 
from itertools import combinations_with_replacement
count=0
for c in combinations_with_replacement("TBL", 4):
    count+=1
print(count)

#for 4 ingredients and 7 items

counti=0
for c in combinations_with_replacement("TBLE", 7):
    counti+=1
print(counti)

