try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    result = n1 / n2

    print("Result:", result)

except ValueError:
    print("Please enter Integer")

except ZeroDivisionError:
    print("Cannot divide by zero.")