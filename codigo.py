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
linea1= c.create_line(10, 10, BASE-10, 10, fill="red")
linea2= c.create_line(BASE-10, 10, BASE-10, ALTURA-10, fill="red")
linea3= c.create_line(BASE-10, ALTURA-10, 10, ALTURA-10, fill="red")
linea4= c.create_line(10, ALTURA-10, 10, 10, fill="red")
linea5 = c.create_line(10, 10, BASE-10, ALTURA-10, fill="green")
linea6 = c.create_line(10, ALTURA-10, BASE-10, 10, fill="green")

#lineas cruz
linea1= c.create_line(204, 33, 204, ALTURA-135, fill="NavajoWhite4", width=3)
linea2= c.create_line(204, 33, BASE-204, 33, fill="NavajoWhite4", width=3)
linea3= c.create_line(255, 33, 255, ALTURA-135, fill="NavajoWhite4", width=3)
linea4= c.create_line(255, ALTURA-135, 306, ALTURA-135, fill="NavajoWhite4", width=3)
linea5= c.create_line(306, ALTURA-135, 306, ALTURA-84, fill="NavajoWhite4", width=3)
linea6= c.create_line(306, ALTURA-84, BASE-204, ALTURA-84, fill="NavajoWhite4", width=3)
linea7= c.create_line(BASE-204, ALTURA-84, BASE-204, ALTURA-33, fill="NavajoWhite4", width=3)
linea8= c.create_line(BASE-204, ALTURA-33, BASE-255, ALTURA-33, fill="NavajoWhite4", width=3)
linea9= c.create_line(BASE-255, ALTURA-33, BASE-255, ALTURA-84, fill="NavajoWhite4", width=3)
linea9= c.create_line(BASE-255, ALTURA-33, BASE-255, ALTURA-84, fill="NavajoWhite4", width=3)
linea10= c.create_line(BASE-255, ALTURA-84,BASE-306, ALTURA-84,  fill="NavajoWhite4", width=3)
linea11= c.create_line(BASE-306, ALTURA-84,BASE-306, ALTURA-135,  fill="NavajoWhite4", width=3)
linea12= c.create_line(BASE-306, ALTURA-135,BASE-255, ALTURA-135,  fill="NavajoWhite4", width=3)


ventana_principal.mainloop()