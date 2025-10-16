# Ejercicio 1: Sistema de Control de Sensores Múltiples

from abc import ABC, abstractmethod
from datetime import datetime
import random

# Implementa aquí tu solución

class Sensor(ABC):
    """Clase base abstracta para sensores en sistemas mecatrónicos"""
    
    def __init__(self, id_sensor, unidad_medida, rango_min, rango_max):
        self.id_sensor = id_sensor
        self.unidad_medida = unidad_medida
        self.rango_operacion = (rango_min, rango_max)
        self.historial_mediciones = []
        self.calibrado = False
    
    @abstractmethod
    def leer_dato(self):
        """Lee un dato del sensor y retorna el valor medido"""
        pass
    
    @abstractmethod
    def calibrar(self):
        """Calibra el sensor según sus especificaciones"""
        pass
    
    @abstractmethod
    def validar_lectura(self, valor):
        """Valida que la lectura esté dentro del rango operacional"""
        pass
    
    def registrar_medicion(self, valor):
        """Registra la medición en el historial"""
        registro = {
            'timestamp': datetime.now(),
            'valor': valor,
            'unidad': self.unidad_medida,
            'sensor_id': self.id_sensor
        }
        self.historial_mediciones.append(registro)
        return registro


# Implementa aquí las clases:
# - SensorTemperatura (LM35, termopar)
# - SensorPresion (MPX5700)
# - SensorDistancia (HC-SR04)
# - Encoder (rotatorio)
# - Acelerometro (MPU6050)

class SensorTemperatura(Sensor):
    """Sensor de temperatura LM35 o termopar"""
    def __init__(self, pin, id_sensor="TEMP-01"):
        super().__init__(id_sensor, "°C", -40, 125)
        self.pin = pin
        self.offset_calibracion = 0.0
    
    def leer_dato(self):
        # Simula lectura del sensor
        pass
    
    def calibrar(self):
        # Implementa calibración con offset
        pass
    
    def validar_lectura(self, valor):
        # Valida rango de temperatura
        pass


class SensorPresion(Sensor):
    """Sensor de presión MPX5700"""
    def __init__(self, pin, id_sensor="PRES-01"):
        super().__init__(id_sensor, "kPa", 0, 700)
        self.pin = pin
        self.compensacion_temperatura = True
    
    def leer_dato(self):
        pass
    
    def calibrar(self):
        pass
    
    def validar_lectura(self, valor):
        pass


class SensorDistancia(Sensor):
    """Sensor ultrasónico HC-SR04"""
    def __init__(self, pin_trigger, pin_echo, id_sensor="DIST-01"):
        super().__init__(id_sensor, "cm", 2, 400)
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo
        self.filtro_mediana = []
    
    def leer_dato(self):
        pass
    
    def calibrar(self):
        pass
    
    def validar_lectura(self, valor):
        pass


class Encoder(Sensor):
    """Encoder rotatorio incremental"""
    def __init__(self, pin_a, pin_b, ppr, id_sensor="ENC-01"):
        super().__init__(id_sensor, "pulsos", 0, float('inf'))
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pulsos_por_revolucion = ppr
        self.contador = 0
        self.direccion = 1
    
    def leer_dato(self):
        pass
    
    def calibrar(self):
        pass
    
    def validar_lectura(self, valor):
        pass


class Acelerometro(Sensor):
    """Acelerómetro MPU6050 (3 ejes)"""
    def __init__(self, i2c_address, id_sensor="ACC-01"):
        super().__init__(id_sensor, "m/s²", -16, 16)
        self.i2c_address = i2c_address
        self.datos_ejes = {'x': 0, 'y': 0, 'z': 0}
        self.filtro_digital = True
    
    def leer_dato(self):
        pass
    
    def calibrar(self):
        pass
    
    def validar_lectura(self, valor):
        pass


# Implementa la clase SistemaAdquisicion
class SistemaAdquisicion:
    """Sistema de adquisición de datos para múltiples sensores"""
    
    def __init__(self):
        self.sensores = []
        self.frecuencia_muestreo = 100  # Hz
    
    def agregar_sensor(self, sensor):
        """Agrega un sensor al sistema"""
        self.sensores.append(sensor)
    
    def leer_sensor(self, sensor):
        """Lee un sensor específico usando polimorfismo"""
        pass
    
    def leer_todos(self):
        """Lee todos los sensores registrados"""
        pass
    
    def generar_reporte(self):
        """Genera reporte con estadísticas de todos los sensores"""
        pass


# Programa principal
if __name__ == "__main__":
    # Crea diferentes sensores
    temp = SensorTemperatura(pin=0, id_sensor="TEMP-01")
    presion = SensorPresion(pin=1, id_sensor="PRES-01")
    distancia = SensorDistancia(pin_trigger=2, pin_echo=3, id_sensor="DIST-01")
    encoder = Encoder(pin_a=4, pin_b=5, ppr=600, id_sensor="ENC-01")
    acelerometro = Acelerometro(i2c_address=0x68, id_sensor="ACC-01")
    
    # Crea el sistema de adquisición
    sistema = SistemaAdquisicion()
    sistema.agregar_sensor(temp)
    sistema.agregar_sensor(presion)
    sistema.agregar_sensor(distancia)
    
    # Prueba tu implementación aquí
    # sistema.leer_sensor(temp)
    # datos = sistema.leer_todos()
    # sistema.generar_reporte()

