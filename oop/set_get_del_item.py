class Alpha:
    # Метод для считывания значения по индексу:
    def __getitem__(self, index):
        return self.value[index]

    # Метод для присваивания значения по индексу:
    def __setitem__(self, index, val):
        self.value[index] = val

    def __delitem__(self, index):
        del self.value[index]

    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(self.value)


A = Alpha()
A.value = [11, 55, 77]
print(A)

for k in range(len(A)):
    print(A[k], end=" ")
print()
A[1] = "A"
print(A)
del A[0]
print(A)
