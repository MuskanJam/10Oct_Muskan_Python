# Write python program that swap two number with temp variable and without temp variable.
#Temp variable.

# a=int(input("Enter any number of A:"))
# b=int(input("Enter any number of B:"))

# c=a
# a=b
# b=c
# print("A=",a)
# print("B=",b)

# Without using temp variable.
a=int(input("Enter any number of A:"))
b=int(input("Enter any number of B:"))

a,b=b,a
print("A=",a)
print("B=",b)