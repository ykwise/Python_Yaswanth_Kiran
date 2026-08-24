file = open("names.txt","w")
file.write("1.Yaswanth\n2.Abhi\n3.Jagadeesh\n4.Yogesh\n5.Venkat\n")
file.close()

file = open("names.txt","r")
lines = file.readlines()
for line in lines:
    print(line,end="")
file.close()

# file = open("names.txt", "w")

# file.write("1.Yaswanth\n2.Abhi\n3.Jagadeesh\n4.Yogesh\n5.Venkat\n")

# file.close()

# file = open("names.txt", "r")

# lines = file.readlines()

# for line in lines:
#     print(line, end="")

# file.close()