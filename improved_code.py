# this imports pythons random module
import random
import os

SCORE_FILE = "scores.txt"  # File to store the scores

# Function to save the score
def save_score(player_score, computer_score):
    # Open the save file in write mode
    with open(SCORE_FILE, "w") as file:
        file.write(f"Player: {player_score}\nComputer: {computer_score}\n")

# Load scores from the file
def load_score():
    # Check if the file exists first
    # Only opens the file is it exists
    if os.path.exists(SCORE_FILE):
        # Opens file in read mode
        with open(SCORE_FILE, "w") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                player_score = int(lines[0].split(": ")[1])
                computer_score = int(lines[1].split(": ")[1])
                return player_score, computer_score
    return 0, 0  # Default scores if no file is found

# this block is what the user inputs
def get_user_choice():
    # this is a variable that is a dictionary so each letter corresponds to its full form with use of key value pairs
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # this is another input variable which prompts the user to type the letter
    user_input = input("Enter R for Rock, P for Paper, S for scissors: ").strip().upper()
    # this looks up the user input that you type in the command and returns what it corresponds to from the dictionary
    return choices[user_input]
# print(my_choice())


# this block is what the computer generates
def get_computer_choice():
    # this choices variable is separate from the first because its in its own block of code so there is no yellow squiggle
    # it is a list of different options for the computer
    choices = ['Rock', 'Paper', 'Scissors']
    # this is a method from the random module that picks randomly from my choices variable
    return random.choice(choices)
# print(computer_option())


# new block that takes 2 arguments, so the function expects 2 values
def determine_winner(user, computer):
    # if statement block
    if user == computer:
        return "It's a draw!"
    elif (user == 'Rock' and computer == 'Scissors') or (user == 'Paper' and computer == 'Rock') or (user == 'Scissors' and computer == 'Paper'):
        return "You win!"
    else:
        return "You lose!"


# new block of code
def play_game():
    while True:  # Loop to allow replay
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (Y/N): ").strip().upper()
        if play_again != 'Y':
            print("Thanks for playing!")
            break  # Exit the loop if the user doesn't enter 'Y'

# Run the game
play_game()


