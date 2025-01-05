from src.chess.Application.Model.Pieza import Pieza

class Knight(Pieza):
    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        moves = []
        if self.fila() + 2 <= 7 and self.columna() +1 <= 7:
            moves.append((self.fila() + 2, self.columna() + 1))
        if self.fila() + 1 <= 7 and self.columna() +2 <= 7:
            moves.append((self.fila() + 1, self.columna() + 2))
        if self.fila() + 2 <= 7 and self.columna() - 1 >= 0:
            moves.append((self.fila() + 2, self.columna() - 1))
        if self.fila() + 1 <= 7 and self.columna() -2 >= 0:
            moves.append((self.fila() + 1, self.columna() -2))
        if self.fila() - 2 >= 0 and self.columna() +1 <= 7:
            moves.append((self.fila() - 2, self.columna() + 1))
        if self.fila() - 1 >= 0 and self.columna() + 2 <= 7:
            moves.append((self.fila() -1, self.columna() + 2))
        if self.fila() - 2 >= 0 and self.columna() - 1 >= 0:
            moves.append((self.fila() - 2, self.columna() - 1))
        if self.fila() -1 >= 0 and self.columna() -2 >= 0:
            moves.append((self.fila() -1,  self.columna() - 2))
        return moves
