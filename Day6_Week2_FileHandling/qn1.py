file = open("hello.txt","w")
lines = file.write("Hello Python\n")
file.close()

file = open("hello.txt","r")
content = file.read()
print(content)
file.close()
