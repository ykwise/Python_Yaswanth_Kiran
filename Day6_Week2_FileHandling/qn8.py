#8.Read a file containing numbers and use a for loop to print only the even numbers.

file = open("numbersum.txt","r")
lines = file.readlines()

for i in range(len(lines)):
    if(int(lines[i])%2 == 0):
        print(lines[i])

file.close()