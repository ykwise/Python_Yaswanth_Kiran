def checkPalindrome(s):
    rev = ""
    for i in range (len(s)-1,-1,-1):
        rev += s[i]
    if(rev == s):
        return True
    else:
        return False
s = input("Enter String: ").lower()
print(checkPalindrome(s))