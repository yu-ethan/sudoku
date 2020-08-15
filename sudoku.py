import copy
import random

class Board:

    #evil sudoku
    # board = [
    #     [0, 0, 9, 1, 0, 6, 0, 0, 0],
    #     [3, 7, 0, 0, 0, 0, 0, 0, 6],
    #     [0, 0, 4, 0, 0, 5, 0, 0, 0],
    #     [2, 0, 0, 0, 0, 1, 5, 0, 0],
    #     [0, 4, 0, 8, 0, 3, 0, 9, 0],
    #     [0, 0, 3, 9, 0, 0, 0, 0, 8],
    #     [0, 0, 0, 5, 0, 0, 7, 0, 0],
    #     [6, 0, 0, 0, 0, 0, 0, 2, 4],
    #     [0, 0, 0, 2, 0, 8, 1, 0, 0]
    # ]

    def __init__(self):
        self.board = []
        self.starting_board = []
        self.ans_board = []
        self.rows = 9
        self.columns = 9
    
    #generates a sudoku board, storing board solution, beginning and a temp board
    #temp board is the board that will be worked on/changed
    def generate_board(self):
        randlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(randlist)
        self.board.append(randlist)
        for _ in range(9):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.solve()
        self.ans_board = copy.deepcopy(self.board)
        self.remove_nums()
        self.starting_board = copy.deepcopy(self.board)
    
    def remove_nums(self):
        stack = rand_coords_list()
        while len(stack) != 0:
            coords = stack.pop()
            row = coords[0]
            col = coords[1]
            temp = self.board[row][col]
            self.set_zero(row, col)
            if not self.unique_solve(row, col, temp):
                self.board[row][col] = temp
            
        


    def valid(self, row, col, num):
        #checking if valid in row
        for x in range(self.columns):
            if num == self.board[row][x]:
                return False       
        #checking if valid in column
        for y in range(self.rows):
            if num == self.board[y][col]:
                return False
        #checking if valid in square
        y = int(row/3) * 3
        x = int(col/3) * 3
        for i in range(y, y+3):
            for j in range(x, x+3):
                if num == self.board[i][j]:
                    return False
        #passed all checks
        return True

    def next_empty(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == 0:
                    return i, j
        return None, None

    def solve(self):
        row, col = self.next_empty()
        if row == None and col == None:
            #no more valid indexes == board is full
            return True
        for i in range(1, 10):
            if self.valid(row, col, i):
                self.board[row][col] = i
                if self.solve():
                    #if it returns false, then it will loop to next i, and check valid
                    return True
        #reached here = no valid num, backtrack to previous
        self.board[row][col] = 0
        return False
    
    def set_zero(self, row, col):
        self.board[row][col] = 0

    def set_val(self, row, col, val):
        self.board[row][col] = val
    
    #modified solve function for generator use to find unique boards
    #added constraint that at specific row, col cannot be solved with num
    #if it still can solve, then that means board is not unique and solved with another num
    def unique_solve(self, row, col, num):
        bcopy = copy.deepcopy(self.board)
        unique = True
        for i in range(1, 10):
            if i != num:
                if self.valid(row, col, i):
                    if self.solve():
                        unique = False
        if unique == False:
            self.board = bcopy
        return unique
            
    def number_empty(self):
        zeros = 0
        for row in range(self.rows):
            zeros += self.board[row].count(0)
        return zeros
    
    def print_board(self):
        for y in range(self.rows):
            print(self.board[y])

#uses a stack to eliminate chance of random selection of same coords
def rand_coords_list():
    stack = []
    for i in range(0,9):
        for j in range(0,9):
            stack.append([i,j])
    random.shuffle(stack)
    return stack

if __name__ == "__main__":
    b = Board()
    b.generate_board()
    b.print_board()

