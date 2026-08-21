def checkLongestWord(s):
    words = s.split()
    longest = words[0]
    for word in words:
        if(len(word) > len(longest)):
            longest = word
    return longest
s = input("Enter the String: ")
print(checkLongestWord(s))