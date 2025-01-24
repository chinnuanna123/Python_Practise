import pandas as pd # importing panda
#df = pd.read_csv(r"C:\Users\Dell\Desktop\n2\details.csv") # reading csv file from another location into df
#print(df.to_string()) # printing the data full
#print(df.tail(1)) # printing the last row of data
#print(df.head(1)) # printing the first row
#print(df.describe()) # describe about the rank
#print(df["Name"]) # Accessing the colomn
#df["Mark"] = ["100","97","90","80"] #Adding new column to the Sheet
#print(df)
#mydataset = {  "cars": ["BMW", "Volvo", "Ford"], # creating data using dictionaries
#  "colors": ["black", "Red", "White"]
#}
#df = pd.DataFrame(mydataset) # load data into a DataFrame object
#print(df)
#a = [1, 7, 2]
#b = pd.Series(a)
#print(b)
# cleaning 
#new_df = df.dropna() # dropna() method to drop empty cells
#print(new_df)
#Use Pandas to load and analyze a dataset (e.g., sum, mean, median)
#Use Pandas to filter, group, and sort data in a DataFrame
#dataset = {
#    "name":["Chinnu","Anna","Kurian","Jis","Akhila"],
#    "Salary":[25000,45000,50000,55000,60000],
#  "Department":["HR","Sales","Engineering","Engineering","Sales"]
#}
#df = pd.DataFrame(dataset)
#print(df)
#total_salary = df["Salary"].sum()
#print(total_salary)
#median_salary = df["Salary"].median()
#print(median_salary)
#mean_salary = df.groupby("Department")["Salary"].mean()
#print("Average salary by department :", mean_salary)
#high_salary = df[df["Salary"]>55000]
#print("Employee with highest salary:", high_salary)

#import numpy as np
#a = np.array([1, 2, 3, 4, 5])
#print(a)
#print(a[0]) # accessing array of elements
#print(a[1]+a[2])
#a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#print(a)
#print(a[0, 1, 2])
#a = np.array(42)
#b = np.array([1, 2, 3, 4, 5])
#c = np.array([[1, 2, 3], [4, 5, 6]])
#d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)
#Perform matrix operations using NumPy (e.g., addition, multiplication)
#A = np.array([[1,2],[3,4]])
#B = np.array([[5,6],[7,8]])
#print("\nThe matrix A:",A)
#print("\nThe matrix B:",B)
#print(f"\nThe sum of two matrices : {A+B}")
#print(f"\n The Multiplication of two arrays: {A*B}")




