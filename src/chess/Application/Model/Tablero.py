import tkinter as tk

class Tablero:
    def __init__(self, ventana):
        # Guardamos la ventana principal
        self.ventana = ventana
        self.tablero_frame = tk.Frame(self.ventana)
        self.tablero_frame.pack(pady=50)


    def agregar_casilla(self, fila, columna, color):
        # Crear una casilla como un Frame
        casilla = tk.Frame(
            self.tablero_frame,
            width=60,
            height=60,
            bg=color
        )
        casilla.grid(row=fila, column=columna)