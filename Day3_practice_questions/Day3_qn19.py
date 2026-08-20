s = "Python is easy and Python is powerful"
words = s.split()
checked = []
count = 0
for word in words:
    if word == "Python":
        count+=1
print(count)


