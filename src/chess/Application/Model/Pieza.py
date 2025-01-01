import json
from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color):
        self._color = color


    def __getitem__(self, key):
        data = {
            'pieza': self.__class__.__name__.lower(),
            'color': self.color()
        }
        if key in data:
            return data[key]
        raise KeyError(f"La clave '{key}' no existe")

    def color(self):
        return self._color

    @abstractmethod
    def possible_moves(self, position):
        pass