"""
Enunciado:
Desarrolla un test para la función implementada calculate_rectangle_area, la función recibe dos parámetros ancho y
alto, y devuelve el área del rectángulo, calculada como ancho * alto. utilizando el enfoque de Desarrollo Guiado
por Pruebas (TDD).

Instrucciones de Implementación:
- Realizar los test considerando los distintos casos de prueba descritos a continuación.
- Ejecutar las pruebas y verificar que la implementación sea correcta.

Casos de Prueba:
    Prueba con valores enteros positivos para ancho y alto.
    Prueba con ancho/alto negativo.
    Prueba con ancho/alto no numérico.

Ejemplo:
    area = calcular_area_rectangulo(5, a)
    print("Área del rectángulo:", area)

"""

import pytest
from ej4c1 import calculate_rectangle_area

def test_calculate_rectangle_area(): 
    # Prueba con valores enteros positivos para ancho y alto.   
    width = 3
    lenght = 7
    expected_area = 21
    assert calculate_rectangle_area(width, lenght) == expected_area
    
def test_value_error_calculate_rectangle_area():
    # Prueba con ancho/alto negativo.
    width = -2
    length = 8
    
    with pytest.raises(ValueError):
        calculate_rectangle_area(width, length)
    

def test_type_error_calculate_rectangle_area():
    # Prueba con ancho/alto no numérico.
    witdh = "a"
    length = 5
    
    with pytest.raises(TypeError):
        calculate_rectangle_area(witdh, length)