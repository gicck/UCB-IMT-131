## Actividad 1 — Respaldo automático de proyectos

Escenario:
Un ingeniero de software debe mantener respaldos de su proyecto. Cada vez que ejecuta el script, se debe crear una copia comprimida con fecha y hora.

Tareas:

1. Crear un directorio `backups/` si no existe.
2. Comprimir el directorio `src/` en un archivo con nombre `backup_YYYY-MM-DD_HH-MM.tar.gz`.
3. Guardar el archivo dentro de `backups/`.
4. Mostrar cuántos respaldos existen actualmente.

Solución: **backup_proyecto.sh**

```bash
#!/bin/bash
# Script: backup_proyecto.sh
# Uso: ./backup_proyecto.sh

```

## Actividad 2 — Análisis de uso de disco

Escenario real:
Un ingeniero debe monitorear el uso de disco en un servidor y detectar directorios que ocupan demasiado espacio.

Tareas:

1. Analizar el directorio `/var/log/`.
2. Mostrar los 5 subdirectorios/archivos más pesados.
3. Guardar el reporte en `reporte_disco.txt`.
4. Mostrar en pantalla el total de espacio usado.

---
Solución: **analiza_disco.sh**

```bash
#!/bin/bash
# Script: analiza_disco.sh
# Uso: ./analiza_disco.sh
```
