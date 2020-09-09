#functions
def double(x):
    "this funnctionn multiplies its aegument by two"
    return x*2
print(double(4),double(1.2),double('abc'))
#The double function takes only one parameter. 
#Notice the docstring on the second line.
#It documents the purpose and usage of the function. 
#Let’s try to access it.

print('The docstring is:',double.__doc__)
help(double)

#help(print)

def sum_of_squares(a,b):
    "Computes the sum of argumnents squared"
    return a**2 +b**2
print(sum_of_squares(3,4))
 #It would be nice that the number of arguments could be arbitrary, not just two. 
 #We could pass a list to the function as a parameter.
def sum_of_squares(lst):
    "Computes the sum of squares"
    s=0
    for x in lst:
        s+=x**2
    return s
print(sum_of_squares([-2]))
print(sum_of_squares([-2,3,4]))

#tryinng with tuples
def sum_of_squares(*t):
    "computes sum of squares in tuples"
    s=0
    for x in t:
        s+=x**2
    return s
print(sum_of_squares((-2)))
print(sum_of_squares(-2,4,5))
#The strange looking argument notation (the star) is called argument packing.
#It packs all the given positional arguments into a tuple t. 
#We will encounter tuples again later, but it suffices now to say that tuples are immutable lists.
#With the for loop we can iterate through all the elements in the tuple.
def length(*t,degree=2):
    s=0
    for x in t:
        s+=abs(x)**degree
    return s**(1/degree)
print(length(-4,3))
print(length(-4,3,degree=3))

