import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero

def crear_tablero(tablero):
    for i in range(0, 8):
        for j in range(0, 8):
            color = 'beige' if (i+j) % 2 == 0 else 'saddlebrown'
            tablero.agregar_casilla(i, j, color)
    colocar_piezas_salida(tablero)

def colocar_piezas_principales(tablero, color, posicion_inicial):
    tablero.colocar_pieza(posicion_inicial, 0, 'rock', color, '../../img/' + color + '_rock.png')
    tablero.colocar_pieza(posicion_inicial, 1, 'knight', color, '../../img/' + color + '_knight.png')
    tablero.colocar_pieza(posicion_inicial, 2, 'bishop', color, '../../img/' + color + '_bishop.png')
    tablero.colocar_pieza(posicion_inicial, 3, 'queen', color, '../../img/' + color + '_queen.png')
    tablero.colocar_pieza(posicion_inicial, 4, 'king', color, '../../img/' + color + '_king.png')
    tablero.colocar_pieza(posicion_inicial, 5, 'bishop', color, '../../img/' + color + '_bishop.png')
    tablero.colocar_pieza(posicion_inicial, 6, 'knight', color, '../../img/' + color + '_knight.png')
    tablero.colocar_pieza(posicion_inicial, 7, 'rock', color, '../../img/' + color + '_rock.png')

def colocar_peones(tablero, color, posicion_inicial):
    for i in range(0, 8):
        tablero.colocar_pieza(posicion_inicial, i, 'pawn', color, '../../img/' + color + '_pawn.png')

def colocar_piezas_salida(tablero):
    colocar_piezas_principales(tablero, 'black', 0)
    colocar_piezas_principales(tablero, 'white', 7)
    colocar_peones(tablero, 'black', 1)
    colocar_peones(tablero, 'white', 6)


def crear_nombres(root):
    etiqueta_jugador = tk.Label(root, text="JUGADOR", font=("Terminal", 25), foreground="red")
    etiqueta_jugador.place(x=375, y=550)
    etiqueta_jugador = tk.Label(root, text="CPU", font=("Terminal", 25), foreground="green")
    etiqueta_jugador.place(x=60, y=10)

def start():
    root = tk.Tk()
    root.title("Ajedrez molón de Melgar")

    # Ajustar el tamaño de la ventana
    root.geometry("600x600")
    tablero = Tablero(root)
    crear_tablero(tablero)
    crear_nombres(root)
    root.mainloop()