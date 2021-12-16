import random


def player_guessing_game():
    number = random.randint(1, 10)
    player_name = input("Hello, enter your name. ")
    number_of_guesses = 0
    print(
        f"Okay! {player_name} I am thinking of a number between 1 and 10. Type your guess :"
    )
    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print("Your guess is too low")
        if guess > number:
            print("Your guess is too high")
        if guess == number:
            break

    if guess == number:
        print(f"You guessed the number in {number_of_guesses}")
    else:
        print(f"You did not guess the number, the number was {number}")


def computer_guessing_game():
    low = 1
    high = 10
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct(C)? "
        ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The Computer guessed your number, {guess} correctly!")


def main():
    while True:
        print("Let's play a guessing game!!!")
        print(
            "If you want the computer to guess your number press 1 otherwise if you want to guess the computers number press 2."
        )

        choice = input()
        if choice == "1":
            computer_guessing_game()
        elif choice == "2":
            player_guessing_game()
        else:
            print("You did not enter a valid choice.")

        keep_going = input("Do yo want to play again? (y/n): ")
        if keep_going.lower() != "y":
            break

    # __name__


if __name__ == "__main__":
    main()
