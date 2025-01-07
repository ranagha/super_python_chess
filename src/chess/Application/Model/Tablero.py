import tkinter as tk
from PIL import Image, ImageTk
from src.chess.Application.Model.Rock import Rock
from src.chess.Application.Model.Knight import Knight
from src.chess.Application.Model.Bishop import Bishop
from src.chess.Application.Model.King import King
from src.chess.Application.Model.Queen import Queen
from src.chess.Application.Model.Pawn import Pawn

def crear_pieza(tipo: str, color: str, fila, columna):
    piezas = {
        "pawn": Pawn,
        'king': King,
        'queen': Queen,
        'knight': Knight,
        'bishop': Bishop,
        'rock': Rock
    }
    # Verificamos si el tipo está en el diccionario
    if tipo in piezas:
        return piezas[tipo](color, fila, columna)
    else:
        raise ValueError(f"La pieza {tipo} no existe")


def obtener_color_casilla(fila, columna):
    # Alterna entre 'beige' y 'saddlebrown' según las coordenadas
    if (fila + columna) % 2 == 0:
        return "beige"  # Casilla blanca
    else:
        return "saddlebrown"  # Casilla negra


class Tablero:
    def __init__(self, ventana):
        # Guardamos la ventana principal
        self.posibles_moves = []
        self.ventana = ventana
        self.tablero_frame = tk.Frame(self.ventana)
        self.tablero_frame.pack(pady=50)
        self.casillas = [[None for _ in range(8)] for _ in range(8)]
        self.piezas = [[None for _ in range(8)] for _ in range(8)]
        self.seleccionado = False
        self.selected_pieza = None
        self.selected_origen_fila = None
        self.selected_origen_columna = None


    def agregar_casilla(self, fila, columna, color):
        # Crear una casilla como un Frame
        casilla = tk.Frame(
            self.tablero_frame,
            width=60,
            height=60,
            bg=color
        )
        casilla.grid(row=fila, column=columna)
        casilla.bind("<Button-1>", lambda event: self.move(event, fila, columna))
        self.casillas[fila][columna] = casilla

    def colocar_pieza(self, fila, columna, pieza, color):
        imagen_path = '../../img/' + color + '_' + pieza + '.png'
        pieza_imagen = Image.open(imagen_path).convert("RGBA")
        color_casilla = obtener_color_casilla(fila, columna)
        # Redimensionar la imagen (si es necesario)
        pieza_imagen = pieza_imagen.resize((50, 50))  # Ajusta el tamaño según necesites
        # Convertir la imagen a un formato que Tkinter puede manejar
        pieza_imagen_tk = ImageTk.PhotoImage(pieza_imagen)
        pieza_fisica = tk.Label(self.tablero_frame, image=pieza_imagen_tk, bg=color_casilla)
        pieza_fisica.image = pieza_imagen_tk  # Necesario para mantener la referencia
        pieza_fisica.grid(row=fila, column=columna)
        self.piezas[fila][columna] = crear_pieza(pieza, color, fila, columna)
        pieza_fisica.bind("<Button-1>", lambda event: self.move(event, fila, columna))

    def quitar_pieza(self, fila, columna):
        casilla = tk.Frame(
            self.tablero_frame,
            width=60,
            height=60,
            bg='saddlebrown'
        )
        casilla.grid(row=fila, column=columna)
        self.casillas[fila][columna] = casilla


    def move(self, event, fila, columna):
        if not self.seleccionado:
            self.selecciona_pieza(event, fila, columna)
        else:
            self.mueve_pieza(event, fila, columna)


    def selecciona_pieza(self, event, fila, columna):
        if self.piezas[fila][columna] is not None:
            self.seleccionado = True
            self.selected_origen_fila = fila
            self.selected_origen_columna = columna
            casilla = tk.Frame(
                self.tablero_frame,
                width=60,
                height=60,
                bg='orange'
            )
            casilla.grid(row=fila, column=columna)
            self.casillas[fila][columna] = casilla
            self.selected_pieza = self.piezas[fila][columna]
            self.colocar_pieza(fila, columna, self.selected_pieza['pieza'], self.selected_pieza['color'])
            self.posibles_moves = self.selected_pieza['possibles_moves']
            for filai, columnai in self.posibles_moves:
                casilla = tk.Frame(
                    self.tablero_frame,
                    width=60,
                    height=60,
                    bg='lightgray'
                )
                casilla.grid(row=filai, column=columnai)
                casilla.bind("<Button-1>", lambda new_event: self.move(new_event, filai, columnai))
                self.casillas[filai][columnai] = casilla

    def mueve_pieza(self, event, fila, columna):
        for filai, columnai in self.posibles_moves:
            print(filai, columnai, fila, columna)
            if filai == fila and columnai == columna:
                print(filai, columnai, fila, columna)
                self.seleccionado = False
                self.piezas[fila][columna] = {'pieza': self.selected_pieza['pieza'], 'color': self.selected_pieza['color']}
                self.piezas[self.selected_origen_fila][self.selected_origen_columna] = None
                self.quitar_pieza(self.selected_origen_fila, self.selected_origen_columna)
                self.agregar_casilla(self.selected_origen_fila, self.selected_origen_columna, obtener_color_casilla(self.selected_origen_fila, self.selected_origen_columna))
                for filaj, columnaj in self.posibles_moves:
                    self.agregar_casilla(filaj, columnaj, obtener_color_casilla(filaj, columnaj))
                self.colocar_pieza(fila, columna, self.selected_pieza['pieza'], self.selected_pieza['color'])