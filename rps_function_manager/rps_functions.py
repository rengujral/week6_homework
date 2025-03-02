# this imports pythons random module
import random
from rps_function_manager.rps_score_manager import save_score, read_score

# this block is what the user inputs
def get_user_choice():
    """
    Prompts the user to enter R, P, or S and returns the full name of their choice.
    :return: str: The user's choice - 'Rock', 'Paper', or 'Scissors'.
    """
    # this is a variable that is a dictionary so each letter corresponds to its full form with use of key value pairs
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # this is another input variable which prompts the user to type the letter
    user_input = input("Enter R for Rock, P for Paper, S for scissors: ").strip().upper()
    # this looks up the user input that you type in the command and returns what it corresponds to from the dictionary

    # from renee_week5
    # if loop determining if user input is valid
    if user_input in choices:
        # if valid it displays the full name of the input
        return choices[user_input]
    else:
        # else it states that the input is invalid and prompts the user to enter a choice again
        print("Invalid Choice! Please enter one of the three choices above!")
        return get_user_choice()


# this block is what the computer generates
# from renee, serena and khrisha's code
def get_computer_choice() -> str:
    """
    Randomly selects a choice for the computer.
    :return: str: The computer's choice - 'Rock', 'Paper', or 'Scissors'.
    """
    computer_choices = {0:"Rock", 1:'Paper', 2:'Scissors'}
    # we create a list map the values
    return computer_choices[random.choice([0, 1, 2])]
# the function random.choice() from the module random returns a randomly selected value from the list[]


# new block that takes 2 arguments, so the function expects 2 values
# from Renee's week 5 homework
def determine_winner(user, computer):
    """
    Determines the winner based on user and computer choices.
    :param user: The user's choice ('Rock', 'Paper', or 'Scissors').
    :param computer: The computer's choice ('Rock', 'Paper', or 'Scissors').
    :return: str: A message declaring the result - win, lose, or draw.
    """
     # dictionary defining winning key value pairs
    winning_conditions = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
     # if loop determining whether user beats computer or if there is a draw and displaying corresponding message
    if user == computer:
        return "It's draw!"
    elif winning_conditions[user] == computer:
        return "You win!"
    else:
        return "You lose.."
    # # if statement block
    # if user == computer:
    #     return "It's a draw!"
    # elif (user == 'Rock' and computer == 'Scissors') or (user == 'Paper' and computer == 'Rock') or (user == 'Scissors' and computer == 'Paper'):
    #     return "You win!"
    # else:
    #     return "You lose!"


# new block of code
def play_game():
    """
    Plays a single round of Rock, Paper, Scissors. Prompts the user for input, generates a random computer choice
    :return: str: determining whether the user is a winner or a loser
    """
    # Load the current score from the file
    player_score, computer_score = read_score()

    # Get choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # another variable for the winner block of code
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Update score based on result
    if "win" in result.lower():
        player_score += 1
    elif "lose" in result.lower():
        computer_score += 1

    # Save the updated scores
    save_score(player_score, computer_score)

    # print(f"Current Score - You: {player_score}, Computer: {computer_score}")
    # save_score(player_score, computer_score)

# main trick
if __name__=='__main__':
    play_game()