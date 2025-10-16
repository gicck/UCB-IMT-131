# Ejercicio 3: Refactorización usando Clases Abstractas (ABC)

from abc import ABC, abstractmethod

# Código inicial problemático (NO USAR - solo referencia)
"""
class ActuadorLineal:
    def mover(self, distancia):
        print(f"Moviendo linealmente {distancia}mm")

class ActuadorRotativo:
    def girar(self, angulos):
        print(f"Girando {angulos} grados")

class ActuadorNeumatico:
    def activar_cilindro(self, presion):
        print(f"Activando cilindro a {presion} PSI")
"""

# Implementa aquí tu refactorización:

# 1. Clase base abstracta Actuador
class Actuador(ABC):
    """Clase base abstracta para todos los actuadores"""
    
    def __init__(self):
        self._tiempo_operacion = 0
        self._estado = "inactivo"
    
    @abstractmethod
    def activar(self):
        """Método abstracto que debe ser implementado por las clases hijas"""
        pass
    
    @abstractmethod
    def desactivar(self):
        """Método abstracto que debe ser implementado por las clases hijas"""
        pass
    
    @abstractmethod
    def obtener_posicion_actual(self):
        """Método abstracto que debe ser implementado por las clases hijas"""
        pass
    
    def obtener_estado(self):
        """Método concreto disponible para todas las clases hijas"""
        return self._estado
    
    def tiempo_operacion(self):
        """Método concreto disponible para todas las clases hijas"""
        return self._tiempo_operacion


# 2. Refactoriza las clases existentes:
# - ActuadorLineal (debe heredar de Actuador)
# - ActuadorRotativo (debe heredar de Actuador)
# - ActuadorNeumatico (debe heredar de Actuador)

# 3. Crea nuevas clases:
# - ActuadorHidraulico
# - SistemaActuadores (clase gestora)

# Programa principal
if __name__ == "__main__":
    # Demuestra:
    # - Que no se puede instanciar la clase abstracta directamente
    # - Polimorfismo con diferentes tipos de actuadores
    # - Manejo uniforme de actuadores con SistemaActuadores
    pass
