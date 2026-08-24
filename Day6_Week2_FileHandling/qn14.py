for i in range(5):
    n = int(input("Enter the num: "))
    file = open("file14.txt","a")
    file.write(f"{n}\n")

file = open("file14.txt","r")
lines = file.read()
print(lines)
file.close()