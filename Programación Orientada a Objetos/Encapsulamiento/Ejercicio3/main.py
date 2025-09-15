# Imports necesarios para que funcione el ejemplo
from motor_controller import MotorController
from modulo_navegacion import ModuloNavegacion
from modulo_emergencia import ModuloEmergencia
from modulo_teleoperacion import ModuloTeleoperacion

# Crear motores con encapsulamiento
motor_left = MotorController("LEFT_MOTOR", max_speed=120)
motor_right = MotorController("RIGHT_MOTOR", max_speed=120)

# Crear módulos
navegacion = ModuloNavegacion()
emergencia = ModuloEmergencia()
teleop = ModuloTeleoperacion(max_joystick_speed=100)

# Uso seguro
navegacion.mover_adelante(motor_left, motor_right, velocidad=90)
teleop.controlar_manual(motor_left, joystick_value=0.8)  # 80% velocidad

# Emergencia funciona correctamente
emergencia.detener_todo([motor_left, motor_right])

# Estado después de emergencia
print(f"Motor izquierdo: {motor_left.speed} RPM, Emergencia: {motor_left.is_emergency_active}")