from figurageometrica import FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    """
   Clase para crear un objeto de tipo rectangulo.
    """
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto
    def perimetro(self):
        return 2*(self.ancho * self.alto)
    def __str__(self):
        return "Rectangulo(ancho={self._ancho}, alto={self._alto})"

