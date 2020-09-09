#Opening a file
#Before we can read the conntents of the file we must tell python which file we are going to work with and what we will be doing with the file
#This is donne with open() function 
#open() returns a file handle - a variable used to perform operations on the file
#Similar to "File->Open" in a Word processor
#handle=open(filename,mode)
#returns a handle use to manipulate the file
#filename is a string
#mode is optional if we are planning to read the file'r' or write 'w'

#Counting lines in a file
#fhand=open('mbox.txt')
#count=0
#for line in fhand:
    #count=count+1
#print('Line count',count)

#Code1
#Write a program that prompts for a file name, then opens that file and reads through the file
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for i in fh:
    upper_fh=i.upper()
    print(upper_fh.rstrip())

#code2
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines 
#and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
average=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:    0.8475") : continue
    print(line)
    average=average+ float(line[20:-1].strip())
    count=count+1

print("Average spam confidence:",(average/count))

