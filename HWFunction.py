'''Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates'''
#
#
# def text():
#     print(
#         '“Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\n\t\t\t\t\t\t\t\t\t\tBill Gates')
#
#
# text()
'''Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними.'''

# def even(number1, number2):
#     for i in range(number1, number2 + 1):
#         if i % 2 == 0:
#             print(i)
#
#
# print(even(1, 10))

'''Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.'''
def displaying_an_empty_or_filled_square(length, symbol, switcher=False):
    space = ' '
    square = ''
    symb_leng = len(symbol)
    if switcher:
        for i in range(length):
            square = square + length * symbol + '\n'
    else:
        for i in range(length):
            if i == 0 or i == (length - 1):
                square = square + (length * symbol) + '\n'
            else:
                square = square + symbol + ((length - 2) * symb_leng * space) + symbol + '\n'
    print(square)


displaying_an_empty_or_filled_square(3, '||')
displaying_an_empty_or_filled_square(5, '**', True)
displaying_an_empty_or_filled_square(7, '* *')
displaying_an_empty_or_filled_square(8,'+','True')


'''Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров.'''

# def minimum(*args):
#     min_number = args[0]
#     for number in args:
#         if min_number < number:
#             min_number = number
#         return min_number
#
#
# print(minimum(5, 12, 23, 45, 67, 100 ))

'''Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами.
'''
#
# def multiple_numbers(number, number2):
#     result = 1
#     if number < number2:
#         for i in range(number, number2 + 1):
#             result = result * i
#             # print(i)
#         return result
#     elif number > number2:
#         for i in range(number2, number):
#             result = result * i
#         return result
#         #
#
#
# print(multiple_numbers(5, 1))

'''Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4'''

# def length_number(number):
#     count = 0
#     for i in str(number):
#         if i in str(number):
#             count = count + 1
#     return count
#
#
# print(length_number(5))

'''Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром'''


# def palindrome(palindrome_number):
#     palindrome_number = str(palindrome_number)
#     temp_number_1 = palindrome_number[:(len(palindrome_number) // 2)]
#     temp_number_2 = palindrome_number[(len(palindrome_number) // 2):]
#    # print(temp_number_1, temp_number_2)
#     temp_number_1 = int(temp_number_1)
#     n1_1 = temp_number_1 // 100
#     n1_2 = temp_number_1 // 10 % 10
#     n1_3 = temp_number_1 % 10
#     print(n1_1, n1_2, n1_3)
#     temp_number_2 = int(temp_number_2)
#     n2_1 = temp_number_2 // 100
#     n2_2 = temp_number_2 // 10 % 10
#     n2_3 = temp_number_2 % 10
#     print(n2_1, n2_2, n2_3)
#     if n1_1 == n2_3 and n1_2 == n2_2 and n1_3 == n2_1: #возвращаем True, если число является палиндромом
#         return True
#
#     else:
#         return False
#
#
# print(palindrome(123321))
# print(palindrome(123322))
