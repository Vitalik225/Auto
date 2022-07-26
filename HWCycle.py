'''Задание 1
Напишите программу, которая запрашивает два
целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.'''
# x = int(input("Enter number [x] : "))
# y = int(input("Enter number  [y]: "))
# for i in range(1, x+1):
#     print("="*5)
#     print(f"Normal cycle : {i} ")
#     i = i ** y
#     print(f"Decree every number = {i}")
#     print("="*5)
'''Задание 2
Подсчитать количество в диапазоне  от 
100 до 999 у которых есть две одинаковые цифры'''
# numbers = 0
# n1 = 0
# n2 = 0
# n3 = 0
# count = 0
# for numbers in range(100, 999 + 1):
#     n1 = numbers // 100
#     n2 = (numbers % 100) // 10
#     n3 = numbers % 10
#     if n1 == n2 or n1 == n3:
#         count = count + 1
#         print(f"Numbers : {n1,n2,n3} , Count= {count}")

# '''Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.'''
# numbers = 0
# n1 = 0
# n2 = 0
# n3 = 0
# n4 = 0
# count = 0
# for numbers in range(100, 9999 + 1):
#     n1 = numbers // 1000
#     n2 = numbers % 1000 // 100
#     n3 = numbers % 100 // 10
#     n4 = numbers % 10
#     if n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4:
#         count = count + 1
#         print(f"Numbers : {n1, n2, n3, n4} , Count= {count}")

'''Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и 
вывести обратно на экран. '''
# number = int(input("Enter number : "))    #если идет ввод от 1 до 10
# for i in range(number):
#     if i == 3 or i == 6:
#         continue
#     print(i)

number = input("Enter number [123456789] : ")           #решение через строки
new_number = ''
for new_number in number:
    if new_number == '3' or new_number == '6':
        continue
    print(new_number)
