import pandas as pd

def seleccion_basica(df):
    print("=== DataFrame original ===")
    print(df)

    print("\n--- Primera fila ---")
    print(df.iloc[0])

    print("\n--- Primeras 5 filas ---")
    print(df.iloc[:5])

    print("\n--- Última fila ---")
    print(df.iloc[-1])

    print("\n--- Filas específicas (0, 2, 4) ---")
    print(df.iloc[[0, 2, 4]])


if __name__ == "__main__":
    data = {"Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"], "Edad": [25, 40, 38, 50, 29, 45]}
    df = pd.DataFrame(data)
    seleccion_basica(df)