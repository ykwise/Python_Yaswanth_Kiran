numbers = [1,2,3,2,4,1,5]
checked_list = []
count = 0


for num in numbers:
    if num not in checked_list:
        if(numbers.count(num) > 1):
            count+=1


        checked_list.append(num)
print(count)