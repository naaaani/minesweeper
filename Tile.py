class Tile():

    def __init__(self, x, y):
        self.num_value = 0
        self.hidden = True
        self.x = x
        self.y = y
        
    def set_mine(self):
        self.num_value = -1

    def get_hidden(self):
        return self.hidden
    
    def get_value(self):
        return self.num_value
    
    def set_value(self, value):
        self.num_value = value

    def get_coords(self):
        return [self.x, self.y]