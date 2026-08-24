file = open("studentdetails.txt","w")
file.write("name : yaswanth\nage : 21\ncourse : Python\n")
file.close()

file = open("studentdetails.txt","r")
content = file.read()
print(content)
file.close()