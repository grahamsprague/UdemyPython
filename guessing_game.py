'''
Guessing Game
'''

import sys
from random import randint

X = int(sys.argv[1])
Y = int(sys.argv[2])

answer = randint(X, Y)



while True:
    try:
        guess = int(input(f'Enter a number between {X} and {Y} :'))
        if (X - 1) < guess < (Y + 1):
            # in range
            if guess == answer:
                print(f'You are correct! The answer is {answer}!')
                break
            else:
                print('Incorrect. Please try again.')
    except ValueError:
        print('You must enter a number!:')