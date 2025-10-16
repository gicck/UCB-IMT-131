# Ejercicios de Polimorfismo - Mecatrónica

## Ejercicio 1: Sistema de Control de Sensores Múltiples

### Enunciado:
Crea un sistema de adquisición de datos que pueda leer diferentes tipos de sensores usando polimorfismo, aplicable en sistemas mecatrónicos.

### Requisitos:

1. **Clase abstracta `Sensor`:**
   - Métodos abstractos: `leer_dato()`, `calibrar()`, `validar_lectura(valor)`
   - Método concreto: `registrar_medicion()` que guarda historial de lecturas
   - Atributos: `id_sensor`, `unidad_medida`, `rango_operacion`

2. **Implementar diferentes sensores:**
   - `SensorTemperatura`: LM35 o termopar, rango -40°C a 125°C, calibración offset
   - `SensorPresion`: MPX5700, 0-700 kPa, compensación de temperatura
   - `SensorDistancia`: Ultrasonido HC-SR04, 2-400 cm, filtrado de ruido
   - `Encoder`: Encoder rotatorio, pulsos por revolución, detección de dirección
   - `Acelerometro`: MPU6050, 3 ejes, filtrado digital

3. **Clase `SistemaAdquisicion`:**
   - Método `leer_sensor(sensor)` que use polimorfismo
   - Método `leer_todos(sensores)` para adquirir datos de múltiples sensores
   - Método `generar_reporte(sensores)` con estadísticas de todos los sensores

### Tareas:
- Implementar todas las clases con herencia y polimorfismo
- Demostrar que la misma función puede leer cualquier tipo de sensor
- Manejar errores de validación específicos de cada sensor (fuera de rango, desconexión)
- Crear un programa que lea múltiples sensores simultáneamente

### Ejemplo de uso esperado:
```python
temp = SensorTemperatura(pin=0, id="TEMP-01")
presion = SensorPresion(pin=1, id="PRES-01")
distancia = SensorDistancia(pin_trigger=2, pin_echo=3, id="DIST-01")

sistema = SistemaAdquisicion()
sistema.leer_sensor(temp)
sistema.leer_sensor(presion)
datos = sistema.leer_todos([temp, presion, distancia])
```

---

## Ejercicio 2: Sistema de Control de Actuadores

### Enunciado:
Desarrolla un sistema de control que pueda comandar diferentes tipos de actuadores de manera polimórfica en un sistema mecatrónico.

### Requisitos:

1. **Clase abstracta `Actuador`:**
   - Métodos abstractos: `activar(intensidad)`, `desactivar()`, `obtener_estado()`
   - Atributos: `id_actuador`, `pin_control`, `estado_actual`
   - Método concreto: `verificar_limites()` que valida rangos operacionales

2. **Implementar actuadores específicos:**
   - `MotorDC`: control PWM 0-255, dirección (horario/antihorario), RPM actual
   - `ServoMotor`: ángulo 0-180°, velocidad de movimiento, posición actual
   - `MotorPasoAPaso`: pasos por revolución, microstepping, velocidad
   - `SolenoideLineal`: ON/OFF, fuerza de empuje, posición extendida/retraída
   - `BombaHidraulica`: caudal 0-100%, presión de trabajo, protección térmica

3. **Clase `ControladorActuadores`:**
   - Método `comandar(actuador, parametros)` que ejecuta comando polimórfico
   - Método `secuencia(actuadores, comandos)` ejecuta secuencia coordinada
   - Método `parada_emergencia(actuadores)` detiene todos los actuadores

### Tareas:
- Implementar todas las clases usando herencia de la clase abstracta
- Demostrar polimorfismo: el controlador funciona con cualquier tipo de actuador
- Manejar excepciones específicas (sobrecorriente, sobrecalentamiento, límites)
- Crear un programa que controle múltiples actuadores en una secuencia

### Aplicación práctica:
Sistema de brazo robótico con diferentes tipos de actuadores trabajando coordinadamente.

---

## Ejercicio 3: Sistema de Control de Movimiento con Duck Typing

### Enunciado:
Crea un sistema de planificación de trayectorias que aproveche el duck typing de Python, trabajando con diferentes tipos de movimiento sin herencia explícita.

### Requisitos:

