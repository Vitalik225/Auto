# import random
#
# player_score = 0
# bot_score = 0
# player_choice = ''
# bot_choice = ''
# game = True
# while game:
#     for i in range(1, 4):
#         print(f'ROUND {i}')
#         player_choice = ''
#         while player_choice != 'r' and player_choice != 'p' and player_choice != 's':
#            player_choice = str(input("Enter [r],[p],[s] : "))
#         bot_choice = random.choice('rps')
#         print(f'Player choice : {player_choice} Bot choice : {bot_choice}')
#         if player_choice == bot_choice:
#             print('Draw round')
#         elif player_choice == 'r':
#             if bot_choice == 's':
#                 print('Player won the round!')
#                 player_score = player_score + 1
#             else:
#                 print('Bot won the round!')
#                 bot_score = bot_score + 1
#         elif player_choice == 's':
#             if bot_choice == 'p':
#                 print('Player won the round!')
#                 player_score = player_score + 1
#             else:
#                 print('Bot won the round!')
#                 bot_score = bot_score + 1
#         elif player_choice == 'p':
#             if bot_choice == 'r':
#                 print('Player won the round!')
#                 player_score = player_score + 1
#             else:
#                 print('Bot won the round!')
#                 bot_score = bot_score + 1
#     if player_score == bot_score:
#         print('Draw game')
#     elif player_score > bot_score:
#         print('Player won game!')
#     elif player_score < bot_score:
#         print('Bot won game!')
#     game = str(input("Press any key + enter to continue \n or press enter to exit"))

'''improve version'''
import random

player_score = 0
bot_score = 0
player_choice = ''
bot_choice = ''
game = True
while game:
    for i in range(1, 4):
        print(f'ROUND {i}')
        player_choice = ''
        while player_choice != 'r' and player_choice != 'p' and player_choice != 's' and player_choice != 'l' and player_choice != 'k':
            player_choice = str(input("Enter [r],[p],[s],[l],[k] : "))
        bot_choice = random.choice('rpslk')
        print(f'Player choice : {player_choice} Bot choice : {bot_choice}')
        if player_choice == bot_choice:
            print('Draw round')
        elif player_choice == 'r':
            if bot_choice == 's' or bot_choice == 'l':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 's':
            if bot_choice == 'p' or bot_choice == 'l':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 'p':
            if bot_choice == 'r' or bot_choice == 'k':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 'l':
            if bot_choice == 'k' or bot_choice == 'p':
                print("Player won the round !")
                player_score = player_score + 1
            else:
                print("Bot won the round!")
                bot_score = bot_score + 1
        elif player_choice == 'k':
            if bot_choice == 's' or bot_choice == 'r':
                print('Player won the round')
                player_score = player_score + 1
            else:
                print("Bot won the round!")
                bot_score = bot_score + 1
    if player_score == bot_score:
        print('Draw game')
    elif player_score > bot_score:
        print('Player won game!')
    elif player_score < bot_score:
        print('Bot won game!')
    game = str(input("Press any key + enter to continue \n or press enter to exit"))
