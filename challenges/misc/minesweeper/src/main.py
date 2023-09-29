import sys

mines = [
    [1, 9, 9, 1, 1, 9, 9, 1, 1, 9, 9, 2, 9, 9, 1, 0, 1, 9, 9, 1, 0, 0, 0],
    [2, 4, 4, 3, 2, 3, 4, 4, 3, 3, 3, 3, 4, 4, 3, 2, 2, 4, 3, 2, 1, 2, 2],
    [9, 2, 9, 9, 1, 1, 9, 9, 9, 1, 1, 9, 2, 9, 9, 2, 9, 2, 9, 1, 1, 9, 9],
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 4, 5, 3, 3, 1, 2, 3, 4, 3],
    [1, 9, 1, 1, 9, 9, 1, 0, 1, 9, 2, 9, 1, 1, 9, 9, 9, 1, 0, 1, 9, 9, 1],
    [2, 3, 3, 3, 3, 4, 2, 1, 2, 3, 4, 3, 2, 3, 3, 5, 4, 4, 2, 2, 3, 4, 3],
    [1, 9, 9, 2, 9, 2, 9, 1, 1, 9, 9, 2, 9, 2, 9, 2, 9, 9, 9, 1, 1, 9, 9],
    [1, 3, 4, 4, 2, 3, 3, 3, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 1, 3, 3],
    [0, 1, 9, 9, 1, 1, 9, 9, 1, 1, 9, 9, 2, 9, 2, 9, 1, 0, 0, 0, 0, 1, 9],
    [1, 2, 3, 4, 3, 3, 3, 4, 2, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 2, 1],
    [9, 1, 1, 9, 9, 2, 9, 2, 9, 1, 1, 9, 1, 1, 9, 2, 9, 9, 9, 9, 9, 1, 0],
    [3, 3, 2, 3, 4, 4, 3, 3, 3, 3, 3, 2, 1, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0],
    [9, 9, 1, 1, 9, 9, 2, 9, 2, 9, 9, 1, 0, 0, 1, 9, 2, 9, 1, 0, 0, 0, 0],
    [3, 4, 3, 2, 3, 4, 4, 3, 3, 4, 3, 2, 1, 1, 2, 1, 3, 3, 3, 2, 2, 3, 1],
    [1, 9, 9, 1, 1, 9, 9, 2, 9, 2, 9, 1, 1, 9, 1, 0, 1, 9, 9, 2, 9, 9, 9]]

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

rows = 15
cols = 23
mines_counter = 88
flag_counters = 88
dig_counters = 161
numbers = [" 0️⃣ ", " 1️⃣ ", " 2️⃣ ", " 3️⃣ ", " 4️⃣ ", " 5️⃣ ", " 6️⃣ ", " 7️⃣ ", " 8️⃣ "]


def print_board():
    print("\nMines left: " + str(mines_counter))

    print("    ", end="")
    for i in range(65, 88):
        print(" " + chr(i), end=" ")
    print()

    for row in range(0, 15):
        print("%02d" % (row + 1,), end=" |")
        for col in range(0, 23):
            if board[row][col] == 0:  # untouched
                print(" ⬜️", end="")
            elif board[row][col] == 1:  # flagged
                print(" ⛳️", end="")
            else:
                print(numbers[mines[row][col]], end="")  # mined
        print("")


def user_input():
    inp = input("\n\nEnter your choice: ").split()
    if len(inp) >= 2:
        try:
            action = inp[0].lower()
            coordinates = []

            for i in range(1, len(inp)):
                y = int(inp[i][1:]) - 1
                x = ord(inp[i][0].upper()) - 65

                if 0 <= y < 15 and 0 <= x < 23:
                    coordinates.append({"x": x, "y": y})
                else:
                    print("Invalid coordinate. Please keep the coordinates within A-W and 1-15.")

            user = {"action": action, "coordinates": coordinates}
            return user
        except:
            print("Invalid input format. Please use 'action xy' format.")
    else:
        print("Invalid input format. Please use 'action xy' format.")


def loser():
    print("💣💥 You dug a mine! Try again and hope better.")
    sys.exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("\n\n\nThis is a minesweeper. A few rows have been cleared to help you.")
    print("Enter your choice in the form 'action xy ...'. For example: 'flag A13' or 'flag A13 B13 C13'.")
    print("The actions you can do are: 'flag' and 'dig' and 'unflag'.")

    while (True):
        print_board()
        user = user_input()
        if user is not None:
            action = user.get("action")
            coordinates = user.get("coordinates")

            for coord in coordinates:
                x, y = coord["x"], coord["y"]

                if action == "flag":
                    if board[y][x] != 2:
                        board[y][x] = 1
                        flag_counters -= 1
                        if mines[y][x] == 9:
                            mines_counter -= 1
                elif action == "dig":
                    if mines[y][x] == 9:
                        loser()
                    else:
                        board[y][x] = 2
                        dig_counters += 1
                elif action == "unflag":
                    board[y][x] = 0
                    flag_counters += 1
                    if mines[y][x] == 9:
                        mines_counter += 1
                else:
                    print("Invalid action, please try again.")
            if dig_counters == 257:
                print_board()
                print(
                    "\nCongrats! You solved the minesweeper. Here is your first flag: flag-701_7u_5415_0u_p053r_l35_p13d5.")
                print("You now need to investigate the board a bit more to discover the second flag.\n")
                exit()
