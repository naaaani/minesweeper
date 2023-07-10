#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

WINDOW_WIDTH = 255
WINDOW_HEIGHT = 255
background_colour = (234, 212, 252)
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Minesweeper')
SCREEN.fill(background_colour)

MAP_DETAILS = {
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
    if y-1 > -1 and map[y-1][x] != -1:
        map[y-1][x] += 1  # north
    if x+1 < len(map[0]) and map[y][x+1] != -1:
        map[y][x+1] += 1  # east
    if y+1 < len(map) and map[y+1][x] != -1:
        map[y+1][x] += 1  # south
    if x-1 > -1 and map[y][x-1] != -1:
        map[y][x-1] += 1  # west
    if y-1 > -1 and x+1 < len(map[0]) and map[y-1][x+1] != -1:
        map[y-1][x+1] += 1  # north-east
    if y+1 < len(map) and x+1 < len(map[0]) and map[y+1][x+1] != -1:
        map[y+1][x+1] += 1  # south-east
    if y+1 < len(map) and x-1 > -1 and map[y+1][x-1] != -1:
        map[y+1][x-1] += 1  # south-west
    if y-1 > -1 and x-1 > -1 and map[y-1][x-1] != -1:
        map[y-1][x-1] += 1  # north-west


def drawGrid():
    color = (255, 255, 255)
    MARGIN = 5
    BLOCKSIZE = 20

    for row in range(MAP_DETAILS["x"]):    
        for column in range(MAP_DETAILS["y"]):
            pygame.draw.rect(SCREEN,
                             color,
                             [(MARGIN + BLOCKSIZE) * column + MARGIN,
                                 (MARGIN + BLOCKSIZE) * row + MARGIN,
                                 BLOCKSIZE,
                                 BLOCKSIZE])


def main():
    field = []
    field = crate_field(
        MAP_DETAILS["x"], MAP_DETAILS["y"], MAP_DETAILS["mines"], field)
    headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    print(tabulate(field, headers, tablefmt="grid"))

    drawGrid()
    pygame.display.flip()
    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


main()
