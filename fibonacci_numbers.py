n = 15

a, b = 1,1
print(a, b, end=" ")
# За каждый цикл вычисляется одно новое число:
for k in range(n-2):
    a,b = b,a+b
    # Отображение нового числа:
    print(b, end=" ")