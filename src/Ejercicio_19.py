import pandas as pd
import numpy as np

def combinaciones_iloc(df):
    print("=== DataFrame original ===")
    print(df)
    
    vista1 = df.iloc[:5]
    vista2 = df.iloc[::2]
    vista3 = df.sample(5)
    vista4 = df.iloc[np.random.choice(df.index, size=5, replace=False)]

    print("\n--- Vista 1 (primeras 5 filas) ---")
    print(vista1)

    print("\n--- Vista 2 (filas pares) ---")
    print(vista2)

    print("\n--- Vista 3 (muestra aleatoria) ---")
    print(vista3)

    print("\n--- Vista 4 (muestra estratificada aleatoria) ---")
    print(vista4)


if __name__ == "__main__":
    data = {"Num": list(range(1, 21))}
    df = pd.DataFrame(data)
    combinaciones_iloc(df)