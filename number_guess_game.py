


def repeat():
    repeat = 'nil'
    while True:
        repeat = str(input("""
            Would you like to play again? (Yes / No) > """))
        if repeat.lower() == 'yes':
            game()
        elif repeat.lower() == 'no':
            print("""
            Thank you for playing
            """)
            break
        else:
            print("""
            Not a valid entry
            """)

def game():
    import random
    # generate random number between 1 - 10
    secret_num = random.randint(1, 10)
    no_of_guesses_left = 3
    while no_of_guesses_left > 0:
        guess = input("""
            Guess a number between 1 and 10: """)
        try:
            guess = (int(guess))
        except ValueError:
            print("""
            {} is not a valid number
            """.format(guess))
        else:
            if guess == secret_num:
                print("""
            You got it!  My number was {}
                """.format(secret_num))
                repeat()
            elif guess < 1 or guess > 10:
                print("""
            Number out of range.  Please read instructions
                """)
            elif guess > secret_num:
                print("""
            Too high!  Try again!
                """)
                no_of_guesses_left -= 1
                print("""
            You have {} guesses left
                """.format(no_of_guesses_left))
            elif guess < secret_num:
                print("""
            Too low!  Try again!
                """)
                no_of_guesses_left -= 1
                print("""
            You have {} guesses left
                """.format(no_of_guesses_left))
        if no_of_guesses_left == 0:
            print("""
            Sorry, you're out of guesses...my number was {}
            """
            .format(secret_num))
            repeat()
game()
