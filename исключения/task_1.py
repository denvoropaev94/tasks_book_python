while True:
    res = input("Введите натуральное число!")
    try:
        num = int(res)
        if num < 1:
            msg = 'Число должно быть натуральным!'
            raise ArithmeticError(msg)
    except ArithmeticError as e:
        print(e)
    except:
        print("Ошибка ввода")
    else:
        break

print("Сумма от 1 до", num, "=", sum(range(num + 1)))
