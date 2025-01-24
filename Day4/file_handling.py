#f1 = open("file1.txt","x")#creating file file1.txt
#f1 = open("file1.txt","r")# opening file in read mode.if we open a file in read mode which is not existing ,it will show an error
#data = f1.read()
#print(data)
# output is "Hi Welcome to File handling in python"
#f1 = open("file2.txt","w")#opening file2(which doesn't exists) in write mode will not through an error like read mode
#f1 = open("file1.txt","w")# the write mode will overwrite the existing file or create a new file
#f1.write("Welcome To Python")
#f1 = open("file3.txt","r+") #shows error as file3.txt doesn't exists
#f1 = open("file2.txt","r+")# in r+ mode we can read and write the file
#f1.write("Good Moring")
#print(f1.tell()) # tells about the position of file handler
#print(f1.read())
#print(f1.tell())
#f1.write("hi")
#print(f1.read())
#print(f1.tell())
#f1.close()
# output
#0
#Good MorningGodd Morninghi
#24
#26
#f1 = open("file2.txt","w+") #opening file in W+ mode
#print(f1.tell())
#f1.write("Hi team")
#print(f1.tell())
#f1.write("Good Morning")
#print(f1.tell())
#f1.seek(0) # to move the file pointer to the begining position
#print(f1.read())
#f1.close()
#output
#0
#7
#19
#hi teamGood Morning
#f1=open("file1.txt","a")# append mode read operation wont support
#f1.write("File handling")
#f1.close()
#f1=open("file1.txt","a+")# "a+" read operation supports
#print(f1.tell())
#f1.write("Hello")
#f1.seek(0)
#print(f1.read())
#f1.close()
#output
#42
#Welcome To Python
#File handlingHello
#Write a program to read a file and count word occurrences
#f1 = open("file2.txt","r+")
#data = f1.read()
#print(f1.tell())
#list = data.split()
#count = len(list)
#print("The total number of words present in the file :",count)

#f1.close()   
# output
#20
#The total number of words present in the file : 4
# Write a user’s input to a file and then read it back
#f1 = open("file1.txt","w+")
#data = input("enter the userinput: ")
#f1.write(data)
#f1.seek(0)
#print(f1.read())
#f1.close()
#Write a script to modify the content of an existing file
#f1 = open("file2.txt","a+")
#print(f1.tell())
#user_input = input("Enter the text to modify the existing file:")
#f1.write(user_input)
#f1.seek(0)
#print("The file after modification: ", f1.read())
#f1.close()
#context managers
#with open("file2.txt","r") as f1:
#    print(f1.read())
#print(f1.closed)    #file is closed automatically 







