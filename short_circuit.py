from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Den'))
print(hello('Nik'))
print(bye('Alina'))
print(hello('Oleg'))
print(bye('Sasha'))
