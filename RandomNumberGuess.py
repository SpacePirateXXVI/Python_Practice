#This is a random game.

import random

name = input("Hello. What is your name? : " )

print('Well ' +name+ ' ,I am thinking of a number between 1 and 20, care to take a guess?: ')
SecretNumber = random.randrange(1,21)

for guessesTaken in range(1,7):
    print ('Take a guess')
    guess = int(input() )
    if guess< SecretNumber:
        print("No, that is too less")
    elif guess > SecretNumber:
        print("No, that is too much")
    else:
        break # This condtion is for the correct guess !

if guess == SecretNumber:
    print('Good job ' + name + ' :) ')
else:
    print("Nope, the number I was thinking of was" +str(SecretNumber))

