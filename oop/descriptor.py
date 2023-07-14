# class Range:
#     def __init__(self, min_val: int = None, max_val: int = None):
#         self.min_val = min_val
#         self.max_val = max_val
#
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)
#
#     def __delete__(self, instance):
#         raise AttributeError(f'Свойство {self.param_name} нельзя удалять!')
#
#     def validate(self, value):
#         if not isinstance(value, int):
#             raise TypeError(f'Значение {value} должно быть целым числом')
#         if self.min_val is not None and value <= self.min_val:
#             raise ValueError(f'Значение {value} должно быть больше и равно {self.min_val}')
#         if self.max_val is not None and value >= self.max_val:
#             raise ValueError(f'Значение {value} должно быть меньше и равно {self.max_val}')
#
#
# class Student:
#     age = Range(3, 103)
#     grade = Range(1, 12)
#     office = Range(3, 44)
#
#     def __init__(self, name, age, grade, office):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.office = office
#
#     def __repr__(self):
#         return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'
#
#
# if __name__ == '__main__':
#     std1 = Student('Mark', 10, 4, 32)
#     # std2 = Student('Nik', 123, 11, 23)
#     print(f'{std1 = }')
#     std1.age = 12
#     print(f'{std1 = }')
#     # std1.grade = 12.0
#     # std1.office = 90
#     # del std1.age
#     print(f'{std1.__dict__ = }')

class Text:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')


class User:
    first_name = Text(str.istitle)
    last_name = Text(str.isupper)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'User(first_name = {self.first_name}, last_name = {self.last_name})'



us1 = User('Den', 'VOROP')
print(f'{us1 = }')
