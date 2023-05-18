"""
from tkinter import *

ventana = Tk()

canvas = Canvas(ventana, width=200, height=200)
canvas.pack()

# Crear un rectángulo sin color de fondo
rectangulo = canvas.create_rectangle(50, 50, 150, 150, outline="black")

ventana.mainloop()
########################################################################
import tkinter as tk
import random

def mover_objeto():
    canvas.move(objeto, random.randint(-5, 5), random.randint(-5, 5))
    # Mueve el objeto en coordenadas aleatorias entre -5 y 5 en x e y
    ventana.after(1000, mover_objeto)  # Mueve el objeto cada segundo

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=400, height=400)
canvas.pack()

objeto = canvas.create_rectangle(50, 50, 100, 100, fill="red")

mover_objeto()

ventana.mainloop()
"""

from tkinter import *
import random
import math

# Definición de variables
BASE = 660
ALTURA = 460
MOVIMIENTO_STEP = 2
FPS = 60

def mover_objeto():
    x, y = c.coords(objeto)
    objetivo_x = random.randint(30, BASE - 30)
    objetivo_y = random.randint(30, ALTURA - 30)
    

    distancia = math.sqrt((objetivo_x - x) ** 2 + (objetivo_y - y) ** 2)
    if distancia > MOVIMIENTO_STEP:
        dx = int((objetivo_x - x) * MOVIMIENTO_STEP / distancia)
        dy = int((objetivo_y - y) * MOVIMIENTO_STEP / distancia)
    else:
        dx = objetivo_x - x
        dy = objetivo_y - y
    
    c.move(objeto, dx, dy)
    ventana_principal.after(int(1000 / FPS), mover_objeto)

# Ventana principal de la app
ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Lineas rectas")
ventana_principal.geometry("700x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

# Frame de graficación
frame_graficacion = Frame(ventana_principal, bg="green", width=680, height=480)
frame_graficacion.place(x=10, y=10)

# Canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA, bg="green")
c.place(x=10, y=10)

# Decoración de la cancha
lineacentro = c.create_line(BASE/2, 0, BASE/2, ALTURA, fill="white", width=5)
rectangulo = c.create_rectangle(0, 0, BASE, ALTURA, outline="white", width=5)
elipse = c.create_oval((BASE/2)-50, (ALTURA/2)-50, (BASE/2)+50, (ALTURA/2)+50, outline="white", width=5)

# Objeto o balón
image = PhotoImage(file="balon.png")
objeto = c.create_image(random.randint(30, BASE-30), random.randint(30, ALTURA-30), image=image)

# Frame de controles
frame_controles = Frame(ventana_principal, bg="khaki", width=680, height=90)
frame_controles.place(x=10, y=500)

# Botón de mover
boton_mover = Button(frame_controles, command=mover_objeto, bg="orange", text="Mover", width=10, height=0)
boton_mover.place(x=290, y=30)

ventana_principal.after(int(1000 / FPS), mover_objeto)
ventana_principal.mainloop()
