entriesList = list(map(int,input("Enter the Values: ").split()))
class EmptylogError(Exception):
    pass

def show_logs(entries):
    if not  entries:
        raise EmptylogError("No logs Found")
    else:
        for entry in entries:
            print(entry)

try:
    show_logs(entriesList)
except EmptylogError as e:
    print(f"Error: {e}")
