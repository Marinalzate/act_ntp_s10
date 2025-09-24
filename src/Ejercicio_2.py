import pandas as pd

def filtrar_empleados(df):
    print("=== Empleados mayores de 40 años ===")
    filtro1 = df.loc[df["Edad"] > 40]
    print(filtro1)
    print(f"Total encontrados:{len(filtro1)}\n")

    print("=== Empleados del departamento IT ===")
    filtro2 = df.loc[df["Departamento"] == "IT"]
    print(filtro2)
    print(f"Total encontrados: {len(filtro2)}\n")

    print("=== Empleados con salario > 80000 ===")
    filtro3 = df.loc[df["Salario"] > 80000]
    print(filtro3)
    print(f"Total encontrados: {len(filtro3)}\n")


if __name__ == "__main__":
    data = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía"],
        "Edad": [25, 45, 38, 50, 29],
        "Departamento": ["IT", "Ventas", "IT", "RRHH", "IT"],
        "Salario": [75000, 82000, 65000, 90000, 72000]
    }
    ids = [101, 102, 103, 104, 105]

    df = pd.DataFrame(data, index=ids)

    filtrar_empleados(df)