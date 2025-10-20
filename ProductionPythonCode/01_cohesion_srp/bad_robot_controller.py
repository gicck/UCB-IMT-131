class RobotController:
    """Un controlador de robot que hace TODO - ¡viola el SRP!"""
    
    def __init__(self):
        self.position = {"x": 0, "y": 0, "heading": 0}
        self.battery_level = 100
        self.obstacles = []
        self.delivery_status = "idle"
        
    def move_forward(self, distance):
        # Lógica de movimiento
        if self.battery_level < 10:
            print("ERROR: ¡Batería muy baja!")
            self.send_alert_email("admin@company.com", "¡Batería baja!")
            return False
            
        # Actualizar posición
        self.position["x"] += distance * math.cos(self.position["heading"])
        self.position["y"] += distance * math.sin(self.position["heading"])
        
        # Drenar batería
        self.battery_level -= distance * 0.5
        
        # Registrar en base de datos
        self.save_to_database(f"Movido a {self.position}")
        
        # Verificar obstáculos
        if self.detect_obstacle_in_path():
            print("¡Obstáculo detectado! Deteniendo.")
            return False
            
        return True
    
    def detect_obstacle_in_path(self):
        # Lógica de lectura de sensores mezclada con navegación
        sensor_data = self.read_lidar_sensor()
        if min(sensor_data) < 0.5:
            self.log_obstacle_to_file()
            return True
        return False
    
    def deliver_package(self, destination):
        # Lógica de entrega mezclada con navegación, batería y comunicación
        distance = self.calculate_distance(destination)
        
        if self.battery_level < distance * 0.5:
            self.send_alert_email("admin@company.com", "No se puede completar la entrega")
            return False
            
        self.move_forward(distance)
        self.delivery_status = "delivered"
        self.save_to_database(f"Entregado en {destination}")
        self.send_alert_email("customer@email.com", "¡Paquete entregado!")
        
        return True
    
    def read_lidar_sensor(self):
        # Lectura simulada del sensor
        return [1.2, 0.8, 1.5, 0.3, 2.0]
    
    def send_alert_email(self, recipient, message):
        # Lógica de email incrustada en el controlador del robot
        print(f"Enviando email a {recipient}: {message}")
        # Imagina código de conexión SMTP aquí...
    
    def save_to_database(self, event):
        # Lógica de base de datos incrustada en el controlador del robot
        print(f"Guardando en BD: {event}")
        # Imagina código de conexión a base de datos aquí...
    
    def calculate_distance(self, destination):
        # Cálculo de distancia
        return 10  # Simplificado
    


# Tarea para los Estudiantes
# ¡Refactoriza este código siguiendo el SRP! Crea clases separadas con alta cohesión:
# Clases Sugeridas (Los estudiantes deben identificarlas):

# NavigationSystem - Manejar posición, movimiento y búsqueda de rutas
# SensorManager - Leer y procesar datos de sensores (LIDAR, cámaras, etc.)
# BatteryMonitor - Rastrear nivel de batería, estimar alcance, gestionar energía
# ObstacleDetector - Procesar datos de sensores para identificar obstáculos
# NotificationService - Enviar alertas (email, SMS, panel de control)
# DataLogger - Registrar eventos en base de datos/archivo
# DeliveryManager - Coordinar el flujo de trabajo de entrega usando otros componentes