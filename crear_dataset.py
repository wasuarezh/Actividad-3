import os
import pandas as pd

# Imprimir la ruta actual de trabajo
print(f"Ruta actual: {os.getcwd()}")

try:
    # Definir los datos del transporte masivo
    data = {
        'Estacion_Inicio': ['Estacion_A', 'Estacion_B', 'Estacion_C', 'Estacion_A', 'Estacion_B', 'Estacion_A'],
        'Estacion_Fin': ['Estacion_B', 'Estacion_C', 'Estacion_D', 'Estacion_C', 'Estacion_D', 'Estacion_D'],
        'Distancia_km': [5, 3, 7, 8, 10, 12],
        'Tiempo_Minutos': [10, 7, 15, 18, 22, 25],
        'Flujo_Pasajeros': [200, 150, 250, 300, 100, 180]
    }

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Guardar el DataFrame como CSV en una ruta específica (por ejemplo, el Escritorio)
    df.to_csv('C:/Users/Wilder/Desktop/Actividad 3/transporte_masivo_data.csv', index=False)

    # Confirmación de éxito
    print("Archivo transporte_masivo_data.csv generado correctamente.")
except Exception as e:
    print(f"Error al generar el archivo CSV: {e}")


