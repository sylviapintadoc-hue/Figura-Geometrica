class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser mayor que 0")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            raise ValueError("El alto debe ser mayor que 0")

    def area(self):
        return self._ancho * self._alto

    def __str__(self):
        return f"FiguraGeometrica(ancho={self._ancho}, alto={self._alto})"



if __name__ == '__main__':
    figura = FiguraGeometrica(6, 8)
    print(figura)
    print("Área:", figura.area())
