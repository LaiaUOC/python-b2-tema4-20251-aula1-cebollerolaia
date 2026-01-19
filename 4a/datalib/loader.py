import csv

def load_csv(filepath: str) -> list:
    """
    Función para cargar datos desde un archivo CSV, retornando una lista de diccionarios, donde
    cada diccionario representa una fila del archivo CSV.
    """
    data = []
    with open(filepath, newline="") as file: # newline="" asegura que no haya lineas en blanco por los saltos de linea
        reader = csv.DictReader(file) # Convierte cada fila en un diccionario
        for row in reader:
            data.append(row) # Unimos todos los diccionarios en una lista
    return data
