#12.Create a file and write numbers from 1 to 10, with each number on a separate line.
file = open("file12.txt","w")
file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")
file.close()

file = open("file12.txt","r")
lines = file.read()
print(lines)
file.close()