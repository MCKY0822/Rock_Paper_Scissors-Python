import random

while True:

    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input('rock, paper or scissors?: ').lower()
        print('invalid choice!')

    if player == computer:
        print('Player: ', player)
        print('Computer: ', computer)
        print("It's a TIE!")

    elif player == 'rock':
        if computer == 'scissors':
            print('Player: ', player)
            print('Computer: ', computer)
            print("You WIN!")
        if computer == 'paper':
            print('Player: ', player)
            print('Computer: ', computer)
            print("You LOSE!")

    elif player == 'paper':
        if computer == 'rock':
            print('Player: ', player)
            print('Computer: ', computer)
            print("You WIN!")
        if computer == 'scissors':
            print('Player: ', player)
            print('Computer: ', computer)
            print("You LOSE!")

    elif player == 'scissors':
        if computer == 'paper':
            print('Player: ', player)
            print('Computer: ', computer)
            print("You WIN!")
        if computer == 'rock':
            print('Player: ', player)
            print('Computer: ', computer)
            print("You LOSE!")

    play_again = input('Play Again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print('Good bye!')