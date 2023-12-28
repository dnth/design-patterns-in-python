from interface_chair import IChair

class SmallChair(IChair):
    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    
    def get_dimensions(self):
        return {
            'height': self._height,
            'width': self._width,
            'depth': self._depth
        }