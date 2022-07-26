# import random
# 
# game = True
# while game:  # while True , но тогде не получится выйти исходя из того, что мы уже умеем
#     guess_number = 0
#     secret_number = random.randint(1, 20)
#     count_of_try = 0
#     cheat_mode = 777  # режим волшебных семерок -режим читов показывает загаданное число
#     while secret_number != guess_number:
#         guess_number = int(input("Enter secret number in range [1-20] : "))
#         if guess_number == cheat_mode:  # условие для чита
#             print(secret_number)
#             count_of_try = count_of_try - 1  # при использовании читы счетчик попыток снижается на 1(не учитывается)
#         elif secret_number > guess_number:
#             print('Your number less than secret')
#         elif secret_number < guess_number:
#             print('Your number greater than secret')
#         count_of_try = count_of_try + 1
#         if count_of_try > 3:  # после  3 неудачных попыток игра делает намеки на чит
#             print("Do u want win the game ??? press '''777'''")
#         if guess_number == cheat_mode:
#             print(f"You Win!!! but u are a fuck****ggg cheater !!!!!!") # игра выводит заранее сообщение о победе но не поощряет читы
#     print(f'You win! Tries : {count_of_try} ,Secret number is {secret_number}')
#     game = str(input("Press any key + enter to continue \n or press enter to exit"))
