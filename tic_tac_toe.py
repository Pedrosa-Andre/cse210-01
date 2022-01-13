from array import array
import os
clear = lambda: os.system('clear')

board = '123456789'
grid = '.|.|.\n-+-+-\n.|.|.\n-+-+-\n.|.|.\n'

def display_grid(board):
    y = 0
    for x in grid:
        if (x == '.'):
            print(board[y], end = '')
            y += 1
        else:
            print(x, end = '')
    print('')

def has_winner(board):
    x = y = 0
    for i in range(len(board)):
        if (board[i] == 'x'):
            x += 2**i
        if (board[i] == 'y'):
            y += 2**i
    if (x in [7,56,448,73,146,292,84,273]):
        print('Winner X')
    if (y in [7,56,448,73,146,292,84,273]):
        print('Winner Y')


clear();
display_grid(board)
has_winner('xy.xy.x..')
print()
has_winner('xxyxy.y..')
print()
has_winner('x.xyyy...')