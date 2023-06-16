# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

# first_var = 1
# senods = 2
# trird = "Hello"
# fourths = 45.12
# s = 0
#
# for item in globals().copy():
#     if not item.startswith('__'):
#         if item.endswith('s'):
#             if len(item) > 1:
#                 new_name = item[:-1]
#                 globals()[new_name] = None
#         else:
#             globals()[item] = globals().get(item)
# print(globals())


# -----------------------------------------------------
# Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
# dictionary_companies = {'Apple': [123, 800, -900],
#                         'Voga': [10000, 12312, 454645, 58857867, 2452426, -12432543],
#                         'RealMadrid': [500000, 32352350, 54534534, -13253],
#                         'Barsa': [-124314, 4325234, -1343254356346]
#                         }
#
#
# def profit_of_companies(dict_companies):
#     for key, value in dict_companies.items():
#         if sum(value) < 0:
#             return False
#     return True
#
#
# print(profit_of_companies(dictionary_companies))

# --------------------------------------------------
#
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

# my_list = [10, 1, 37, 700, -800, 0, -100, 200]
#
# def sum_between_numbers(input_list, start, end):
#     if start < 0:
#         start = 0
#         return sum(input_list[start:end])
#     # quit()
#     if start > len(input_list):
#         return None
#     return sum(input_list[start+1:end])
#
#
# print(sum_between_numbers(my_list, 3, 21))

# ----------------------------------------------------
# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# def summa_with_premiya(str_list: list[str], int_list: list[int], str2_list: list[str]):
#     dictionary_peoples = {}
#     for index, name in enumerate(str_list):
#         dictionary_peoples[name] = int_list[index] * (float(str2_list[index][0:-1]) + 100) / 100
#     return dictionary_peoples
#
# names = ['Den', 'Nik', 'Oleg', 'Sasha', 'Gleb']
# stavka = [10000, 5000, 5000, 1000, 100]
# procent = ["20.25%", "10.25%", "10.25%", "1.25%", "5.25%"]
# print(summa_with_premiya(names, stavka, procent))


# ----------------------------------------------------
# Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


# my_list = [10, 1, 37, 700, -800, 0, -100, 200]
# print(my_list)
#
# def my_sort(input_list):
#     for i in range(len(input_list)):
#         for j in range(len(input_list) - 1 - i):
#             if input_list[j] > input_list[j + 1]:
#                 input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
#
# my_sort(my_list)
# print(my_list)

# --------------------------------------
# Напишите функцию для транспонирования матрицы
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpon_matrix = [[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
# print(matrix)
# print(transpon_matrix)

# 2 cпособ
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# zip_rows = zip(*matrix)
# transpose_matrix = [list(row) for row in zip_rows]
# print(transpose_matrix)
# ----------------------------------------------------------------

# Напишите функцию
# принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# def flatten_dict(d):
#     new_dict = []
#     keyz = [i for i in d.keys()]
#     valuez = [i for i in d.values()]

# def dict_key_parameters(**kwargs):
#     new_dict = {}
#     for key, value in kwargs.items():
#         new_dict[value] = key
#     return new_dict
#
# print(dict_key_parameters(den=10, nik=9, oleg=5))
