class AbstractState:
    def get_name(self):
        assert(False)
    
    def activate(self):
        pass

    def deactivate(self):
        pass

    def proc_event(self, event):
        assert(False)
    
    def update(self):
        assert(False)