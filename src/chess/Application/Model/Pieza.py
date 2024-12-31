from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color):
        self.color = color

    def color(self):
        return self.color

    @abstractmethod
    def possible_moves(self, position):
        pass