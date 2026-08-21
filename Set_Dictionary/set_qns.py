#1st Question
set_1 = {1,2,3,4,5}
set_1.add(6)
print(set_1)

#2nd question 
set_2 = {10, 20, 30, 40}
set_2.remove(30)
print(set_2)

#3rd question
set_3a = {1,2,3}
set_3b = {3,4,5}
set_union = set_3a.union(set_3b)
print(set_union)

#4th question
set_4a = {1, 2, 3, 4}
set_4b = {3, 4, 5, 6}
set_int = set_4a.intersection(set_4b)
print(set_int)

#5th question
set_5a =  {1, 2, 3, 4} 
set_5b = {3, 4, 5}
print(set_5a - set_5b)

#6th question
set_6a = {1, 2, 3}
set_6b = {2, 3, 4}
set_sd = set_6a ^ set_6b
print(set_sd)

#7th question
set_7 = {1,2,3,2,1}
set_7.remove(2)
print(set_7)

#8th question
set8a = {1,2,3,4,10}
set8b = {2,5,10,12,20}
set8c = set8a.intersection(set8b)
print(set8c)

#9th question
set9 = {1,2,3,4,10}
print(set9)
set9.clear()
print(set9)

#10th question
set_10 = {10, 20, 30, 40}
print(20 in set_10)
