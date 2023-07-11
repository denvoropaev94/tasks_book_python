class MyClass:
    # Конструктор
    def __init__(self):
        self.value = 123
        print("Создается обьект", self.value)

    # Деструктор
    def __del__(self):
        print("Удаляется обьект", self.value)

    #     Метод для присваиваний значений полю
    def set(self, n):
        self.value = n

    #     Метод для отображения значения поля
    def show(self):
        print("Поле обьекта", self.value)


obj = MyClass()
obj.show()
obj.set(100)
# obj.show()
MyClass.show(obj)
MyClass.set(obj, 200)
obj.show()
# Явный вызов конструктора
MyClass.__init__(obj)
MyClass.__del__(obj)
obj.show()
obj.value = 321
obj.show()
obj.__init__()
obj.__del__()
obj.show()
