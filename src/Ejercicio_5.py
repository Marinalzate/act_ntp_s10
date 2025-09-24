import pandas as pd

def modificar_empleados(df):
    print("=== Estado inicial del DataFrame ===")
    print(df)
    print()

    df.loc[df["Departamento"] == "IT", "Salario"] *= 1.10

    df.loc[df["Edad"]> 60, "Activo"] = False

    df.loc[df["Departamento"] == "RRHH", "Ciudad"] = "Bogota"

    print("=== Estado final del DataFrame (modificado) ===")
    print(df)


if __name__ == "__main__":
    data = {
                "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"],
        "Edad": [25, 62, 38, 50, 29, 64],
        "Departamento": ["IT", "Ventas", "IT", "RRHH", "Marketing", "RRHH"],
        "Salario": [75000, 82000, 65000, 90000, 72000, 95000],
        "Activo": [True, True, True, True, True, True],
        "Ciudad": ["Medellín", "Cali", "Bogotá", "Medellín", "Cali", "Medellín"]
    }
    ids = [101, 102, 103, 104, 105, 106]

    df = pd.DataFrame(data, index=ids)

    modificar_empleados(df)     