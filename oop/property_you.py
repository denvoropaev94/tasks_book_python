from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, age, passport, weigth):
        self.verify_fio(fio)

        self.__fio = fio
        self.age = age
        self.passport = passport
        self.weight = weigth

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО допускается использовать только буквенные символы')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 18 or age > 60:
            raise TypeError('Возраст должен быть целым числом и быть в диапозоне [18-60]')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Вес должен быть вещественным числом от 20 кг')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой!")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 2 or len(s[1]) != 7:
            raise TypeError("Неверный формат паспорта")
        for p in s[0]:
            if not p.isalpha():
                raise TypeError("Серия должна состоять из букв")
        for p in s[1]:
            if not p.isdigit():
                raise TypeError("Номер паспорта должен быть числовым")

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.verify_age(value)
        self.__age = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.verify_weight(value)
        self.__weight = value

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        self.verify_ps(value)
        self.__passport = value


person1 = Person('Воропаев Денис Витальевич', 28, 'BM 5678901', 90.5)
person1.age = 28
person1.passport = 'BM 1231231'
person1.weight = 89.12
print(person1.__dict__)
