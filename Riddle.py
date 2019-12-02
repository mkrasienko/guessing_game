#This is a guessing game. It uses the ridddle from the 1995 Batman Forever movie. It will give the user 3 chances to guess the answer. It will not accept a blank answer. If the user fails to guess correctly in 3 tries, they will be given a chance to play again.
import re
import time

def riddle(): #function checks users answer and returns boolean of variable out_of _guesses
    out_of_guesses = False
    secret_word = 'bat'
    guess_count = 0
    guess = ''
    answer = None
    while answer == None and not out_of_guesses:
        guess = input('\nEnter a guess: ').lower()
        answer = re.search(r'\bbat\b', guess, re.I)
        if guess == '': #checks for blank answer
            print('You have to enter an answer. Please try again.')
        elif guess_count == 0 and answer == None:
            guess_count += 1
            print('That\'s not it! Try again. You have 2 guesses left')
        elif guess_count == 1 and answer == None:
            print('That\'s not it! Last chance.')
            guess_count += 1
        elif guess_count == 2 and answer == None:
            out_of_guesses = True
        else:
            out_of_guesses = False
    return out_of_guesses


print('\nI see without seeing. To me, darkness is as clear as daylight. What am I? - You have 3 tries.')

wrong_answer = riddle()

while wrong_answer == True:
    print('WRONG! You\'re out of guesses. YOU LOSE!')
    time.sleep(1)
    play_again = input('--\nWant to play again? (Y/N): ')
    if play_again in ['y', 'Y']:
        wrong_answer = riddle()
    else:
        print('Bye! Bye!')
        break
if wrong_answer == False:
    print('Good guess. YOU WIN!')