# Присвойте total значение 0. Пока значение total равно 50 или менее,
# предложите пользователю ввести число. Прибавьте это число к total и выведите сообщение «The total is... [total]».
# Цикл должен остановиться, когда значение total превысит 50.
# total = 0
# while total <= 50:
#     num = int(input("Введите число: "))
#     total += num
# print("The total is... ", total)

# Предложите пользователю ввести число. Продолжайте запрашивать число, пока введенное число не будет больше 5,
# после чего выведите сообщение «The last number you entered was a [число]» и остановите программу.
# num = 0
# while num <= 5:
#     num = int(input("Enter a number: "))
# print("The last number you entered was a ", num)

# Предложите пользователю вве- сти сначала одно число, а затем другое.
# Сложите два числа и спросите, хочет ли он прибавить еще одно.
# Если он введет «y», предложите ввести еще одно число; это продолжается до тех пор, пока пользователь не введет ответ «y».
# После того как цикл остановится, выведите сумму.
# num1 = int(input("Enter a number: "))
# total = num1
# again = "y"
# while again == "y":
#     num2 = int(input("Enter another number: "))
#     total = total + num2
#     again = input("Do you want to add another number? (y/n) ")
# print("The total is ",total)


# Предложите пользователю ввести имя человека, которого пользователь хочет пригласить на вечеринку.
# После этого выведите сообщение «[имя] has been invited» и увеличьте счет- чик на 1.
# Спросите, хочет ли пользователь пригласить кого-то еще.
# Продолжайте запрашивать имена, пока пользователь не ответит отрицательно, и выведите количество приглашенных.
# again = "y"
# count = 0
# while again == "y":
#     name = input("Хотите пригласить  кого-нибудь на вечеринку? ")
#     print(name, " has been invited")
#     count = count + 1
#     again = input("Хотите пригласить еще кого-нибудь на вечеринку? (y/n) ")
# print("You have ", count, " people coming to your party")

# Создайте переменную с именем compnum и присвойте ей значение 50.
# Предложите пользователю ввести число.
# Пока предположение не совпадает со значением compnum, сообщите, больше оно или меньше compnum,
# и предложите ввести другое число.
# Если введенное значение совпадет с compnum, выведите сообщение «Well done, you took [попытки] attempts».
# compnum = 50
# guess = int(input("Can you guess the number I am thinking of? "))
# count = 1
# while guess != compnum:
#     if guess < compnum:
#         print("Too low")
#     else:
#         print("Too high")
#     count = count + 1
#     guess = int(input("Have another guess: "))
# print("Well done, you took ", count, " attempts")

# Предложите пользователю ввести число от 10 до 20.
# Если введенное значение меньше 10, выведите со- общение «Too low» и предложите повторить попытку.
# Если введенное значение больше 20, выведите со- общение «Too high» и предложите повторить попытку.\
# Повторяйте до тех пор, пока не будет введено значение из диапазона от 10 до 20,
# после чего выведите сообщение «Thank you».
# num = int(input("Enter a number between 10 and 20: "))
# while num < 10 or num > 20:
#     if num < 10:
#         print("Too low")
#     else:
#         print("Too high")
#     num = int(input("Try again: "))
# print("Thank you")
# Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles hanging on the wall,
# and if 1 green bottle should accidentally fall».
# Затем выведите вопрос: «how many green bottles will be hanging on the wall?».
# Если пользователь ответит правильно, выведите сообщение «There will be [счетчик] green bottles hanging on the wall».
# Если пользователь ответит неправиль- но, выведите сообщение «No, try again», пока не будет дан правильный ответ.
# Когда счетчик умень- шится до 0, выведите сообщение «There are no more green bottles hanging on the wall».

num = 10
while num > 0:
    print("There are ", num, " green bottles hanging on the wall.")
    print( num, " green bottles hanging on the wall.")
    print("And if 1 green bottle should accidentally fall,")
    num = num - 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == num:
        print("There will be ", num, " green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.")
