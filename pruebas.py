import tkinter as tk
import random

def mover_objeto(dx, dy):
    c.move(objeto, dx, dy)
    x1, y1, x2, y2 = c.bbox(objeto)  # Obtener las coordenadas del objeto
    if x1 < 0 or y1 < 0 or x2 > ancho or y2 > alto:  # Verificar si el objeto está fuera del rango de visión
        reiniciar_objeto()

def reiniciar_objeto():
    c.delete(objeto)  # Eliminar el objeto actual
    x = random.randint(50, ancho - 50)
    y = random.randint(50, alto - 50)
    nuevo_objeto = c.create_rectangle(x, y, x+50, y+50, fill="blue")  # Crear un nuevo objeto
    return nuevo_objeto

def mover_arriba(event=None):
    mover_objeto(0, -10)

def mover_abajo(event=None):
    mover_objeto(0, 10)

def mover_izquierda(event=None):
    mover_objeto(-10, 0)

def mover_derecha(event=None):
    mover_objeto(10, 0)

ventana = tk.Tk()
ancho = 400
alto = 400
c = tk.Canvas(ventana, width=ancho, height=alto)
c.pack()

objeto = c.create_rectangle(50, 50, 100, 100, fill="blue")

boton_arriba = tk.Button(ventana, text="Arriba", command=mover_arriba)
boton_arriba.pack()

boton_abajo = tk.Button(ventana, text="Abajo", command=mover_abajo)
boton_abajo.pack()

boton_izquierda = tk.Button(ventana, text="Izquierda", command=mover_izquierda)
boton_izquierda.pack()

boton_derecha = tk.Button(ventana, text="Derecha", command=mover_derecha)
boton_derecha.pack()

ventana.bind("<Up>", mover_arriba)
ventana.bind("<Down>", mover_abajo)
ventana.bind("<Left>", mover_izquierda)
ventana.bind("<Right>", mover_derecha)

ventana.mainloop()
