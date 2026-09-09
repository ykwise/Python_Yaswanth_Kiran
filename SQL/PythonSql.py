import psycopg2


conn = psycopg2.connect("postgresql://neondb_owner:npg_0xmUtpECrgL3@ep-plain-sky-a52q3u4w-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur = conn.cursor()

def create_table():
    cur.execute("""
        create table If not exists student(
            id     INTEGER PRIMARY KEY,
            name   Varchar(50),
            age    INTEGER

        );
        
""")
    print("Table Created Successfully")
    conn.commit()
    print()
    

def insert_values():
    insert_query = """
            insert into student(id,name,age) values(%s,%s,%s);
"""
    n = int(input("Enter the number of Records: "))
    for i in range(n):
        id = int(input("Enter the id: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        print()

        cur.execute(insert_query,(id,name,age))
        conn.commit()
        print("Data Inserted Succesfully")
    print()
        

def delete_student():
    id = int(input("Enter the id: "))
    delete_query = """ Delete from student where id = %s;"""
    cur.execute(delete_query,(id,))
    conn.commit()
    print("Data deleted Successfully")
    print()

def show_data():
    select_query = "select * from student;"
    cur.execute(select_query)
    for row in cur.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

    print()
    

  

def exit():
    print("Exiting..")
    return False

def display():
    print("1.Create Table\n2.Insert Values\n3.Delete Student\n4.Show Data\n5.Exit\n")


isRun = True



while(isRun):
    display()
    option = int(input("Enter the Option: "))
    if(option==1):
        create_table()
    elif(option == 2):
        insert_values()
    elif(option == 3):
        delete_student()
    elif(option == 4):
        show_data()
    elif(option==5):
       isRun = exit()
    else:
        print("Please Enter Valid Input")




