#---------------------------------
# Desktop app -Estudiante 
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *   
from tkinter import messagebox, ttk

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
ventana_principal.config(bg="khaki")

#--------------------------------
# frame graficacion
#--------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=240)
frame_graficacion.place(x=10, y=10)

#canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.configure(bg="yellow")
c.place(x=10, y=10)

#lineas
color="#ff5733"
linea1= c.create_line(BASE/2, 0, BASE/2, ALTURA, fill="red",width=3)
linea2= c.create_line(0, ALTURA/2, BASE, ALTURA/2, fill="red",width=3)
# poligonos
poligono1= c.create_polygon(BASE/4,0, 0, ALTURA/4,BASE/4, ALTURA/2, BASE/2, ALTURA/4, fill=color, outline="blue")
poligono2= c.create_polygon(BASE-BASE/4,0, BASE/2, ALTURA/4,BASE-BASE/4, ALTURA/2, BASE, ALTURA/4, fill="blue", outline="blue")
poligono2= c.create_polygon(0,ALTURA-ALTURA/4, BASE/4, ALTURA/2,BASE/2, ALTURA-ALTURA/4, BASE/4, ALTURA, fill="green", outline="blue")
poligono2= c.create_polygon(BASE-BASE/4,ALTURA/2, BASE, ALTURA-ALTURA/4,BASE-BASE/4, ALTURA, BASE/2, ALTURA-ALTURA/4, fill="black", outline="blue")

#forma pacman
cuerpo1 = c.create_arc(BASE/4-45,ALTURA/4-45, (BASE/4)+45, (ALTURA/4)+45,start=35, extent=285 ,fill="yellow2")
ojo1= c.create_oval(BASE/4-10,ALTURA/4-10, (BASE/4)+10, (ALTURA/4)+10,fill="black")
cuerpo1 = c.create_arc((BASE-BASE/4)-45, (ALTURA/4)-45, (BASE-BASE/4)+45, (ALTURA/4)+45,start=35, extent=285 ,fill="yellow2")
cuerpo1 = c.create_arc((BASE/4)-45,ALTURA-ALTURA/4-45, (BASE/4)+45, (ALTURA-ALTURA/4)+45,start=35, extent=285 ,fill="yellow2")
cuerpo1 = c.create_arc(BASE-BASE/4-45,ALTURA-ALTURA/4-45, (BASE-BASE/4)+45, (ALTURA-ALTURA/4)+45,start=35, extent=285 ,fill="yellow2")
#pacman


ventana_principal.mainloop()