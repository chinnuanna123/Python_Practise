n = int(input("enter a number to find the factorial:"))
fact = 1
for i in range(1,n + 1):
    fact*=i
print(f"The factorial of a given number is: {fact}")
