import pandas as pd
import numpy as np

def seleccion_multiple(df):
    print("=== DataFrame original ===")
    print(df)
    print()

    print("\n--- Filas en las posiciones [0, 3, 5] ---")
    print(df.iloc[[0, 3, 5]])

    filas_aleatorias = np.random.choice(df.index, size=3, replace=False)
    print("\n--- Filas aleatorias ---")
    print(df.iloc[filas_aleatorias])

    print("\n--- Estadísticas de las filas seleccionadas ([0, 3, 5]) ---")
    print(df.iloc[[0, 3, 5]].describe())


if __name__ == "__main__":
    data = {"Valor": list(range(100, 120))}
    df = pd.DataFrame(data)
    seleccion_multiple(df)