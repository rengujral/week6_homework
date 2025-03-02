from combined_main import play_game


# Create while true infinite loop to loop through the game
while True:
    # Call the function play_game() which starts a round of Rock, Paper, Scissors
    play_game()
    # Ask the user if they want to play again.
    # .strip() removes any extra spaces before or after the input.
    rps_loop = input("\nDo you want to play again? (yes/no)\n").strip()
    # Check if the user entered "yes"
    if rps_loop == "yes":
        print("Yay!")
    else:
        # If the user enters anything other than "yes", prints a goodbye message
        print("Okay, goodbye.")
        # Break used to stop the game and exit
        break
