from cuadrado import Cuadrado
from rectangulo import Rectangulo
"""
Programa principal
"""

def sumar_areas(figura):
    total = 0
    for figura in figura:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


if __name__ == "__main__":
    print("=== PRUEBAS DEL TALLER ===\n")

    # Crear objetos correctos
    c1 = Cuadrado(5)
    c2 = Cuadrado(10)
    r1 = Rectangulo(4, 8)
    r2 = Rectangulo(3, 6)

    figuras = [c1, c2, r1, r2]

    # Mostrar información
    for f in figuras:
        print(f)
        print("Área:", f.area())
        print("Perímetro:", f.perimetro())
        print("-" * 25)

    # Probar valor inválido
    try:
        c1.ancho = -9
    except Exception as e:
        print("ERROR al intentar asignar un valor inválido:", e)

    print("\nSuma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))
