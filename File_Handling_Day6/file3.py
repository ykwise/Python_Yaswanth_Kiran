# file = open("data.txt","r")
# content = file.readline()
# print(content)
# file.close()

# file = open("data.txt","w")
# file.write("Hello World\n")
# file.close()

# file = open("file4.py","r")
# lines = file.readlines()
# print(lines)
# file.close()

file = open("file4.py","w")
file.write("import datetime\nnow = datetime.datetime.now()\nprint(now)")
file.close()
file = open("file4.py","r")
lines = file.read()
print(lines)
file.close()

exec(lines)

