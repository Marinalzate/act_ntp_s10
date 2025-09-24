import pandas as pd
import numpy as np

def seleccion_avanzada(df):
    print("=== DataFrame original ===")
    print(df)
    
    print("\n--- Subconjunto de filas 0-2 y columnas 1-2 ---")
    print(df.iloc[0:3, 1:3])
    
    mask = np.array([True, False, True, False, True])
    print("\n--- Usando un array booleano para seleccionar filas ---")
    print(df.iloc[mask])
    
    print("\n--- Promedio de las columnas seleccionadas (B y C) ---")
    print(df.iloc[:, [1, 2]].mean())


if __name__ == "__main__":
    data = {"A": [10, 20, 30, 40, 50], "B": [5, 15, 25, 35, 45], "C": [2, 4, 6, 8, 10]}
    df = pd.DataFrame(data)
    seleccion_avanzada(df)