from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:
    @staticmethod
    def get_chair(chair):
        if chair == 's':
            return SmallChair()
        if chair == 'm':
            return MediumChair()
        if chair == 'b':
            return BigChair()