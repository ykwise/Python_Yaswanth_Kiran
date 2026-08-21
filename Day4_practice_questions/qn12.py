def checkPrime(n):
    count = 0
    for i in range(1,n+1):
        if(n % i == 0):
            count+=1
    if(count==2):
        return "Prime"
    else:
        return "Not Prime"
n = int(input("Enter the num: " ))
print(checkPrime(n))

