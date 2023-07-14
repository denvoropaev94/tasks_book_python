class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')

    @age.deleter
    def age(self):
        self._age = 0

user = User('Den', 'Voropaev')
user.age = 28
print(f'My name {user.full_name} and me {user.age} years')
print('one year last')
user.age = 29
print(f'My name {user.full_name} and me {user.age} years')
del user.age
print(f'My name {user.full_name} and me {user.age} years')