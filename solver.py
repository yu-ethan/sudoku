#sudoku solver using hidden singles

#algorithm - take sudoku board, and fill it all in with possible
#candidates to find hidden singles

import copy

def boardCols(board):
    boardColumns = []
    for i in range(len(board)):
        column = []
        for j in range(len(board)):
            column.append(board[j][i])
        boardColumns.append(column)
    return boardColumns

def boardSq(board):
    cols = 0
    boardSquares = []
    for i in range(len(board)):
        square = []
        rows = int(i / 3) * 3
        if i % 3 == 0:
            cols = 0
        for k in range(rows, rows + 3):
            for l in range(cols, cols + 3):
                square.append(board[k][l])
        boardSquares.append(square)
        cols += 3
    return boardSquares

def checkSingleEmpty(board):
    for i in range(len(board)):
        countZeros = board[i].count(0)
        if countZeros == 1:
            row = i
            index = board[row].index(0)
            return True, row, index
    else:
        return False, 0, 0

def columnConvert(row, index):
    origrow = index
    origindex = row
    return origrow, origindex

def squareConvert(row, index):
    origrow = int(row/3) * 3 + int(index/3)
    origindex = (row%3 * 3) + index%3
    return origrow, origindex

def checkSquare(num, row, index, boardsq):
    sqrow = int(row/3)*3 + int(index/3)
    if num not in boardsq[sqrow]:
        return True

def singleIndex(board, row):
    for i in range(1,10):
        if i not in board[row]:
            return i

def printboard(board):
    for i in range(len(board)):
        print(board[i])

def singles(board, boardcopy, boardcols, boardsq):
    for i in range(len(boardcopy)):
        for j in range(len(boardcopy[i])):
            if board[i][j] == 0:
                candidatelist = []
                for k in range(1, 10):
                    if k not in boardcopy[i] and k not in boardcols[j]:
                        if checkSquare(k, i, j, boardsq):
                            candidatelist.append(k)
                if len(candidatelist) == 1:
                    board[i][j] = candidatelist[0]
                    boardcopy[i][j] = candidatelist[0]
                else:
                    boardcopy[i][j] = candidatelist

def hiddendoubles(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], list) and len(board[i][j]) == 2:
                check = board[i][j]
                for k in range(j, len(board)):
                    if isinstance(board[i][k], list) and len(board[i][k]) >= 2:
                        difference = list(set(check) ^ set(board[i][k]))
                        if len(difference) == 1:
                            remove = difference[0]
                            if remove in check:
                                check.remove(remove)
                                board[i][j] = check
                            else:
                                board[i][k].remove(remove)

def hiddensingle(board, origboard):
    var = 0
    for i in range(len(board)):
        sum = [0,0,0,0,0,0,0,0,0]
        for j in range(len(board)):
            if isinstance(board[i][j], list):
                for e in board[i][j]:
                    sum[e-1] += 1
        for k in range(len(sum)):
            if sum[k] == 1:
                var = k+1
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], list):
                if var in board[i][j]:
                    origboard[i][j] = var
                    return

def zeroCounter(board):
    zero = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                zero += 1
    return zero

def sudoku(board):
    boardColumns = boardCols(board)
    boardcopy = copy.deepcopy(board)
    boardSquares = boardSq(board)

    #row single check
    found, row, index = checkSingleEmpty(board)
    if found == True:
        num = singleIndex(board, row)
        board[row][index] = num
        #printboard(board)
        return

    #column single check
    found, colrow, colindex = checkSingleEmpty(board)
    if found == True:
        num = singleIndex(boardCols, colrow)
        row, index = columnConvert(colrow, colindex)
        board[row][index] = num
        #printboard(board)
        return

    #square single check
    found, sqrow, sqindex = checkSingleEmpty(boardSquares)
    if found == True:
        num = singleIndex(boardSquares, sqrow)
        row, index = squareConvert(sqrow, sqindex)
        board[row][index] = num
        #printboard(board)
        return

    singles(board, boardcopy, boardColumns, boardSquares)
    hiddendoubles(boardcopy)
    hiddensingle(boardcopy, origboard)


# origboard = [
#     [2, 0, 8, 7, 3, 4, 6, 0, 1],
#     [0, 0, 0, 0, 0, 6, 7, 3, 5],
#     [0, 3, 0, 0, 0, 0, 8, 2, 4],
#     [5, 0, 9, 0, 8, 0, 0, 0, 3],
#     [0, 0, 4, 3, 0, 9, 1, 0, 2],
#     [0, 0, 3, 0, 4, 0, 5, 0, 9],
#     [4, 8, 0, 2, 0, 0, 9, 1, 7],
#     [0, 0, 7, 4, 1, 0, 0, 0, 6],
#     [0, 6, 2, 9, 7, 5, 3, 4, 8]
# ]

origboard = [
    [3, 2, 7, 0, 9, 0, 0, 0, 0],
    [8, 6, 0, 5, 0, 7, 3, 4, 9],
    [4, 0, 0, 0, 0, 1, 6, 0, 2],
    [2, 0, 6, 1, 8, 9, 0, 5, 0],
    [0, 0, 4, 7, 6, 2, 9, 0, 0],
    [0, 1, 0, 0, 4, 5, 2, 6, 8],
    [1, 0, 0, 4, 5, 0, 8, 0, 0],
    [6, 0, 0, 0, 0, 8, 5, 0, 0],
    [9, 5, 0, 2, 0, 3, 4, 0, 6]
]


zero = zeroCounter(origboard)
while(zero != 0):
    sudoku(origboard)
    zero = zeroCounter(origboard)
printboard(origboard)
print("Finished Sudoku. ")




