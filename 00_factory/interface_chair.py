from abc import ABC, abstractmethod

class IChair(ABC):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        "Gets the dimensions of the chair"
