# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2020/12/26 16:18
# File Name     : ex05.py
# Dev Tool      : PyCharm
import os
from colorama import init, Fore

init(autoreset=True)
data = {1: 'Stone', 2: 'Scissors', 3: 'Cloth'}

os.system('cls')

while True:
    player1 = int(input('Player 1: <1 Stone> <2 Scissors> <3 Cloth>'))
    os.system('cls')
    player2 = int(input('Player 2: <1 Stone> <2 Scissors> <3 Cloth>'))
    os.system('cls')
    result = f'{Fore.RED}Player1:[{data[player1]}] Player2:[{data[player2]}]'
    if player1 == player2:
        print('Result: Draw.', result)
    elif (player1 + 1) % 3 == player2:
        print('Result: Player1 Wins!', result)
    elif (player1 - 1) % 3 == player2:
        print('Result: Player2 Wins!', result)
    else:
        print('Result: Unknown!', result)
    enter = input()
    if enter != '':
        break
    os.system('cls')
