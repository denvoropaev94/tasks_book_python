mytext = input("Введите текст для проверки")
symbs = list(input("Введите буквы для поиска"))

print("Ищем такие буквы: ", symbs)
for s in symbs:
    if s in mytext:
        print("В тексте есть буква ", s)
        break
    else:
        print("В тексте нет буквы ", s)
else:
    print("Таких букв в тексте нет ")
print("The end")