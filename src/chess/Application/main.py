import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero

def crear_tablero(tablero):
    color = 'black'
    first_color = 'black'
    for i in range(0, 8):
        if first_color == 'white':
            first_color = 'black'
        else:
            first_color = 'white'
        for j in range(0, 8):
            color = first_color if j == 0 else color
            tablero.agregar_casilla(i, j, color)
            if color == 'white':
                color = 'black'
            else:
                color = 'white'
    tablero.colocar_pieza(0, 0, '../../img/black_rock.png')
    tablero.colocar_pieza(0, 1, '../../img/black_knight.png')
    tablero.colocar_pieza(0, 2, '../../img/black_bishop.png')
    tablero.colocar_pieza(0, 3, '../../img/black_king.png')
    tablero.colocar_pieza(0, 4, '../../img/black_queen.png')
    tablero.colocar_pieza(0, 5, '../../img/black_bishop.png')
    tablero.colocar_pieza(0, 6, '../../img/black_knight.png')
    tablero.colocar_pieza(0, 7, '../../img/black_rock.png')

    tablero.colocar_pieza(1, 0, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 1, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 2, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 3, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 4, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 5, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 6, '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 7, '../../img/black_pawn.png')

    tablero.colocar_pieza(7, 0, '../../img/white_rock.png')
    tablero.colocar_pieza(7, 1, '../../img/white_knight.png')
    tablero.colocar_pieza(7, 2, '../../img/white_bishop.png')
    tablero.colocar_pieza(7, 3, '../../img/white_king.png')
    tablero.colocar_pieza(7, 4, '../../img/white_queen.png')
    tablero.colocar_pieza(7, 5, '../../img/white_bishop.png')
    tablero.colocar_pieza(7, 6, '../../img/white_knight.png')
    tablero.colocar_pieza(7, 7, '../../img/white_rock.png')

    tablero.colocar_pieza(6, 0, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 1, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 2, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 3, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 4, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 5, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 6, '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 7, '../../img/white_pawn.png')

def crear_nombres(root):
    etiqueta_jugador = tk.Label(root, text="Jugador", font=("Arial", 12))
    etiqueta_jugador.place(x=475, y=550)
    etiqueta_jugador = tk.Label(root, text="CPU", font=("Arial", 12))
    etiqueta_jugador.place(x=60, y=15)

def start():
    root = tk.Tk()
    root.title("Ajedrez molón de Melgar")

    # Ajustar el tamaño de la ventana
    root.geometry("600x600")
    tablero = Tablero(root)
    crear_tablero(tablero)
    crear_nombres(root)
    root.mainloop()