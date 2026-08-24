file = open("file_5th.txt","w")
file.write("Hi This\nis Yaswant\nfrom westgodavari\n")
file.close()

file = open("file_5th.txt","r")
line = file.readline()
print(line)

line = file.readline()
print(line)

line = file.readline()
print(line)
file.close()

