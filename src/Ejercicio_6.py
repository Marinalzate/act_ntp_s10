import pandas as pd

def filtrar_strings(df):
    print("=== DataFrame original ===")
    print(df)
    print()

    filtro_nombre = df.loc[df["Nombre"].str.contains("1", na=False)]
    print("\n--- Empleados cuyo nombre contiene '1' ---")
    print(filtro_nombre)
    print("Total encontrados:", len(filtro_nombre))

    filtro_apellido = df.loc[df["Apellido"].str.endswith("5", na=False)]
    print("\n--- Empleados cuyo apellido termina en '5' ---")
    print(filtro_apellido)
    print("Total encontrados:", len(filtro_apellido))


    filtro_ciudad = df.loc[df["Ciudad"].str.startswith("B", na=False)]
    print("\n--- Empleados de ciudades que empiezan con 'B' ---")
    print(filtro_ciudad)
    print("Total encontrados:", len(filtro_ciudad))

if __name__ == "__main__":
    data = {
             "Nombre": ["Ana1", "Luis", "Marta", "Pedro1", "Sofia", "Carlos"],
        "Apellido": ["Gomez", "Lopez5", "Ramirez", "Martinez5", "Torres", "Perez"],
        "Ciudad": ["Bogotá", "Cali", "Barranquilla", "Medellín", "Bucaramanga", "Cartagena"],
        "Departamento": ["IT", "Ventas", "IT", "RRHH", "Marketing", "RRHH"],
        "Salario": [75000, 82000, 65000, 90000, 72000, 95000],
        "Edad": [25, 62, 38, 50, 29, 64],
        "Activo": [True, True, True, True, True, True],   
    }
    ids = [101, 102, 103, 104, 105, 106]

    df = pd.DataFrame(data, index=ids)

    filtrar_strings(df)    