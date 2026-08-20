str= input("Enter the String: ").lower()
words = str.split(" ")
first = words[0]
for word in words:
    if(word < first):
        first = word
print(first)