#19 Create a simple student record program that asks for name, age, and marks, writes them to student.txt, and then reads the file and displays the information.

isRunning = True;

while isRunning:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    file = open("student.txt","a")
    file.write(f"{name}\n{age}\n{marks}\n")
    isRunning = False

file = open("student.txt","r")
lines = file.read()
print(lines)
file.close()

    
