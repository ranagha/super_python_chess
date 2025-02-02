import tkinter as tk
from src.chess.Application.Model.Tablero import Tablero

def crear_tablero(tablero):
    for i in range(0, 8):
        for j in range(0, 8):
            color = 'beige' if (i+j) % 2 == 0 else 'saddlebrown'
            tablero.agregar_casilla(i, j, color)
    colocar_piezas_salida(tablero)

def colocar_piezas_principales(tablero, color, posicion_inicial):
    orden_piezas = ['rock', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rock']
    for i in range(0, 8):
        tablero.colocar_pieza(posicion_inicial, i, orden_piezas[i], color)

def colocar_peones(tablero, color, posicion_inicial):
    for i in range(0, 8):
        tablero.colocar_pieza(posicion_inicial, i, 'pawn', color)

def colocar_piezas_salida(tablero):
    colocar_piezas_principales(tablero, 'black', 0)
    colocar_piezas_principales(tablero, 'white', 7)
    colocar_peones(tablero, 'black', 1)
    colocar_peones(tablero, 'white', 6)


def crear_nombres(root):
    etiqueta_jugador = tk.Label(root, text="JUGADOR", font=("Terminal", 24), foreground="red")
    etiqueta_jugador.place(x=375, y=540)
    etiqueta_jugador = tk.Label(root, text="CPU", font=("Terminal", 24), foreground="green")
    etiqueta_jugador.place(x=60, y=5)

def start():
    root = tk.Tk()
    root.title("Ajedrez molón de Melgar")

    # Ajustar el tamaño de la ventana
    root.geometry("600x600")
    tablero = Tablero(root)
    crear_tablero(tablero)
    crear_nombres(root)
    root.mainloop()