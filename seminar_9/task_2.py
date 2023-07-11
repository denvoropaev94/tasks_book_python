from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text  = ''

    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Den'))
print(bye('Nik'))
print(hello('Mark'))
print(bye('ulia'))
