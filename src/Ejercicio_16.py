import pandas as pd

def seleccion_pasos(df):
    print("=== DataFrame original ===")
    print(df)

    print("\n--- Cada segunda fila ---")
    print(df.iloc[::2])

    print("\n--- Filas en orden inverso ---")
    print(df.iloc[::-1])

    print("\n--- Cada quinta fila desde la posición 2 ---")
    print(df.iloc[2::5])

    print("\n--- Filas 0-5 cada 2 y columnas 0-2 ---")
    print(df.iloc[0:6:2, 0:3])

if __name__ == "__main__":
    data = {"Num": list(range(1, 21))}
    df = pd.DataFrame(data)
    seleccion_pasos(df)