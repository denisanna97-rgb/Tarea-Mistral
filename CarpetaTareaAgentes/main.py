"""
PROYECTO MARVEL/DC - PREDICCIÓN DE APARICIONES
Ejecuta los 3 agentes en secuencia
"""

import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agente_1_normalizador import ejecutar_agente1
from agente_2_entrenador import ejecutar_agente2
from agente_3_comunicador import ejecutar_agente3


def main():
    
    print("PROYECTO MARVEL/DC - PREDICCIÓN DE APARICIONES")
    
    
    # Buscar el archivo CSV
    posibles_rutas = [
        '../data/07_Marvel_DC_Comic_Characters.csv',
        '07_Marvel_DC_Comic_Characters.csv',
        '../07_Marvel_DC_Comic_Characters.csv'
    ]
    
    ruta_data = None
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            ruta_data = ruta
            break
    
    if ruta_data is None:
        print("   Error: No se encontró el archivo 07_Marvel_DC_Comic_Characters.csv")
        print("   Asegúrate de que el archivo esté en la carpeta 'data'")
        return
    
    df = pd.read_csv(ruta_data)
    print(f" Dataset cargado: {df.shape[0]} filas × {df.shape[1]} columnas")
    
    # Identificar columna objetivo
    target = None
    for col in df.columns:
        if 'aparicion' in col.lower() or 'appear' in col.lower():
            target = col
            break
    
    if target is None:
        print("\n Columnas disponibles:")
        for i, col in enumerate(df.columns):
            print(f"   [{i}] {col}")
        target = input("\n Escribe el nombre de la columna de APARICIONES: ")
    
    print(f" Columna objetivo: '{target}'")
    
    # AGENTE 1
    
    print("AGENTE 1 - NORMALIZADOR")
    
    df_limpio = ejecutar_agente1(df, target)
    
    # AGENTE 2
    
    print("AGENTE 2 - ENTRENADOR")
    
    resultados = ejecutar_agente2(df_limpio, target)
    
    # AGENTE 3
    
    print("AGENTE 3 - COMUNICADOR")
    
    X = df_limpio.drop(columns=[target])
    ejecutar_agente3(resultados, target, X)
    
    # Resumen
    
    print("PROYECTO COMPLETADO")
    
    print(f" R² del modelo: {resultados['metricas']['r2']:.4f} ({resultados['metricas']['r2']*100:.2f}%)")
    print(f" Error promedio: {resultados['metricas']['mae']:.2f} apariciones")


if __name__ == "__main__":
    main()