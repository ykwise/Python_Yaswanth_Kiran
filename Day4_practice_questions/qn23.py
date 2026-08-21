students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
max = 0
high = ""
for name in students.keys():
    if(students[name] > max):
        max = students[name]
        high = name
print(f"name :{high} max: {max}")



