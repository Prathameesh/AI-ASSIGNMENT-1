#5. To input two numbers and an operator from the user. Display the result calculatedbased on the operator entered.
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
op=input("Enter an operator(+,_,*) only")
if op=="+":
	print("The addition is",n1+n2)
elif op=="-":
	print("The subtraction is",n1-n2)
elif op=="*":
	print("The multiplication is",n1*n2)
else:
	print("You have entered wrong operator")

