import tkinter as tk
import random

def mover_objeto():
    global x, y, dx, dy
    x += dx
    y += dy

    # Verificar colisión con las paredes
    if x <= 0 or x + tamaño >= ancho:
        dx *= -1
    if y <= 0 or y + tamaño >= alto:
        dy *= -1

    # Mover el objeto
    c.coords(objeto, x, y, x + tamaño, y + tamaño)

    # Programar el siguiente movimiento
    ventana.after(10, mover_objeto)

ventana = tk.Tk()
ancho = 400
alto = 400
c = tk.Canvas(ventana, width=ancho, height=alto)
c.pack()

tamaño = 50
x = random.randint(0, ancho - tamaño)
y = random.randint(0, alto - tamaño)
dx = random.choice([-1, 1])  # Dirección del movimiento en el eje X
dy = random.choice([-1, 1])  # Dirección del movimiento en el eje Y

objeto = c.create_oval(x, y, x + tamaño, y + tamaño, fill="blue")

mover_objeto()

ventana.mainloop()

