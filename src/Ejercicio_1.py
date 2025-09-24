import pandas as pd

def seleccionar_empleados(df):
    print("=== Seleccion de un empleado por ID ===")
    print(df.loc[101])
    print()

    print("=== Seleccion de multiples empleados por lista de IDs ===")
    print(df.loc[[101, 103, 105]])
    print()

    print("=== Seleccion de un rango de empleados ===")
    print(df.loc[101:105])
    print()

if __name__ == "__main__":
    data = {
        "Nombre": ["Ana", "Luis", "Marta", "Pedro", "Sofía"],
        "Departamento": ["IT", "Ventas", "RRHH", "IT", "Marketing"],
        "Salario": [3000, 2500, 2800, 3200, 2700]
    } 
    ids = [101, 102, 103, 104, 105]

    df = pd.DataFrame(data, index=ids)

    seleccionar_empleados(df)    