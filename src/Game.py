import pygame

from menu_state import Menu
from play_state import Play

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen_width = 800
        self.screen_height = 800
        self.create_screen()
        
        self.number_of_mines = 10
        
        self.menu = Menu(self)
        self.play = Play(self)
        
        
        self.active_state = None
        self.set_active_state(self.menu)

    def create_screen(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                              flags=pygame.RESIZABLE | pygame.SCALED)
        pygame.display.flip()
    
    def set_active_state(self, state):
        if self.active_state is not None:
            self.active_state.deactivate()
        self.active_state = state
        self.active_state.activate()
    
    def get_screen(self):
        return self.screen
    
    def get_screen_dim(self):
        return (self.screen_width, self.screen_height,)
    
    def menu_start_pressed(self):
        self.set_active_state(self.play)
        
    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                self.active_state.proc_event(event)
                pygame.display.get_surface().fill((200,200,255,))
                self.active_state.update()
                pygame.display.update()     
    

if __name__ == "__main__":
    game = Game()
    game.main_loop()