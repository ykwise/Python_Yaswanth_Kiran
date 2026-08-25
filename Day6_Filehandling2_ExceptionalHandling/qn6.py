filename = input("Enter filename: ")

try:
    file = open(filename,"x")
    print("File Created Succesfully")
except FileExistsError:
    print("File already exists")
finally:
    print("Done!!!")


