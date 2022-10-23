print("What do you want to do?")
w = str(input(" add, \n subtract, \n multiply, \n divide : "))


if(w == "add"):
    i = float(input("What is the first number?"))
    j = float(input("What is the second number?"))
    k = i + j
    print("the addition is = ", k)
elif(w == "sub"):
    i = float(input("What is the first number?"))
    j = float(input("What is the second number?"))
    k = i - j
    print("The subtraction is = ", k)
elif(w == "mul"):
    i = float(input("What is the first number?"))
    j = float(input("What is the second number?"))
    k = i * j
    print("The multiplication is = ", k)
else:
    i = float(input("What is the first number?"))
    j = float(input("What is the second number?"))
    k = i / j 
    print("The division is = ", k)

