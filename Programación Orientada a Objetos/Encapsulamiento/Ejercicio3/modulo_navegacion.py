from motor_controller import MotorController

class ModuloNavegacion:
    def mover_adelante(self, motor_izq, motor_der, velocidad=80):
        """Movimiento seguro usando interfaz encapsulada"""
        # ✅ CORRECTO: Usa métodos públicos seguros
        success_left = motor_izq.set_speed(velocidad)
        success_right = motor_der.set_speed(velocidad)
        
        if success_left and success_right:
            print("Navegación: Moviendo adelante")
            return True
        else:
            print("Navegación: Error al configurar velocidad")
            return False
    
    def girar_derecha(self, motor_izq, motor_der, velocidad=60):
        """Giro diferencial usando interfaz segura"""
        motor_izq.set_speed(velocidad)
        motor_der.set_speed(-velocidad//2)  # Motor derecho más lento