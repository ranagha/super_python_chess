from src.chess.Application.Model.Pieza import Pieza

class Pawn(Pieza):
    def __init__(self, color: str, fila: int, columna: int):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        if self.fila() == 6 and self.color() == 'white':
            return [(5, self.columna()), (4, self.columna())]
        else:
            if self.fila() == 1 and self.color() == 'black':
                return [(2, self.columna()), (3, self.columna())]
            else:
                if self.color() == 'white' and self.fila()-1 >= 0:
                    return [(self.fila()-1, self.columna())]
                if self.color() == 'black' and self.fila()+1 <= 7:
                    return [(self.fila()+1, self.columna())]
                else:
                    return []