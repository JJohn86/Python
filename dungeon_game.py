import random
import os



# pick random location for exit
# pick random location for monster

# check for win/loss
# clear screen and re-draw grid








CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def draw_map(player, monster, door):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == monster:
                output = tile.format("M")
            elif cell == door:
                output = tile.format("D")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == monster:
                output = tile.format("M|")
            elif cell == door:
                output = tile.format("D|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y
    #get player location
    #if move == left, x+1, right, x-1
    #if move == up, y+1, down y-1
    return player

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN", "HELP", "QUIT"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    #if players move
    return moves

def finish_game():
    print("Thank you for playing!")
    quit()

def play_again():
    clear_screen()
    again = input("Would you like to play again? (YES / no) > ")
    again = again.upper()
    if again == "NO":
        finish_game()
    if again == "YES":
        start_game()
    else:
        input("not a valid answer.... >")
        play_again()

def get_help():
    clear_screen()
    print("\nWelcome to the dungeon!")
    print("Somewhere in this dungeon there is a monster and an exit")
    print("Find the exit without running into the monster\n")

    print("Enter HELP for information")
    print("Enter QUIT at any time to quit\n")
    input("Enter any key to continue > ")

def start_game():
    monster, door, player = get_locations()
    while True:
        valid_moves = get_moves(player)
        clear_screen()
        print("You're currently in room {}".format(player))
        print("The monster is currently in room {}".format(monster))
        print("The door is at {}".format(door))
        draw_map(player, monster, door)
        print("")
        print("Command Options: {}\n".format(", ".join(valid_moves)))


        move = input("> ")
        move = move.upper()

        if move == "QUIT":
            break
        if move == "HELP":
            get_help()
            continue
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                input("You found the moster room and have been eaten... goodbye \nPress any key to continue")
                play_again()
            if player == door:
                input("You found the door and have escaped.  Congratulations!! \nPress any key to continue >")
                play_again()
        else:
            input("\n ** Invalid move, are you at a wall? ** \n Press any button to continue > ")
            continue

get_help()
start_game()
