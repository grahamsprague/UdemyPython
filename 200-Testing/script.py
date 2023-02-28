'''
This is an extercise of wrapping try around a 
fuction and then creating unit tests for that function.
'''

from random import randint


def guess(a_guess, a_answer):
    '''
    Checks the players input
    '''
    if 0 < a_guess < 11:
        if a_guess == a_answer:
            print('you got it!')
            return True
    else:
        print('you must enter a number 1-10')
        return False

# only execute this if it is the file being run
if __name__ == '__main__':

    # generate a number 1~10
    answer = randint(1, 10)

    # input from user?
    # check that input is a number 1~10
    while True:
        try:
            my_guess = int(input('guess a number 1-10: '))
            if guess(my_guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue

