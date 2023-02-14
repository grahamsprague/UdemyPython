'''
Guessing Game

To run the script use python, the script name and then provide 2 paras
python command: 'python'
python file: 'guessing_game.py'
param 1: start of number range '1'
param 2: end of number range '10'

example command
python ./guessing_game.py 1 10

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