import pygame
from pygame_button import Button
from abstract_state import AbstractState

class Menu(AbstractState):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ORANGE = (255, 180, 0)

    def __init__(self, game):

        self.game = game
        self.screen = self.game.get_screen() 
        self.create_button()
        self.create_title()

    def activate(self):
        pass
            
    def get_name(self):
        return "menu"

    def create_button(self):

        (width, height,) = self.game.get_screen_dim()
        button_width = width / 4
        button_height = height / 4

        style = {
            "hover_color": Menu.BLUE,
            "clicked_color": Menu.GREEN,
            "clicked_font_color": Menu.BLACK,
            "hover_font_color": Menu.ORANGE
        }
        self.button = Button(
            (0, 0, button_width, button_height), Menu.RED, self.press, text="Start", **style
        )
        self.button.rect.center = (width / 2, height / 4 * 3)

    def create_title(self):

        font = pygame.font.SysFont('Arial', 50)
        self.title_surface = font.render('Minesweeper', False, (20, 20, 40,))
        (screen_width, screen_height,) = self.game.get_screen_dim()
        (title_width, title_height,) = self.title_surface.get_size()
        self.title_x = (screen_width / 2) - (title_width / 2)
        self.title_y = (screen_height / 4) - (title_height / 2)
    
    def proc_event(self, event):       
        self.button.check_event(event)
       
    def press(self):
        self.game.menu_start_pressed()

    def update(self):
        self.button.update(self.screen)
        self.screen.blit(self.title_surface, (self.title_x, self.title_y,))

    def proc_event(self, event):       
        self.button.check_event(event)