1. **Implementar diferentes tipos de movimiento SIN herencia:**
   - `MovimientoLineal`: atributos `punto_inicio`, `punto_fin`, `velocidad`
   - `MovimientoCircular`: atributos `centro`, `radio`, `angulo_inicial`, `angulo_final`
   - `MovimientoBezier`: atributos `puntos_control[]`, `precision`
   - `MovimientoParabolico`: atributos `velocidad_inicial`, `angulo`, `gravedad`
   - `MovimientoHelicoidal`: atributos `radio`, `paso`, `revoluciones`

2. **Cada tipo de movimiento debe tener:**
   - Método `calcular_trayectoria()` que retorna lista de puntos (x, y, z)
   - Método `calcular_tiempo_total(velocidad)` duración del movimiento
   - Método `obtener_punto_en_tiempo(t)` posición en instante específico
   - Método `describir()` que retorna descripción del movimiento

3. **Clase `PlanificadorTrayectorias`:**
   - Método `generar_plan(movimientos)` que planifica secuencia de movimientos
   - Método `calcular_duracion_total(movimientos)` suma tiempos de todos los movimientos
   - Método `optimizar(movimientos)` minimiza tiempo total
   - Método `visualizar(movimientos)` genera gráfica de trayectorias

### Tareas:
- Implementar todos los movimientos SIN usar herencia
- Demostrar duck typing: el planificador funciona con cualquier objeto que tenga los métodos correctos
- Agregar manejo de errores si un objeto no tiene los métodos necesarios
- Crear un programa que planifique una secuencia mixta de movimientos

### Desafío adicional:
- Implementar detección y evitación de colisiones entre trayectorias
- Agregar validación usando `hasattr()` para verificar que los objetos tienen los métodos necesarios
- Calcular velocidades y aceleraciones en cada punto de la trayectoria

### Aplicación práctica:
Sistema de control para CNC, impresora 3D, o brazo robótico con diferentes tipos de interpolación.

---

## Ejercicio 4: Sistema de Control de Robot Móvil Autónomo

### Enunciado:
Diseña un sistema de control para un robot móvil que gestione diferentes configuraciones de locomoción usando polimorfismo.

### Requisitos:

1. **Clase base `SistemaLocomocion`:**
   - Atributos: `velocidad_max`, `radio_giro`, `estado`, `posicion_actual`, `orientacion`
   - Métodos abstractos: `avanzar(velocidad)`, `girar(angulo)`, `detener()`, `calcular_cinematica()`
   - Métodos concretos: `obtener_odometria()`, `actualizar_posicion()`, `verificar_obstaculos()`

2. **Implementar diferentes configuraciones:**
   - `DiferencialDosRuedas`: control independiente ruedas izq/der, giro en el lugar
   - `Ackermann`: dirección tipo automóvil, radio mínimo de giro, ángulo máximo
   - `Omnidireccional`: movimiento en cualquier dirección, 3-4 ruedas mecanum
   - `Oruga`: tracción continua, control de velocidad por PWM, alta tracción
   - `PatasHexapodo`: 6 patas, secuencia de marcha tripode, estabilidad en terreno irregular

3. **Clase `ControladorRobot`:**
   - Método `ejecutar_movimiento(locomocion, comando)` que controla cualquier configuración
   - Método `navegar_a_punto(locomocion, x_destino, y_destino)` navegación autónoma
   - Método `esquivar_obstaculo(locomocion, sensores)` maniobra evasiva
   - Método `optimizar_energia(locomocion, trayectoria)` selecciona movimientos eficientes

### Tareas:
- Implementar jerarquía de clases con herencia y polimorfismo
- Cada tipo de locomoción debe tener cinemática y control específico
- Demostrar que el controlador puede trabajar con cualquier configuración
- Implementar algoritmo de navegación que se adapte al tipo de locomoción
- Simular odometría y actualización de posición para cada tipo

### Bonus:
- Agregar cálculo de consumo energético específico para cada configuración
- Implementar control PID adaptativo según el tipo de locomoción
- Agregar detección y recuperación de situaciones de bloqueo (rueda patinando, volcado)
- Simular diferentes superficies (asfalto, arena, pendiente) y su efecto en cada tipo

### Aplicación práctica:
Sistema de control universal para robots móviles en competencias, almacenes automatizados, o exploración de terrenos.
