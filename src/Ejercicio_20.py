import pandas as pd
import numpy as np

def analisis_iloc(df):
    print("=== DataFrame original ===")
    print(df)
    
    vista_posiciones = df.iloc[:10]
    vista_inversa = df.iloc[::-1]
    vista_random = df.sample(5)
    vista_systematica = df.iloc[::3]

    print("\n--- Vista de las 10 primeras filas ---")
    print(vista_posiciones)

    print("\n--- Vista en orden inverso ---")
    print(vista_inversa)

    print("\n--- Vista aleatoria (5 filas) ---")
    print(vista_random)

    print("\n--- Vista sistemática (cada 3 filas) ---")
    print(vista_systematica)

    print("\n--- Métricas: Muestra Aleatoria vs. Muestra Sistemática ---")
    print("\nEstadísticas de la muestra aleatoria:")
    print(vista_random.describe())
    print("\nEstadísticas de la muestra sistemática:")
    print(vista_systematica.describe())


if __name__ == "__main__":
    data = {"Valor": list(range(1, 51))}
    df = pd.DataFrame(data)
    analisis_iloc(df)