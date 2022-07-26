from random import randrange

n = 10
my_list = [randrange(1, 10) for i in range(n)]
print(my_list)
my_list2 = [randrange(1, 10) for i in range(n)]
print(my_list2)
my_list3 = []
choose = 0
max_number = 0
min_number = 0
choose = str(input(
    "Enter your choise:\n[1]=concatination\n[2]=sort\n[3]=same numbers\n[4]=unique numbers\n[5]=min max in 3  list\n::"))
if choose == '1':
    my_list3 = my_list + my_list2
    print(my_list3)

elif choose == '2':
    my_list3 = list(set(my_list)) + list(set(my_list2))
    print(my_list3)

elif choose == '3':
    for i in my_list:  # первый цикл проходит по первому списку
        for j in my_list2:  # вторйо цикл проходит по второму списку
            if i == j:  # ставим условие если элемент из 1 списка равен элементу во 2 списке то доабвляем в третий список
                my_list3.append(i)
    print(set(my_list3))  # убираем повторяющиеся числа
    print(my_list3)  # общие элементы
elif choose == '4':
    for i in my_list:
        for j in my_list2:
            if i not in my_list2:
                if j not in my_list:
                    my_list3.append(i)
                    my_list3.append(j)
    print(set(my_list3))
elif choose == '5':
    max_number = my_list[0]
    for number in my_list:
        if number >= max_number:
            max_number = number
    max_number_list2 = my_list2[0]
    for number_list2 in my_list2:
        if number_list2 >= max_number_list2:
            max_number_list2 = number_list2
    my_list3.append(max_number)
    my_list3.append(max_number_list2)
    min_number = my_list[0]
    for number in my_list:
        if number <= min_number:
            min_number = number
    min_number_list2 = my_list2[0]
    for number_list2 in my_list2:
        if number_list2 <= min_number_list2:
            min_number_list2 = number_list2
    my_list3.append(min_number)
    my_list3.append(min_number_list2)
    print(my_list3)
