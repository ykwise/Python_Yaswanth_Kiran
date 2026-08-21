def find_largest(nums):
    max = nums[0]

    for num in nums:
        if(num > max):
            max = num
        
    print(f"Max : {max}")

List_1 = [1,2,3,4,5,10,9,11,8]
find_largest(List_1)
    