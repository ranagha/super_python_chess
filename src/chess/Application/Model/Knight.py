from src.chess.Application.Model.Pieza import Pieza

class Knight(Pieza):
    def __init__(self, color):
        super().__init__(color)

    def possible_moves(self, position):
        pass