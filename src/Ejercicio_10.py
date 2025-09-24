import pandas as pd

def realizar_analisis_completo(df: pd.DataFrame):
    print("--- Datos Originales de Empleados ---")
    print(df)

    vista_it = df.loc[df["Departamento"] == "IT"]
    print("\n  Empleados en el departamento de IT:")
    print(vista_it)

    vista_finanzas = df.loc[df["Departamento"] == "Finanzas"]
    print("\n  Empleados en el departamento de Finanzas:")
    print(vista_finanzas)

    vista_activos = df.loc[df["Activo"] == True]
    print("\n  Empleados Activos:")
    print(vista_activos)

    print("\n--- Salario y Edad Promedio por Grupo ---")
    metricas_depto = df.groupby("Departamento")[["Salario", "Edad"]].mean()
    print("\n  Métricas por Departamento:")
    print(metricas_depto)

    metricas_ciudad = df.groupby("Ciudad")[["Salario", "Edad"]].mean()
    print("\n  Métricas por Ciudad:")
    print(metricas_ciudad)

    print("\n--- Segmentos Clave de Empleados ---")
    umbral_salario_alto = df["Salario"].quantile(0.9)
    top_performers = df.loc[df["Salario"] >= umbral_salario_alto]
    print(f"\n  Top Performers (Salario >= {umbral_salario_alto:.2f}):")
    print(top_performers)

    recien_llegados = df.loc[df["Experiencia"] <= 2]
    print("\n  Recién Llegados (<= 2 años de experiencia):")
    print(recien_llegados)

if __name__ == "__main__":
    datos = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos", "Laura", "Andrés"],
        "Departamento": ["IT", "Finanzas", "IT", "RRHH", "Marketing", "Finanzas", "IT", "Marketing"],
        "Salario": [75000, 82000, 65000, 95000, 72000, 120000, 68000, 105000],
        "Edad": [25, 40, 38, 50, 29, 45, 23, 36],
        "Activo": [True, True, True, False, True, True, True, True],
        "Ciudad": ["Bogotá", "Cali", "Medellín", "Bogotá", "Bucaramanga", "Medellín", "Bogotá", "Cali"],
        "Experiencia": [3, 12, 7, 15, 5, 20, 1, 2],
    }
    df_empleados = pd.DataFrame(datos)
    realizar_analisis_completo(df_empleados)