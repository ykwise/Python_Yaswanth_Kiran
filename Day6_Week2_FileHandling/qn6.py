file = open("studentdetails.txt","r")

lines = file.readlines()

for i in range(len(lines)):
    line = file.readline()
    print(lines[i])
