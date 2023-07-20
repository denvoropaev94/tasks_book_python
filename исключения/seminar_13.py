# d = {'42': 73}
# try:
#     key, val = input('Ключ и значение: ').split()
#     if d[key] == val:
#         r = 'Sovpadenie'
# except ValueError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# else:
#     print(r)
# finally:
#     print(d)
# class User:
#     def __init__(self, name, age):
#         if 6 < len(name) < 30:
#             self.name = name
#         else:
#             raise ValueError(f'Длина имени должна быть между 6 и 30 символами {len(name)}')
#         if not isinstance(age, (int,float)):
#             raise TypeError(f'Возраст должен быть числом {type(age) = }')
#         elif age < 0 :
#             raise ValueError(f'Возраст должен быть положительным {age = }')
#         else:
#             self.age = age

# user1 = User('Deniska', 29)
# user2 = User('Nikitka', 36)

def func(a, b, c):
    if a < b < c:
        raise ValueError('НЕ перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято')
    elif max(a, b, c) < 5:
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то пошло не так')


# func(11, 7, 3)
# func(3, 2, 3)
func(73, -40, 9)
# func(10, 20, 30)
