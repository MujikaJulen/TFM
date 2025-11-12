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

# *? Se podría configurar para que solo haya que cambiar una vez la articulación

index = columnas.AnkleL["idx"]  # Índice de la columna con la que se trabaja
mensaje = columnas.AnkleL["msg"] # Eje Y en el gráfico 
archive_name = "resultados_01_01_02.csv"  # Nombre del archivo CSV a cargar


#########################
#### CARGA DE DATOS #####
#########################

# Dirección en la que se almacenan los datos procesados en formato CSV
path_csv = "/home/mujikajulen/Documentos/TFM/DatosProcesados/"

# Cargar el CSV con separador y formato decimal UTF-8
df = pd.read_csv(path_csv + archive_name, sep = ";", decimal = ",")
df.columns = df.columns.str.strip() # Eliminar espacios en los nombres de columnas

# ** Si se quieren comprobar las columnas del archivo CSV

# print("Columnas detectadas:", df.columns.tolist())

###########################
### EXTRACCIÓN DE DATOS ###
###########################

# Extraer la serie de ángulos, seleccionando los datos por índice
angles = df.iloc[:, index]  # Ángulo de la rodilla izquierda

# Detectar mínimos en la serie de ángulos
minimums, peak_values = find_peaks(-angles, height=-150, distance=10)

# minimos: devuelve los frames en los que se observan los mínimos
# peak_values : valores de los mínimos detectados


# Eliminar datos inválidos alejados de la media del resto de mínimos. Se consideran valores anómalos.
minimum_values = angles.iloc[minimums] # Devuelve los frames en los que se dan los valores mínimos
filtered_minimum = minimums[(minimum_values > (np.mean(minimum_values) - 10)) & 
                            (minimum_values < (np.mean(minimum_values) + 10))]

# Mostrar resultados
print("Frames con mínimos detectados:", filtered_minimum)

# Segmentación de las repeticiones de la marcha


###########################
### VISUALIZACIÓN DATOS ###
###########################

plt.plot(angles) 
plt.plot(filtered_minimum, angles[filtered_minimum], "rx")
plt.title("Detección de ciclos en la marcha")
plt.xlabel("Frame")
plt.ylabel(mensaje)
plt.show()


