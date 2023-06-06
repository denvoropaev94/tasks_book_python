#Напишите программу с функцией, которая создает вложенный список. Размеры списка
# указываются аргументами функции. Список заполняется случайными буквами.

# import random
#
#
# def symbs(m, n):
#     var = [chr(k) for k in range(ord('a'), ord('z') + 1)]
#     res = [['' for i in range(n)] for j in range(m)]
#     for i in range(m):
#         for j in range(n):
#             val1 = random.choice(var)
#             res[i][j] = val1
#     return res
#
#
# c = symbs(3, 2)
# print(c)

###############################################
# Напишите программу, в которой есть функция для заполнения вложенного списка. Список
# заполняется натуральными числами «змейкой»: сначала заполняется первая строка, затем
# последний столбец (сверху вниз), последняя строка (справа налево), первый столбец (снизу
# вверх), вторая строка (слева направо), и так далее.
# n - размерность матрицы n x n
# b - результирующая матрица
# st - текущее значение-счетчик для записи в матрицу
# m - коеффициент, используемый для заполнения верхней
# матрицы последующих витков, т.к. одномерные матрицы
# следующих витков имеют меньше значений
#
# n = int(input("Размерность матрицы: "))
#
# b = [[0]*n for i in range(n)]
# st, m = 1, 0
# # Заранее присваиваю значение центральному элементу
# # матрицы
# b[n//2][n//2]=n*n
# for v in range(n//2):
#     #Заполнение верхней горизонтальной матрицы
#     for i in range(n-m):
#         b[v][i+v] = st
#         st+=1
#
#     #Заполнение правой вертикальной матрицы
#     for i in range(v+1, n-v):
#         b[i][-v-1] = st
#         st+=1
#
#     #Заполнение нижней горизонтальной матрицы
#     for i in range(v+1, n-v):
#         b[-v-1][-i-1] =st
#         st+=1
#
#     #Заполнение левой вертикальной матрицы
#     for i in range(v+1, n-(v+1)):
#         b[-i-1][v]=st
#         st+=1
#
#     m+=2
#
# b.reverse()
# for el in b:
#     el.reverse()
#     print(el)
#
# -----------------------------------------------------
# Напишите программу, в которой создается вложенный список из случайных чисел. В
# матрице, которая реализуется данным вложенным списком, удаляется строка и столбец.
# Номер строки и номер столбца, которые нужно удалить, вводятся пользователем.
# from random import randint
#
# x,y = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
# # x, y = 10, 10  # Строк, столбцов
# matrix = [[randint(0, 99) for j in range(y)] for i in range(x)]
# print(*matrix, sep='\n')
# a, b = int(input('Удалить строку ')), int(input('Удалить столбец '))
# del matrix[a]
# for row in matrix:
#     del row[b]
# print(*matrix, sep='\n')

#------------------------------------------------------------------
# a = [322,124,121,22,665,345,9,234,96898,2341,34,566]
#
# def bSort(array):
#     # определяем длину массива
#     length = len(array)
#     #Внешний цикл, количество проходов N-1
#     for i in range(length):
#         # Внутренний цикл, N-i-1 проходов
#         for j in range(0, length-i-1):
#             #Меняем элементы местами
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#
# bSort(a)
# print(a)
# array = [23,11,3,5,78,345,2111,7777]
#
# def print_new(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         new_arr.append(arr[i])
#         maximum = max(new_arr)
#         index_max = new_arr.index(maximum)
#     new_arr.clear()
#     new_arr.append(maximum)
#     new_arr.append(index_max)
#     print(new_arr)
#     # print(maximum)
#     # print(index_max)
#
# print_new(array)
#------------------------------------------------------------------------
from random import randint
x = int(input("Введите количество элементов: "))
spisok = [randint(0, 99) for i in range(x)]
new_spisok = []
new_spisok2 = []
for i in range(len(spisok)):
    if i % 2 == 0:
        new_spisok.append(spisok[i])
        new_spisok.sort(reverse=False)
    else:
        new_spisok2.append(spisok[i])
        new_spisok2.sort(reverse=True)

    #     spisok.sort(reverse=True)
    # else:
    #     spisok.sort(reverse=False)
print(spisok)
print(new_spisok + new_spisok2)
# print(new_spisok2)