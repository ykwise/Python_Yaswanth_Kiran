
file = open("notes.txt", "w")
file.write("My name is Yaswanth\n")
file.close()


sentence = input("Enter a new sentence: ")


file = open("notes.txt", "a")
file.write(sentence + "\n")
file.close()


file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()