import pygame

from abstract_state import AbstractState
from map import Map
from Tile import Tile

class Play(AbstractState):
    def __init__(self, game, number_of_mines):
        self.game = game
        self.number_of_mines = number_of_mines
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
        margin = 5
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
                    
                rect_width = game_grid.get_width() / self.number_of_mines
                rect_height = rect_width
                
                rectangle = pygame.Rect((margin + rect_width) * column + margin,
                                         (margin + rect_height) * row + margin,
                                         rect_width,
                                         rect_height)
            
                rect = pygame.draw.rect(surface=game_grid, color=color, rect=rectangle)
                
                if not current_tile.is_hidden():
                    content = str(current_tile.num_value)
                    text = font.render(content, True, (0, 0, 0))
                    game_grid.blit(text, rect)
                            
    def create_side_panel(self) -> pygame.surface:
        width = self.screen_width / 4
        height = self.screen_height
        
        sidepanel = pygame.Surface(size=(width, height))
        sidepanel.fill((0,0,0))
        return sidepanel
    
    def create_game_grid(self) -> pygame.surface:
        width = (self.screen_width - 200 - 10)
        height = width
        
        game_grid = pygame.Surface(size=(width, height), flags=pygame.SCALED)
        game_grid.fill((0, 0, 255))
        return game_grid
        
    def activate(self):
        self.draw_grid()

    def deactivate(self):
        pass

    def proc_event(self, event):
        pass
        # if event.type == pygame.MOUSEBUTTONUP:
        #     mouse_pos = pygame.mouse.get_pos()
        #     column = mouse_pos[0] // (20 + 5)
        #     row = mouse_pos[1] // (20 + 5)
        #     print(row, column)

        #     if row >= 10 or column >= 10:
        #         pass
        #     if event.button == 3:
        #         self.handle_right_click(row, column)
        #     elif event.button == 1:
        #         self.handle_left_click(row, column)
        #     if event.type == pygame.VIDEORESIZE:
        #         pygame.display.update()
    
    def update(self):
        self.draw_grid()
                
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