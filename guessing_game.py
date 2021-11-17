import random


def player_guessing_game():
    number=random.randint(1,10) #Intilize a random number between 1 and 10 inclusive
    player_name=input("Hello, enter your name. ") #Ask user to input their name
    number_of_guesses=0 # Intilize the number of guesses variable to track how many guesses the user takes.
    print('Okay! '+ player_name+ ' I am thinking of a number between 1 and 10. Type your guess :') #Message to prompt the user and ask for their guess.
    while number_of_guesses < 5: #While loop to check if the user guess is the same as the random number that was generated. User only has five chances
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))

def computer_guessing_game():
    low=1
    high=10
    feedback=''
    while feedback !='c':
        if low!= high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high (H), too low (L), or correct(C)? ").lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Yay! The Computer guessed your number, {guess} correctly!")

def main():
    print("Let's play a guessing game!!!")
    print("If you want the computer to guess your number press 1 otherwise if you want to guess the computers number press 2.")

    choice=input()
    if choice=="1":
        computer_guessing_game()
    elif choice=="2":
        player_guessing_game()
    else:
        print("You did not enter a valid choice.")

    # __name__
if __name__=="__main__":
    main()