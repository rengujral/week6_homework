import random
import os  # Used to check if the save file exists

# Function to print top banner
def print_banner(game):
    banner_message = f"{'#' * 50}\n\n   ARE YOU READY TO PLAY {game}?\n\n{'#' * 50}"
    return banner_message

# File to store the game scores
SAVE_FILE = "scores.txt"  # This is the file where scores will be saved and loaded from


# Function to load the saved scores from a file
def load_scores():
    # Check if the save file exists before attempting to read it
    if os.path.exists(SAVE_FILE):  # If the file exists, we load the data
        with open(SAVE_FILE, "r") as file:  # Open the file in read mode
            data = file.read().strip().split(",")  # Read file content, remove extra spaces and split by commas
            return {
                "total_games": int(data[0]),  # Total number of games played
                "user_wins": int(data[1]),  # Total number of user wins
                "computer_wins": int(data[2]),  # Total number of computer wins
                "ties": int(data[3])  # Total number of ties
            }
    # If no file exists, return a dictionary with default values (no games played)
    return {"total_games": 0, "user_wins": 0, "computer_wins": 0, "ties": 0}


# Function to save the current scores to a file
def save_scores(stats):
    # Open the save file in write mode to overwrite the current scores
    with open(SAVE_FILE, "w") as file:
        # Write the stats as a comma-separated string (total_games, user_wins, computer_wins, ties)
        file.write(f"{stats['total_games']},{stats['user_wins']},{stats['computer_wins']},{stats['ties']}")


# Function to request input from the user
def get_user_choice():
    # Define the possible choices for the user
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    while True:  # Keep asking for input until a valid choice is made
        user_input = input(
            "Enter R for Rock, P for Paper, S for Scissors: ").strip().upper()  # Get user input, ensure it's uppercase
        if user_input in choices:  # If the user input is valid, return the corresponding choice
            return choices[user_input]
        print("Invalid choice. Please enter R, P, or S.")  # If input is invalid, prompt again


# Function to determine the computer's choice
def get_computer_choice():
    # Define the possible choices for the computer
    computer_choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
    # Randomly choose an index from 0, 1, 2, which corresponds to the three choices
    return computer_choices[random.choice([0, 1, 2])]


# Function to determine the winner
def determine_winner(user, computer, stats):
    stats["total_games"] += 1  # Increment the total number of games played

    # Check if it's a tie
    if user == computer:
        stats["ties"] += 1  # If it's a tie, increment the tie count
        return "It's a tie!"
    # Check for user win conditions (Rock beats Scissors, Scissors beats Paper, Paper beats Rock)
    elif (user == 'Rock' and computer == 'Scissors') or \
            (user == 'Scissors' and computer == 'Paper') or \
            (user == 'Paper' and computer == 'Rock'):
        stats["user_wins"] += 1  # If the user wins, increment user wins
        return "You win!"
    else:  # In all other cases, the computer wins
        stats["computer_wins"] += 1  # If the computer wins, increment computer wins
        return "You lose!"

def print_final_message(user_score,computer_score,tie_message,win_message,lose_message):
    if user_score == computer_score:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {tie_message}")
    elif user_score > computer_score:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {win_message}")
    else:
        print(f"The final score is player: {user_score} and computer :{computer_score}\n {lose_message}")


# Function to play a single round of the game
def play_game(stats):
    print(print_banner("ROCK,PAPER,SCISSORS"))
    # Get the user's and the computer's choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    number_of_rounds = int(input("How many rounds would you like to play?").strip())

    
    # Print both choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner of the round and print the result
    result = determine_winner(user_choice, computer_choice, stats)
    print(result)

    # Print the current score after the round
    print(f"\nScore so far: ")
    print(
        f"Total Games: {stats['total_games']} | User Wins: {stats['user_wins']} | Computer Wins: {stats['computer_wins']} | Ties: {stats['ties']}")


# Main game loop
def main():

    # Load existing scores (from a previous session)
    stats = load_scores()

    # Ask if the user wants to continue from the last game, if there are saved stats
    if stats["total_games"] > 0:
        choice = input("\nWould you like to continue from your last game? (yes/no): ").strip().lower()
        if choice == "no":
            # If the user wants to reset, initialize stats to zero
            stats = {"total_games": 0, "user_wins": 0, "computer_wins": 0, "ties": 0}

    # Game loop: keep playing until the user chooses to stop
    while True:
        # Play a single round of the game
        play_game(stats)

        # Save the current game stats
        save_scores(stats)

        # Ask if the user wants to play again
        rps_loop = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if rps_loop != "yes":  # If the user doesn't want to play again, exit the loop
            print(
                "Thanks for playing! Your progress has been saved.")
            break


if __name__ == "__main__":
    main()