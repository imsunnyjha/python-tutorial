#strings

a='first'
b='second'
print(a+b)
print(" ".join([a,b,b,a]))

#interpolation of strings
print("%i plus %i is equal to %i" % (1,3,4))    #format synatx
print("{} plus {} is equal to {}".format(1,3,4))    #format method
print(f"{1} plus {3} is equal to {4}")      #f-string

#specifier s is used for strings
print('%s concatenated with %s produces %s' %('water','melon','water'+'melon'))
