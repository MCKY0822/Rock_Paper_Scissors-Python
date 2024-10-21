import random

while True:
    
    player_score = 0
    computer_score = 0
    round_count = 0
    max_rounds = 3
    
    while round_count < max_rounds:
        print(f"\nRound {round_count + 1} of {max_rounds}")
        choices = ['rock', 'paper', 'scissors']
        computer = random.choice(choices)

        player = None
        while player not in choices:
            player = input('rock, paper or scissors?: ').lower()

        print('Player: ', player)
        print('Computer: ', computer)

        if player == computer:
            print("It's a TIE!")
        
        elif player == 'rock':
            if computer == 'scissors':
                print("You WIN this round!")
                player_score += 1
            else:
                print("You LOSE this round!")
                computer_score += 1

        elif player == 'paper':
            if computer == 'rock':
                print("You WIN this round!")
                player_score += 1
            else:
                print("You LOSE this round!")
                computer_score += 1

        elif player == 'scissors':
            if computer == 'paper':
                print("You WIN this round!")
                player_score += 1
            else:
                print("You LOSE this round!")
                computer_score += 1

        round_count += 1
        print(f"Current Score -> Player: {player_score} | Computer: {computer_score}")
    

    print("\nGame Over!")
    if player_score > computer_score:
        print(f"You are the WINNER! Final Score -> Player: {player_score} | Computer: {computer_score}")
    elif player_score < computer_score:
        print(f"Computer wins! Final Score -> Player: {player_score} | Computer: {computer_score}")
    else:
        print(f"It's a TIE! Final Score -> Player: {player_score} | Computer: {computer_score}")

    
    play_again = input('Do you want to play again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print('Thank you for playing. Goodbye!')