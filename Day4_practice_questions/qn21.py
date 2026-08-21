nums = [10, 20, 10, 30, 20, 40, 30]

seen = set()
dup = set()
for num in nums:
    if num in seen:
        dup.add(num)
    else:
        seen.add(num)
print(dup)