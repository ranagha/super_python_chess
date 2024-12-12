import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero


def start():
    root = tk.Tk()
    root.title("Ajedrez molón de Melgar")

    # Ajustar el tamaño de la ventana
    root.geometry("600x600")
    tablero = Tablero(root)
    color = 'black'
    first_color = 'black'
    for i in range(0, 8):
        if first_color == 'white':
            first_color = 'black'
        else:
            first_color = 'white'
        for j in range(0, 8):
            color = first_color if j == 0 else color
            tablero.agregar_casilla(i,j, color)
            if color == 'white':
                color = 'black'
            else:
                color = 'white'
    root.mainloop()