
# Create a file containing:
# Rahul 80
# Aman 35
# Priya 92
# Neha 45
# Read the file and print only students who scored 50 or above.

file = open("file15.txt","w")
file.write("Rahul 80\nAman 35\nPriya 92\nNeha 45\n")
file.close()

file = open("file15.txt","r")
lines = file.readlines()

for line in lines:
    names,marks = line.split()

    if(int(marks) > 50):
        print(names,marks)
file.close()