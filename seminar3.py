# my_tuple = (11, 12.34, True, "HELLLO", 77, False, "Mine")
#
# my_dict = {}
#
# for i in my_tuple:
#     if type(i) not in my_dict:
#         my_dict[type(i)] = [i]
#     else:
#         my_dict[type(i)].append(i)
#
#
# print(my_dict)

# ---------------------------------------
# my_list = [2,4,5,6,2,8,9,9,9,9,13,245,123,123,0,10,0]

# print(my_list.count(9))
# for i in my_list:
#     if my_list.count(i) == 2:
#         my_list.remove(i)
#         my_list.remove(i)
#
# print(my_list)
# ---------------------------------------------------
# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.
# my_list = [21,4,5,6,2,8,9,9,9,9,13,245,123,123,0,10,0]
#
# new_list = []
# for i in range(len(my_list)):
#     if my_list[i] % 2 != 0:
#         new_list.append((my_list[i],i+1))
# print(new_list)

# -------------------------------------------------------
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
#
# text = input("Введите что-нибудь: ").lower().split(" ")
# text.sort()
# max_len = len(max(text, key=len))
#
# for i,el in enumerate(text,1):
#     print(f'{i:>2} {el:>{max_len}}')
# print(text)

# -------------------------------------------------------------
# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.
# text = input("Введите что-нибудь: ").lower().replace(" ","")
# my_dict = {}
#
# for i in set(text):
#     my_dict[i] = text.count(i)
# print(my_dict)

# 2 sposob
# text = input("Введите что-нибудь: ").lower().replace(" ","")
# my_dict = {}
#
# for el in text:
#     my_dict[el] = my_dict.get(el,0) + 1
#
# print(my_dict)
# -------------------------------------------------------------
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться на любое большее количество друзей.
# import random
#
#
# pack_items = ["палатка", "удочка", "фонарь", "аптечка",  "сидушка", "котелок", "спички", "гитара", "сухпаек",
#               "рация", "карта", "вода", "фильтр", "спальник", "коврик", "фляшка", "фотоаппарат"]
#
# names = ["Ден", "Никита", "Саша", "Катя", "Ира", "Настя", "Олег", "Дима", "Марк"]
#
#
# def find_items_everybody_has(input_dict):
#     items_everybody_has = set()
#     for value in input_dict.values():
#         items_everybody_has = items_everybody_has.union(value)
#     for value in input_dict.values():
#         items_everybody_has = items_everybody_has & set(value)
#     return items_everybody_has
#
#
# def find_unique_items(input_dict):
#     total_items = []
#     result_list_of_unique_items = []
#     for value in input_dict.values():
#         for j in range(len(value)):
#             total_items.append(value[j])
#     set_of_total_ites = set(total_items)
#     for item in set_of_total_ites:
#         if total_items.count(item) == 1:
#             result_list_of_unique_items.append(item)
#     return set(result_list_of_unique_items)
#
#
# def find_items_everybody_except_one_has(input_dict):
#     items_everybody_has = find_items_everybody_has(input_dict)
#     unique_items = find_unique_items(input_dict)
#     total_items = []
#     result_dict = {}
#     for value in input_dict.values():
#         for j in range(len(value)):
#             total_items.append(value[j])
#     result_list_of_items = set(total_items) - items_everybody_has - unique_items
#     for key, value in input_dict.items():
#         for item in result_list_of_items:
#             if item not in value:
#                 result_dict[key] = item
#     return result_dict
#
#
# def trip(number_of_people: int, number_of_items: int):
#     travel_dict = {}
#
#     while len(travel_dict) < number_of_people:
#         travel_dict[random.sample(names, k=1)[0]] = (random.sample(pack_items, k=number_of_items))
#     print(travel_dict)  # для проверки правильности решения
#
#     items_everybody_has = find_items_everybody_has(travel_dict)
#     if not items_everybody_has:
#         items_everybody_has = None
#     unique_items = find_unique_items(travel_dict)
#     if not unique_items:
#         unique_items = None
#     item_everybody_except_one_has = find_items_everybody_except_one_has(travel_dict)
#     if not item_everybody_except_one_has:
#         item_everybody_except_one_has = None
#
#     return items_everybody_has, unique_items, item_everybody_except_one_has
#
#
# print(trip(3, 3))

# --------------------------------------------------------------------------------
# # Дан список повторяющихся элементов. Вернуть список
# # с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# my_list = [11, 12.34, True, "HELLLO", 77, False, "Mine", False, 11, 12.34, "Mine", 34, 12, 11]
#
# def list_with_duplicate_elements(input_list):
#     result = []
#     for i in my_list:
#         if my_list.count(i) > 1:
#             result.append(i)
#     return set(result)
# # print(set(result))
# print(list_with_duplicate_elements(my_list))

# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов

# a = [1 ,3, 4, 5, 6, 4, 3, 4, 5, 3, 20, 7, 20, 7]
#
# print(set(a))


# def ununique(input_masive : list[int]):
#     set_b = set(a)
#     result_massive = []
#     for i in set_b:
#         if a.count(i) > 1:
#             result_massive.append(i)
#     return result_massive
#
# print(ununique(a))


#-----------------------------------------------------------
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
#
# text = 'Python - geek высокоуровневый язык программирования программ программ\
#  с динамической строгой типизацией и geek автоматическим управлением памятью,\
#   ориентированный на повышение производительности разработчика, Python кода и всё качества,\
#    а Python на обеспечение переносимости Синтаксис на Python программ py py py py. \
# Язык является полностью объектно-ориентированным gb том высокоуровневый, gb всё является объектами.\
# Синтаксис ядра языка кода, Синтаксис gb чего на практике разработчика возникает необходимость обращаться к документации.\
#  Сам же язык известен Синтаксис интерпретируемый и разработчика в том числе для написания скриптов.\
#   Синтаксис языка кода кода кода низкая Python работы и высокоуровневый высокое потребление высокоуровневый\
#    написанных на нём программ по Python geek Python кодом, разработчика на высокоуровневый языках, gb как разработчика или C++'


# lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')', '?', '_', '`'  ]   # и т.д.
# lst = []
#
# for word in text.lower().split():
#     if not word in lst_no:
#         _word = word
#         if word[-1] in lst_no:
#             _word = _word[:-1]
#         if word[0] in lst_no:
#             _word = _word[1:]
#         lst.append(_word)
#
# _dict = dict()
# for word in lst:
#     _dict[word] = _dict.get(word, 0) + 1
#
# # сортируем словарь посредством формирования списка (значение, ключ)
# _list = []
# for key, value in _dict.items():
#     _list.append((value, key))
#     _list.sort(reverse=True)
#
# # самое частое слово в этом тексте
# # print(f'самое частое слово в этом тексте -> `{_list[0][1]}`, использовалось `{_list[0][0]}` раз.')
# print(_list)



# def count_number_of_words(input_str: str, top:int):
#     symbols_to_delete = ".?,!<>@'\"%:()&^$;/\\|#~`,«»."
#     processed_text = input_str.lower()
#     for symbol in symbols_to_delete:
#         processed_text = processed_text.replace(f'{symbol}', '')
#     final_text = processed_text.split()
#     my_dict = dict()
#     for word in final_text:
#         my_dict[word] = my_dict.get(word, 0) + 1
#     my_list = []
#     for key, value in my_dict.items():
#         my_list.append((value, key))
#         my_list.sort(reverse=True)
#     return (my_list[:top])
#
#
# print(count_number_of_words(text, 10))


# ------------------------------------------------------
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# # вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#
# from itertools import chain, combinations
#
# items = {'Спальник': 5.0,
#          'Палатка': 10.0,
#          'Топор': 2.5,
#          'Еда': 7.0,
#          'Вода': 5.0,
#          'Бадминтон': 1.5,
#          'Радио': 3.0}
#
#
# def max_cargo(inventory: dict[str, float], capacity: int) -> list[list[str], float]:
#     backpack = [[], 0]
#     for item, weight in inventory.items():
#         if backpack[1] + weight <= capacity:
#             backpack[0].append(item)
#             backpack[1] += weight
#         else:
#             break
#     return backpack
#
#
# print(max_cargo(items, 30))

#
# def powerset(inventory: list[str]):
#     return chain.from_iterable(combinations(inventory, r) for r in range(len(inventory) + 1))
#
#
# def all_options(inventory: dict[str, float], capacity: int):
#     result = []
#     for cur_option in powerset(list(inventory)):
#         if cur_option:
#             weight = 0
#             for item in cur_option:
#                 weight += inventory.get(item)
#             if weight <= capacity and weight > capacity - min(inventory.values()):
#                 result.append((cur_option, weight))
#     return result
#
#
# for option in all_options(items, 30):
#     print(option)

# digits = set(input("введите число: "))
# print(digits)

# text1 = input("Первый текст - ")
# my_set1 = set(text1)
#
# text2 = input("Второй текст - ")
# my_set2 = set(text2)
#
# super_set = my_set1 & my_set2
#
# print("Буквы из первого текста: ", my_set1)
# print("Буквы из второго текста: ", my_set2)
# print("Общие буквы: ", super_set)