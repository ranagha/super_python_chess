from src.chess.Application.Model.Pieza import Pieza

class Knight(Pieza):
    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        pass