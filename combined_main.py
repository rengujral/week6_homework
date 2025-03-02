import random
SAVE_FILE = "scores.txt"  # This is the file where scores will be saved and loaded from

def print_banner(game):
    banner_message = f"{'#' * 50}\n\n   ARE YOU READY TO PLAY {game}?\n\n{'#' * 50}"
    return banner_message




# Function to load the saved scores from a file
# def load_scores():
#     # Check if the save file exists before attempting to read it
#     if os.path.exists(SAVE_FILE):  # If the file exists, we load the data
#         with open(SAVE_FILE, "r") as file:  # Open the file in read mode
#             data = file.read().strip().split(",")  # Read file content, remove extra spaces and split by commas
#             user_score = int(data[0]),  # Total number of user wins
#             computer_score = int(data[1]) # Total number of computer wins
#
#     # If no file exists, return a dictionary with default values (no games played)
#     return user_score, computer_score
#
# def save_scores(stats):
#     # Open the save file in write mode to overwrite the current scores
#     with open(SAVE_FILE, "w") as file:
#         # Write the stats as a comma-separated string (total_games, user_wins, computer_wins, ties)
#         file.write(f"{stats['total_games']},{stats['user_wins']},{stats['computer_wins']},{stats['ties']}")

def get_user_choice():
    # this is a variable that is a dictionary so each letter corresponds to its full form with use of key value pairs
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # this is another input variable which prompts the user to type the letter
    user_input = input("Enter R for Rock, P for Paper, S for scissors: ").strip().upper()
    # this looks up the user input that you type in the command and returns what it corresponds to from the dictionary
    return choices[user_input]


def get_computer_choice():
    computer_choices = {0: "Rock", 1:'Paper', 2:'Scissors'}
    computer_choice = computer_choices[random.choice([0, 1, 2])]
    # we create a list map the values
    return computer_choice


def determine_winner(computer, user, user_score, computer_score):
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
    if user_score == computer_score:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {tie_message}")
    elif user_score > computer_score:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {win_message}")
    else:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {lose_message}")


def play_game():
    print(print_banner("ROCK,PAPER,SCISSORS"))
    user_score = 0
    computer_score = 0
    number_of_rounds = int(input("How many rounds would you like to play?").strip())

    for round in range(1, number_of_rounds+1):
        users_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {users_choice} and computer chose {computer_choice}\n")
        round_user_score, round_computer_score = determine_winner(computer_choice, users_choice, user_score, computer_score)
        print(f"The score in round {round} is player: {user_score} and computer: {computer_score}\n")
        user_score += round_user_score
        computer_score += round_computer_score

    print_final_message(user_score, computer_score, tie_message="It is a tie, nobody won", win_message="Congratulations, you won!", lose_message="Sorry, you lost!")


def main():
    play_game()


if __name__ == '__main__':
    main()