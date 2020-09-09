x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 


x = 5
print(type(x))

#Python does not have a random() function to make a random number, 
#but Python has a built-in module called random that can be used to make random numbers

import random

print(random.randrange(1, 10)) 

#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

#If you have only one statement to execute, you can put it on the same line as the if statement.
a=10
b=4
if a > b: print("a is greater than b")

#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B") 

#if statements cannot be empty, but if you for some reason have an if statement with no content, 
#put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass