from interface_chair import IChair

class BigChair(IChair):
    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    
    def get_dimensions(self):
        return {
            'height': self._height,
            'width': self._width,
            'depth': self._depth
        }