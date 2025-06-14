import pydicom
import os
import numpy as np
import matplotlib.pyplot as plt

#Clase para crear objetos tipo paciente extraidos de los archivos tipo DICOM
class Paciente:
    def __init__(self, nombre, edad, id_paciente, imagen_asociada):
        self.__nombre = nombre
        self.__edad = edad
        self.__id_paciente = id_paciente
        self.__imagen_asociada = imagen_asociada  # matriz 3D (volumen DICOM)
