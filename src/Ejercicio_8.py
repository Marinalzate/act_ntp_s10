import pandas as pd

def filtrar_salarios(df):
    print("=== DataFrame original ===")
    print(df)
    print()

    def clasificar_salario(salario):
        if salario < 70000:
            return "Bajo"
        elif salario < 90000:
            return "Medio"
        else:
            return "Alto"

    df["Categoria_Salario"] = df["Salario"].apply(clasificar_salario)

    promedio = df["Salario"].mean()
    filtro_superior = df.loc[df["Salario"] > promedio]
    print("\n--- Empleados con salario superior al promedio ---")
    print(filtro_superior)

    p75 = df["Salario"].quantile(0.75)
    filtro_p75 = df.loc[df["Salario"] >= p75]
    print("\n--- Empleados con salario en el percentil 75 ---")
    print(filtro_p75)

    print("\n--- Distribución de categorías ---")
    print(df["Categoria_Salario"].value_counts())


if __name__ == "__main__":
    data = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"],
        "Departamento": ["IT", "Finanzas", "IT", "RRHH", "Marketing", "Finanzas"],
        "Salario": [75000, 82000, 65000, 95000, 72000, 120000],
        "Edad": [25, 40, 38, 50, 29, 45],
        "Activo": [True, True, True, True, True, True],
    }
    df = pd.DataFrame(data)
    filtrar_salarios(df)