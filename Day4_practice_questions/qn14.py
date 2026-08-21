nums = [1,5,2,4,10,7]
max = nums[0]
min = nums[0]
for num in nums:
    if(num > max):
        max = num
    if(num < min):
        min = num
print(f"Max : {max}")
print(f"Min: {min}")