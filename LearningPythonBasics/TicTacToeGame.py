
current_player = "X"


def reset_board():
    return ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def print_board():

    line = ""
    new_line = " - - - - - - - "
    print(new_line)
    for i in range(0, 9):
        # print(i)
        if i % 1 / 3 == 0:
            line += " | "

        line += board_1[i]

        if i > 0 and (i + 1) % 3 == 0:
            line += " |"
            print(line)
            print(new_line)
            line = ""


def is_line_winner(val, a, b, c):
    if val != "X" and val != "O":
        return False
    test = "a[" + str(a) + ", " + str(b) + ", " + str(c) + "]:"
    # print(test, str(board_1[a]), board_1[a] == val and board_1[b] == val and board_1[c] == val)
    if board_1[a] == val and board_1[b] == val and board_1[c] == val:
        return True

    return False


def is_winner(val):
    # win state: 3 in a row
    # line by line
    # vertical line by line
    # corner to corner
    if (is_line_winner(val, 0, 1, 2) or
            is_line_winner(val, 3, 4, 5) or
            is_line_winner(val, 6, 7, 8) or
            is_line_winner(val, 0, 4, 8) or
            is_line_winner(val, 6, 4, 2) or
            is_line_winner(val, 0 , 3, 6) or
            is_line_winner(val, 1, 4, 7) or
            is_line_winner(val, 2, 5, 8)):
        return True

    return False


def set_selection(val, ind):
    if not ("X" == val or "O" == val):
        print("incorrect player symbol")
        return False
    elif 0 > ind or ind > 8:
        print("Out of Range")
        return False
    elif board_1[ind] == "X" or board_1[ind] == "O":
        print("Position already taken:", board_1[ind])
        return False

    board_1[ind] = val
    print("placed", val, "at", ind)
    return True


def is_game_over():
    # check board for open spaces
    # if no spots found return TRUE
    # else return FALSE
    for place in board_1:
        if not (place == "X" or place == "O"):
            print("found available spot")
            return False

    return True


def player_turn(val):
    turn = True
    while turn:
        print(val, "- Turn")
        print_board()
        index = int(input("Enter a number on the board to place an {}: ".format(val)))

        placed = set_selection(val, index)
        if placed:
            # print("Placed", val)
            turn = False
        # else:
            # print("Not Placed", val, "at index:", index)


board_1 = reset_board()

game_loop = True

while game_loop:

    print("Turn X:")
    current_player = "X"
    player_turn("X")

    # print("Is game over:", is_game_over())
    if is_winner(current_player):
        print_board()
        game_loop = False
        print(current_player, "is the winner")
    elif is_game_over():
        print_board()
        game_loop = False
        print("Draw Game - No Winner")
    else:
        print("Turn O:")
        current_player = "O"
        player_turn("O")

        # print("Is game over:", is_game_over())
        if is_winner(current_player):
            print_board()
            game_loop = False
            print(current_player, "is the winner")
        elif is_winner(current_player):
            print_board()
            game_loop = False
            print(current_player, "is the winner")
        elif is_game_over():
            print_board()
            game_loop = False
            print("Draw Game - No Winner")

print("thanks for playing")