import pandas as pd
import numpy as np

def indices_dinamicos(df):
    print("=== DataFrame original ===")
    print(df)
    
    indices_mayores = df.index[df["Valor"] > 50].tolist()
    print("\n--- Índices con Valor > 50 ---")
    print(indices_mayores)
    
    posiciones_pares = [i for i in df.index if i % 2 == 0]
    print("\n--- Posiciones pares ---")
    print(posiciones_pares)
    
    p90 = int(np.percentile(df.index, 90))
    print("\n--- Filas >= percentil 90 ---")
    print(df.iloc[p90:])
    
    print("\n--- Muestra aleatoria de 5 filas ---")
    print(df.sample(5))


if __name__ == "__main__":
    data = {"Valor": list(range(1, 101))}
    df = pd.DataFrame(data)
    indices_dinamicos(df)