#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate
from math import floor

from Tile import Tile
from Screen import Screen

MAP_DETAILS = {
    "x": 9,
    "y": 9,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines

def get_random_coords(field, row_count, column_count):
    row_index = randint(0, row_count - 1)
    column_index = randint(0, column_count - 1)
    if field[row_index][column_index] != -1:
        return [row_index, column_index]
    else:
        return get_random_coords(field, row_count, column_count)

def crate_field(row_count, column_count, mine_count):
    field = [[Tile(x, y) for x in range(column_count)] for y in range(row_count)]
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

def draw_table(field):
    headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    num_map = []
    
    for row in field:
        new_line = []
        for tile in row:
            new_line.append(tile.num_value)
        num_map.append(new_line)

    print(tabulate(num_map, headers, tablefmt="grid"))

def draw_grid(field, display, screen):
    color = (255, 255, 255)
    block_height = (display.screen_height - display.menu_margin -
                     display.map_margin) / MAP_DETAILS["y"]
    block_width = block_height
    font = pygame.font.SysFont('arial', 20)
    side_margin = (display.screen_width - (display.map_margin * 2)  - (MAP_DETAILS["y"] * block_width)) / 2 

    for row in range(MAP_DETAILS["x"]):
        for column in range(MAP_DETAILS["y"]):
            #TODO function to put stg at [x,y]
            content = str(field[row][column].num_value)
            text = font.render(content, True, (0, 0, 0))

            rect_left = (block_height) * column + display.map_margin + side_margin
            rect_top = (block_width) * row  + display.map_margin + display.menu_margin

            rect = pygame.draw.rect(
                screen, 
                color,
                pygame.Rect(rect_left, rect_top, block_height, block_width)        
            )

            screen.blit(text, rect)
    
def is_clicked(tile, click_coords):
    low_value = tile[0]
    square_lenght = tile[2]
    high_value = low_value + square_lenght

    if click_coords[0] > low_value and click_coords[0] < high_value:
        return True
    return False

def main():
    pygame.init()
    display = Screen(800, 600, (234, 212, 252))

    screen = pygame.display.set_mode((display.screen_width, display.screen_height))
    pygame.display.set_caption('Minesweeper')
    screen.fill(display.background_color)


    field = crate_field(
        MAP_DETAILS["x"], MAP_DETAILS["y"], MAP_DETAILS["mines"])
    
    draw_table(field)

    draw_grid(field, display, screen)
    
    pygame.display.flip()

    block_width = (display.screen_height - display.menu_margin -
                    display.map_margin) / MAP_DETAILS["y"]
    side_margin = (display.screen_width - (display.map_margin * 2) -
                    (MAP_DETAILS["y"] * block_width)) / 2
    side_margin = (display.screen_width - (display.map_margin * 2) -
                    (MAP_DETAILS["y"] * block_width)) / 2 

    running = True
    while running:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos() #TODO calculate tile clicked
                print(mouse_pos)
                print(floor((mouse_pos[0] - side_margin -
                             display.menu_margin) / block_width))

main()
