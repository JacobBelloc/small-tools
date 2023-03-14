def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board, player):
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]

    print("Welcome to Tic Tac Toe!")
    print("Player 1: X | Player 2: O")

    for i in range(9):
        print_board(board)
        print("It's Player", players.index(current_player) + 1, "'s turn.")
        move = -1
        while move not in range(1, 10) or board[move-1] != " ":
            try:
                move = int(input("Enter your move (1-9): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        board[move-1] = current_player

        if check_win(board, current_player):
            print_board(board)
            print("Congratulations! Player", players.index(current_player) + 1, "wins!")
            return

        if i == 8:
            print_board(board)
            print("It's a tie!")
            return

        current_player = players[i % 2 + 1]

if __name__ == "__main__":
    tic_tac_toe()
