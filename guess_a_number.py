import random
from time import sleep

sleep(1)
print('Hello and welcome to Guess A Number!')
sleep(1)
difficulty = input('Difficulty (1-5): ')
if difficulty != '1' and difficulty != '2' and difficulty != '3' and \
        difficulty != '4' and difficulty != '5' and not difficulty.isdigit():
    while difficulty != '1' and difficulty != '2' and difficulty != '3' and \
            difficulty != '4' and difficulty != '5' and not difficulty.isdigit():
        difficulty = input('Please choose a valid difficulty! Difficulty (1-5): ')

sleep(1)
comp_num = 0
player_input = 0

if difficulty == '1':
    comp_num = random.randint(1, 10)
if difficulty == '2':
    comp_num = random.randint(1, 50)
if difficulty == '3':
    comp_num = random.randint(1, 100)
if difficulty == '4':
    comp_num = random.randint(1, 500)
if difficulty == '5':
    comp_num = random.randint(1, 1000)

while True:
    if difficulty == '1':
        player_input = input("Guess the number (1-10): ")
    if difficulty == '2':
        player_input = input("Guess the number (1-50): ")
    if difficulty == '3':
        player_input = input("Guess the number (1-100): ")
    if difficulty == '4':
        player_input = input("Guess the number (1-500): ")
    if difficulty == '5':
        player_input = input("Guess the number (1-1000): ")

    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue

    if int(player_input) == comp_num:
        print('You guessed it!')
        break
    elif int(player_input) > comp_num:
        print('Too high!')
        sleep(0.1)
    else:
        print('Too low!')
        sleep(0.1)
