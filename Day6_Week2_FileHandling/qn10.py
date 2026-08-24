#10. Read a file containing numbers and find the largest and smallest number using a for loop.

file = open("numbersum.txt","r")
lines = list(map(int,file.readlines()))
print(lines)
max = lines[0]
min = lines[0]

for num in lines:
    if(num > max):
        max = num
    if(num < min):
        min = num
print(f"max: {max}")
print(f"min: {min}")

file.close()
