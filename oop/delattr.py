class Alpha:

    def __getattr__(self, item):
        return "такого атрибута нет"

    def __delattr__(self, item):
        if item == "number":
            print("Удалять нельзя!")
        else:
            object.__delattr__(self,item)

A = Alpha()
A.value = 100
print(A.value)
del A.value
print(A.value)
A.number = 777
print(A.number)
del A.number
print(A.number)
del A.__dict__["number"]
print(A.number)
