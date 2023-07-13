# class Alpha:
#     def __getattribute__(self, item):
#         print("Alpha: запрос поля", item)
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         print("Нет такого поля!!!")
#         return "Alpha: " + item
#
#
# class Bravo:
#
#     def __getattribute__(self, item):
#         print("Bravo: запрос поля ", item)
#         try:
#             res = object.__getattribute__(self, item)
#         except AttributeError:
#             res = "Bravo: нет поля " + item
#         return res
#
#
# # Создание обьектов и обращение к полям
# print("Обьект A class Alpha")
# A = Alpha()
# A.value = 777
# print("Поле value: ", A.value)
# print("Еще раз:", object.__getattribute__(A, "value"))
# A.value = 333
# print("Поле value: ", A.value)
# print(A.color)
# print("Обьект B class Bravo")
# B = Bravo()
# B.mylist = [1, 2, 3]
# print("Поле mylist: ", B.mylist)
# print("Еще раз:", object.__getattribute__(B, "mylist"))
# B.mylist = ["a", "b", "c"]
# print("Поле mylist: ", B.mylist)
# print(B.myset)
# ------------------------------------------------------------
# Обращение к несуществующим атрибутам
class Alpha:
    def __getattr__(self, item):
        return len(item)


class Bravo:

    def show(self, x):
        print("Метод show():", x)

    def __getattr__(self, item):
        if len(item) < 5:
            return lambda x: print("Первый метод:", x)
        else:
            return lambda x: print("Второй метод:", x * x)

print("Объект А класса Alpha")
A = Alpha()
A.value = "Alpha"
print("Поле value:", A.value)
print("Поле color:", A.color)
print("Поле myattr:", A.myattr)
print("Объект B класса Bravo")
B = Bravo()
B.show(10)
B.hi(10)
B.display(10)
