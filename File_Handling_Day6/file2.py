import os
import sys
import datetime
import math
from datetime import datetime
import pathlib 
from pathlib import Path
from collections import Counter
import sqlite3


now = datetime.now()

print(math.sqrt(16))
print(math.ceil(5.1))
print(math.floor(5.9))
print(math.factorial(6))
print(now)

files = Path(".").glob("*.py")

for file in files:
    print(file)

print(sys.argv)

arr = [1,2,3,4,4,5,6]
print(Counter(arr))

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute(""" 
    Create Table IF NOT EXISTS Students(
    id Integer,
    name Text)
""")
connection.commit()
connection.close()
