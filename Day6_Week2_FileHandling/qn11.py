#11.Create a file students.txt and write 5 student names into it using write().
file = open("file11.txt","w")
file.write("yaswanth\nuday\nashish\nmani\nsai\nhemanth\nabhi\nmounika\nAnkitha\n")
file.close()

file = open("file11.txt","r")
content = file.read()
print(content)
file.close()
