class Tile():

    def __init__(self, x, y):
        self.num_value = 0
        self.hidden = True
        self.x = x
        self.y = y
        self.has_flag = False
        
    def set_mine(self):
        self.num_value = -1
    
    def set_value(self, value):
        self.num_value = value

    def get_coords(self):
        return [self.x, self.y]
    
    def is_mine(self):
        return self.num_value == -1
    
    def is_flagged(self):
        return self.has_flag
    
    def set_flag(self):
        self.has_flag = not self.has_flag