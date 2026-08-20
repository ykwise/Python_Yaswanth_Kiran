n = input("Enter the String: ").lower()
words = n.split(" ")
first = words[0]
for word in words:
    if(word < first):
       first = word
print(first)