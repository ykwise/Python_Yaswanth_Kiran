file = open("students.txt", "w")
file.write("Rahul\n")
file.write("Priya\n")
file.write("Arjun\n")
file.close()


name1 = input("Enter name1: ")
name2 = input("Enter  name2: ")

file = open("students.txt", "a")
file.write(name1 + "\n")
file.write(name2 + "\n")
file.close()


file = open("students.txt", "r")
content = file.read()


print(content)

file.close()