import random

# Function to get the computer's random choice
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the result of each round
def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to display the choices and the result
def display_choices_and_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    print(result)

# Function to track and display scores
def display_scores(user_score, computer_score):
    print(f"\nCurrent Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}\n")

# Main function to run the game
def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Type 'exit' at any time to end the game.\n")

    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()

        # Check if user wants to exit the game
        if user_input == 'exit':
            print("Thanks for playing!")
            display_scores(user_score, computer_score)
            break

        # Check for valid input
        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Get computer's choice and determine the result
        computer_pick = computer_choice()
        result = check_winner(user_input, computer_pick)

        # Update scores based on result
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Display choices, result, and current scores
        display_choices_and_result(user_input, computer_pick, result)
        display_scores(user_score, computer_score)

        # Ask user if they want to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            display_scores(user_score, computer_score)
            break

# Run the game
play_game()