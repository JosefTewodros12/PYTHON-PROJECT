import random
from board import Board
from art import logo

game = Board()
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
i = 0
print(logo)
while i < 5:
    game.grid_board()
    try:
        player_number = int(input("Please input the number of grid: "))
        if game.board[player_number] in ['X', 'O']:
            print("Spot already taken")
            continue
        game.play_move(player_number, YELLOW+'X'+RESET)

        if game.winner_of_game():
            game.grid_board()
            break
        if i == 4:
            game.grid_board()
            print(YELLOW+"It's a draw"+RESET)
            break
        computer_number = random.randint(0, 8)
        while game.board[computer_number] in ['X', 'O']:
            computer_number = random.randint(0, 8)

        game.computer_move(computer_number, BLUE+'O'+RESET)
        if game.winner_of_game():
            game.grid_board()
            break
    except (ValueError, IndexError):
        print("The number is not valid try to write number between 0 and 8")
    i += 1
