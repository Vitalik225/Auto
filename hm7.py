# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.

number = int(input("Enter the number 1 for 100 : "))
if number < 1 or number > 100:
    print("Error!!" * 4)
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 != 0 and number % 5 != 0:
    print(number)

# Задание 2
# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.

# number = int(input("Enter the number : "))
# chose = input("Chose the degree [2],[3],[4],[5],[6],[7] : ")
# if chose == "2":
#     print(number ** 2)
# elif chose == "3":
#     print(number ** 3)
# elif chose == "4":
#     print(number ** 4)
# elif chose == "5":
#     print(number ** 5)
# elif chose == "6":
#     print(number ** 6)
# elif chose == "7":
#     print(number ** 7)
# else:
#     print('Error')


# Задание 3
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.
# price = float(input("Enter the price  : "))  # price for 1 minute
# chose = input("Choose mobile operator :  [Mo1],[Mo2],[Mo3] ")  # Mo = Mobile operator
# price_talk = 0  # full price for talk
# time_talk = 10  # full time of talk (minutes)
# price_talk = price * time_talk
# if price < 0:
#     print("Error!Please type valid price ")
# elif chose == "Mo1" or chose == "Mo2" or chose == "Mo3":
#     print(f"Payment bill : {price_talk}")

# Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.
#
# sale_level = int(input("Enter sale level for I manager : "))
# sale_level_2 = int(input("Enter sale level for II manager : "))
# sale_level_3 = int(input("Enter sale level for III manager : "))
# salary = 200  # base salary
# salary_1 = 0  # salary 1 manager
# salary_2 = 0  # salary for 2 manager
# salary_3 = 0  # salary for 3 manager
# percent_from_sale_level = 0  # percent for 1 manager
# percent_from_sale_level_2 = 0  # 2 manager
# percent_from_sale_level_3 = 0  # 3 manager
# if sale_level > 0 and sale_level < 500:  #
#     percent_from_sale_level = (sale_level * 3) / 100  # 3 %
#     salary_1 = salary + percent_from_sale_level
# elif sale_level >= 500 and sale_level <= 1000:
#     percent_from_sale_level = (sale_level * 5) / 100  # 5 %
#     salary_1 = salary + percent_from_sale_level
# elif sale_level > 1000:
#     percent_from_sale_level = (sale_level * 8) / 100  # 8 %
#     salary_1 = salary + percent_from_sale_level
# if sale_level_2 > 0 and sale_level_2 < 500:
#     percent_from_sale_level_2 = (sale_level_2 * 3) / 100
#     salary_2 = salary + percent_from_sale_level_2
# elif sale_level_2 >= 500 and sale_level_2 <= 1000:
#     percent_from_sale_level_2 = (sale_level_2 * 5) / 100
#     salary_2 = salary + percent_from_sale_level_2
# elif sale_level_2 > 1000:
#     percent_from_sale_level = (sale_level_2 * 8) / 100
#     salary_2 = salary + percent_from_sale_level
# if sale_level_3 > 0 and sale_level_3 < 500:
#     percent_from_sale_level_3 = (sale_level_3 * 3) / 100
#     salary_3 = salary + percent_from_sale_level_3
# elif sale_level_3 >= 500 and sale_level_3 <= 1000:
#     percent_from_sale_level_3 = (sale_level_3 * 5) / 100
#     salary_3 = salary + percent_from_sale_level_3
# elif sale_level_3 > 1000:
#     percent_from_sale_level = (sale_level_3 * 8) / 100
#     salary_3 = salary + percent_from_sale_level
# else:
#     print("Error")
#
# print(f"Salary I manager : {salary_1}")
# print(f"Salary II manager : {salary_2}")
# print(f"Salary III manager : {salary_3}")
#
# if salary_1 > salary_2 and salary_1 > salary_3:
#     print(f"Best manager : -I- your salary : {salary_1 + 200} ")
# elif salary_2 > salary_1 and salary_2 > salary_3:
#     print(f"Best manager : -II-  your salary : {salary_2 + 200} ")
# elif salary_3 > salary_1 and salary_3 > salary_2:
#     print(f"Best manager : -III- your salary : {salary_3 + 200} ")
# elif salary_1 == salary_2 and salary_1 == salary_3:
#     print("No Bonuses")
#
# else:
#     print("Error")
