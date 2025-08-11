#!/bin/bash
# ============================================
# Generador de paquete de práctica Linux
# ============================================

# Crear estructura de carpetas
mkdir -p proyecto_mecatronica/datos_iniciales/sensores/{temperatura,posicion,fuerza}

# =========================
# Archivos de sensores
# =========================
echo -e "Lectura 1: 25.3\nLectura 2: 25.7\nLectura 3: 26.1" > proyecto_mecatronica/datos_iniciales/sensores/temperatura/temp_2025-08-11.txt
echo -e "Lectura 1: 26.0\nLectura 2: 26.4\nLectura 3: 26.8" > proyecto_mecatronica/datos_iniciales/sensores/temperatura/temp_2025-08-12.txt
echo -e "Lectura 1: 26.0\nLectura 2: 26.4\nLectura 3: 26.8" > proyecto_mecatronica/datos_iniciales/sensores/temperatura/temp_2025-06-12.txt

echo -e "Lectura 1: X=10,Y=20\nLectura 2: X=12,Y=22" > proyecto_mecatronica/datos_iniciales/sensores/posicion/pos_2025-08-11.txt
echo -e "Lectura 1: X=15,Y=25\nLectura 2: X=17,Y=27" > proyecto_mecatronica/datos_iniciales/sensores/posicion/pos_2025-08-12.txt
echo -e "Lectura 1: X=15,Y=25\nLectura 2: X=17,Y=27" > proyecto_mecatronica/datos_iniciales/sensores/posicion/pos_2025-06-12.txt

echo -e "Lectura 1: 50N\nLectura 2: 55N" > proyecto_mecatronica/datos_iniciales/sensores/fuerza/fuerza_2025-08-11.txt
echo -e "Lectura 1: 60N\nLectura 2: 65N" > proyecto_mecatronica/datos_iniciales/sensores/fuerza/fuerza_2025-08-12.txt
echo -e "Lectura 1: 60N\nLectura 2: 65N" > proyecto_mecatronica/datos_iniciales/sensores/fuerza/fuerza_2025-06-12.txt

# =========================
# Otros archivos de datos
# =========================
cat > proyecto_mecatronica/datos_iniciales/log_dron.txt <<EOL
[OK] Motor encendido
[ERROR] Sensor de altitud no responde
[OK] GPS activo
[ERROR] Batería baja
[OK] Comunicación establecida
[ERROR] Fallo en el giroscopio
EOL

cat > proyecto_mecatronica/datos_iniciales/config_robot_v1.txt <<EOL
velocidad_maxima=1.5
fuerza_maxima=100
modo_operacion=automatico
sensor_proximidad=activo
EOL

cat > proyecto_mecatronica/datos_iniciales/config_robot_v2.txt <<EOL
velocidad_maxima=1.8
fuerza_maxima=100
modo_operacion=manual
sensor_proximidad=activo
EOL

cat > proyecto_mecatronica/datos_iniciales/temperaturas.csv <<EOL
2025-08-11 10:00,75
2025-08-11 10:01,82
2025-08-11 10:02,79
2025-08-11 10:03,85
2025-08-11 10:04,90
2025-08-11 10:05,77
EOL

cat > proyecto_mecatronica/datos_iniciales/frutas.txt <<EOL
manzana
pera
uva
sandía
pera
EOL

# =========================
# Guion de clase
# =========================
cat > proyecto_mecatronica/0_README.md <<'EOL'
# 🛠 Taller de Linux para 
## Módulo: Basic File and Directory Operations + Text Processing and Editing

### Objetivo
Aprender a manipular archivos y procesar datos en Linux usando casos reales

---

## Actividad 1 — Organización de datos de sensores
**Escenario:**  
Un prototipo de brazo robótico genera datos diarios de temperatura, posición y fuerza. Debes organizar los datos y preparar un reporte diario.

