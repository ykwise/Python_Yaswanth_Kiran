numbers = [12,5,8,21,4,15,10]
max = numbers[0]
min = numbers[0]
sum=0
for i in range(0,len(numbers)-1):
    if(numbers[i] > max):
        max = numbers[i]
    if(numbers[i] < min):
        min = numbers[i]
    
    sum += numbers[i]
print("Max: ",max)
print("Min: ",min)
print("Sum: ",sum)