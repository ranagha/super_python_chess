import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero

def crear_tablero(tablero):
    color = 'black'
    first_color = 'black'
    tablero.colocar_pieza(0, 0, '../../img/1.png')
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