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
        self.collisions = []


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
            self.collisions = []
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
            self.calculate_colision()
            for filai, columnai in self.posibles_moves:
                casilla = tk.Frame(
                    self.tablero_frame,
                    width=60,
                    height=60,
                    bg='lightgray'
                )
                casilla.grid(row=filai, column=columnai)
                casilla.bind("<Button-1>", lambda new_event, fi=filai, co=columnai: self.move(new_event, fi, co))
                self.casillas[filai][columnai] = casilla
                if self.piezas[filai][columnai] is not None:
                    self.colocar_pieza(filai, columnai, self.piezas[filai][columnai]['pieza'], self.piezas[filai][columnai]['color'])

    def mueve_pieza(self, event, fila, columna):
        if fila == self.selected_origen_fila and columna == self.selected_origen_columna:
            self.seleccionado = False
            self.agregar_casilla(self.selected_origen_fila, self.selected_origen_columna,
                                 obtener_color_casilla(self.selected_origen_fila, self.selected_origen_columna))
            self.colocar_pieza(fila, columna, self.selected_pieza['pieza'], self.selected_pieza['color'])
            for filaj, columnaj in self.posibles_moves:
                self.agregar_casilla(filaj, columnaj, obtener_color_casilla(filaj, columnaj))
                if self.piezas[filaj][columnaj] is not None:
                    self.colocar_pieza(filaj, columnaj, self.piezas[filaj][columnaj]['pieza'], self.piezas[filaj][columnaj]['color'])
        else:
            for filai, columnai in self.posibles_moves:
                if filai == fila and columnai == columna:
                    self.seleccionado = False
                    self.piezas[fila][columna] = {'pieza': self.selected_pieza['pieza'], 'color': self.selected_pieza['color']}
                    self.piezas[self.selected_origen_fila][self.selected_origen_columna] = None
                    self.quitar_pieza(self.selected_origen_fila, self.selected_origen_columna)
                    self.agregar_casilla(self.selected_origen_fila, self.selected_origen_columna, obtener_color_casilla(self.selected_origen_fila, self.selected_origen_columna))
                    for filaj, columnaj in self.posibles_moves:
                        self.agregar_casilla(filaj, columnaj, obtener_color_casilla(filaj, columnaj))
                        if self.piezas[filaj][columnaj] is not None:
                            self.colocar_pieza(filaj, columnaj, self.piezas[filaj][columnaj]['pieza'],
                                               self.piezas[filaj][columnaj]['color'])
                    self.colocar_pieza(fila, columna, self.selected_pieza['pieza'], self.selected_pieza['color'])


    def casilla_vacia(self, fila, columna):
        return self.piezas[fila][columna] is None

    def casilla_enemiga_encontrada(self, fila, columna):
        if self.piezas[fila][columna] is None:
            return False
        return self.selected_pieza['color'] != self.piezas[fila][columna]['color'] and self.selected_pieza['pieza'] != 'pawn'

    def casilla_amiga_encontrada(self, fila, columna):
        if self.piezas[fila][columna] is None:
            return False
        return self.selected_pieza['color'] == self.piezas[fila][columna]['color']

    def en_linea(self, origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna):
        return (self.en_linea_horizontal(origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna) or
        self.en_linea_vertical(origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna) or
        self.en_linea_diagonal(origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna))

    def en_linea_horizontal(self, origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna):
        if origen_fila == intermedio_fila and intermedio_fila == final_fila:
            return min(origen_columna, final_columna) < intermedio_columna < max(origen_columna, final_columna)
        return False

    def en_linea_vertical(self, origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna):
        if origen_columna == intermedio_columna and intermedio_columna == final_columna:
            return min(origen_fila, final_fila) < intermedio_fila < max(origen_fila, final_fila)
        return False

    def en_linea_diagonal(self, origen_fila, origen_columna, intermedio_fila, intermedio_columna, final_fila, final_columna):
        return abs(origen_fila - intermedio_fila) == abs(intermedio_fila - final_fila) and abs(origen_columna - intermedio_columna) == abs(intermedio_columna - final_columna)

    def detras_de_colision(self, fila, columna):
        for filai, columnai in self.collisions:
            return self.en_linea(self.selected_origen_fila, self.selected_origen_columna, filai, columnai, fila, columna)

    def calculate_colision(self):
        temporal_moves = []
        for filai, columnai in self.posibles_moves:
            if self.casilla_enemiga_encontrada(filai, columnai):
                self.collisions.append((filai, columnai))
            if self.casilla_amiga_encontrada(filai, columnai):
                self.collisions.append((filai, columnai))
        for filai, columnai in self.posibles_moves:
            if not self.detras_de_colision(filai, columnai) and (
                    self.casilla_vacia(filai, columnai) or self.casilla_enemiga_encontrada(filai, columnai)):
                temporal_moves.append((filai, columnai))

        if self.selected_pieza['pieza'] == 'pawn' and self.selected_pieza['color'] == 'black':
            if self.selected_origen_fila+1 <= 7 and self.selected_origen_columna+1 <= 7 and self.piezas[self.selected_origen_fila+1][self.selected_origen_columna+1] is not None:
                temporal_moves.append((self.selected_origen_fila+1, self.selected_origen_columna+1))
            if self.selected_origen_fila+1 <= 7 and self.selected_origen_columna - 1 >= 0 and self.piezas[self.selected_origen_fila + 1][self.selected_origen_columna - 1] is not None:
                temporal_moves.append((self.selected_origen_fila + 1, self.selected_origen_columna - 1))

        if self.selected_pieza['pieza'] == 'pawn' and self.selected_pieza['color'] == 'white':
            if self.selected_origen_fila-1 >= 0 and self.selected_origen_columna+1 <= 7 and self.piezas[self.selected_origen_fila-1][self.selected_origen_columna+1] is not None:
                temporal_moves.append((self.selected_origen_fila-1, self.selected_origen_columna+1))
            if self.selected_origen_fila-1 >= 0 and self.selected_origen_columna - 1 >= 0 and self.piezas[self.selected_origen_fila -1][self.selected_origen_columna - 1] is not None:
                temporal_moves.append((self.selected_origen_fila -1, self.selected_origen_columna - 1))

        self.posibles_moves = temporal_moves

