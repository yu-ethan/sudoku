import copy
class Board:

    #evil sudoku
    board = [
        [0,0,9,1,0,6,0,0,0],
        [3,7,0,0,0,0,0,0,6],
        [0,0,4,0,0,5,0,0,0],
        [2,0,0,0,0,1,5,0,0],
        [0,4,0,8,0,3,0,9,0],
        [0,0,3,9,0,0,0,0,8],
        [0,0,0,5,0,0,7,0,0],
        [6,0,0,0,0,0,0,2,4],
        [0,0,0,2,0,8,1,0,0]
    ]

    def __init__(self):
        self.rows = 9
        self.columns = 9

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

if __name__ == "__main__":
    b = Board()
    print(b.number_empty())
    b.solve()
    b.print_board()

