from idlelib.outwin import file_line_pats

from src.chess.Application.Model.Pieza import Pieza

class Bishop(Pieza):
    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        movements = []
        filai = self.fila()
        columnai = self.columna()
        while filai < 7 and columnai < 7:
            filai = filai + 1
            columnai = columnai + 1
            movements.append((filai, columnai))
        filai = self.fila()
        columnai = self.columna()
        while filai < 7 and columnai > 0:
            filai = filai + 1
            columnai = columnai -1
            movements.append((filai, columnai))
        filai = self.fila()
        columnai = self.columna()
        while filai > 0 and columnai < 7:
            filai = filai - 1
            columnai = columnai + 1
            movements.append((filai, columnai))
        filai = self.fila()
        columnai = self.columna()
        while filai > 0 and columnai > 0:
            filai = filai - 1
            columnai = columnai - 1
            movements.append((filai, columnai))
        return movements