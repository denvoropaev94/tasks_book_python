# Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа.
# Предложите пользователю ввести название одной из этих стран и
# выведите индекс (то есть позицию в списке) этого элемента кортежа.
#
# my_tuple = ('Belarus', 'Russia', 'Spain', 'OAE', 'Italy')
# print(my_tuple)
# input_country = input("Введите название страны: ")
#
# print(my_tuple.index(input_country))

# ---------------------------------------------------
# Доработайте программу 069 так, чтобы она предлагала пользователю ввести число
# и выводила название страны, находящейся в заданной позиции.
# my_tuple = ('Belarus', 'Russia', 'Spain', 'OAE', 'Italy')
# print(my_tuple)
# input_number = int(input("Введите число: "))
# print(my_tuple[input_number])


# # --------------------------------------------------------
# Создайте список с названиями двух видов спорта.
# Предложите пользователю ввести свой любимый вид спорта и
# добавьте его в конец списка. Отсортируйте список и выведите его.
# sport_list = ['football', 'tennis']
# print(sport_list)
# number_one = input("Введите свой любимый вид спорта! ")
# sport_list.append(number_one)
# print(sorted(sport_list))


# ----------------------------------------------------------
# Создайте список с названиями шести школьных предметов.
# Спросите у пользователя, какие из этих предметов ему не нравятся.
# Удалите выбранные предметы из списка и выведите его повторно.
# school_sub = ['matem', 'rus', 'belrus', 'bio', 'chem', 'eng']
# print(school_sub)
# opros = input("Какие предметы тебе нетнравятся? ")
# school_sub.remove(opros)
# print(school_sub)

# -------------------------------------------------------------
# Предложите пользователю ввести названия четырех любимых блюд
# и сохраните их в словаре с числовыми индексами, начиная с 1.
# Выведите содержимое словаря с указанием индексов и элементов.
# Спросите пользователя, какой элемент он хочет исключить, и удалите его из списка.
# Отсортируйте оставшиеся данные и выведите содержимое словаря.

# food_dict = {}
# fav_food1 = input("Введите любимое блюдо: ")
# food_dict[1] = fav_food1
# fav_food2 = input("Введите любимое блюдо: ")
# food_dict[2] = fav_food2
# fav_food3 = input("Введите любимое блюдо: ")
# food_dict[3] = fav_food3
# fav_food4 = input("Введите любимое блюдо: ")
# food_dict[4] = fav_food4
# print(food_dict)
#
# input_remove = int(input("Какой элемент вы хотите исключить из списка? "))
# del food_dict[input_remove]
#
# print(sorted(food_dict.values()))

# ------------------------------------------------------------------
# Введите список из десяти цветов. Предложите пользователю ввести начальное число
# в диапазоне от 0 до 4 и конечное число в диапазоне от 5 до 9.
# Выведите список цветов из интервала, заданного начальным и конечным числом.
# colours = ["red", "blue", "green", "black", "white", "pink", "grey", "purple", "yellow", "brown"]
# start = int(input("Введите начальное число в диапозоне 0-4: "))
# end = int(input("Введите начальное число в диапозоне 5-9: "))
# print(colours[start:end+1])

# -----------------------------------------------------------------------
# Создайте список из четырех трехзначных чисел.
# Выведите содержимое списка, при этом каждый элемент должен выводиться на отдельной строке.
# Предложите пользователю ввести число из трех цифр.
# Если введенное число совпадает с одним из чисел в списке, выведите позицию этого числа;
# в противном случае выведите со- общение «That is not in the list».
# mu_spisok = [321, 989, 777, 121]
# for i in mu_spisok:
#     print(i)
# input_num = int(input("Введите число: "))
# if input_num in mu_spisok:
#     print(mu_spisok.index(input_num))
# else:
#     print("That is not in the list")

# --------------------------------------------------------------------------
# Предложите пользователю ввести имена трех людей, которых он хочет пригласить на вечеринку,
# и сохраните их в списке. После того как будут введены все три числа, спросите,
# хочет ли пользователь добавить еще одно имя. Если ответ будет положительным,
# предложите ему добавлять имена, пока не получите ответ «no».
# После ответа «no» выведите количество людей, приглашенных на вечеринку.

# name1 = input("Enter a name of somebody you want to invite to your party: ")
# name2 = input("Enter another name: ")
# name3 = input("Enter a third name: ")
# party = [name1, name2, name3]
# another = input("Do you want to invite another (y/n): ")
# while another == "y":
#     newname = party.append(input("Enter another name: "))
#     another = input("Do you want to invite another (y/n): ")
# print("You have ", len(party), " people coming to your party")


# ----------------------------------------------------------------------
# Измените программу , чтобы после ввода списка имен программа выводила полный список.
# Предложите пользователю ввести одно из имен в списке и выведите позицию имени в списке.
# Спросите, хочет ли пользователь, чтобы этот человек присутствовал на вечеринке. Если пользователь ответит «no»,
# удалите элемент из списка и снова выведите список.
# name1 = input("Enter a name of somebody you want to invite to your party: ")
# name2 = input("Enter another name: ")
# name3 = input("Enter a third name: ")
# party = [name1, name2, name3]
# another = input("Do you want to invite another (y/n): ")
# while another == "y":
#     newname = party.append(input("Enter another name: "))
#     another = input("Do you want to invite another (y/n): ")
# print("You have ", len(party), " people coming to your party")
# print(party)
# selection = input("Enter one of the names: ")
# print(selection, " is in position ", party.index(selection), " on the list ")
# stillcome = input("Do you still want them to come? (y/n): ")
# if stillcome == "n":
#     party.remove(selection)
# print(party)


# -------------------------------------------------------------------------------
# Создайте список с названиями четырех телевизионных передач и выведите их на отдельных строках.
# Предложите пользователю ввести название еще одной передачи и позицию,
# на которой она должна быть вставлена в список. Снова выведите список,
# в котором все пять передач находятся на новых позициях.

# tv = ["Task master", "Top Gear", "The Big Bang Theory", "How I met Your Mother"]
# for i in tv:
#     print(i)
# print()
# newtv = input("Enter another TV show: ")
# position = int(input("Enter a number between 0 and 3: "))
# tv.insert(position, newtv)
# for i in tv:
# print (i)


# -------------------------------------------------------------------------------
# Создайте пустой список с име- нем nums. Предложите поль- зователю последовательно вводить числа.
# После ввода каждого числа добавьте его в конец списка nums и вы- ведите список.
# После того как пользователь введет три числа, спросите, хочет ли он оставить последнее введенное число
# в списке. Если пользователь от- ветит «no», удалите последний элемент из списка. Выведите список.
# nums = []
# count = 0
# while count < 3:
#     num = int(input("Enter a number: "))
#     nums.append(num)
#     print(nums)
#     count = count + 1
# lastnum = input("Do you want the last number saved (y/n): ")
# if lastnum == "n":
#     nums.remove(num)
# print(nums)