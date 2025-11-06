# Librerías
import pandas as pd 
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Archivos de datos
import columnas

#########################
### PARTICULARIZACIÓN ###
#########################

index = columnas.KneeR["idx"]  # Índice de la columna con la que se trabaja
mensaje = columnas.KneeR["msg"] # Eje Y en el gráfico 
archive_name = "resultados_Joseba_cerca.csv"  # Nombre del archivo CSV a cargar

#########################
#### CARGA DE DATOS #####
#########################

# Dirección en la que se almacenan los datos procesados en formato CSV
path_csv = "/home/mujikajulen/Documentos/TFM/DatosProcesados/"

# Cargar el CSV con separador y formato decimal UTF-8
df = pd.read_csv(path_csv + archive_name, sep = ";", decimal = ",")
df.columns = df.columns.str.strip() # Eliminar espacios en los nombres de columnas

# Verifica columnas
# print("Columnas detectadas:", df.columns.tolist())

###########################
### EXTRACCIÓN DE DATOS ###
###########################

# Extraer la serie de ángulos, seleccionando los datos por índice
angles = df.iloc[:, index]  # Ángulo de la rodilla izquierda

# Detectar mínimos en la serie de ángulos
minimums, peak_values = find_peaks(-angles, height=-150, distance=10)

# minimos: devuelve na lista de índices donde se detectan los mínimos
# peak_values : diccionario con el valor de cada pico detectado


# Eliminar datos inválidos
minimum_values = angles.iloc[minimums]
filtered_minimum = minimums[(minimum_values > (np.mean(minimum_values) - 10)) & 
                            (minimum_values < (np.mean(minimum_values) + 10))]

# Mostrar resultados
print("Frames con mínimos detectados:", filtered_minimum)

# Visualizar
plt.plot(angles)
plt.plot(filtered_minimum, angles[filtered_minimum], "rx")
plt.title("Detección de ciclos en la marcha")
plt.xlabel("Frame")
plt.ylabel(mensaje)
plt.show()


