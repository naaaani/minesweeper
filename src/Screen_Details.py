import pygame

class Screen_Details():

    def __init__(self, screen_width, screen_height, background_color, font):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu_margin = self.screen_height / 20
        self.map_margin = self.screen_width / 20
        self.background_color = background_color
        self.font = pygame.font.SysFont('arial', 20)

    def set_width(self, screen_width):
        self.screen_width = screen_width

    def get_font(self):
        return self.font