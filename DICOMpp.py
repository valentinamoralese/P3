import os #Para trabajar con rutas o archivos 
import random #Para seleccionar un archivo al azar
import pydicom #Para leer archivos tipo DICOM
import matplotlib.pyplot as plt #Para visualizar los archivos tipo DICOM como plots

#Ruta de carpeta con archivos
ruta_dicom = r'archivosDCM' 

# Obtener todos los archivos con extensión .dcm
archivos = [os.path.join(ruta_dicom, f) for f in os.listdir(ruta_dicom) if f.endswith('.dcm')]

# Verifica si se encontraron archivos
if not archivos:
    print("No se encontraron archivos .dcm en la carpeta especificada.")
else:
    #Leer un archivo aleatorio y mostrar metadatos 
    archivo_aleatorio = random.choice(archivos)
    ds = pydicom.dcmread(archivo_aleatorio)
    print(ds)

    print("Archivo DICOM seleccionado aleatoriamente:")
    print("Archivo:", os.path.basename(archivo_aleatorio))

    print("\n Metadatos anonimizados:")
    print("Modality:", ds.get("Modality", "No disponible")) #Tipo de estudio
    print("Study Date:", ds.get("StudyDate", "No disponible")) #Fecha del estudio
    print("Manufacturer:", ds.get("Manufacturer", "No disponible")) #Fabricante del equipo
    print("BodyPartExamined:", ds.get("BodyPartExamined", "No disponible")) #Parte del cuerpo examinada
    print("SliceThickness:", ds.get("SliceThickness", "No disponible")) #Grosor del corte
    print("InstanceNumber:", ds.get("InstanceNumber", "No disponible")) #Número de imágen en secuencia

    #Ordenar archivos por InstanceNumber 
    dicoms_ordenados = []

    for archivo in archivos:
        ds = pydicom.dcmread(archivo)
        instancia = getattr(ds, "InstanceNumber", 0)
        dicoms_ordenados.append((instancia, ds, os.path.basename(archivo))) 
        dicoms_ordenados.sort(key=lambda x: x[0])  # Ordenar por InstanceNumber

    print("\n Lista ordenada por InstanceNumber:")
    for pos, ds, nombre_archivo in dicoms_ordenados:
        print(f"InstanceNumber: {pos}  |  Archivo: {nombre_archivo}")


    #Mostrar la imagen en la última posición
    ds_ultima = dicoms_ordenados[-1][1]

    if 'PixelData' in ds_ultima:
        print("\n✅ Este archivo contiene imagen (PixelData). Mostrando imagen...")
        plt.imshow(ds_ultima.pixel_array, cmap='gray')
        plt.title(f"Imagen de la última posición (InstanceNumber: {dicoms_ordenados[-1][0]})")
        plt.axis('off')
        plt.show()
    else:
        print("⚠️ El archivo no contiene datos de imagen (PixelData no disponible).")

