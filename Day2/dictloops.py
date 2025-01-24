fruits = {}
fruits["Apple"] = input("enter the color:")
fruits["Orange"] = input("enter the color:")
fruits["Banana"] = input("enter the color:")
print(dict(fruits))
for key,value in fruits.items():
    print(f"{key}:{value}")
    