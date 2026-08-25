file = open("info.txt", "w")
file.write("Hey Hi I AM Yaswanth\n")
file.close()

new  = input("Enter a sentence: ")

file = open("info.txt", "w")
file.write(new + "\n")
file.close()

file = open("info.txt", "r")
content = file.read()

print(content)

file.close()