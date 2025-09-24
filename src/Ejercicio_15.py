import pandas as pd

def modificar_datos(df):
    print("=== DataFrame original ===")
    print(df)
    print()

    # Modifica el valor en la fila 0, columna 0
    df.iloc[0, 0] = 99
    
    # Modifica los valores en las filas 1 y 2, columna 1
    df.iloc[1:3, 1] = [55, 66]
    
    # Modifica los valores en las filas 2 y 3, columnas 0 y 2
    df.iloc[2:4, [0, 2]] = [[100, 200], [300, 400]]

    print("\n--- DataFrame modificado ---")
    print(df)


if __name__ == "__main__":
    data = {"A": [1, 2, 3, 4], "B": [10, 20, 30, 40], "C": [100, 200, 300, 400]}
    df = pd.DataFrame(data)
    modificar_datos(df)