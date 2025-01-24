Details = {}
def my_details():
  Details["Name"] = input("enter the name :")
  Details["Age"] = input("enter the age :")
  Details["Married"] = input("married YES or NO: ")

my_details()
for x, y in Details.items():
  print(f"{x}:{y}")