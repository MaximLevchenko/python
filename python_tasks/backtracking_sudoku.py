import copy
from itertools import *
'''
def print_board(bd):
    for i in range(len(Board)):
        if i % 1 == 0 and i != 0:
            print('- - -  ')
        for j in range(len(bd[0])):
            if j % 1 == 0 and j != 0:
                print('|', end='')
            if j==2:
                print(bd[i][j])
            else:
                print(str(bd[i][j]), end='')
def find_empty(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j]==0:
                return i,j  #column, row


print_board(Board)
'''

Board = [[0, 0, 0],
         [1, 0, 0],
         [0, 3, 1]]
def is_distinct(list_of_nums):
    used_nums=[]
    for i in list_of_nums:
        if i==0:
            continue#continue is used to start the iteration again with another num in the loop
        if i in used_nums:
            return False
        else:
            used_nums.append(i)
    return True


def is_valid(bd):
    for i in range(len(Board)):
        row=[bd[i][0],bd[i][1],bd[i][2]]
        if not is_distinct(row):
            return False
        col=[bd[0][i],bd[1][i], bd[2][i]]
        if not is_distinct(col):
            return False
    return True

def solve( brd , empties = 9):
    '''
      Solves a mini-Sudoku
      brd is the board
      empty is the number of empty cells
    '''

    if empties == 0:
        #Base case
        return is_valid( brd )
    for row,col in product(range(3), repeat=2):
        cell=brd[row][col]
        if cell!=0:
            continue
        brd2 = brd
        for test in [1, 2, 3]:
            brd2[row][col] = test
            if is_valid(brd2) and solve(brd2, empties - 1):
                return True
            # BackTrack
            brd2[row][col] = 0
    return False

solve(Board, 6)
for row in Board:#Prints a solution
    print(row)