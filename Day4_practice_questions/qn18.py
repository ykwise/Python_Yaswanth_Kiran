t1 = (1,2,3,4,5)
sum = 0
max = t1[0]
min = t1[0]
for i in t1:
    sum += i

    if(i > max):
        max = i
    if(i < min):
        min = i
print(f" Max {max}")
print(f" Min {min}")
print(f" Sum {sum}")