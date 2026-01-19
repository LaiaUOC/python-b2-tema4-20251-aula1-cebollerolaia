def mean(data: list[dict], key: str) -> float:
    """
    Función para calcular la media de los valores numéricos de una clave específica en una lista
    de diccionarios.
    """
    return sum(float(row[key]) for row in data)/len(data)

def median(data: list[dict], key: str) -> float:
    """
    Función para calcular la mediana de los valores numéricos de una clave específica en una
    lista de diccionarios.
    """
    sorted_list = sorted(float(row[key]) for row in data)
    n = len(sorted_list)
    midpoint = n//2
    if n%2 == 1:
        return sorted_list[midpoint]
    else:
        return (sorted_list[midpoint - 1] + sorted_list[midpoint])/2
