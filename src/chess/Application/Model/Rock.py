from src.chess.Application.Model.Pieza import Pieza

class Rock(Pieza):
    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)

    def possible_moves(self):
        movements = []

        #derecha
        filai = self.fila()
        while filai < 7:
            filai = filai + 1
            movements.append((filai, self.columna()))

        # izquierda
        filai = self.fila()
        while filai > 0:
            filai = filai - 1
            movements.append((filai, self.columna()))

        # arriba
        columnai = self.columna()
        while columnai < 7:
            columnai = columnai + 1
            movements.append((self.fila(), columnai))

        # abajo
        columnai = self.columna()
        while columnai > 0:
            columnai = columnai - 1
            movements.append((self.fila(), columnai))
        return movements