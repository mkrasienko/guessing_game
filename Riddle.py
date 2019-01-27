def riddle():
    out_of_guesses = False
    secret_word: str = "bat"
    guess_count = 0
    guess_limit = 3
    guess = ""
    while guess != secret_word and not out_of_guesses:
        guess = input("\nEnter a guess: ")
        if guess_count == 0 and "bat" not in guess:
            guess_count += 1
            print(f"That's not it! Try again. You have {guess_limit - guess_count} guesses left")
        elif guess_count == 1 and "bat" not in guess:
            print("That's not it! Last chance.")
            guess_count += 1
        elif guess_count == 2 and "bat" not in guess:
            out_of_guesses = True

    return out_of_guesses


print("\nI see without seeing. To me, darkness is as clear as daylight. What am I? - You have 3 tries.")

out_of_guesses = riddle()

while out_of_guesses is True:
    if out_of_guesses:
        print("WRONG! You're out of guesses. YOU LOSE!")
        play_again = input("--\nWant to play again? (Y/N): ")
        if play_again in ["y", "Y"]:
            riddle()
            print(out_of_guesses)
    elif out_of_guesses is False:
        print("Good guess. YOU WIN!")
        break
    else:
        print("\nBye bye!")
        break
else:
    print("Good guess. YOU WIN!")
