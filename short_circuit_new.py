from typing import Callable


def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}

    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d

    return loc


small = main(4)
big = main(3)
print(small(7), big(7), small(3))
