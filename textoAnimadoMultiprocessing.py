import os
import multiprocessing
import tkinter as tk
from tkinter import ttk
import time

main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)

#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def crearAnimacion(a, b, char):
    mylabel = createLabel(a,b)
    texto=""
    retardo: float=0.25
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update_idletasks()
        main_window.update()

#Aqui entra la concurrencia. 
if __name__ == '__main__':
    animacion_1 = multiprocessing.Process(name = 'animacion1',target= crearAnimacion,args=(10,10,'X',))
    animacion_2 = multiprocessing.Process(name = 'animacion2',target= crearAnimacion,args=(10,30,'Y',))
    animacion_3 = multiprocessing.Process(name = 'animacion3',target= crearAnimacion,args=(10,50,'Z',))
    
    animacion_1.start()
    animacion_2.start()
    animacion_3.start()

    animacion_1.join()
    animacion_2.join()
    animacion_3.join()

    opcionFinalizar()
    main_window.mainloop()    