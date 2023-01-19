
values = list(range(1, 10))


def draw_board(values):
    print("\n")
    print("\t     |     |")
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t     |     |")
    print("\n")


def take_input(token):
    valid = False
    while not valid:
        player_answer = input("Enter position for " + token + ":")
        try:
            player_answer = int(player_answer)
        except:
            print("Incorrect input, try again!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(values[player_answer - 1]) not in "XO"):
                values[player_answer - 1] = token
                valid = True
            else:
                print("Thise field is taken already!")
        else:
            print("Incorrect input, enter nums from 1 to 9.")


def check_win(values):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if values[each[0]] == values[each[1]] == values[each[2]]:
            return values[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "player won!")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    draw_board(board)

main(values)

input("Press any key for EXIT")
