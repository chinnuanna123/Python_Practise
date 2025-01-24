def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
#a = int(input("Enter the number to find its facrorial: "))
output = factorial(5)    
print(f"The factorial is : {output}")
