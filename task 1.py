#1.Input three numbers and print the largest of three numbers using if statement
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
larg=a
if b>larg:
	larg=b
if c>larg:
	larg=c
print("Largest of all is",larg)
	