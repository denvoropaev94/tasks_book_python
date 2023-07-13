# from collections import defaultdict
#
#
# class Storage:
#
#     def __init__(self):
#         self.storage = defaultdict(list)
#
#     def __str__(self):
#         txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
#         return f'Объекты хранилища по типам:\n{txt}'
#
#     def __call__(self, value):
#         self.storage[type(value)].append(value)
#         return f'К типу {type(value)} добавлен {value}'
#
#
# s = Storage()
# print(s(12))
# print(s(777))
# print(s("hi"))
# print(s(1000))
# print(s('Den'))
# print(s((12, 121, 1212)))
# print(s)
class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'MyClass(a = {self.a}, b = {self.b})'

    def __call__(self, *args, **kwargs):
        self.a.append(args)
        self.b.update(kwargs)
        return True


x = MyClass([42], {73: True})
y = x(3.14, 100, 500, start = 1)
# x(y=y)
print(x)