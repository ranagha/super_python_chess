from src.chess.Application.Model.Pieza import Pieza

class King(Pieza):
    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        return [
            (min(self.fila() + 1, 7), self.columna()),
            (max(self.fila() - 1, 0), self.columna()),
            (min(self.fila() + 1, 7), min(self.columna() + 1, 7)),
            (max(self.fila() - 1, 0), max(self.columna() - 1, 0)),
            (min(self.fila() + 1, 7), max(self.columna() - 1, 0)),
            (max(self.fila() - 1, 0), min(self.columna() + 1, 7)),
            (self.fila(), min(self.columna() + 1, 7)),
            (self.fila(), max(self.columna() - 1, 0))
        ]