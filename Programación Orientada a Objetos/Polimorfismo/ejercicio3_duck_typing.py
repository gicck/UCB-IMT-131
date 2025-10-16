# Ejercicio 3: Sistema de Cálculo de Áreas con Duck Typing

# IMPORTANTE: Este ejercicio NO usa herencia explícita
# Demuestra el concepto de Duck Typing en Python

import math

# Implementa las figuras geométricas SIN usar herencia

class Rectangulo:
    """Clase para representar un rectángulo"""
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass
    
    def describir(self):
        pass


class Circulo:
    """Clase para representar un círculo"""
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass
    
    def describir(self):
        pass


class Triangulo:
    """Clase para representar un triángulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        # Para simplificar, asumimos triángulo equilátero
        pass
    
    def describir(self):
        pass


class Trapecio:
    """Clase para representar un trapecio"""
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        # Para simplificar, asumimos trapecio isósceles
        pass
    
    def describir(self):
        pass


class Rombo:
    """Clase para representar un rombo"""
    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass
    
    def describir(self):
        pass


# Implementa la clase CalculadoraGeometrica
class CalculadoraGeometrica:
    """Clase que trabaja con cualquier figura que tenga los métodos necesarios"""
    
    @staticmethod
    def calcular_area_total(figuras):
        """
        Calcula el área total de una lista de figuras
        Usa duck typing: funciona con cualquier objeto que tenga calcular_area()
        """
        pass
    
    @staticmethod
    def comparar_areas(figura1, figura2):
        """
        Compara las áreas de dos figuras
        """
        pass
    
    @staticmethod
    def generar_reporte(figuras):
        """
        Genera un reporte detallado de todas las figuras
        """
        pass
    
    @staticmethod
    def validar_figura(figura):
        """
        Valida que un objeto tenga los métodos necesarios
        Usa hasattr() para verificar
        """
        metodos_requeridos = ['calcular_area', 'calcular_perimetro', 'describir']
        for metodo in metodos_requeridos:
            if not hasattr(figura, metodo):
                return False, f"Falta el método: {metodo}"
        return True, "Figura válida"


# Programa principal
if __name__ == "__main__":
    # Crea diferentes figuras
    rectangulo = Rectangulo(5, 10)
    circulo = Circulo(7)
    triangulo = Triangulo(6, 8)
    trapecio = Trapecio(10, 6, 5)
    rombo = Rombo(8, 6)
    
    # Lista mixta de figuras
    figuras = [rectangulo, circulo, triangulo, trapecio, rombo]
    
    # Usa la calculadora (demuestra polimorfismo/duck typing)
    calc = CalculadoraGeometrica()
    
    # Prueba tus implementaciones
    # print(calc.calcular_area_total(figuras))
    # print(calc.comparar_areas(rectangulo, circulo))
    # calc.generar_reporte(figuras)
    
    # Prueba validación
    # print(calc.validar_figura(rectangulo))
