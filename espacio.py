#---------------------------------
# Desktop app -Estudiante 
#---------------------------------
# se importa la libreria tkinter con todas sus funciones
from tkinter import * 
import random

#variables globales
BASE=660
ALTURA=460

#def variables

def mover_objeto(x, y):
    reiniciar_circulos()
    xd,yd = c.coords(objeto)
    if xd < 0:
        x += 660
    elif xd > 660:
        x -= 660
    elif yd < 0:
        y += 460
    elif yd > 460:
        y -= 460
    c.move(objeto, x, y)

def reiniciar_circulos():
    c.delete("circulo") 
    for i in range(50):
        x_estrella = random.randint(0, BASE - 20)
        y_estrella = random.randint(0, ALTURA - 20)
        color = "#"
        for caracter in range(6):   
            color = color + random.choice("0123456789ABCDF")
            tamaño = random.randint(0,20)
        c.create_oval(x_estrella,y_estrella, x_estrella+tamaño, y_estrella+tamaño, fill = color, tags="circulo")

def mover_arriba(event=None):
    mover_objeto(0, -10)
    
def mover_abajo(event=None):
    mover_objeto(0, 10) 

def mover_izquierda(event=None):
    mover_objeto(-10, 0)  

def mover_derecha(event=None):
    mover_objeto(10, 0) 

#-----------------------------
# ventana principal de la app
#-----------------------------
# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Graficas 2D - Lineas rectas")
# tamaño de la ventana
ventana_principal.geometry("700x650")
# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)
# color de fondo de la ventana
ventana_principal.config(bg="white")

#--------------------------------
# frame graficacion
#--------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=680, height=480)
frame_graficacion.place(x=10, y=10)

#canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.configure(bg="black")
c.place(x=10, y=10)

#asteroides
reiniciar_circulos()

#objeto o balon 
image = PhotoImage(file="nave (1).png")
objeto = c.create_image(100,200, image=image)

#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.configure(bg="khaki", width=680, height=140)
frame_controles.place(x=10, y = 500)

#barra de arriva
boton_mover_arriva= Button(frame_controles, command=mover_arriba)
boton_mover_arriva.configure(bg = "orange",text="⬆", width=2, height=0)
boton_mover_arriva.place(x=290,y=30)
#barra de la derecha
boton_mover_derecha= Button(frame_controles, command=mover_derecha)
boton_mover_derecha.configure(bg = "orange",text="➡", width=2, height=0)
boton_mover_derecha.place(x=335,y=45)
#barra de la izquierda
boton_mover_izquierda= Button(frame_controles, command=mover_izquierda)
boton_mover_izquierda.configure(bg = "orange",text="⬅", width=2, height=0)
boton_mover_izquierda.place(x=245,y=45)
#barra pa abajo
boton_mover_abajo= Button(frame_controles, command=mover_abajo)
boton_mover_abajo.configure(bg = "orange",text="⬇", width=2, height=0)
boton_mover_abajo.place(x=290,y=60)
   
#teclas
ventana_principal.bind("<Up>", mover_arriba)
ventana_principal.bind("<Down>", mover_abajo)
ventana_principal.bind("<Left>", mover_izquierda)
ventana_principal.bind("<Right>", mover_derecha)



ventana_principal.mainloop()