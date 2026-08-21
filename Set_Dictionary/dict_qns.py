#1st question
dict_1 = {
    "name" : "yaswanth",
    "age" : 21,
    "marks" : 50
}

for value in dict_1.values():
    print(value)


#2nd question
dict_2 = {"name": "Rahul", "age": 20}
dict_2["city"] = "Hyderabad"
print(dict_2)

#3rd question
dict_3 = {"name": "Rahul", "age": 20}
dict_3["age"] = 21
print(dict_3)

#4th question
dict_4 = {"name": "Rahul", "age": 20, "city": "Hyderabad"}
del(dict_4["city"])
print(dict_4)

#5th question
dict_5 =  {"name": "Rahul", "age": 20, "city": "Hyderabad"}
print("name" in dict_5)

#6th question
dict_6 = {"apple": 50, "banana": 30, "mango": 40}
for key in dict_6.keys():
    print(key)

#7th question
dict_7 = {"apple": 50, "banana": 30, "mango": 40}
for val in dict_6.values():
    print(val)

#8th question
dict_8 = {"apple": 50, "banana": 30, "mango": 40}
for item in dict_8.items():
    print(item)

#9th question
dict_9 = {"a": 10, "b": 20, "c": 30}
sum = 0
for val in dict_9.values():
    sum += val
print(sum)

#10th question
dict_10 = {"Yaswanth": 50, "abhii": 100, "Jaga": 30 , "Yogii" : 75 , "Venkat" : 80}
max = 0
high_name = ""
for name in dict_10.keys():
    if(dict_10[name] > max):
        max = dict_10[name]
        high_name = name
print(max)
print(high_name)





