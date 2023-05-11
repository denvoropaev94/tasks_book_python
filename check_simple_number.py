number = int(input("Введите число: "))

num = number//2

k = 2

while k <= num:
    if number % k == 0:
        print("Число не простое, а золотое)))")
        break
    else:
        k += 1
else:
    print("Это простое число")
print("Проверка завершена!!!")

