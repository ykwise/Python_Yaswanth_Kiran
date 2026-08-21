def find_fact(n):
    if(n == 0):
        return 1
    return n * find_fact(n-1)
n = int(input("Enter the num: "))
print(find_fact(n))