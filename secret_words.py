import random


def load_secret_words(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()


def play_game():
    secret_words = load_secret_words('secret_words.txt')
    secret_word = random.choice(secret_words)
    attempts = 3  # Number of attempts the player has

    print("Welcome to the Word Guessing Game!")

    while attempts > 0:
        guess = input(
            f"Guess the secret word (length: {len(secret_word)}): ").lower()
        attempts -= 1

        if guess != secret_word:
            if len(guess) < len(secret_word):
                print("The word you guessed is too short.")
            elif len(guess) > len(secret_word):
                print("The word you guessed is too long.")
            else:
                print(f"Wrong word! You have {attempts} attempts left.")
        else:
            print(
                f"Congratulations! You guessed the secret word '{secret_word}' correctly!")
            break
    else:
        print(
            f"Sorry, you've run out of attempts. The secret word was '{secret_word}'.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    elif play_again == "no":
        print("Sorry to see you go, LOSER!")

play_game()
