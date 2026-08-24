#13 Take 5 names from the user using input() and write them into a file.
for i in range(5):
    n = input("enter value:")
    file = open("file13.txt","a")
    file.write(f"{n}\n")

file = open("file13.txt","r")
lines = file.read()
print(lines)
file.close()
