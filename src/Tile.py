class Tile():

    def __init__(self, x, y):
        self.num_value: int = 0
        self.hidden: bool = True
        self.x: int = x
        self.y: int = y
        self.has_flag: bool = False
        
    def set_mine(self):
        self.num_value = -1
    
    def set_value(self, value):
        self.num_value = value

    def is_hidden(self) -> bool:
        return self.hidden
    
    def uncover(self):
        self.hidden = False
        
    def get_coords(self) -> tuple[int, int]:
        return [self.x, self.y]
    
    def is_mine(self) -> bool:
        return self.num_value == -1
    
    def is_flagged(self) -> bool:
        return self.has_flag
    
    def set_flag(self):
        if self.hidden:
            self.has_flag = not self.has_flag