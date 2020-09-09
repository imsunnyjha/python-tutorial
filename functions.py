#store and reuse
def thing():                    #function is defined using def keyword
    print('Hello')
    print('Fun')
thing()                         #calling the function, will run thing
print('ZIP')                    
thing()                         #calls again

#max and min function
big=max('Hello world')
print(big)
tiny=min('Hello world')         #space has smallest numeric value so after printing tiny it will be  a balnk space
print(tiny)

#building function

#we create a new function usinng def keyword followed by optional parameters in parantheses
def print_lyrics():
    print("I'm a lumberjack and I am okay")
    print("I sleep all night and work all day")
#def statement doesn't runs the code but only defines it
print_lyrics()                   #function is invoked here and now will run the code which was defined earlier

#parameters
#A parameter is a variable which we use in the function definition

def great(lang):
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
great('es')
great('fr')
great('kk')

#return values
#Often a function will take its arguments do some computation and return a value to be used as the value of the funnction call in the callinng expression

def greet():
    return 'Hello'
print(greet(),"Sunny")
print(greet(),"Simran")

#multiple parameters

def addtwo(a,b):
    added=a+b
    return added
x=addtwo(88,9)
print(x)

#sample code
def func(x):
    print(x)
func(10)
func(20)

#sample code
def stat():
    print('hello')
    return
    print('world')
stat()

#sample code
def addnew(a,b):
    ans=a+b
    return a
x=addnew(2,8)
print(x)

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function. 

def computepay(h,r):
    if h<=40:
       p= h*r
    elif h>40:
       p=40*r + (h-40)*1.5*r
    return p

hrs = input("Enter Hours:")
h=float(hrs)
rph = input("Enter rate per hour:")
r=float(rph)
p = computepay(h,r)
print("Pay",p)



