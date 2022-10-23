import random

number = random.randint(0,10)

print(number)

player_name = input("What is your name? \n : ")

number_of_guesses = 0


print('okay! '+ player_name+ ' I am going Guessing a number between 1 and 10, What do you think it would be?:')

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break

if guess == number:
    print('You have won and you guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))



