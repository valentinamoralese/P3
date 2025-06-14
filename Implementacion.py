
from Clases import DICOM, Paciente
import pydicom
import os
import numpy as np
import matplotlib.pyplot as plt


# Diccionarios globales
diccionario_pacientes = {}
diccionario_imagenes = {}

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Procesar carpeta DICOM")
        print("2. Crear paciente desde DICOM cargado")
        print("3. Cargar imagenes JPG o PNG")
        print("4. Realizar transformación geométrica a imagen ya cargada")
        print("5. Realizar binarización")
        print("6. Salir")
       

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            carpeta = input("Ingrese la ruta de la carpeta DICOM: ").strip()
            if not os.path.isdir(carpeta):
                print("Ruta inválida.")
                return
            dicom_obj = DICOM(carpeta)
            dicom_obj.procesar_y_guardar(diccionario_imagenes)
            print(diccionario_imagenes)

            # Mostrar cortes reconstruidos en un subplot
            dicom_obj.mostrar_cortes()

            
        
        elif opcion == '2':
            break
        elif opcion == '3':
            break
        elif opcion == '4':
            break
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

