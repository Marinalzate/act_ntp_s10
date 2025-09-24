import pandas as pd

def seleccion_columnas(df):
    print("=== DataFrame original ===")
    print(df)

    print("\n--- Primeras 3 columnas ---")
    print(df.iloc[:, :3])

    print("\n--- Columnas específicas (0, 2) ---")
    print(df.iloc[:, [0, 2]])

    print("\n--- Última columna ---")
    print(df.iloc[:, -1])

    print("\n--- Filas 0-2 y columnas 1-2 ---")
    print(df.iloc[0:3, 1:3])


if __name__ == "__main__":
    data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9], "D": [10, 11, 12]}
    df = pd.DataFrame(data)
    seleccion_columnas(df)