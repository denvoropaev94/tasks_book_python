class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old
    @old.deleter
    def old(self):
        del self.__old


p1 = Person('Den', 28)
p1.old = 29
print(p1.old, p1.__dict__)