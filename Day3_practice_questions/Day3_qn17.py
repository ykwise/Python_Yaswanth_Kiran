numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sum = 0

for i in range(0,len(numbers)):
    for j in range(0,len(numbers[i])):
        sum+=numbers[i][j]
print(sum)