# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.first < self.stop:
#             self.first, self.second = self.second, self.first + self.second
#             if self.start <= self.first < self.stop:
#                 return self.first
#         raise StopIteration
#
#
# fib = Fibonacci(10, 110)
# for num in fib:
#     print(num)
class Iter:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop):
            self.start += 1
            return chr(i)
        raise StopIteration


chars = Iter(65, 91)
for c in chars:
    print(c)
