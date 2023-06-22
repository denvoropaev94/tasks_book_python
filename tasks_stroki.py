# text = input("Введите текст: ")
# symb = input("Какую букву Вы хотите найти? ")
# num = text.find(symb)
# my_list = []
# while num != -1:
#     my_list.append(num)
#     num = text.find(symb, num + 1)
# if len(my_list) == 0:
#     print("Такой буквы нет в тексте !")
# else:
#     print(f"Позиции буквы '{symb}' в тексте: {my_list}")

# =========================================================
# txt = "Python"
# num = 20
# A = txt.ljust(num, "_")
# B = txt.center(num)
# C = txt.rjust(num, "*")
# print("|", A, "|")
# print("|", B, "|")
# print("|", C, "|")

# -----------------------------------------------------------
# Попарный обмен символами
# text = input("Введите какой-то текст: ")
# new_text = ""
# num = 0
#
# while num < len(text) - 1:
#     new_text += text[num+1] + text[num]
#     num += 2
# if num < len(text):
#     new_text += text[num]
# print(new_text)
# --------------------------------------------------------------

# Шифрования текста. Шифр Цезаря. При шифровании текста каждая буква заменяется другой(следующую в алфавите)
# text = input("Введите какой-то текст: ")
# print("--------------------------------")
# new_text = ""
# m = ord("а")
# n = ord("я")
# M = ord("А")
# N = ord("Я")
# # Создание шифра
# for s in text:
#     k = ord(s)
#     if (m <= k < n) or (M <= k < N):
#         s = chr(k+1)
#     elif k == n:
#         s = chr(m)
#     elif k == N:
#         s = chr(M)
#     new_text += s
# print("Шифр: ", new_text)

# --------------------------------------------
# Средняя длина слова
# text = input("Введите какой-то текст: ")
# text = text.lower()
# print(text)
# L = text.split(" ")
# print(L)
# s = 0
# n = 0
# for k in range(len(L)):
#     # отбрасываем ненужные символы
#     w = L[k].strip(".,:;-?!")
#     if len(w) != 0:
#         # отбражение слова и его длины
#         print(w.center(12), "-", len(w))
#         # сумма букв в слове
#         s += len(w)
#         # количество слов
#         n += 1
# s /= n
# print("Средняя длина: ", s)

# ---------------------------------------------------------
# Все большие буквы меняются на маленькие, а маленькие - на большие
# text = input("Введите какой-либо текст")
# new_text = ""
# for k in text:
#     if 65 <= ord(k) < 97:
#         k = chr(ord(k)+32)
#         new_text += k
#     elif 97 <= ord(k) < 123:
#         k = chr(ord(k) - 32)
#         new_text += k
# print(new_text)

# # ---------------------------------------------------------
# text = input("Введите какой-либо текст")
# new_text = ""
# n = 0
# while n < len(text)-1:
#     new_text += text[n + 1] + text[n]
#     n += 2
# if n < len(text)-1:
#     new_text += text[n]
# print(new_text)

# -------------------------------------------------------------
# Напишите программу, в которой пользователь вводит два текстовых значения,
# и на их основе создается новый текст.
# В этот новый текст поочередно включаются буквы из текстов, введенных пользователем.
# Когда один из текстов заканчивается, в качестве символов из этого текста используется «звездочка»

# text1 = input("Введите какой-либо текст: ")
# text2 = input("Введите какой-либо текст 2: ")
#
# while len(text1) < len(text2):
#     text1 += "*"
# while len(text2) < len(text1):
#     text2 += "*"
# print(''.join([text1[i] + text2[i] for i in range(len(text1))]))

# --------------------------------------------------------------------
#Расшифровка текста Цезаря
# text = input("Введите какой-то текст: ")
# print("--------------------------------")
# new_text = ""
# m = ord("а")
# n = ord("я")
# M = ord("А")
# N = ord("Я")
# # Создание шифра
# for s in text:
#     k = ord(s)
#     if (m < k < n) or (M < k < N):
#         s = chr(k-1)
#     elif k == n:
#         s = chr(m)
#     elif k == m:
#         s = chr(n)
#     elif k == N:
#         s = chr(M)
#     elif k == M:
#         s = chr(N)
#     new_text += s
# print("Шифр: ", new_text)
# ===================================================================
# text = input("Введите текст: ")
# new_text = ""
# my_list = text.split(" ")
# print(my_list)
# new_list = []
# for k in range(len(my_list)):
#     # отбрасываем ненужные символы
#     w = my_list[k].strip(".,:;-?!")
#     if len(w) != 0:
#         w = w[::-1]
#         new_list.append(w)
# print(new_list)
# =================================================================
# Предложите пользователю ввести слово в верхнем регистре.
# Если не все буквы слова будут указаны в верхнем регистре, попросите ввести слово заново.
# Повторяйте попытки, пока пользователь не введет сообщение в верхнем регистре.
# msg = input("Enter a message in uppercase: ")
# tryagain = False
# while tryagain == False:
#     if msg.isupper():
#         print("Thank you")
#         tryagain = True
#     else:
#         print("Try again")
#         msg = input("Enter a message in uppercase: ")
# ==================================================================
# Предложите пользователю ввести его почтовый индекс. Выведите первые две буквы слова в верхнем регистре1.
# msg = input("Enter a mail: ").upper()
# print(msg[:2])
# ==================================================================
# Предложите пользователю ввести имя, а затем сообщите, сколько в нем глас- ных букв.
# name = input("Enter your name: ")
# count = 0
# name = name.lower()
# for x in name:
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         count = count + 1
# print("Vowels = ", count)
# =====================================================================
# pswd1 = input("Enter a password: ")
# pswd2 = input("Enter it again: ")
# if pswd1 == pswd2:
#     print("Thank you")
# elif pswd1.lower() == pswd2.lower():
#     print("They must be in the same case")
# else:
#     print("Incorrect")

# ========================================================
# Предложите пользователю ввести слово, а затем выведите буквы слова в обратном порядке в разных строках.
# text = input("Enter a text: ")
# l =[]
# for letter in text[::-1]:
#     print(letter)
