import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero


def start():
    root = tk.Tk()
    root.title("Ajedrez molón de Melgar")

    # Ajustar el tamaño de la ventana
    root.geometry("600x600")
    tablero = Tablero(root)
    tablero.agregar_casilla(0,0, 'white')
    root.mainloop()