class Count:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 3:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name
        print("Create", self.name)



c1 = Count("Den")
print(c1)
c2 = Count("Nk")
print(c2)
c3 = Count("Sanu")
print(c3)
c4 = Count("Oleg")
print(c4)
