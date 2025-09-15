from motor_controller import MotorController

class ModuloEmergencia:
    def detener_todo(self, motores: list[MotorController]):
        """Parada de emergencia usando interfaz encapsulada"""
        print("🚨 EMERGENCIA: Deteniendo todos los motores")
        for motor in motores:
            # ✅ CORRECTO: Usa método público seguro
            motor.activate_emergency()
    
    def reset_sistema(self, motores):
        """Resetear sistema después de emergencia"""
        print("🔄 Reseteando sistema...")
        for motor in motores:
            motor.reset_emergency()
            motor.enable()