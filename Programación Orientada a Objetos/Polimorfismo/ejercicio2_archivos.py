# Ejercicio 2: Sistema de Control de Actuadores

from abc import ABC, abstractmethod
import time

# Implementa aquí tu solución

class Actuador(ABC):
    """Clase base abstracta para actuadores en sistemas mecatrónicos"""
    
    def __init__(self, id_actuador, pin_control):
        self.id_actuador = id_actuador
        self.pin_control = pin_control
        self.estado_actual = "inactivo"
        self.tiempo_operacion = 0
        self.ultima_activacion = None
    
    @abstractmethod
    def activar(self, intensidad):
        """Activa el actuador con la intensidad especificada"""
        pass
    
    @abstractmethod
    def desactivar(self):
        """Desactiva el actuador completamente"""
        pass
    
    @abstractmethod
    def obtener_estado(self):
        """Retorna el estado actual del actuador"""
        pass
    
    def verificar_limites(self, valor, min_val, max_val):
        """Valida que el valor esté dentro de los rangos operacionales"""
        if valor < min_val or valor > max_val:
            raise ValueError(f"Valor {valor} fuera de rango [{min_val}, {max_val}]")
        return True


# Implementa aquí las clases:
# - MotorDC
# - ServoMotor
# - MotorPasoAPaso
# - SolenoideLineal
# - BombaHidraulica

class MotorDC(Actuador):
    """Motor DC con control PWM"""
    def __init__(self, id_actuador, pin_pwm, pin_dir):
        super().__init__(id_actuador, pin_pwm)
        self.pin_direccion = pin_dir
        self.pwm_actual = 0  # 0-255
        self.rpm_actual = 0
        self.direccion = "horario"
    
    def activar(self, intensidad):
        """
        Activa el motor con PWM especificado
        intensidad: 0-255 para PWM, signo indica dirección
        """
        pass
    
    def desactivar(self):
        pass
    
    def obtener_estado(self):
        pass
    
    def cambiar_direccion(self):
        """Invierte la dirección de rotación"""
        pass


class ServoMotor(Actuador):
    """Servomotor de posición"""
    def __init__(self, id_actuador, pin_pwm):
        super().__init__(id_actuador, pin_pwm)
        self.angulo_actual = 90  # posición inicial centrada
        self.angulo_min = 0
        self.angulo_max = 180
        self.velocidad_movimiento = 60  # grados/segundo
    
    def activar(self, intensidad):
        """
        Mueve el servo al ángulo especificado
        intensidad: ángulo deseado (0-180°)
        """
        pass
    
    def desactivar(self):
        pass
    
    def obtener_estado(self):
        pass
    
    def mover_suave(self, angulo_objetivo):
        """Mueve el servo suavemente al ángulo objetivo"""
        pass


class MotorPasoAPaso(Actuador):
    """Motor paso a paso con control de microstepping"""
    def __init__(self, id_actuador, pin_step, pin_dir, pasos_por_rev=200):
        super().__init__(id_actuador, pin_step)
        self.pin_direccion = pin_dir
        self.pasos_por_revolucion = pasos_por_rev
        self.posicion_actual = 0  # en pasos
        self.microstepping = 1  # 1, 2, 4, 8, 16
        self.velocidad = 100  # pasos/segundo
    
    def activar(self, intensidad):
        """
        Mueve el motor un número específico de pasos
        intensidad: número de pasos a mover
        """
        pass
    
    def desactivar(self):
        pass
    
    def obtener_estado(self):
        pass
    
    def mover_angulo(self, angulo):
        """Mueve el motor un ángulo específico en grados"""
        pass


class SolenoideLineal(Actuador):
    """Solenoide o actuador lineal eléctrico"""
    def __init__(self, id_actuador, pin_control):
        super().__init__(id_actuador, pin_control)
        self.extendido = False
        self.fuerza_empuje = 10  # Newtons
        self.carrera = 50  # mm
    
    def activar(self, intensidad):
        """
        Activa el solenoide
        intensidad: 0 (retraer) o 1 (extender)
        """
        pass
    
    def desactivar(self):
        pass
    
    def obtener_estado(self):
        pass


class BombaHidraulica(Actuador):
    """Bomba hidráulica con control de caudal"""
    def __init__(self, id_actuador, pin_pwm):
        super().__init__(id_actuador, pin_pwm)
        self.caudal_actual = 0  # 0-100%
        self.presion_trabajo = 0  # bar
        self.temperatura = 25  # °C
        self.proteccion_termica = 80  # °C máximo
    
    def activar(self, intensidad):
        """
        Activa la bomba con caudal especificado
        intensidad: 0-100 (porcentaje de caudal)
        """
        pass
    
    def desactivar(self):
        pass
    
    def obtener_estado(self):
        pass
    
    def verificar_temperatura(self):
        """Verifica que la temperatura esté en rango seguro"""
        pass


# Implementa la clase ControladorActuadores
class ControladorActuadores:
    """Controlador universal para múltiples tipos de actuadores"""
    
    def __init__(self):
        self.actuadores = []
        self.emergencia_activa = False
    
    def agregar_actuador(self, actuador):
        """Agrega un actuador al controlador"""
        self.actuadores.append(actuador)
    
    def comandar(self, actuador, parametros):
        """
        Envía comando a un actuador específico usando polimorfismo
        """
        pass
    
    def secuencia(self, comandos):
        """
        Ejecuta una secuencia coordinada de comandos
        comandos: lista de tuplas (actuador, parametros, tiempo_espera)
        """
        pass
    
    def parada_emergencia(self):
        """Detiene todos los actuadores inmediatamente"""
        pass
    
    def obtener_estado_sistema(self):
        """Retorna el estado de todos los actuadores"""
        pass


# Programa principal
if __name__ == "__main__":
    # Crea diferentes actuadores
    motor_dc = MotorDC("MOTOR-01", pin_pwm=9, pin_dir=8)
    servo = ServoMotor("SERVO-01", pin_pwm=10)
    stepper = MotorPasoAPaso("STEP-01", pin_step=11, pin_dir=12, pasos_por_rev=200)
    solenoide = SolenoideLineal("SOL-01", pin_control=13)
    bomba = BombaHidraulica("BOMBA-01", pin_pwm=14)
    
    # Crea el controlador
    controlador = ControladorActuadores()
    controlador.agregar_actuador(motor_dc)
    controlador.agregar_actuador(servo)
    controlador.agregar_actuador(stepper)
    
    # Prueba tu implementación
    # Ejemplo: secuencia de brazo robótico
    # secuencia_movimientos = [
    #     (servo, 90, 1.0),      # Mover servo a 90°, esperar 1s
    #     (motor_dc, 150, 2.0),  # Activar motor DC, esperar 2s
    #     (stepper, 400, 1.5),   # Mover stepper 400 pasos, esperar 1.5s
    # ]
    # controlador.secuencia(secuencia_movimientos)

