from random import randint

from Tile import Tile

class Map():
    def __init__(self):
        self.map = []
        
    def get_random_coord(self, row_count, column_count) -> tuple[int, int]:
        row_index = randint(0, row_count - 1)
        column_index = randint(0, column_count - 1)

        current_tile: Tile = self.map[row_index][column_index]

        if not current_tile.is_mine():
            return [row_index, column_index]
        else:
            return self.get_random_coord(row_count, column_count)

    def create_map(self, row_count, column_count, mine_count):
        self.column_count = column_count
        self.row_count = row_count
        self.map = [[Tile(x, y) for x in range(column_count)]
                for y in range(row_count)]
        for _ in range(mine_count):
            [row_index, column_index] = self.get_random_coord(row_count, column_count)
            self.set_mine(row_index, column_index)
            self.count_num_values_around_mine(row_index, column_index)
            
    def count_num_values_around_mine(self, y, x):
        if y-1 > -1 and self.map[y-1][x].num_value != -1:
            self.map[y-1][x].num_value += 1  # north
        if x+1 < len(self.map[0]) and self.map[y][x+1].num_value != -1:
            self.map[y][x+1].num_value += 1  # east
        if y+1 < len(self.map) and self.map[y+1][x].num_value != -1:
            self.map[y+1][x].num_value += 1  # south
        if x-1 > -1 and self.map[y][x-1].num_value != -1:
            self.map[y][x-1].num_value += 1  # west
        if y-1 > -1 and x+1 < len(self.map[0]) and self.map[y-1][x+1].num_value != -1:
            self.map[y-1][x+1].num_value += 1  # north-east
        if y+1 < len(self.map) and x+1 < len(self.map[0]) and self.map[y+1][x+1].num_value != -1:
            self.map[y+1][x+1].num_value += 1  # south-east
        if y+1 < len(self.map) and x-1 > -1 and self.map[y+1][x-1].num_value != -1:
            self.map[y+1][x-1].num_value += 1  # south-west
        if y-1 > -1 and x-1 > -1 and self.map[y-1][x-1].num_value != -1:
            self.map[y-1][x-1].num_value += 1  # north-west

    def set_mine(self, row, column):
        self.map[row][column].set_mine()

    def get_map(self) -> list[list]:
        return self.map
    
    def get_column_count(self):
        return self.column_count
    
    def get_row_count(self):
        return self.row_count
