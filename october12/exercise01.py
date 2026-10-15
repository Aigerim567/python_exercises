number = (input("Введите число: "))
try:
    number = int(number)
    print(number)
except ValueError:
    print("Это не число")

