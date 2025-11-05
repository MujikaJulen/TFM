import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

colFrame = 0
colView = 1
colHipL = 2
colHipR = 3
colKneeL = 4
colKneeR = 5
colAnkleL = 6
colAnkleR = 7
colCGx = 14
colCGy = 15

# Dirección en la que se almacenan los datos procesados en formato CSV
direccion_csv = "/home/mujikajulen/Documentos/TFM/DatosProcesados/"

# Cargar el CSV con separador y formato decimal UTF-8
df = pd.read_csv(direccion_csv + "resultados_Joseba_cerca.csv", sep=";", decimal=",")
df.columns = df.columns.str.strip() # Eliminar espacios en los nombres de columnas

# Verifica columnas
print("Columnas detectadas:", df.columns.tolist())

# Extraer la serie de ángulos, seleccionando los datos por índice
angles = df.iloc[:, colAnkleR]

# Detectar mínimos en la serie de ángulos
minimos, _ = find_peaks(-angles, height=-150, distance=10)

# minimos: devuelve na lista de índices donde se detectan los mínimos
# _ : diccionario con el valor de cada pico detectado


# Eliminar datos inválidos
valores_minimos = angles.iloc[minimos]
umbral_minimos = np.mean(valores_minimos) - 10
minimos_filtrados = minimos[(valores_minimos > (np.mean(valores_minimos) - 10)) & 
                            (valores_minimos < (np.mean(valores_minimos) + 10))]

# Mostrar resultados
print("Frames con mínimos detectados:", minimos_filtrados)

# Visualizar
plt.plot(angles)
plt.plot(minimos_filtrados, angles[minimos_filtrados], "rx")
plt.title("Detección de ciclos en la marcha")
plt.xlabel("Frame")
plt.ylabel("Ángulo de rodilla izquierda")
plt.show()
