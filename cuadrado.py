from figurageometrica import FiguraGeometrica
class Cuadrado(FiguraGeometrica):
    """
    Clase para crear un objeto de tipo Cuadrado.
    """
    def __init__(self, lado):
        self.ancho = lado
        self.alto = lado
    def area(self):
        return self._ancho * self._alto
    def perimetro(self):
        return 4 * self._ancho
    def __str__(self):
        return f"Cuadrado(lado={self._ancho})"




