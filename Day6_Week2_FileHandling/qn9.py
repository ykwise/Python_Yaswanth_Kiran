# 9.Read a file containing names and print only names whose length is greater than 5.

file = open("names.txt","r")
lines = file.readlines()
for i in range(len(lines)):
    if(len(lines[i]) > 5):
        print(lines[i])
file.close()
 