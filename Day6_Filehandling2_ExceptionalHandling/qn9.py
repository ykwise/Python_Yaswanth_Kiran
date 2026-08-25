filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    print("File opened successfully")

    content = file.read()
    print(content)

    file.close()

except FileNotFoundError:
    print("File does not exist")

except Exception as e:
    print("An unexpected error occurred:", e)