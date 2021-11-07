import random

number=random.randint(1,10) #Intilize a random number between 1 and 10 inclusive
player_name=input("Hello, enter your name.") #Ask user to input their name
number_of_guesses=0 # Intilize the number of guesses variable to track how many guesses the user takes.
print('okay! '+ player_name+ ' I am thinking of a number between 1 and 10. Type your guess :') #Message to prompt the user and ask for their guess.
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
