import os 
file = input("Enter file name: ")

try:
    os.remove(file)
    print("file deleted succesfully")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission not given")
except Exception as e:
    print('An Unxepected error has occured')
finally:
    print("Done Checking")