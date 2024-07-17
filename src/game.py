#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

from Tile import Tile
from Screen_Details import Screen_Details
from src.map import Map

MAP_DETAILS = {
    "x": 10,
    "y": 10,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines

def draw_table(field):
    headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    num_map = []

    for row in field:
        new_line = []
        for tile in row:
            new_line.append(tile.num_value)
        num_map.append(new_line)

    print(tabulate(num_map, headers, tablefmt="grid"))


def draw_grid(field, screen_details: Screen_Details, screen_surface: pygame.surface):
    white = (255, 255, 255)
    margin = 5
    block_width = screen_surface.get_height() / (MAP_DETAILS["x"] + margin)
    block_height = block_width

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
    screen_details = Screen_Details(255, 255, (0, 0, 0), font="Arial")

    screen: pygame.surface = pygame.display.set_mode(
        size=(screen_details.screen_width, screen_details.screen_height), flags=pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption('Minesweeper')
    screen.fill(screen_details.background_color)

    map: Map = Map()
    map.create_map(
        MAP_DETAILS["x"], MAP_DETAILS["y"], MAP_DETAILS["mines"])
    field = map.get_map()

    draw_table(field)
    draw_grid(field, screen_details, screen)

    pygame.display.flip()

    running = True
    while running:
        pygame.event.pump()
        pygame.display.flip()
        draw_grid(field, screen_details, screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
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
            if event.type == pygame.VIDEORESIZE:
                pygame.display.update()

main()
