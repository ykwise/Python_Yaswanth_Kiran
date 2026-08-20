age = int(input("Enter person age: "))
has_id = bool(input("Enter id status: "))

if(age > 18 and has_id == "True"):
    print("Allowed")
else:
    print("Not allowed")