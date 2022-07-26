# # Задание 1
# # Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# # числа в этом диапазоне по следующему правилу: если
# # число кратно 7, его надо выводить на экран.
# number1 = int(input("Enter first number : [start]"))
# number2 = int(input("Enter second number : [end]"))
# while number1 < number2:
#     if number1 % 7 == 0:
#         print(number1)
#     number1 += 1

# Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.
# number1 = int(input("Enter first number : [start] : "))
# number2 = int(input("Enter second number : [end] : "))
# choose = input("Enter your choose options  : [1] , [2] , [3], [4] : ")
# count = 0
# if choose == "1":
#     while number1 <= number2:
#         print(number1)
#         number1 += 1
# elif choose == "2":
#     while number1 <= number2:
#         print(number2)
#         number2 -= 1
# elif choose == "3":
#     while number1 <= number2:
#         if number1 % 7 == 0:
#             print(number1)
#         number1 += 1
# elif choose == "4":
#     while number1 <= number2:
#         if number1 % 5 == 0:
#             count += 1
#             print(f"number/5 = {number1} = {count} 'time(s)")
#         number1 += 1
# else:
#     print("Error")

# Задание 3
# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно выве
# сти слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число.
number1 = int(input("Enter first number : [start] : "))
number2 = int(input("Enter second number : [end] : "))
while number1 <= number2:
    if number1 % 3 == 0 and number1 % 5 == 0:
        print("Fizz Buzz")
    elif number1 % 3 == 0:
        print("Fizz")
    elif number1 % 5 == 0:
        print("Buzz")
    else:
        print(number1)
    number1 += 1
