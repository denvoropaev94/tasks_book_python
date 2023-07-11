# A = dict(zip([1, 2, 3], ['D', 'K', 'L']))
#
# B = dict.fromkeys([10, 20, 30], 'Z')
#
# print("A = ", A)
# print("B = ", B)
#
# print("Спавнение словарей: ")
# print("A = B: ", A == B)
# print("A != B: ", A != B)
#
# #добавление одного словаря к другому:
# A.update(B)
# print("Объединение словарей: ")
# print("A = ",A)
#
# A.clear()
# print(A)
#=========================================
# dic = {}
# text = input("Введите текст:").lower()
# for i in text:
#     if i not in dic.keys():
#         dic[i] = text.count(i)
#
# print(dic)

# =========================================
# dic = {}
# text = 'ABCABD'
# for i in range(len(text)):
#     if text[i] not in dic.keys():
#         dic[text[i]] = text[:i] + text[i + 1:]
#
# for k, v in dic.items():
#     print(f'{k}: {v}')

# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items ())
# print(x)
# y = next(x)
# r = next(x)
# print(r)
# z = next(iter(r))
# print(z)