# -*- coding: utf-8 -*-
"""
Cursos Libres CUNIZAB -USAC-
Curso de Introduccion a la IA con Python y Tensorflow
Titulo: Programa de entrenamiento de prediccion de enfermedades con IA
@author: Julio Mulul
Created on Tue Sep  7 14:23:27 2021
"""
#importando los modulos necesarios
from prediccion import clase_prediccion
#importando las librerias
import tkinter
from tkinter import filedialog
from tkinter import *
import os

#creacion del objeto clase_prediccion
obj_prediccion = clase_prediccion()

#creamos nuestra ventana principal
ventana = Tk()
ventana.title("Prediccion") #Cambiar el nombre de la ventana 
ventana.geometry("520x300") #Configurar tamaño 


saludo = tkinter.Label(text= "Bienvenido al programa de prediccion de alzhemier", anchor="center")
#saludo.place(x=35, y=30)
saludo.pack()
saludo.config(font=('Arial', 15))

msg = tkinter.Label(anchor= ("center"))
msg.pack()
msg.config(font=('Arial', 15))

def abrir_archivo():
    msg.config(text="Obteniendo imagen...")
    
    global direccion
    archivo_abierto = filedialog.askopenfilename(initialdir = "/", title = "Seleccione archivo", filetypes = (("jpeg files", "*.jpg"), ("all files", "*.*")))
    boton1 = Button(text = "Predecir", command = prediccion).place(x=250, y=200)
    direccion = archivo_abierto
    
    
    
boton1 = Button(text = "abrir archivo", command = abrir_archivo).place(x=200, y=100)

def cerrar():
    msg.config(text = ("saliendo..."))
    ventana.destroy()
boton2 = Button(text = "salir", command = cerrar).place(x=300, y=100)


def prediccion():
    resultado = obj_prediccion.generar_direccion(direccion)
    print(resultado)
 
    if resultado == 0:
        msg.config(text = ("Leve"))
        
        print("leve!")
        
        
    elif resultado == 2:
        msg.config(text = "Muy Leve")
        
        print("muy leve!")
        
    elif resultado == 3:
        msg.config(text = "Normal")
        
        print("normal!")

ventana.mainloop()