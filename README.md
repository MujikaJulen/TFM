15/11/25 

El código recoge el archivo CSV de un directorio determinado. Se especifica la articulación que se quiere observar (el listado viene en el archivo columnas.py).

Del archivo CSV se obtiene un dataframe que contiene toda la información. De ese df, se extraen los espacios en los nombres de las columnas.

Mediante la función "iloc" se aislan los ángulos de la articulación a observar para poder extraer los mínimos de la función generada y poder segmentar las diferentes
iteraciones de la marcha
