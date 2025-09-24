import pandas as pd

def filtrar_fechas(df):
    print("=== DataFrame original ===")
    print(df)
    print()

    df["Fecha_Ingreso"] = pd.to_datetime(df["Fecha_Ingreso"])

    filtro_2022 = df.loc[df["Fecha_Ingreso"].dt.year == 2022]
    print("\n--- Empleados que ingresaron en 2022 ---")
    print(filtro_2022)
    print("Antigüedad promedio:", (pd.Timestamp.today() - filtro_2022["Fecha_Ingreso"]).dt.days.mean() / 365)

    fecha_limite = pd.Timestamp.today() - pd.DateOffset(years=2)
    filtro_ultimos2 = df.loc[df["Fecha_Ingreso"] >= fecha_limite]
    print("\n--- Empleados que ingresaron en los últimos 2 años ---")
    print(filtro_ultimos2)
    print("Antigüedad promedio:", (pd.Timestamp.today() - filtro_ultimos2["Fecha_Ingreso"]).dt.days.mean() / 365)

    filtro_trim1 = df.loc[df["Fecha_Ingreso"].dt.month.isin([1, 2, 3])]
    print("\n--- Empleados que ingresaron en el primer trimestre ---")
    print(filtro_trim1)
    print("Antigüedad promedio:", (pd.Timestamp.today() - filtro_trim1["Fecha_Ingreso"]).dt.days.mean() / 365)


if __name__ == "__main__":
    data = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"],
        "Departamento": ["IT", "Ventas", "IT", "RRHH", "Marketing", "RRHH"],
        "Fecha_Ingreso": [
            "2022-05-10",
            "2021-03-15",
            "2023-01-20",
            "2020-02-01",
            "2024-07-10",
            "2022-01-05",
        ],
        "Salario": [75000, 82000, 65000, 90000, 72000, 95000],
        "Edad": [25, 62, 38, 50, 29, 64],
        "Activo": [True, True, True, True, True, True],
    }
    ids = [101, 102, 103, 104, 105, 106]

    df = pd.DataFrame(data, index=ids)

    filtrar_fechas(df)
