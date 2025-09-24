import pandas as pd

def filtrar_condiciones(df):
    print("=== Empleados de IT con salario > 70000 ===")
    filtro1 = df.loc[(df["Departamento"] == "IT") & (df["Salario"] > 70000)]
    print(filtro1)
    print(f"Total encontrados: {len(filtro1)}")
    print(filtro1.describe(include="all"))
    print()

    print("=== Empleados de Ventas o Marketing ===")
    filtro2 = df.loc[df["Departamento"].isin(["Ventas", "Marketing"])]
    print(filtro2)
    print(f"Total encontrados: {len(filtro2)}")
    print(filtro2.describe(include="all"))
    print()

    print("=== Empleados activos con más de 5 años de experiencia ===")
    filtro3 = df.loc[(df["Activo"] == True) & (df["Experiencia"] > 5)]
    print(filtro3)
    print(f"Total encontrados: {len(filtro3)}")
    print(filtro3.describe(include="all"))
    print()


if __name__ == "__main__":
    # DataFrame de ejemplo
    data = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"],
        "Departamento": ["IT", "Ventas", "IT", "RRHH", "Marketing", "IT"],
        "Salario": [75000, 82000, 65000, 90000, 72000, 95000],
        "Activo": [True, True, False, True, True, True],
        "Experiencia": [3, 7, 2, 10, 6, 8]
    }
    ids = [101, 102, 103, 104, 105, 106]

    df = pd.DataFrame(data, index=ids)

    filtrar_condiciones(df)