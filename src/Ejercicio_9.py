import pandas as pd
import numpy as np

def aplicar_filtros_complejos(df: pd.DataFrame) -> None:
    """
    Aplica y muestra los resultados de filtros complejos sobre un DataFrame de empleados.

    Args:
        df: El DataFrame de pandas a filtrar.
    """
    print("--- DataFrame Original ---")
    print(df)
    
    # Filtro 1: Empleados activos de IT o Finanzas, con salario alto y jóvenes.
    criterio_activo = df["Activo"] == True
    criterio_depto = df["Departamento"].isin(["IT", "Finanzas"])
    criterio_salario = df["Salario"] > 60000
    criterio_edad = df["Edad"] < 45
    
    filtro_combinado_1 = df.loc[criterio_activo & criterio_depto & criterio_salario & criterio_edad]
    
    print("\n--- Filtro 1: Activos, IT o Finanzas, salario > 60000 y edad < 45 ---")
    print(filtro_combinado_1)

    # Filtro 2: Empleados en ciudades específicas con alta experiencia.
    criterio_ciudad = df["Ciudad"].isin(["Bogotá", "Medellín"])
    criterio_experiencia = df["Experiencia"] > 10

    filtro_combinado_2 = df.loc[criterio_ciudad & criterio_experiencia]
    
    print("\n--- Filtro 2: Ciudades específicas con experiencia > 10 ---")
    print(filtro_combinado_2)

    print("\n--- Resumen Estadístico de Filtro 1 ---")
    print(filtro_combinado_1.describe())

    print("\n--- Resumen Estadístico de Filtro 2 ---")
    print(filtro_combinado_2.describe())

# Bloque principal para la ejecución del script
if __name__ == "__main__":
    datos = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"],
        "Departamento": ["IT", "Finanzas", "IT", "RRHH", "Marketing", "Finanzas"],
        "Salario": [75000, 82000, 65000, 95000, 72000, 120000],
        "Edad": [25, 40, 38, 50, 29, 45],
        "Activo": [True, True, True, False, True, True],
        "Ciudad": ["Bogotá", "Cali", "Medellín", "Bogotá", "Bucaramanga", "Medellín"],
        "Experiencia": [3, 12, 7, 15, 5, 20],
    }
    
    df_empleados = pd.DataFrame(datos)
    aplicar_filtros_complejos(df_empleados)