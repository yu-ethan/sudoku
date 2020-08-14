from sudoku import Board
import random
import copy

def generate_filled():
    board = []
    randlist = [1,2,3,4,5,6,7,8,9]
    random.shuffle(randlist)
    board.append(randlist)
    for i in range(9):
        board.append([0,0,0,0,0,0,0,0,0])
    b = Board()
    b.board = board
    b.solve()
    answer = copy.deepcopy(board)
    remove_nums(b)
    b.print_board()
    return answer, board

def remove_nums(b):
    stack = rand_coords_list()
    while len(stack) != 0:
        coords = stack.pop()
        row = coords[0]
        col = coords[1]
        temp = b.board[row][col]
        b.set_zero(row, col)
        if not b.unique_solve(row, col, temp):
            b.board[row][col] = temp

#uses a stack to eliminate chance of random selection of same coords
def rand_coords_list():
    stack = []
    for i in range(0,9):
        for j in range(0,9):
            stack.append([i,j])
    random.shuffle(stack)
    return stack

generate_filled()
    
    