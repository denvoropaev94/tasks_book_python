# # Функции для использования в декораторах
# def A(h):
#     return lambda x: h(x) * h(7 - x)
#
#
# def B(h):
#     return lambda x, y: h(x, y) + h(y, x)
#
#
# def C(h):
#     return lambda x: h(x, 10 - x)
#
#
# # Функции с декораторами
# @A
# def f(x):
#     return 2 * x - 1
#
#
# @B
# def F(x, y):
#     return (8 - x) * (y + 1)
#
#
# @C
# def H(x, y):
#     return x * y
#
#
# # Проверка результата:
# print("f(3) = ", f(3))
# print("F(5,7) = ", F(5, 7))
# print("H(6) = ", H(6))

# import random
# from typing import Callable
#
#
# def cache(func: Callable):
#     _cache_dict = {}
#
#     def wrapper(*args):
#         if args not in _cache_dict:
#             _cache_dict[args] = func(*args)
#         return _cache_dict[args]
#
#     return wrapper
#
#
# @cache
# def rnd(a: int, b: int) -> int:
#     return random.randint(a, b)
#
#
# print(rnd(1, 10))
# print(f'{rnd(1, 10) = }')
# print(f' {rnd(1, 10) = }')

import random
from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco


@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 100) = }')
print(f' {rnd(1, 1000) = }')
