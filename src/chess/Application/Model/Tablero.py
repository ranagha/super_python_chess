import tkinter as tk

class Tablero:
    def __init__(self, ventana):
        # Guardamos la ventana principal
        self.ventana = ventana
        self.tablero_frame = tk.Frame(self.ventana)
        self.tablero_frame.pack(pady=50)
        self.casillas = [[None for _ in range(8)] for _ in range(8)]


    def agregar_casilla(self, fila, columna, color):
        # Crear una casilla como un Frame
        casilla = tk.Frame(
            self.tablero_frame,
            width=60,
            height=60,
            bg=color
        )
        casilla.grid(row=fila, column=columna)
        self.casillas[fila][columna] = casilla

    def colocar_pieza(self, fila, columna, imagen_path):
        pieza_imagen = tk.PhotoImage(file=imagen_path)
        pieza = tk.Label(self.tablero_frame, image=pieza_imagen)
        pieza.image = pieza_imagen  # Necesario para evitar que se elimine la referencia
        pieza.grid(row=fila, column=columna)