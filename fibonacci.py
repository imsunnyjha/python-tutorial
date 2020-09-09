#fibonacci series
#try again by myself

num=int(input('How many numbers?: '))

n1,n2=0,1
count=0
if num==1:
    print(n1)
else:
    while count<num:
        print(n1)
        next=n2+n1
        n1=n2
        n2=next                    
        count+=1

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

