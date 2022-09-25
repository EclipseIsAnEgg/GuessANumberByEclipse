import random
comp_num = random.randint(1, 100)
while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue
    if int(player_input) == comp_num:
        print('You guessed it!')
        break
    elif int(player_input) > comp_num:
        print('Too high!')
    else:
        print('Too low!')
