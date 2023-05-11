number = int(input("Введите число: "))
while number > 0:
    digit = number % 10
    print("|" + str(digit), end="")
    number = number//10

print("|")