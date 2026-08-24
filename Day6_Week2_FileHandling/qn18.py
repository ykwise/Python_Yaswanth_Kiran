#18.Create a file containing several names. Read the file using a for loop and count how many names are present.

file = open("file11.txt","r")
lines = file.readlines()
count = 0
for word in lines:
    count +=1
print(count)
file.close()