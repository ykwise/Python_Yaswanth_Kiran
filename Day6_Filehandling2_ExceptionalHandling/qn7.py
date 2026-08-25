try:
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    print(f"Sum: {n+m}")
except ValueError:
    print("Please enter Valid input(integer type)")

