numbers = [10,25,30,45,50,75,90,100]
res = []
for num in numbers:
    if((num>30 and num % 5 == 0) and num != 75 ):
        res.append(num)
print(res)