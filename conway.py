#!/bin/python
import sys
import random
import time
import copy

def neighbors(xinput, yinput):
    count = 0
    for xscan in range(-1,2):
        for yscan in range(-1,2):
            if xscan != 0 or yscan != 0:
                    count +=  matrix[int((yinput + yscan) % height)][int((xinput + xscan) % width)]
    return count

def update():
    for y in range(height):
        for x in range(width):
            amount = neighbors(x, y)
            if amount == 2:
                if matrix[y][x] == 0:
                    matrix_buffer[y][x] = 0
                else:
                    matrix_buffer[y][x] = 1
            elif amount == 3:
                matrix_buffer[y][x] = 1
            else:
                matrix_buffer[y][x] = 0

def printmatrix():
    printbuffer = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 0:
                printbuffer = printbuffer + " "
            elif matrix[y][x] == 1:
                printbuffer = printbuffer + "#"
            else:
                print("ERROR")
        printbuffer = printbuffer + "\n" 
    print(printbuffer)

width = 239
height = 75

matrix = [[random.randint(0,1) for i in range(width)] for i in range(height)]

matrix_buffer = copy.deepcopy(matrix)
while True:
    printmatrix()
    time.sleep(0.1)
    update()
    matrix = copy.deepcopy(matrix_buffer)
