import random
import os
SAVE_FILE = "scores.txt"  # This is the file where scores will be saved and loaded from


def print_banner(game):
    """
    This function takes in a name of a game and creates string to display as a banner for it
    :param game: str specifies which game you want to create a banner for
    :return: str returns a string print statement
    """
    banner_message = f"{'#' * 50}\n\n   ARE YOU READY TO PLAY {game}?\n\n{'#' * 50}"
    return banner_message


# Function to load the saved scores from a file
def load_scores():
    """
    This function checks if a file exists, reads it, and assigns information from it to two variables -
    user_score (first element in the string) and computer_score(second element in the string). If no file exists, assigns 0s to the variables
    :return: int returns an integer assigned to user_score and computer_score variables
    """
    # Check if the save file exists before attempting to read it
    if os.path.exists(SAVE_FILE):  # If the file exists, we load the data
        with open(SAVE_FILE, "r") as file:  # Open the file in read mode
            data = file.read().strip().split(",")  # Read file content, remove extra spaces and split by commas
            user_score = int(data[0])  # Total number of user wins
            computer_score = int(data[1]) # Total number of computer wins

    # If no file exists, return a dictionary with default values (no games played)
        return user_score, computer_score

    return 0, 0


def save_scores(user_score, computer_score):
    """
    This function saves user_score and computer_score values to a specified file separated by a comma
    :param user_score: int
    :param computer_score: int
    :return: file
    """
    # Open the save file in write mode to overwrite the current scores
    with open(SAVE_FILE, "w") as file:
        # Write the stats as a comma-separated string (total_games, user_wins, computer_wins, ties)
        file.write(f"{user_score},{computer_score}")

def get_user_choice():
    """
    This function takes a prompted input from a user, strips it of white space and upper cases it, and then returns a string values
    which corresponds to that input from a dictionary
    :return: str
    """
    # this is a variable that is a dictionary so each letter corresponds to its full form with use of key value pairs
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # this is another input variable which prompts the user to type the letter
    user_input = input("Enter R for Rock, P for Paper, S for scissors: ").strip().upper()
    # this looks up the user input that you type in the command and returns what it corresponds to from the dictionary
    return choices[user_input]


def get_computer_choice():
    """
    This function generates a a random number from 0 to 2 and retrieves a string value for it from a dictionary
    :return: str
    """
    computer_choices = {0: "Rock", 1:'Paper', 2:'Scissors'}
    computer_choice = computer_choices[random.choice([0, 1, 2])]
    # we create a list map the values
    return computer_choice


def determine_winner(computer, user, user_score, computer_score):
    """
    This function compares the choices of user and computer and appends user_score or computer_score depending on who won
    :param computer: str computers choice in the game
    :param user: str users choice in the game
    :param user_score: int user score after playing
    :param computer_score: computer score after playing
    :return:
    """
    if computer == user:
        print('It is a tie!')
    elif (user == 'Rock' and computer == 'Scissors') or \
            (user == 'Scissors' and computer == 'Paper') or \
            (user == 'Paper' and computer == 'Rock'):
        user_score += 1
        print("You win!")
    else:
        computer_score += 1
        print("You lose!")
    return user_score, computer_score


def print_final_message(user_score,computer_score,tie_message,win_message,lose_message):
    """
    This function prints a selected final message, depending on the final outcome of the game
    :param user_score: int user score
    :param computer_score: int computer score
    :param tie_message: str a message for when there is a tie
    :param win_message: str a message for when user wins
    :param lose_message: str a message for when computer wins/user loses
    :return:
    """
    if user_score == computer_score:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {tie_message}")
    elif user_score > computer_score:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {win_message}")
    else:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {lose_message}")


def play_game():
    """
    This function asks how many rounds a user wants to play, initialises user and computer scores from a file, and for each round
    runs the get_user_choice and get_computer choice functions to get corresponding choices, updates user_score and computer_score
    based on determine_winner function, prints the final message by calling the print_final_message function, and saves the scores to a file to use for later
    and saves the final scores to a file for later
    :return: 
    """
    print(print_banner("ROCK,PAPER,SCISSORS"))
    user_score, computer_score = load_scores()
    number_of_rounds = int(input("How many rounds would you like to play?").strip())

    for round in range(1, number_of_rounds+1):
        users_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {users_choice} and computer chose {computer_choice}\n")
        user_score, computer_score = determine_winner(computer_choice, users_choice, user_score, computer_score)

        print(f"The score in round {round} is player: {user_score} and computer: {computer_score}\n")

    print_final_message(user_score, computer_score, tie_message="It is a tie, nobody won", win_message="Congratulations, you won!", lose_message="Sorry, you lost!")

    save_scores(user_score, computer_score)
def main():
    play_game()


if __name__ == '__main__':
    main()