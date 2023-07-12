#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255
MARGIN = 5
background_colour = (234, 212, 252)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minesweeper')
SCREEN.fill(background_colour)

MAP_DETAILS = {
    "x": 9,
    "y": 9,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines


class Tile:

    num_value = 0
    hidden = True


def get_random_coords(rows, columns, map):
    row_index = randint(0, rows - 1)
    column_index = randint(0, columns - 1)
    if map[row_index][column_index] != -1:
        return [row_index, column_index]
    else:
        return get_random_coords(rows, columns, map)


def crate_field(rows, columns, mines, map):
    map = [[Tile() for _ in range(columns)] for _ in range(rows)]
    for i in range(mines):
        [row_index, column_index] = get_random_coords(rows, columns, map)
        map[row_index][column_index].num_value = -1
        count_mines(map, row_index, column_index)

    return map


def count_mines(map, y, x):
    if y-1 > -1 and map[y-1][x].num_value != -1:
        map[y-1][x].num_value += 1  # north
    if x+1 < len(map[0]) and map[y][x+1].num_value != -1:
        map[y][x+1].num_value += 1  # east
    if y+1 < len(map) and map[y+1][x].num_value != -1:
        map[y+1][x].num_value += 1  # south
    if x-1 > -1 and map[y][x-1].num_value != -1:
        map[y][x-1].num_value += 1  # west
    if y-1 > -1 and x+1 < len(map[0]) and map[y-1][x+1].num_value != -1:
        map[y-1][x+1].num_value += 1  # north-east
    if y+1 < len(map) and x+1 < len(map[0]) and map[y+1][x+1].num_value != -1:
        map[y+1][x+1].num_value += 1  # south-east
    if y+1 < len(map) and x-1 > -1 and map[y+1][x-1].num_value != -1:
        map[y+1][x-1].num_value += 1  # south-west
    if y-1 > -1 and x-1 > -1 and map[y-1][x-1].num_value != -1:
        map[y-1][x-1].num_value += 1  # north-west


def drawGrid(field):
    color = (255, 255, 255)
    blocksize = 20
    font = pygame.font.SysFont('arial', 20)

    sprite_map = []

    for row in range(MAP_DETAILS["x"]):
        for column in range(MAP_DETAILS["y"]):
            content = str(field[row][column].num_value)
            text = font.render(content, True, (0, 0, 0))
            rect = pygame.draw.rect(SCREEN,
                                    color,
                                    [(MARGIN + blocksize) * column + MARGIN,
                                     (MARGIN + blocksize) * row + MARGIN,
                                        blocksize,  # height
                                        blocksize])  # width
            SCREEN.blit(text, rect)
            sprite_map.append(rect)

    return sprite_map
    


def main():
    pygame.init()

    field = []
    field = crate_field(
        MAP_DETAILS["x"], MAP_DETAILS["y"], MAP_DETAILS["mines"], field)
    headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    num_map = []
    
    for row in field:
        new_line = []
        for tile in row:
            new_line.append(tile.num_value)
        num_map.append(new_line)

    print(tabulate(num_map, headers, tablefmt="grid"))
    print(drawGrid(field))

    pygame.display.flip()
    running = True
    while running:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (SCREEN_WIDTH + MARGIN)
                row = pos[1] // (SCREEN_HEIGHT + MARGIN)
                print (pos)


main()
