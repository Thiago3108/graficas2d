
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
RADIO=50
ANGULO=45 

#funcion para modificar arco
def modificar_arco(angulo):
   b=int(angulo)
   c.itemconfig(aspa1, start=b, extent=ANGULO)
   c.itemconfig(aspa2, start=b+45*2, extent=ANGULO)
   c.itemconfig(aspa3, start=b+45*4, extent=ANGULO)
   c.itemconfig(aspa4, start=b+45*6, extent=ANGULO)

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
frame_graficacion.config(bg="khaki", width=480, height=240)
frame_graficacion.place(x=10, y=10)

#canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.configure(bg="black")
c.place(x=10, y=10)

#base del molino 
base= c.create_polygon(BASE/3,ALTURA, BASE-BASE/3,ALTURA,BASE/2, ALTURA/2, fill="khaki3")

#circulo
aspa1 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO,BASE/2+RADIO, ALTURA/2+RADIO, start=ANGULO-45, extent=ANGULO, fill="red" )
aspa2 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO,BASE/2+RADIO, ALTURA/2+RADIO, start=ANGULO+45, extent=ANGULO, fill="green" )
aspa3 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO,BASE/2+RADIO, ALTURA/2+RADIO, start=ANGULO+45*3, extent=ANGULO, fill="blue" )
aspa4 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO,BASE/2+RADIO, ALTURA/2+RADIO, start=ANGULO+45*5, extent=ANGULO, fill="orange" )

#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.configure(bg="khaki", width=480, height=230)
frame_controles.place(x=10, y = 260)

#barra de deslizamiento
barra_deslizamiento= Scale(frame_controles, label="angulo", from_=0, to_=360, orient="horizontal", length=460, tickinterval=45, command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)

ventana_principal.mainloop()