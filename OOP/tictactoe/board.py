import random


RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


class Board:
    def __init__(self):
        self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    def play_move(self, position, marker):
        self.board[position] = marker

    def computer_move(self, position, marker):
        self.board[position] = marker

    def grid_board(self):
        row0 = ['.......+', '........', '+.......']
        row1 = ['.......+', '........', '+.......']
        row2 = ['.......+', '........', '+.......']
        row3 = ['.......+', '........', '+.......']

        row_decorator = ['       |', '        ', '|        ']

        grids = [row0, row_decorator, row1, row_decorator,
                 row2, row_decorator, row3]

        """Display of tic-tac-toe in grids"""
        row1[0] = f'...{self.board[0]}...+'
        row1[1] = f'...{self.board[1]}....'
        row1[2] = f'+...{self.board[2]}...'

        row2[0] = f'...{self.board[3]}...+'
        row2[1] = f'...{self.board[4]}....'
        row2[2] = f'+...{self.board[5]}...'

        row3[0] = f'...{self.board[6]}...+'
        row3[1] = f'...{self.board[7]}....'
        row3[2] = f'+...{self.board[8]}...'

        for i in grids:
            print(''.join(i))

    def winner_of_game(self):
        if self.board[0] == self.board[1] == self.board[2] == 'X' or \
                self.board[3] == self.board[4] == self.board[5] == 'X' or \
                self.board[6] == self.board[7] == self.board[8] == 'X' or \
                self.board[0] == self.board[4] == self.board[8] == 'X' or \
                self.board[2] == self.board[4] == self.board[6] == 'X' or \
                self.board[0] == self.board[3] == self.board[6] == 'X' or \
                self.board[1] == self.board[4] == self.board[7] == 'X' or \
                self.board[2] == self.board[5] == self.board[8] == 'X':
            print(GREEN+"You, Win!"+RESET)
            return True
        if self.board[0] == self.board[1] == self.board[2] == 'O' or \
                self.board[3] == self.board[4] == self.board[5] == 'O' or \
                self.board[6] == self.board[7] == self.board[8] == 'O' or \
                self.board[0] == self.board[4] == self.board[8] == 'O' or \
                self.board[2] == self.board[4] == self.board[6] == 'O' or \
                self.board[0] == self.board[3] == self.board[6] == 'O' or \
                self.board[1] == self.board[4] == self.board[7] == 'O' or \
                self.board[2] == self.board[5] == self.board[8] == 'O':
            print(RED+"Computer ,Win!"+RESET)
            return True
        return False
