students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
sum = 0
for marks in students.values():
    sum += marks
avg = sum/len(students)
print(f"Average: {avg}")