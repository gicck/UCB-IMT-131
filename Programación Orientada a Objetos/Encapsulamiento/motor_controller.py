# SOLUCIÓN: Motor con encapsulamiento adecuado
class MotorController:
    def __init__(self, motor_id, max_speed=100, min_speed=-100):
        self._id = motor_id
        # Atributos privados - protegidos del acceso directo
        self._max_speed = max_speed
        self._min_speed = min_speed
        self._current_speed = 0
        self._pwm_value = 0
        self._direction = "forward"
        self._emergency_active = False
        self._is_enabled = True
    
    def set_speed(self, target_speed):
        """Método principal para controlar velocidad con validaciones"""
        if not self._is_enabled:
            print(f"Motor {self._id}: Deshabilitado, no se puede mover")
            return False
            
        if self._emergency_active:
            print(f"Motor {self._id}: Emergencia activa, no se puede mover")
            return False
        
        # Validación de límites físicos
        if not self._min_speed <= target_speed <= self._max_speed:
            print(f"Motor {self._id}: Velocidad {target_speed} fuera de rango [{self._min_speed}, {self._max_speed}]")
            return False
        
        # Actualización segura del estado interno
        self._current_speed = target_speed
        self._pwm_value = abs(target_speed)
        self._direction = "forward" if target_speed >= 0 else "reverse"
        
        print(f"Motor {self._id}: Velocidad={self._current_speed}, PWM={self._pwm_value}, Dir={self._direction}")
        return True
    
    def stop(self):
        """Detener motor de forma segura"""
        self._current_speed = 0
        self._pwm_value = 0
        print(f"Motor {self._id}: Detenido")
    
    def activate_emergency(self):
        """Activar modo emergencia"""
        self._emergency_active = True
        self.stop()
        print(f"Motor {self._id}: EMERGENCIA ACTIVADA")
    
    def reset_emergency(self):
        """Resetear modo emergencia"""
        self._emergency_active = False
        print(f"Motor {self._id}: Emergencia reseteada")
    
    def enable(self):
        """Habilitar motor"""
        self._is_enabled = True
        
    def disable(self):
        """Deshabilitar motor"""
        self._is_enabled = False
        self.stop()
    
    # --- PROPIEDADES PARA LECTURA SEGURA ---
    @property
    def speed(self):
        return self._current_speed
    
    @property
    def is_emergency_active(self):
        return self._emergency_active
    
    @property
    def is_enabled(self):
        return self._is_enabled
    
    @property
    def motor_id(self):
        return self._id
    
    # --- MÉTODOS DE COMPATIBILIDAD (TRANSICIÓN) ---
    @property 
    def velocidad_actual(self):
        """Compatibilidad con código legacy - DEPRECADO"""
        import warnings
        warnings.warn("velocidad_actual está deprecado, usar property 'speed'", DeprecationWarning)
        return self._current_speed
    
    @velocidad_actual.setter
    def velocidad_actual(self, value):
        """Setter de compatibilidad que redirige al método seguro"""
        import warnings
        warnings.warn("Asignación directa deprecada, usar set_speed()", DeprecationWarning)
        self.set_speed(value)

# Ejemplo de uso
if __name__ == "__main__":
    motor = MotorController(motor_id=1)
    motor.set_speed(50)
    motor.set_speed(150)  # Fuera de rango
    motor.activate_emergency()
    motor.set_speed(30)   # No debería moverse
    motor.reset_emergency()
    motor.set_speed(-30)
    motor.stop()
    motor.disable()
    motor.set_speed(20)   # No debería moverse
    motor.enable()
    motor.set_speed(20)
    print(f"Velocidad actual (legacy): {motor.velocidad_actual}")

