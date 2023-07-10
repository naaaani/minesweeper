#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
background_colour = (234, 212, 252)
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Minesweeper')
SCREEN.fill(background_colour)

map_details = {
    "x": 9,
    "y": 9,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines

def get_random_coords(rows, columns, map):
        row_index = randint(0, rows - 1)
        column_index = randint(0, columns - 1)
        if map[row_index][column_index] != -1:
            return [row_index, column_index]
        else:
            return get_random_coords(rows, columns, map)

def crate_field(rows, columns, mines, map):
    map = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(mines):
        [row_index, column_index] = get_random_coords(rows, columns, map)
        map[row_index][column_index] = -1
        count_mines(map, row_index, column_index)

    return map

def count_mines(map, y, x):
    if y-1 > -1 and map[y-1][x] != -1: map[y-1][x] += 1                                     #north
    if x+1 < len(map[0]) and map[y][x+1] != -1: map[y][x+1] += 1                            #east
    if y+1 < len(map) and map[y+1][x] != -1: map[y+1][x] += 1                               #south
    if x-1 > -1 and map[y][x-1] != -1: map[y][x-1] += 1                                     #west
    if y-1 > -1 and x+1 < len(map[0]) and map[y-1][x+1] != -1: map[y-1][x+1] += 1           #north-east    
    if y+1 < len(map) and x+1 < len(map[0]) and map[y+1][x+1] != -1: map[y+1][x+1] += 1     #south-east
    if y+1 < len(map) and x-1 > -1 and map[y+1][x-1] != -1: map[y+1][x-1] += 1              #south-west
    if y-1 > -1 and x-1 > -1 and map[y-1][x-1] != -1: map[y-1][x-1] += 1                    #north-west

def drawGrid():
    blockSize = 20
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, (0, 0, 0), rect, 1)

def main():
    field = []
    field = crate_field(map_details["x"], map_details["y"], map_details["mines"], field)
    headers = ["A","B","C","D","E","F","G","H","I"]
    print(tabulate(field, headers, tablefmt="grid"))

    drawGrid()
    pygame.display.flip()
    running = True
    while running:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False


main()