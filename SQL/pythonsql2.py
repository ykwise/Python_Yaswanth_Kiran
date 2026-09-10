import psycopg2
conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_0xmUtpECrgL3@ep-plain-sky-a52q3u4w-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS sep10 (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age FLOAT NOT NULL
    )
""")
conn.commit()
def valid_inp(entry):

    if len(entry) != 3:
        print("Enter ID, NAME and AGE")
        return None

    id = entry[0]
    name = entry[1]
    age = entry[2]

    try:
        id = int(id)
    except:
        print("ID should be an integer")
        return None

    if id <= 0:
        print("ID should be greater than 0")
        return None

    if name.isdigit():
        print("Name should not contain only numbers")
        return None

    try:
        if "." in age:
            years, months = age.split(".")
            years = int(years)
            months = int(months)

            if months > 12:
                print("Months should be below 13")
                return None

            age = years + months / 100
        else:
            age = float(age)

    except:
        print("Age should be a valid number")
        return None

    if age < 0:
        print("Age cannot be negative")
        return None

    return [id, name, age]

def check_user(ids):

    query = """
        SELECT id
        FROM students
        WHERE id IN (%s, %s, %s)
    """

    cur.execute(query, ids)

    result = cur.fetchall()

    if result:
        print("These IDs already exist:")

        for row in result:
            print(row[0])

        return False

    return True

def add_users(list1, list2, list3):

    query = """
        INSERT INTO sep10 (id, name, age)
        VALUES (%s, %s, %s)
    """

    cur.execute(query, list1)
    cur.execute(query, list2)
    cur.execute(query, list3)

    conn.commit()

    print("Users inserted successfully")


entry1 = input("Enter first student (ID NAME AGE): ").strip().split()
entry2 = input("Enter second student (ID NAME AGE): ").strip().split()
entry3 = input("Enter third student (ID NAME AGE): ").strip().split()


list1 = valid_inp(entry1)
list2 = valid_inp(entry2)
list3 = valid_inp(entry3)

if list1 and list2 and list3:

    print("list1 =", list1)
    print("list2 =", list2)
    print("list3 =", list3)

    ids = [list1[0], list2[0], list3[0]]

    if len(ids) != len(set(ids)):
        print("Duplicate IDs found")
    elif check_user(ids):
        try:
            add_users(list1, list2, list3)
        except psycopg2.Error as e:
            
            print(e)
else:
    print("Validation failed")
    print("No users were inserted")

cur.close()
conn.close()

