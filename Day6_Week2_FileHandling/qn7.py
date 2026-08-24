file = open("file_5th.txt","r")
lines = file.readlines()
for i in range(len(lines)):
    print(lines[i])
file.close()