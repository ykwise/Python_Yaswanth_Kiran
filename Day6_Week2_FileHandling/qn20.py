# 20 Create a program that:
# Takes 5 student names from the user.
# Writes them to a file.
# Reads the file using a for loop.
# Prints each student with a serial number.

for i in range(5):
    name = input("Enter name: ")
    file = open("file20.txt","a")
    file.write(f"{name}\n")

file = open("file20.txt","r")
lines = file.readlines()
for i in range(len(lines)):
    print(f"{i+1} {lines[i]} ")
file.close()


