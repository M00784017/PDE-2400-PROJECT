from __future__ import division
import time
import os
import sys
import optparse
import random

import opc

# command line
parser = optparse.OptionParser()
parser.add_option('-s', '--server', dest='server', default='127.0.0.1:7890',
                    action='store', type='string',
                    help='ip and port of server')
parser.add_option('-f', '--fps', dest='fps', default=10,
                    action='store', type='int',
                    help='frames per second')
options, args = parser.parse_args()

X_DIM = 90
Y_DIM = 90

def print_board(board):
    for x in range(X_DIM):
        for y in range(Y_DIM):
            if board[x+y*X_DIM]==1:
                
                print ('X')
            else:
                print('.')

                
                
       
        

def rand_board():
    board = [0] * X_DIM * Y_DIM
    for x in range(X_DIM):
        for y in range(Y_DIM):
            if not random.randint(0,2):
                board[x+y*X_DIM] = 1
    return board

def count_cell_neighbor(x,y, board):
    neighbor_count = 0
    for nei_x in range(-1,2):
        if (x+nei_x<0) or (x+nei_x>=X_DIM):
            continue
        for nei_y in range(-1,2):
            if (y+nei_y<0) or (y+nei_y>=Y_DIM) or (nei_x == 0 and nei_y == 0):
                continue
            neighbor_count += board[(x+nei_x)+(y+nei_y)*X_DIM]
    return neighbor_count

def tick(board):
    new_board = board[:]
    for x in range(X_DIM):
        for y in range(Y_DIM):
            n = count_cell_neighbor(x,y, board)
            if n < 2 or n > 3:
                new_board[x+y*X_DIM] = 0
            elif n == 3:
                new_board[x+y*X_DIM] = 1
    return new_board	

def pixelify_board(board):
    pixels = []
    for cell in board:
        pixels.append((130, 150, 120) if cell else (0,0,0))
    return pixels

def pixelify_triboard(r,g,b):
    pixels = []
    for rcell, gcell, bcell in zip(r,g,b):
        print( rcell,gcell,bcell)
        color = (130 if rcell else 0, 130 if gcell else 0, 130 if bcell else 0)
        pixels.append(color)
    return pixels

board = rand_board()


client = opc.Client(options.server)
while True:
    client.put_pixels(pixelify_board(board), channel=0)
    board = tick(board)
    time.sleep(1 / options.fps)
