#conditional execution

x=5
if x<10:
    print('Smaller')                                                                        
if x>20:
    print('Bigger')

print('Finis')

x=7
if x==5:
    print('Equals 5')
if x>4:
    print('Greater than 4')
if x>=5:
    print('Greater than or equals 5')
if x!=6:
    print('Not equal 6')
#indenting is syntax in python

x=8
print('Before 8')
if x==8:
    print('Is 8')
    print('Is Still 8')
    print('third 8')
print('Afterwards 8')
print('Before 9')
if x==9:
    print('Is 9')
    print('Is still 9')
    print('Third 9')
print('Afterwards 9')

#more conditional
x=5
if x<2:
    print('small')
elif x<10:
    print('Medium')
else:
    print('Large')
print('All Done')

#try-except structure
astr='hello'
try:
    istr=int(astr)  #cannot convert str to int so will go to except block and will continue the code from except
except:
    istr=-1
print('First',istr)
#sample
x=0
if x<2:
    print('Small')
elif x<10:
    print('Medium')
else:
    print('Large')
print('All Done')
#sample code
astr='Hello world'
istr=0
try:
    istr=int(astr)
except:
    istr=-1
print(istr)
#test code
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly. 

hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)

#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

score = input("Enter Score: ")
sg=float(score)
if sg>=0.0 and sg<=1.0:     #in python && operator is a syntax error so use instead 'and' operator in the same context
    if sg>=0.9:
        print('A')
    elif sg>=0.8:
        print('B')
    elif sg>=0.7:
        print('C')
    elif sg>=0.6:
        print('D')
    elif sg<0.6:
        print('F')
else:
    print('ERROR!!!')


