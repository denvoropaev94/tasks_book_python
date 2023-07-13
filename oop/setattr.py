class Alpha:

    def __setattr__(self, key, value):
        if key == "number" and type(value) != int:
            res = 0
        else:
            res = value
        self.__dict__[key] = res

A = Alpha()
A.value = "Object A"
print(A.value)
A.number = 777
print(A.number)
A.number = "Hello"
print(A.number)
A.value = 3213231
print(A.value)
A.__dict__["number"] = "Python"
print(A.number)
A.__dict__["number"] = "Java"
print(A.number)