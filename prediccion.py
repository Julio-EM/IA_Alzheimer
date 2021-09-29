# -*- coding: utf-8 -*-
"""
Cursos Libres CUNIZAB -USAC-
Curso de Introduccion a la IA con Python y Tensorflow
Titulo: Programa de entrenamiento de prediccion de enfermedades con IA
@author: Julio Mulul
Created on Tue Sep  7 14:23:27 2021
"""
#Importamos librerias
from tkinter import filedialog
from tkinter import *
import os
import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

class clase_prediccion():
    
    #Metodo para realizar la prediccion
    def prediccion(self, archivo, red):
        dato = load_img(archivo, target_size = (100, 100))
        dato = img_to_array(dato)
        dato = np.expand_dims(dato, axis = 0)
        arreglo = red.predict(dato) ##[[1,0,0]]
        resultado = arreglo[0] ##[1,0,0]
        respuesta = np.argmax(resultado) #Indice del numero mayor
        print(resultado)
        return respuesta
            
    #metodo para obtener la direccion y crear el objeto cnn
    def generar_direccion(self, direccion):
        modelo = './modelo/modelo.h5'
        pesos = './modelo/pesos.h5'
        
        #Cargamos los resultados del entrenamiento de la CNN
        cnn = load_model(modelo)
        cnn.load_weights(pesos)
        
        #llamamos la funcion predecir y le enviamos la url y cnn
        print("leyendo direccion obtenida...")
        print("Direccion obtenida: ",direccion)
        
        respuesta = self.prediccion(direccion, cnn)
                
        return respuesta