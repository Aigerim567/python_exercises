number = (input("Enter a number: "))
try:
    number = int(number)
    print(number)
except ValueError:
    print("Invalid input")

