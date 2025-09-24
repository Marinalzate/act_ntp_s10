import pandas as pd
import numpy as np

datos_empleados = {
    'nombre': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Marta', 'Juan', 'Elena', 'Diego', 'Carla', 'Javier',
               'Isabel', 'Raúl', 'Verónica', 'Miguel', 'Lucía', 'David', 'Laura', 'Carlos', 'Andrea', 'Fernando'],
    'edad': [25, 30, 45, 55, 60, 32, 28, 51, 40, 38, 58, 29, 35, 48, 53, 27, 33, 50, 42, 36],
    'salario': [50000, 60000, 80000, 95000, 110000, 65000, 55000, 98000, 75000, 70000, 105000, 58000, 68000, 92000, 102000, 52000, 63000, 90000, 85000, 72000],
    'departamento': ['Ventas', 'Recursos Humanos', 'Ingeniería', 'Ingeniería', 'Finanzas', 'Ventas', 'Marketing', 'Ingeniería', 'Recursos Humanos', 'Ventas',
                     'Finanzas', 'Marketing', 'Ingeniería', 'Ventas', 'Marketing', 'Recursos Humanos', 'Ingeniería', 'Finanzas', 'Ingeniería', 'Marketing']
}

df_empleados = pd.DataFrame(datos_empleados)

print("--- 1. Selección de nombre y salario (primeras 10 filas) ---")
seleccion_nombre_salario = df_empleados.loc[:, ['nombre', 'salario']]
print(seleccion_nombre_salario.head(10))


print("\n--- 2. Selección de un rango de columnas (primeras 10 filas) ---")
seleccion_rango_columnas = df_empleados.loc[:, 'nombre':'departamento']
print(seleccion_rango_columnas.head(10))

print("\n--- 3. Selección de empleados mayores de 50 años (primeras 10 filas) ---")
seleccion_mayores_50 = df_empleados.loc[df_empleados['edad'] > 50, ['nombre', 'salario', 'departamento']]
print(seleccion_mayores_50.head(10))