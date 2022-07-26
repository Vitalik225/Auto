'''Задание 1
Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
■ Добавление стран;
■ Удаления стран;
■ Поиска стран по введенным символам;
■ Проверки существует ли страна внутри множества.'''
countries = {'Ukraine', 'England', 'France', 'Dominicana'}
while True:
    command = str(input("Enter your command : [r]-read set ,[c]-create,[d]-delete,[s]-search ::: "))
    if command == 'r':
        print(f'{countries}')
    elif command == 'c':
        countries.add(input("Enter new country : "))
    elif command == 'd':
        countries.discard(input("Please type country for delete : "))
    elif command == 's':    # данный модуль объединяет поиск с првоеркой наличия страны тоесть пункты 4 и 5 задания
        search = str(input("Please enter the coutry (from capital) For Example: U or Ukr) : "))
        for elem in countries:
            if search in elem:
                print(elem)
            else:
                print("Country cannot be found")

'''Задание 2
Существует два множества, содержащие названия
городов. Необходимо создать третье множество, содержащее названия, которые есть в обоих множествах.'''
# cities = {'Odessa', 'Kiev', 'Zhitomir'}
# cities2 = {'Lviv', 'Sumi', 'Yalta'}
# my_set = set()
# print(my_set.union(cities, cities2))

'''Задание 3
Существует два множества, содержащие названия
городов. Необходимо создать третье множество, содержащее названия, которые есть в первом множестве, но
нет во втором'''
# cities = {'Odessa', 'Kiev', 'Yalta'}
# cities2 = {'Lviv', 'Sumi', 'Zhitomir', 'Odessa'}
# my_set = set()
# my_set = cities.difference(cities2)
# print(my_set)

'''Задание 4
Существует два множества, содержащие названия
городов. Необходимо создать третье множество, содержащее названия, которые есть во втором множестве, но
нет в первом.'''
# cities = {'Odessa', 'Kiev', 'Yalta'}
# cities2 = {'Lviv', 'Sumi', 'Zhitomir', 'Odessa'}
# my_set = set()
# my_set = cities2.difference(cities)
# print(my_set)
'''Задание 5
Существует два множества, содержащие названия
городов. Необходимо создать третье множество, содержащее уникальные названия для каждого множества.'''
#
# cities = {'Odessa', 'Kiev', 'Yalta', 'Lviv', 'Sumi', 'Zhitomir', "lala"}
# cities2 = {'Lviv', 'Sumi', 'Zhitomir', 'Odessa', 'Kiev', 'Yalta', 'lolo'}
# temp_cities = set()
# temp_cities2 = set()
# final_set = set()
# temp_cities = cities.difference(cities2)
# temp_cities2 = cities2.difference(cities)
# print(final_set.union(temp_cities, temp_cities2))

'''Задание 6
В словаре хранится набор пар: Название страны ->
Столица. Нужно реализовать функциональность по добавлению, удалению, поиску и замене.'''
# countries = {'Kyiv': 'Ukraine', 'Warsaw': 'Poland', 'Berlin': 'Germany', 'Paris': 'France', 'Rome': 'Italy'}
# while True:
#     command = str(input("Enter the command \n[r]-read\n[c]=create\n[u]-update\n[d]-delete\n"))
#          #Read
#     if command == 'r':
#         for capital in countries:
#             print(f'Capital : {capital}  \tCountry : {countries[capital]}')
#     elif command == 'c':
#         #Create
#         capital = str(input('Enter capital of country : '))
#         country = str(input('Enter country : '))
#         countries[capital] = country
#     elif command == 'u':
#         #Update
#         capital = str(input('Enter capital of country : '))
#         country = str(input('Enter country : '))
#         countries[capital] = country
#     elif command == 'd':
#         #Delete
#         capital = str(input('Enter capital of country : '))
#         del countries[capital]
