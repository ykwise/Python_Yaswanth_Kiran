def find_sum(n):
    if(n == 0):
        return 0
    return n + find_sum(n-1)
n = int(input("Enter the num: "))
print(find_sum(n))