#for strings + means concatenate
#reading and converting 
#We prefer to read data usinng strings and then parse and convert the data as we need
name=input('Enter:')
print(name)
apple=input('Enter:')
x=int(apple)-10
print(x)
#lookinng inside strings
#We can get at any single character in a string using an index specified in square brackets
#banana
#012345 - index operator
fruit='banana'
letter=fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)

#len function

fruit='banana'
x=len(fruit)
print(x)                    #output=6


#looping through strings
fruit='banana'
for letter in fruit:
    print(letter)


#slicing strings
s='Monty Python'
print(s[1:4])
print(s[6:7])
print(s[6:20])

#somethinng weird
stuff='Hello World'
type(stuff)
dir(stuff)