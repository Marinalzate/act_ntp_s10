import pandas as pd

def seleccion_rangos(df):
    print("=== DataFrame original ===")
    print(df)

    print("\n--- Filas 10 a 20 ---")
    print(df.iloc[10:21])

    print("\n--- Últimas 10 filas ---")
    print(df.iloc[-10:])

    print("\n--- Filas pares ---")
    print(df.iloc[::2])

    print("\n--- Cada tercera fila ---")
    print(df.iloc[::3])

if __name__ == "__main__":
    data = {"Valor": list(range(1, 31))}
    df = pd.DataFrame(data)
    seleccion_rangos(df)