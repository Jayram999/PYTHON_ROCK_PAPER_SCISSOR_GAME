import random

def print_instructions():
    """Prints the instructions for the game."""
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
          + 'Rock vs Paper -> Paper wins\n'
          + 'Rock vs Scissors -> Rock wins\n'
          + 'Paper vs Scissors -> Scissors wins\n')

def get_user_choice():
    """Gets the user's choice."""
    while True:
        print('Enter your choice\n'
              '1 - Rock\n'
              '2 - Paper\n'
              '3 - Scissors\n')
        choice = int(input('Enter your choice: '))
        if 1 <= choice <= 3:
            return choice
        else:
            print('Enter a valid choice, please.')

def get_computer_choice():
    """Generates the computer's choice."""
    return random.randint(1, 3)

def get_winner(user_choice, comp_choice):
    """Determines the winner."""
    if user_choice == comp_choice:
        return 'DRAW'
    elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
        return 'Paper'
    elif (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        return 'Rock'
    elif (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 2):
        return 'Scissors'

def print_results(user_choice, comp_choice, result):
    """Prints the results of the game."""
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    print(f'User choice is\n{choices[user_choice]}')
    print('Now it\'s Computer\'s Turn....')
    print(f'Computer choice is\n{choices[comp_choice]}')
    print(f'{choices[user_choice]} Vs {choices[comp_choice]}')

    if result == 'DRAW':
        print('It\'s a Draw')
    elif result == 'Paper':
        print('Paper wins =>')
    elif result == 'Rock':
        print('Rock wins =>')
    elif result == 'Scissors':
        print('Scissors wins =>')

def play_game():
    """Main function to play the game."""
    print_instructions()
    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        result = get_winner(user_choice, comp_choice)
        print_results(user_choice, comp_choice, result)
        
        print('Do you want to play again? (Y/N)')
        ans = input().lower()
        if ans == 'n':
            break

    print('Thanks for playing')

if __name__ == '__main__':
    play_game()
