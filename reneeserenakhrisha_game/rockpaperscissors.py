# prompt the user to enter the value R/S/P
# rock = 0 paper = 1 scissors= 2

# import random to be able to randomise the computer's weapon choice
import random
# function to request input from user
def get_user_choice():
    # prompt the user to enter the initial of the weapon of their choice
    # .upper Converts the player's input to uppercase to ensure case insensitivity.
    user_choice = input("Pick your choice from Rock, Paper, or Scissors by inputting either R, P, or S: ").upper()
    # if loop determining if user input is valid, and establishes intials to value connection
    if user_choice == "P":
        print("Your choice: Paper")
        return "Paper"
    elif user_choice == "S":
        print("Your choice: Scissors")
        return "Scissors"
    elif user_choice == "R":
        print("Your choice: Rock")
        return "Rock"
    else:
        print("Please input either P, S, or R")
        return get_user_choice()


# function to termine the computer choice
def get_computer_choice() -> str:
    computer_choices = {0:"Rock", 1:'Paper', 2:'Scissors'}
    # we create a list map the values
    return computer_choices[random.choice([0, 1, 2])]
# the function random.choice() from the module random returns a randomly selected value from the list[]


# function to define possible combinations
# think of a better name - verb based
def winning_combinations(computer, user):
    if computer == user:
        return'it is a tie'
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Scissors' and computer == 'Paper') or \
         (user== 'Paper' and computer == 'Rock'):
        return"You lose!"
    else:
        return"You win!"

# # dictionary defining winning key value pairs
#     winning_conditions = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
#
#     # if loop determining whether user beats computer or if there is a draw and displaying corresponding message
#     if player == computer:
#         return "It's draw!"
#     elif winning_conditions [player] == computer:
#         return "You win!"
#     else:
#         return "You lose.."
# function created to play the game
def play_game():
    user_turn= get_user_choice()
    computer_turn = get_computer_choice()

    # Display choices
    print(f'the computer choice: {computer_turn}')

    # Determine and print the winner
    result = winning_combinations(user_turn, computer_turn)
    print(result)

# magic trick
if __name__=='__main__':
    play_game()