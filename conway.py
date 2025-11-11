#!/bin/python

import random
import time
import copy


def update_matrix():
    global matrix
    for y in range(height):
        for x in range(width):
            amount = get_neighbors_count(x, y)
            if amount == 2 and matrix[y][x] == 1 or amount == 3:
                matrix_buffer[y][x] = 1
            else:
                matrix_buffer[y][x] = 0
    matrix = copy.deepcopy(matrix_buffer)


def get_neighbors_count(x_input, y_input):
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if matrix[int((y_input + y) % height)][int((x_input + x) % width)] and (x != 0 or y != 0):
                count += 1
    return count


def render_matrix_terminal():
    print_buffer = ""
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 0:
                print_buffer = print_buffer + " "
            else:
                print_buffer = print_buffer + "#"
        print_buffer = print_buffer + "\n" 
    print(print_buffer)


width = 239
height = 75

matrix = [[random.randint(0,1) for i in range(width)] for i in range(height)]

matrix_buffer = copy.deepcopy(matrix)

while True:
    render_matrix_terminal()
    time.sleep(.1)
    update_matrix()
