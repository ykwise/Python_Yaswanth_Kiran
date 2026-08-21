list_1 = [10, 20, 10, 30, 20, 40, 30]
list_2 = list(set(list_1))
print(list_2)

#2nd method
list_1 = [10, 20, 10, 30, 20, 40, 30]
res = []

for num in list_1:
    if num not in res:
        res.append(num)
print(res)

