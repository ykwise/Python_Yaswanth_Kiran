# filename = input("Enter the filename: ")

# try:
#     file = open(filename, "r")
#     print("File exists.")
#     file.close()

# except FileNotFoundError:
#     print("File does not exist.")

# except PermissionError:
#     print("Permission denied. You cannot access this file.")

# except Exception as e:
#     print("An unexpected error occurred:", e)


filename = input("enter filename: ")

try:
    file = open(filename,"r")
    print("file exists")
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("Permission Not Given")
except Exception as e:
    print("An unexpected error occured",e)
finally:
    print("Done Checking")