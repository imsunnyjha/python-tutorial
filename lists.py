#A list is a kind of collection.
#A collection allows us to put many values in a single "variable"
#Ex: friends=['Joseph','Glenn','Riya']
friends=['sunny','bunny','munnny']
print(friends[1])

#Lists are mutable i.e. we can change an element of list using index operator
#Strings are immutable i.e. we cannot change contents of string, we have to make a new string to make any change
x=list()
type(x)
dir(x)

#Building a list from scratch 

stuff=list()
stuff.append('book')
stuff.append(23)
print(stuff)
stuff.append('cookie')
print(stuff)

#A list can hold many items and keeps those items in the order until we do something to change the order
#A list can be sorted i.e change its order
#The sort method unlike in strings means sort yourself

friends=['kiki','do','u','love me']
friends.sort()
print(friends)
print(friends[1])

#code
numlist=list()
while True:
    inp=input('Enter value:')
    if inp == 'done' : break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print(average)

#code
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)