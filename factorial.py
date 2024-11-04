def recursion_factorial(n):
    if n==1 :
        return n
    else:
        return n*recursion_factorial(n-1)

number = int(input("enter the number "))
if number <0 :
    print("sorry factorial doesnt exist for negative numbers")
elif number==0: 
    print("factorial of 0 is 1")
else:
    print("factorial of ", number, "is", recursion_factorial(number))