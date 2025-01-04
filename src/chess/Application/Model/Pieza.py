import json
from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color: str, fila: int, columna: int):
        self._color = color
        self._fila = fila
        self._columna = columna


    def __getitem__(self, key):
        data = {
            'pieza': self.__class__.__name__.lower(),
            'color': self.color(),
            'possibles_moves': self.possible_moves()
        }
        if key in data:
            return data[key]
        raise KeyError(f"La clave '{key}' no existe")

    def color(self):
        return self._color

    def fila(self):
        return self._fila

    def columna(self):
        return self._columna

    @abstractmethod
    def possible_moves(self):
        pass