# В шифре «поросячья латынь» начальная согласная буква слова перемещается в конец слова,
# и к ней до- бавляется суффикс «ay». Если слово начинается с глас- ной,
# к нему просто добавляется суффикс «way». Напри- мер, pig превращается в igpay, banana — в ananabay,
# а aardvark — в aardvarkway. Напишите программу,
# которая предлагает пользователю ввести слово и пре- образует его в «поросячью латынь».
# Проследите за тем, чтобы новое слово выводилось в нижнем регистре.
word = input("Введите какое-нибудь слово: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())
