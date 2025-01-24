people =[
    {"name":"chinnu", "Age":30,"country":"India"},
    {"name":"anju","Age":25,"country":"germany"}
]
names = [person["name"] for person in people]
print(names)
upper_case = [person["name"].upper() for person in people]
print(upper_case)
Ages = [person["Age"] for person in people]
print(Ages)
