#!/usr/bin/env python3
import pygame
from random import randint
from tabulate import tabulate

map_details = {
    "x": 9,
    "y": 9,
    "mines": 10,
}

# also 13*15 with 40 mines, 16*30 with 99 mines

def crate_field(rows, columns, mines, map):
    map = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(mines):
        row_index = randint(0, rows - 1)
        column_index = randint(0, columns - 1)
        map[row_index][column_index] = -1

    return map


def count_mines(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] != -1:
                try:
                    if map[x-1][y-1] == -1 and y > 0 and x > 0:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')

                try:
                    if map[x][y-1] == -1 and y > 0:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')

                try:
                    if map[x+1][y-1] == -1 and y > 0:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')
                
                try:
                    if map[x-1][y] == -1 and x > 0:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')
                    
                try:
                    if map[x+1][y] == -1:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')

                try:
                    if map[x-1][y+1] == -1 and x > 0:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')
                
                try:
                    if map[x][y+1] == -1:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')

                try:
                    if map[x+1][y+1] == -1:
                        map[x][y] += 1

                except IndexError:
                    print('Out of bounds')

def main():

    field = []
    field = crate_field(map_details["x"], map_details["y"], map_details["mines"], field)
    headers = ["A","B","C","D","E","F","G","H","I"]
    count_mines(field)
    print(tabulate(field, headers, tablefmt="grid"))

main()
