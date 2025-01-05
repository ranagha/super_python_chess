from src.chess.Application.Model.Pieza import Pieza

class King(Pieza):
    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        return []