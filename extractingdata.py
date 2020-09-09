#matching and extracting data
#re.search() returns a true/false depending on whether the string matches the reg ex
#re.findall()
#[0-9]+ will return one or more digits

import re
x='My 2 favorite numbers are 19 and 11'
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)      #No uppercase vowels present
print(y)

#Greedy Matching
x='From: using the : character'
y= re.findall('^F.+:',x)        #Will return till the last colon
print(y)

#Non-Greedy Matching
x='From: using the : character'
y=re.findall('^F.+?:',x)
print(y)

#Fine-Tuning String Extraction 
y=re.findall('\S+@\S+',x)
print(y)

