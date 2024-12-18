import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero

def crear_tablero(tablero):
    color = 'saddlebrown'
    first_color = 'saddlebrown'
    for i in range(0, 8):
        if first_color == 'beige':
            first_color = 'saddlebrown'
        else:
            first_color = 'beige'
        for j in range(0, 8):
            color = first_color if j == 0 else color
            tablero.agregar_casilla(i, j, color)
            if color == 'beige':
                color = 'saddlebrown'
            else:
                color = 'beige'
    colocar_piezas_salida(tablero)


def colocar_piezas_salida(tablero):
    tablero.colocar_pieza(0, 0, 'rock', 'black', '../../img/black_rock.png')
    tablero.colocar_pieza(0, 1, 'knight', 'black', '../../img/black_knight.png')
    tablero.colocar_pieza(0, 2, 'bishop', 'black', '../../img/black_bishop.png')
    tablero.colocar_pieza(0, 3, 'queen', 'black', '../../img/black_queen.png')
    tablero.colocar_pieza(0, 4, 'king', 'black', '../../img/black_king.png')
    tablero.colocar_pieza(0, 5, 'bishop', 'black', '../../img/black_bishop.png')
    tablero.colocar_pieza(0, 6, 'knight', 'black', '../../img/black_knight.png')
    tablero.colocar_pieza(0, 7, 'rock', 'black', '../../img/black_rock.png')
    tablero.colocar_pieza(1, 0, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 1, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 2, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 3, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 4, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 5, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 6, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(1, 7, 'pawn', 'black', '../../img/black_pawn.png')
    tablero.colocar_pieza(7, 0, 'rock', 'white', '../../img/white_rock.png')
    tablero.colocar_pieza(7, 1, 'knight', 'white', '../../img/white_knight.png')
    tablero.colocar_pieza(7, 2, 'bishop', 'white', '../../img/white_bishop.png')
    tablero.colocar_pieza(7, 3, 'queen', 'white', '../../img/white_queen.png')
    tablero.colocar_pieza(7, 4, 'king', 'white', '../../img/white_king.png')
    tablero.colocar_pieza(7, 5, 'bishop', 'white', '../../img/white_bishop.png')
    tablero.colocar_pieza(7, 6, 'knight', 'white', '../../img/white_knight.png')
    tablero.colocar_pieza(7, 7, 'rock', 'white', '../../img/white_rock.png')
    tablero.colocar_pieza(6, 0, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 1, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 2, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 3, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 4, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 5, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 6, 'pawn', 'white', '../../img/white_pawn.png')
    tablero.colocar_pieza(6, 7, 'pawn', 'white', '../../img/white_pawn.png')


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