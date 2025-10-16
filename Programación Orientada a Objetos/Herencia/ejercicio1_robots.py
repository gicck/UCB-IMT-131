# Ejercicio 1: Sistema de Control de Robots Industriales

# Implementa aquí tu solución al ejercicio 1
# Clase base Robot

class Robot:
    def __init__(self, modelo, año_fabricacion):
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.estado = "inactivo"
        self.horas_operacion = 0
    
    def encender(self):
        pass
    
    def apagar(self):
        pass
    
    def obtener_estado(self):
        pass
    
    def registrar_horas(self, horas):
        pass

# Clase RobotIndustrial

# Clase RobotSoldador

# Programa principal
if __name__ == "__main__":
    pass
