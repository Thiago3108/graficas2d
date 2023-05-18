#---------------------------------
# Desktop app -Estudiante 
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *   
from tkinter import messagebox, ttk
import random

#constates globales
BASE= 460
ALTURA=220

#-----------------------------
# ventana principal de la app
#-----------------------------
# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Graficas 2D - Lineas rectas")
# tamaño de la ventana
ventana_principal.geometry("500x500")
# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)
# color de fondo de la ventana
ventana_principal.config(bg="white")

#--------------------------------
# frame graficacion
#--------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

#canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.configure(bg="black")
c.place(x=10, y=10)

# graficacion 
x =10
y = 10

for i in range(100):
    x = random.randint(0, BASE - 20)
    y = random.randint(0, ALTURA - 20)
    color = "#"
    for caracter in range(6):   
        color = color + random.choice("0123456789ABCDF")
    circulo = c.create_oval(x,y, x+20, y+20, fill = color)



ventana_principal.mainloop()