#17.Create a file containing 10 numbers. Use readlines() to calculate their average.

file = open("file17.txt","w")
file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
file.close()

file = open("file17.txt","r")
lines = list(map(int,file.readlines()))
sum = 0
for num in lines:
    sum = sum + num

print(sum)
file.close()
