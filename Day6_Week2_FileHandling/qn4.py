file = open("numbersum.txt","w")
file.write("1\n2\n3\n4\n5")
file.close()

file = open("numbersum.txt","r")
lines = file.readlines()
print(lines)
sum = 0
for num in lines:
    sum += int(num)
print(sum)