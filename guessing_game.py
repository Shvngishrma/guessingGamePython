import random

def guessing_game(is_first_game=True):
    if is_first_game:
        print("Welcome to the Guessing Game!")
        print("I have selected a number between 1 and 100. Try to guess it!")

    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        # Input validation to ensure the user enters a valid number
        guess_input = input("Enter your guess: ")
        
        # Check if the input is a valid number
        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess_input)
        attempts += 1

        # Provide feedback on the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guessing_game(is_first_game=False)  # Pass False to skip the welcome message
    else:
        print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    guessing_game()
