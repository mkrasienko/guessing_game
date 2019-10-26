#This is a guessing game. It uses the ridddle from the 1995 Batman Forever movie. It will give the user 3 chances to guess the answer. It will not accept a blank answer. If the user fails to guess correctly in 3 tries, they will be given a chance to play again.
def riddle(): #function checks users answer and returns tuple with indication if user ran out of guesses or won
    out_of_guesses = False
    secret_word: str = "bat"
    guess_count = 0
    win = False
    guess = ""
    while secret_word not in guess and not out_of_guesses:
        guess = input("\nEnter a guess: ")
        if guess == "": #checks for blank answer
            print("You have to enter an answer. Please try again.")
        elif guess_count == 0 and "bat" not in guess and guess != "":
            guess_count += 1
            print(f"That's not it! Try again. You have 2 guesses left")
        elif guess_count == 1 and "bat" not in guess and guess != "":
            print("That's not it! Last chance.")
            guess_count += 1
        elif guess_count == 2 and "bat" not in guess and guess != "":
            out_of_guesses = True
        elif secret_word in guess:
            win = True
    return out_of_guesses, win


print("\nI see without seeing. To me, darkness is as clear as daylight. What am I? - You have 3 tries.")

status = riddle()

while status == (True, False):
    print("WRONG! You're out of guesses. YOU LOSE!")
    play_again = input("--\nWant to play again? (Y/N): ")
    if play_again in ["y", "Y"]:
        status = riddle()
        if status == (False, True):
            break
    elif play_again not in ["y", "Y"]:
        print('Bye! Bye!')
        break
    elif status == (False, True):
        break
if status == (False, True):
    print("Good guess. YOU WIN!")