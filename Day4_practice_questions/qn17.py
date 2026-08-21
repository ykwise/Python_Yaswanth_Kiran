nums = [1,5,2,4,10,7]
first_large = nums[0]
second_large = nums[0]
for num in nums :
    if num > first_large:
        second_large = first_large
        first_large = num
    elif num > second_large and num != first_large:
        second_large = num
print(f"Second_largest {second_large}")

