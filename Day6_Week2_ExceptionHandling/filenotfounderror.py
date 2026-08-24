try:
    total = int(open("scores.txt").read())
except FileNotFoundError:
    print("File is Missing.")
except ValueError:
    print("File is not a number.")
else:
    print(f"Total is {total}")
finally:
    print("Done checking")


try:
    total = int(open("scores.txt").read())
except FileNotFoundError:
    print("File is Missing")
except PermissionError:
    print("Permission is not authorized")

else:
    print(f"Total is {total}")
finally:
    print("Done checking")
