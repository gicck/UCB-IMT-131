from motor_controller import MotorController

class ModuloTeleoperacion:
    def __init__(self, max_joystick_speed=100):
        self._max_joystick_speed = max_joystick_speed
    
    def controlar_manual(self, motor, joystick_value):
        """Control manual con validación automática"""
        # joystick_value entre -1.0 y 1.0
        target_speed = joystick_value * self._max_joystick_speed
        
        success = motor.set_speed(target_speed)
        
        if not success:
            print(f"Teleoperación: No se pudo configurar velocidad {target_speed}")
        
        return success