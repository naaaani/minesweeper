from random import randint

from Tile import Tile

class Game():
    def __init__(self):
        self.map = []
        
    def get_random_coord(self, row_count, column_count) -> tuple[int, int]:
        row_index = randint(0, row_count - 1)
        column_index = randint(0, column_count - 1)

        currentTile: Tile = self.map[row_index][column_index]

        if not self.map[row_index][column_index].is_mine():
            return [row_index, column_index]
        else:
            return self.get_random_coord(row_count, column_count)

    def crate_field(self, row_count, column_count, mine_count):
        self.map = [[Tile(x, y) for x in range(column_count)]
                for y in range(row_count)]
        for _ in range(mine_count):
            [row_index, column_index] = self.get_random_coord(row_count, column_count)
            self.set_mine(row_index, column_index)

    def set_mine(self, row, column):
        self.map[row][column].set_mine()

    def get_field(self) -> list[list]:
        return self.map
