# Ejercicio 2: Sistema de Sensores con Herencia Múltiple

# Implementa aquí tu solución al ejercicio 2

class DispositivoElectronico:
    """Clase base para dispositivos electrónicos"""
    def __init__(self, voltaje_operacion, consumo_energia, pin_conexion):
        self.voltaje_operacion = voltaje_operacion
        self.consumo_energia = consumo_energia
        self.pin_conexion = pin_conexion
    
    def conectar(self):
        pass
    
    def desconectar(self):
        pass
    
    def verificar_alimentacion(self):
        pass


class ComunicacionWireless:
    """Clase base para comunicación inalámbrica"""
    def __init__(self, protocolo, frecuencia, alcance_metros):
        self.protocolo = protocolo
        self.frecuencia = frecuencia
        self.alcance_metros = alcance_metros
    
    def conectar_red(self):
        pass
    
    def enviar_datos(self, datos):
        pass
    
    def recibir_datos(self):
        pass


class SensorAmbiental:
    """Clase base para sensores ambientales"""
    def __init__(self, rango_medicion, precision, unidad_medida):
        self.rango_medicion = rango_medicion
        self.precision = precision
        self.unidad_medida = unidad_medida
    
    def calibrar(self):
        pass
    
    def tomar_lectura(self):
        pass
    
    def validar_rango(self, valor):
        pass


# Implementa aquí las clases derivadas:
# - SensorTemperaturaIoT
# - SensorHumedadIoT

# Programa principal
if __name__ == "__main__":
    pass