**Tareas:**
1. Copia todos los archivos del día `2025-08-11` a una carpeta `reporte_diario`.
2. Mueve los archivos de días anteriores a `historial/`.
3. Lista la estructura final con `tree`.

---

## Actividad 2 — Filtrado de datos de producción
**Escenario:**  
Un sensor de temperatura registra datos en `temperaturas.csv`. Debes filtrar solo los valores mayores a 80°C.

**Tareas:**
1. Usa `awk` para mostrar solo las líneas con temperatura > 80.
2. Guarda el resultado en `temperaturas_altas.csv`.

---

## Actividad 3 — Reporte de fallas en un dron
**Escenario:**  
El archivo `log_dron.txt` contiene mensajes de estado y errores. Debes extraer solo los errores.

**Tareas:**
1. Filtra las líneas con `[ERROR]` usando `grep`.
2. Guarda el resultado en `reporte_errores.txt`.

---

## Actividad 4 — Comparación de configuraciones
**Escenario:**  
Dos ingenieros configuraron el mismo robot (`config_robot_v1.txt` y `config_robot_v2.txt`). Debes encontrar y corregir diferencias.

**Tareas:**
1. Usa `diff` para encontrar diferencias.
2. Corrige un parámetro usando `sed`.
3. Guarda el archivo corregido como `config_robot_final.txt`.

---

## Dinámica de clase
- Trabaja en equipos de 2-3 personas.
- Tiempo por actividad: 25 minutos.
- Revisión cruzada: intercambia tu trabajo con otro equipo y usa `checklist_revisor.md`.
- Exposición: cada equipo explica su solución.
EOL

# =========================
# Checklist de revisión
# =========================
cat > proyecto_mecatronica/checklist_revisor.md <<'EOL'
# ✅ Lista de verificación para revisión cruzada

## Actividad 1
- [ ] Existe carpeta `reporte_diario` con solo archivos del 2025-08-11.
- [ ] Existe carpeta `historial` con archivos de otros días.
- [ ] La estructura de carpetas es clara y ordenada.

## Actividad 2
- [ ] El archivo `temperaturas_altas.csv` contiene solo valores > 80°C.
- [ ] No se eliminaron columnas innecesarias.

## Actividad 3
- [ ] El archivo `reporte_errores.txt` contiene solo líneas con `[ERROR]`.
- [ ] No hay líneas vacías.

## Actividad 4
- [ ] El archivo `config_robot_final.txt` refleja las correcciones.
- [ ] No se eliminaron parámetros importantes.
EOL

# =========================
# Script de evaluación
# =========================
cat > proyecto_mecatronica/evaluar.sh <<'EOL'
#!/bin/bash
echo "🔍 Evaluando actividades..."

# Actividad 1
if [ -d "reporte_diario" ] && [ -d "historial" ]; then
    echo "✅ Actividad 1: Carpetas encontradas"
else
    echo "❌ Actividad 1: Faltan carpetas"
fi

# Actividad 2
if grep -qE ",8[1-9]|,9[0-9]|,100" temperaturas_altas.csv 2>/dev/null; then
    echo "✅ Actividad 2: Filtrado correcto"
else
    echo "❌ Actividad 2: No se encontraron temperaturas > 80°C"
fi

# Actividad 3
if grep -q "\[ERROR\]" reporte_errores.txt 2>/dev/null; then
    echo "✅ Actividad 3: Errores extraídos"
else
    echo "❌ Actividad 3: No se encontraron errores"
fi

# Actividad 4
if diff -q config_robot_v1.txt config_robot_final.txt >/dev/null; then
    echo "❌ Actividad 4: No se detectaron cambios"
else
    echo "✅ Actividad 4: Configuración modificada"
fi
EOL

chmod +x proyecto_mecatronica/evaluar.sh

# # =========================
# # Comprimir en ZIP
# # =========================
# zip -r proyecto_mecatronica.zip proyecto_mecatronica >/dev/null
# echo "✅ Paquete generado: proyecto_mecatronica.zip"
