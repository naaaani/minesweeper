#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

from Tile import Tile
from Screen_Details import Screen_Details

MAP_DETAILS = {
    "x": 10,
    "y": 10,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines


def get_random_coord(game_map, row_count, column_count) -> list[int, int]:
    row_index = randint(0, row_count - 1)
    column_index = randint(0, column_count - 1)
    if game_map[row_index][column_index] != -1:
        return [row_index, column_index]
    else:
        return get_random_coord(game_map, row_count, column_count)


def crate_field(row_count, column_count, mine_count) -> list[list[int, int]]:
    field = [[Tile(x, y) for x in range(column_count)]
             for y in range(row_count)]
    for _ in range(mine_count):
        [row_index, column_index] = get_random_coord(
            field, row_count, column_count)
        field[row_index][column_index].set_mine()
        count_mines(field, row_index, column_index)

    return field


def count_mines(map, y, x) -> int:
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


def draw_grid(field, screen_details, screen_surface):
    white = (255, 255, 255)
    block_width = 20
    block_height = block_width
    margin = 5

    for row in range(MAP_DETAILS["x"]):
        for column in range(MAP_DETAILS["y"]):
            color = white
            current_tile: Tile = field[row][column]
            if current_tile.is_mine():
                color = (0, 0, 0)
            if current_tile.is_flagged():
                color = (255, 0, 0)
            rect = pygame.draw.rect(screen_surface,
                             color,
                             pygame.Rect((margin + block_width) * column + margin,
                                         (margin + block_height) * row + margin,
                                         block_width,
                                         block_height))
            if not current_tile.is_hidden():
                content = str(current_tile.num_value)
                text = screen_details.font.render(content, True, (0, 0, 0))
                screen_surface.blit(text, rect)

    # TODO function to put stg at [x,y]

def handle_right_click(field, row, column):
    target_tile: Tile = field[row][column]
    target_tile.set_flag()
        
def handle_left_click(field, row, column):
    target_tile: Tile = field[row][column]
    if target_tile.is_mine():
        print("You lose")
    elif target_tile.is_hidden():
        target_tile.uncover()
    print(target_tile.is_hidden())

def main():
    pygame.init()
    display = Screen_Details(255, 255, (0, 0, 0), font="Arial")

    screen = pygame.display.set_mode(
        (display.screen_width, display.screen_height))
    pygame.display.set_caption('Minesweeper')
    screen.fill(display.background_color)

    field = crate_field(
        MAP_DETAILS["x"], MAP_DETAILS["y"], MAP_DETAILS["mines"])

    draw_table(field)
    draw_grid(field, display, screen)

    pygame.display.flip()

    running = True
    while running:
        pygame.display.flip()
        draw_grid(field, display, screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                column = mouse_pos[0] // (20 + 5)
                row = mouse_pos[1] // (20 + 5)
                print(row, column)

                if row >= MAP_DETAILS["x"] or column >= MAP_DETAILS["y"]:
                    break
                if event.button == 3:
                    handle_right_click(field, row, column)
                elif event.button == 1:
                    handle_left_click(field, row, column)

main()
