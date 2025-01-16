n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
opr=input("Enter the operator:")
if(opr=="+"):
    print("Result is :",n1+n2)
elif(opr=="-"):
    print("Result is :",n1-n2)
elif(opr=="*"):
    print("Result is :",n1*n2)
elif(opr=="/"):
    print("Result is:",n1/n2)
else:
    print("Invalid opertion")