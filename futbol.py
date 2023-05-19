#---------------------------------
# Desktop app -Estudiante 
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *   
import random

#definicion de variable
def mover_bola():
    global x, y, velocidad_x, velocidad_y
    
    # Actualizar la posición de la bola
    x += velocidad_x
    y += velocidad_y
    
    # Verificar los límites del lienzo y controlar el rebote
    if x <= radio or x >= BASE - radio:
        velocidad_x = -velocidad_x
    if y <= radio or y >= ALTURA - radio:
        velocidad_y = -velocidad_y
    
    # Mover la bola en el lienzo
    c.move(bola, velocidad_x, velocidad_y)
    
    # Llamar a la función de forma recursiva después de un intervalo de tiempo
    c.after(30, mover_bola)

#variables globales
BASE=660
ALTURA=460
#Variables de la pelota
radio = 30
x = random.randint(30,BASE-30)#BASE / 2
y = random.randint(30,ALTURA-30)#ALTURA / 2
velocidad_x = 5
velocidad_y = 3
#-----------------------------
# ventana principal de la app
#-----------------------------
# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Graficas 2D - Lineas rectas")
# tamaño de la ventana
ventana_principal.geometry("700x600")
# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)
# color de fondo de la ventana
ventana_principal.config(bg="white")

#--------------------------------
# frame graficacion
#--------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=680, height=480)
frame_graficacion.place(x=10, y=10)

#canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.configure(bg="green")
c.place(x=10, y=10)

#decoracion de la cancha
lineacentro= c.create_line(BASE/2, 0, BASE/2, ALTURA, fill="white",width=5)
rectangulo= c.create_rectangle(0,0,BASE, ALTURA, outline="white", width=5)
elipse = c.create_oval((BASE/2)-50, (ALTURA/2)-50, (BASE/2)+50, (ALTURA/2)+50,  outline="white", width=5)
elipse1 = c.create_oval(-BASE/2, ALTURA/7, BASE/4, ALTURA-ALTURA/7,  outline="white", width=5)
elipse2 = c.create_oval(BASE-BASE/4, ALTURA-ALTURA/12, BASE*2, ALTURA/12,  outline="white", width=5)

# Cargar la imagen de la bola
imagen_bola = PhotoImage(file="balon.png")

# Crear la bola en el lienzo utilizando la imagen

bola = c.create_image(x, y, image=imagen_bola)

#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.configure(bg="khaki", width=680, height=90)
frame_controles.place(x=10, y = 500)

#barra de deslizamiento
boton_mover= Button(frame_controles, command=mover_bola)
boton_mover.configure(bg = "orange",text="Mover", width=10, height=0)
boton_mover.place(x=290,y=30)

ventana_principal.mainloop()