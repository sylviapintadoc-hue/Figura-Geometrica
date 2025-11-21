# Figura-Geometrica

-Ejecucion--
<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/890461d3-fac1-4187-b7fb-a907a29abd0d" />


# Taller de Figuras Geométricas – Programación Orientada a Objetos (POO)

Este proyecto implementa clases en Python usando los principios básicos de POO:

- Encapsulamiento  
- Herencia  
- Sobrescritura de métodos  
- Métodos `area()` y `perimetro()`  
- Validación con `@property` y `@setter`  

El taller incluye las clases:

- `FiguraGeometrica` (clase base)
- `Cuadrado`
- `Rectangulo`
- `main.py` (programa principal)

---

##  Estructura del Proyecto

```
/TallerFigurasPOO/
│── figurageometrica.py
│── cuadrado.py
│── rectangulo.py
│── circunferencia.py  (opcional)
│── main.py
└── README.md
```

---

##  Descripción de cada clase

### FiguraGeometrica
Clase padre que contiene:
- `ancho`, `alto` con encapsulamiento  
- Validaciones (> 0)  
- Método `area()`  
- Método `__str__()`  

### Cuadrado
Hereda de `FiguraGeometrica` y:
- Recibe solo un `lado`
- Sobrescribe:
  - `area()`
  - `perimetro()`
  - `__str__()`

### Rectangulo
Hereda de `FiguraGeometrica` y:
- Recibe `ancho` y `alto`
- Sobrescribe:
  - `area()`
  - `perimetro()`
  - `__str__()`

---

