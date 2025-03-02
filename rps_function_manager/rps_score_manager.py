import os

def save_score(player_score, computer_score):
    """Creates and writes file to store scores"""
    with open("score.txt", 'w') as file:
        file.write(f"User: {player_score}\n")
        file.write(f"Computer: {computer_score}")

def read_score():
    if os.path.exists("score.txt"):
        with open("score.txt", "r") as file:
            scores = file.readlines()
        try:
            if len(scores) == 2:  # Ensure file has two lines
                player_score = int(scores[0].strip().split(":")[-1])  # Extract the number after "User:"
                computer_score = int(scores[1].strip().split(":")[-1]) # Extract the number after "Computer:"
                print(f"Scores: Player = {player_score}, Computer = {computer_score}")
                return player_score, computer_score
        except ValueError:
            print("Resetting scores.")
            return 0,0 # Default scores if file doesn't exist or is corrupt


