s = input("Enter String: ").lower()

vCount = 0
cCount = 0
dCount = 0

for i in range(0, len(s)):
    if s[i].isalpha():

        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            vCount += 1
        else:
            cCount += 1

    if s[i].isdigit():
        dCount += 1

print("Vowels:", vCount)
print("Consonants:", cCount)
print("Digits:", dCount)