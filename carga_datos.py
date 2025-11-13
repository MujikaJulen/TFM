# Librerías
import pandas as pd 
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Archivos de datos
import columnas

# Ruta del archivo CSV
path_csv = "/home/mujikajulen/Documentos/TFM/DatosProcesados/"


########################
###### FUNCIONES #######
########################

def data_csv(file_path, file_name):
    df = pd.read_csv(file_path + file_name, sep = ";", decimal = ",")
    df.columns = df.columns.str.strip() # Eliminar espacios en los nombres de columnas
    return df

def minimum_extraction(angles, height, distance):
    minimums, peak_values = find_peaks(-angles, height = -height, distance = distance)
    minimum_values = angles.iloc[minimums]
    filtered_minimum = minimums[(minimum_values > (np.mean(minimum_values) - 10)) & 
                            (minimum_values < (np.mean(minimum_values) + 10))]
    return filtered_minimum

def visualization(angles, filtered_minimum, title):
    plt.figure(figsize=(12,6))
    plt.plot(angles) 
    plt.plot(filtered_minimum, angles[filtered_minimum], "rx")
    plt.title(title)
    plt.xlabel("Frame")
    plt.ylabel("Grados")
    plt.grid(True)
    plt.show()
    
def gait_iteration(filtered_minimum, angles):
    print(f"Frames en los que se ha detectado un mínimo: {filtered_minimum}")
    for i in range(len(filtered_minimum)-1):
        init_frame = filtered_minimum[i]
        end_frame = filtered_minimum[i+1]
        gait_cycle = angles.loc[init_frame:end_frame]
        print(f"Ciclo de la marcha {i+1}. Comienzo: {init_frame}, Fin: {end_frame}")
        visualization(gait_cycle, [], f"Ciclo de la marcha {i+1}")
if __name__ == "__main__":
    
    file_name = "resultados_01_01_02.csv"
    file_path = "/home/mujikajulen/Documentos/TFM/DatosProcesados/"
    
    idx = columnas.AnkleR["idx"]  # Índice de la columna con la que se trabaja
    msg = columnas.AnkleR["msg"] # Eje Y en el gráfico 
    
    df = data_csv(file_path, file_name)
    angles = df.iloc[:,idx]
    filtered_minimum = minimum_extraction(angles, height = 70, distance = 20)
    visualization(angles, filtered_minimum, msg)
    
    gait_iteration(filtered_minimum, angles)


