from interface_chair import IChair

class MediumChair(IChair):
    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    
    def get_dimensions(self):
        return {
            'height': self._height,
            'width': self._width,
            'depth': self._depth
        }