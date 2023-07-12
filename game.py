#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255
MARGIN = 5
BACKGROUND_COLOR = (234, 212, 252) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minesweeper')
screen.fill(BACKGROUND_COLOR)

MAP_DETAILS = {
    "x": 9,
    "y": 9,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines


class Tile():

    num_value = 0
    hidden = True
    def set_mine(self):
        self.num_value = -1


def get_random_coords(field, row_count, column_count):
    row_index = randint(0, row_count - 1)
    column_index = randint(0, column_count - 1)
    if field[row_index][column_index] != -1:
        return [row_index, column_index]
    else:
        return get_random_coords(field, row_count, column_count)

def crate_field(row_count, column_count, mine_count):
    field = [[Tile() for _ in range(column_count)] for _ in range(row_count)]
    for i in range(mine_count):
        [row_index, column_index] = get_random_coords(field, row_count, column_count)
        field[row_index][column_index].set_mine()
        count_mines(field, row_index, column_index)

    return field

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

def draw_grid(field): # TODO separate this into create, draw
    color = (255, 255, 255)
    blocksize = 20
    font = pygame.font.SysFont('arial', 20)

    sprite_map = []

    for row in range(MAP_DETAILS["x"]):
        for column in range(MAP_DETAILS["y"]):
            #TODO function to put stg at [x,y]
            content = str(field[row][column].num_value)
            text = font.render(content, True, (0, 0, 0))
            rect = pygame.draw.rect(
                screen, 
                color,                    
                [
                    (MARGIN + blocksize) * column + MARGIN,
                    (MARGIN + blocksize) * row + MARGIN,
                    blocksize,  # height
                    blocksize   # width
                ]
            )
            screen.blit(text, rect)
            sprite_map.append(rect)

    return sprite_map
    
def is_clicked(tile, click_coords):
    low_value = tile[0]
    square_lenght = tile[2]
    high_value = low_value + square_lenght

    if click_coords[0] > low_value and click_coords[0] < high_value:
        return True
    return False

def main():
    pygame.init()

    field = crate_field(
        MAP_DETAILS["x"], MAP_DETAILS["y"], MAP_DETAILS["mines"])
    headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    num_map = []
    
    for row in field:
        new_line = []
        for tile in row:
            new_line.append(tile.num_value)
        num_map.append(new_line)

    print(tabulate(num_map, headers, tablefmt="grid"))
    sprite_map = draw_grid(field) #TODO storing of coords not needed
    print(sprite_map)
    pygame.display.flip()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for tile in sprite_map:
                    if is_clicked(tile, pos): #TODO find tile by pos
                        print('hit')
                        break

main()
