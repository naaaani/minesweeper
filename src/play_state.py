import pygame

from abstract_state import AbstractState
from map import Map
from Tile import Tile

class Play(AbstractState):
    def __init__(self, game, number_of_mines):
        self.game = game
        self.number_of_mines = number_of_mines
        (self.screen_width, self.screen_height,) = self.game.get_screen_dim()
        self.screen = self.game.get_screen()
        
        self.map: Map = Map()
        self.map.create_map(10, 10, 10)
            
    def get_name(self):
        return "play"
    
    def draw_grid(self):
        white = (255, 255, 255)
        margin = 5
        block_width = self.screen_height / (self.game.number_of_mines + margin)
        block_height = block_width
        
        field = self.map.get_map()

        for row in range(10):
            for column in range(10):
                color = white
                current_tile: Tile = field[row][column]
                if current_tile.is_mine():
                    color = (0, 0, 0)
                if current_tile.is_flagged():
                    color = (255, 0, 0)
                rect = pygame.draw.rect(self.screen,
                                 color,
                                 pygame.Rect((margin + block_width) * column + margin,
                                         (margin + block_height) * row + margin,
                                         block_width,
                                         block_height))
                if not current_tile.is_hidden():
                    content = str(current_tile.num_value)
                    text = 'Arial'.render(content, True, (0, 0, 0))
                    self.screen.blit(text, rect)
    
    def activate(self):
        self.draw_grid()

    def deactivate(self):
        pass

    def proc_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            column = mouse_pos[0] // (20 + 5)
            row = mouse_pos[1] // (20 + 5)
            print(row, column)

            if row >= 10 or column >= 10:
                pass
            if event.button == 3:
                self.handle_right_click(row, column)
            elif event.button == 1:
                self.handle_left_click(row, column)
            if event.type == pygame.VIDEORESIZE:
                pygame.display.update()
    
    def update(self):
        self.draw_grid()
                
    def handle_right_click(self, row, column):
        print(row, column)
        target_tile: Tile = self.map[row][column]
        target_tile.set_flag()
        
    def handle_left_click(self, row, column):
        target_tile: Tile = self.map.get_map()[row][column]
        if target_tile.is_mine():
            print("You lose")
        elif target_tile.is_hidden():
            target_tile.uncover()
        print(target_tile.is_hidden())