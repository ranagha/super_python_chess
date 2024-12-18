import tkinter as tk
from PIL import Image, ImageTk


def obtener_color_casilla(fila, columna):
    # Alterna entre 'beige' y 'saddlebrown' según las coordenadas
    if (fila + columna) % 2 == 0:
        return "beige"  # Casilla blanca
    else:
        return "saddlebrown"  # Casilla negra


class Tablero:
    def __init__(self, ventana):
        # Guardamos la ventana principal
        self.ventana = ventana
        self.tablero_frame = tk.Frame(self.ventana)
        self.tablero_frame.pack(pady=50)
        self.casillas = [[None for _ in range(8)] for _ in range(8)]
        self.piezas = [[None for _ in range(8)] for _ in range(8)]


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

    def colocar_pieza(self, fila, columna, pieza, color, imagen_path):
        pieza_imagen = Image.open(imagen_path).convert("RGBA")
        color_casilla = obtener_color_casilla(fila, columna)
        # Redimensionar la imagen (si es necesario)
        pieza_imagen = pieza_imagen.resize((50, 50))  # Ajusta el tamaño según necesites

        # Convertir la imagen a un formato que Tkinter puede manejar
        pieza_imagen_tk = ImageTk.PhotoImage(pieza_imagen)

        pieza = tk.Label(self.tablero_frame, image=pieza_imagen_tk, bg=color_casilla)
        pieza.image = pieza_imagen_tk  # Necesario para mantener la referencia
        pieza.grid(row=fila, column=columna)
        self.piezas[fila][columna] = {pieza: pieza, color: color}

