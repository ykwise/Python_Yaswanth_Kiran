try:
    height = int(input("Enter the height in meters: "))
    weight = int(input("Enter the weight in Kgs: "))
    BMI = weight/(height ** 2)
except ZeroDivisionError:
    print("Please Provide height greater than Zero")
except ValueError:
    print("Please Provide Valid input ")
else:
    print(f"BMI is {BMI}")
finally:
    print("Done checking")