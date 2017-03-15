# Game where the computer tries to guess your number based on high low clues


def repeat():
    repeat = 'nil'
    while True:
        repeat = str(input("""
Would you like to play again? (Yes / No) > 
            """))
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
    #secret_num = random.randint(1, 10)
    print("""
Lets play a game.

Instructions: Think of a number between 1 and 10 and the computer will guess 3 times...
""")
    input("""
Enter any key to proceed >
""")
    no_of_guesses_left = 3
    random_number = random.randint(1, 10)
    while no_of_guesses_left > 0:
        guess = input("""
Is your number {}?
""".format(random_number))
        if guess.lower() == 'yes':
            print("""
Yay!  I win!""")
            repeat()
            break
        elif guess.lower() == 'no':
            no_of_guesses_left -= 1
            if no_of_guesses_left == 0:
                print("""
Huh, I guess you won...
""")
                repeat()
                break
            else:
                hint = ''
                while hint != 'higher' or hint != 'lower':
                    hint = input("""
Is your number higher, or lower?
""")
                    if hint.lower() == 'higher':
                        random_number = random.randint((random_number + 1), 10)
                        break
                    elif hint.lower() == 'lower':
                        random_number = random.randint(1, (random_number - 1))
                        break
                    else:
                        print("""
Not a valid entry
""")
        else:
            print("""
not a valid entry...
""")




game()
