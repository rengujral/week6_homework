import os

def save_score(player_score, computer_score):
    """Creates and writes file to store scores"""
    with open("score.txt", 'w') as file:
        file.write(f"User: {player_score}\n")
        file.write(f"Computer: {computer_score}")

def read_score():
    if os.path.exists("score.txt"):
        with open("score.txt", "r") as file:
            print("Previous Scores:\n")
            print(file.read())