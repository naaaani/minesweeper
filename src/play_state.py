import pygame
from math import floor

from abstract_state import AbstractState
from map import Map
from Tile import Tile

class Play(AbstractState):
    def __init__(self, game):
        self.game = game
        (self.screen_width, self.screen_height,) = self.game.get_screen_dim()
        self.screen = pygame.display.get_surface()
        self.side_panel = self.create_side_panel()
        self.game_grid = self.create_game_grid()
        self.map: Map = Map()
        self.map.create_map(10, 10, 10)
            
    def get_name(self):
        return "play"
    
    def draw_grid(self):
        white = (255, 255, 255)
        font = pygame.font.SysFont('Arial', 50)
        
        field = self.map.get_map()
        
        sidepanel = self.create_side_panel()
        sidepanel_horizontal_position = self.screen_width - sidepanel.get_width()
        self.screen.blit(sidepanel, (sidepanel_horizontal_position, 0))
        
        game_grid = self.create_game_grid()
        game_grid_position = (0, 0)
        self.screen.blit(game_grid, game_grid_position)

        for row in range(10):
            for column in range(10):
                color = white
                current_tile: Tile = field[row][column]
                if current_tile.is_mine():
                    color = (0, 0, 0)
                if current_tile.is_flagged():
                    color = (255, 0, 0)
                
                rect_width = 0
                grid_width = game_grid.get_width()
                grid_height = game_grid.get_height()
                column_count = self.map.get_column_count()          
                
                if grid_height <= grid_width:
                    rect_width = grid_width / (column_count + 1)
                elif grid_height > grid_width:
                    rect_width = grid_height / (column_count + 1)
                                
                rect_height = rect_width
                margin = rect_width / 10
                
                rectangle = pygame.Rect((margin + rect_width) * column + margin,
                                         (margin + rect_height) * row + margin,
                                         rect_width,
                                         rect_height)
            
                pygame.draw.rect(surface=game_grid, color=color, rect=rectangle)
                
                if not current_tile.is_hidden():
                    content = str(current_tile.num_value)
                    text = font.render(content, True, (0, 0, 0))
                    game_grid.blit(text, rectangle)
        
        self.screen.blit(game_grid, game_grid_position)
     
    def create_side_panel(self) -> pygame.Surface:
        width = floor(pygame.display.get_surface().get_width() / 4)
        height = self.screen_height
        
        sidepanel = pygame.Surface(size=(width, height))
        sidepanel.fill((0,0,0))
        return sidepanel
    
    def create_game_grid(self) -> pygame.Surface:
        width = (self.screen_width - self.side_panel.get_width() - 10)
        height = width
        
        game_grid = pygame.Surface(size=(width, height), flags=pygame.RESIZABLE)
        game_grid.fill((0, 0, 255))
        return game_grid
        
    def activate(self):
        self.draw_grid()

    def deactivate(self):
        pass

    def proc_event(self, event):
      pass
    
    def update(self):
        window = pygame.display.get_surface()
        (self.screen_width, self.screen_height) = (window.get_width(), window.get_height())
        self.draw_grid()
        pygame.display.update()
                
    def handle_right_click(self, row, column):
        target_tile: Tile = self.map[row][column]
        target_tile.set_flag()
        
    def handle_left_click(self, row, column):
        target_tile: Tile = self.map.get_map()[row][column]
        if target_tile.is_mine():
            print("You lose")
        elif target_tile.is_hidden():
            target_tile.uncover()
        print(target_tile.is_hidden())