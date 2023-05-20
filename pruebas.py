from tkinter import *
import random

# Variables globales
ANCHO_CANVAS = 400
ALTO_CANVAS = 300
RADIO_PELOTA = 50
VELOCIDAD_PELOTA = 3

# Función para mover la pelota
def mover_pelota():
    global direccion_x, direccion_y  # Declarar las variables como globales
    
    # Obtener las coordenadas actuales de la pelota
    x, y, _, _ = c.coords(pelota_id)

    # Calcular las nuevas coordenadas de la pelota
    nuevo_x = x + direccion_x * VELOCIDAD_PELOTA
    nuevo_y = y + direccion_y * VELOCIDAD_PELOTA

    # Verificar los límites del Canvas
    if nuevo_x + RADIO_PELOTA <= 0 or nuevo_x + RADIO_PELOTA >= ANCHO_CANVAS:
        direccion_x = random.choice([-1, 1])  # Cambiar la dirección en el eje x en una dirección aleatoria
        color = "#" + ''.join(random.choices("0123456789ABCDEF", k=6))  # Generar un color aleatorio
        c.itemconfig(texto_id, fill=color)  # Cambiar el color del texto

    if nuevo_y + RADIO_PELOTA <= 0 or nuevo_y + RADIO_PELOTA >= ALTO_CANVAS:
        direccion_y = random.choice([-1, 1])  # Cambiar la dirección en el eje y en una dirección aleatoria
        color = "#" + ''.join(random.choices("0123456789ABCDEF", k=6))  # Generar un color aleatorio
        c.itemconfig(texto_id, fill=color)  # Cambiar el color del texto

    # Mover la pelota a la nueva posición
    c.move(pelota_id, direccion_x * VELOCIDAD_PELOTA, direccion_y * VELOCIDAD_PELOTA)
    c.move(texto_id, direccion_x * VELOCIDAD_PELOTA, direccion_y * VELOCIDAD_PELOTA)

    # Programar el siguiente movimiento de la pelota
    ventana.after(10, mover_pelota)

# Crear la ventana principal
ventana = Tk()
ventana.title("Movimiento de Pelota")
ventana.geometry(f"{ANCHO_CANVAS}x{ALTO_CANVAS}")

# Crear el Canvas
c = Canvas(ventana, width=ANCHO_CANVAS, height=ALTO_CANVAS, bg="gray15")
c.pack()

# Crear el círculo como fondo de la pelota
x_inicial = ANCHO_CANVAS // 2
y_inicial = ALTO_CANVAS // 2
pelota_id = c.create_oval(x_inicial - RADIO_PELOTA, y_inicial - RADIO_PELOTA, x_inicial + RADIO_PELOTA, y_inicial + RADIO_PELOTA, fill="gray15", outline="gray15")

# Crear el texto "DVD" en el centro del círculo
texto_id = c.create_text(x_inicial, y_inicial, text="DVD", font=("Helvetica", 26), fill="black")

# Definir la dirección inicial de la pelota
direccion_x = 1  # Movimiento hacia la derecha
direccion_y = 1  # Movimiento hacia abajo

# Iniciar el movimiento de la pelota
mover_pelota()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()