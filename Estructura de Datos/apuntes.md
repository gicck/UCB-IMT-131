# Estructuras de Datos en Python

## Listas

Las listas son colecciones **mutables** y **ordenadas** que pueden contener elementos de diferentes tipos.

```python
# Crear una lista
frutas = ['manzana', 'banana', 'cereza']

# Métodos principales
frutas.append('naranja')      # Agregar al final
frutas.insert(0, 'kiwi')      # Insertar en posición
frutas.remove('banana')       # Eliminar por valor
elemento = frutas.pop()       # Eliminar y retornar último
frutas.sort()                 # Ordenar in-place
frutas.reverse()              # Invertir orden
```

### Listas como Pilas (LIFO - Last In, First Out)

```python
stack = [3, 4, 5]
stack.append(6)        # Apilar
stack.append(7)
print(stack.pop())     # Desapilar → 7
print(stack.pop())     # Desapilar → 6
# Resultado: [3, 4, 5]
```

### Listas como Colas (FIFO - First In, First Out)

**Nota:** Las listas NO son eficientes para colas. Usa `collections.deque`:

```python
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")      # Agregar al final
queue.append("Graham")
print(queue.popleft())     # Quitar del principio → "Eric"
print(queue.popleft())     # → "John"
# Resultado: deque(['Michael', 'Terry', 'Graham'])
```

### Comprensión de Listas

```python
# Sintaxis: [expresión for item in iterable if condición]

# Cuadrados de números
cuadrados = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrar números positivos
vec = [-4, -2, 0, 2, 4]
positivos = [x for x in vec if x >= 0]
# [0, 2, 4]

# Combinar dos listas
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

---

## La instrucción `del`

`del` elimina elementos por índice o variables completas (a diferencia de `pop()` que retorna el valor).

```python
a = [1, 2, 3, 4, 5, 6]

# Eliminar por índice
del a[0]              # [2, 3, 4, 5, 6]

# Eliminar un rango
del a[2:4]            # [2, 3, 6]

# Vaciar la lista
del a[:]              # []

# Eliminar la variable
del a                 # La variable 'a' ya no existe
```

---

## Tuplas

Las tuplas son colecciones **inmutables** y **ordenadas**. Se usan para datos que no deben cambiar.

### Diferencias clave con Listas

| Característica | Lista | Tupla |
|---------------|-------|-------|
| **Mutabilidad** | Mutable (puedes modificar) | Inmutable (no puedes modificar) |
| **Sintaxis** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Velocidad** | Más lenta | Más rápida |
| **Uso típico** | Colecciones homogéneas que cambian | Datos heterogéneos fijos |
| **Métodos** | Muchos (append, remove, etc.) | Solo count() e index() |

### Ejemplos de Tuplas

```python
# Crear tuplas
t = 12345, 54321, 'hola'   # Sin paréntesis
t = (12345, 54321, 'hola')  # Con paréntesis (recomendado)

# Las tuplas son inmutables
t[0] = 88888  # Error: TypeError: no se puede modificar

# Pero pueden contener objetos mutables
t = ([1, 2, 3], [4, 5, 6])
t[0].append(4)  # Esto sí funciona

# Tuplas especiales
vacia = ()              # Tupla vacía
singleton = ('hola',)   # Nota: la coma final es necesaria

# Desempaquetado
x, y, z = t  # Asigna cada valor a una variable
```

### ¿Cuándo usar tuplas?

- **Retornar múltiples valores** de una función
- **Claves de diccionarios** (las listas no pueden)
- **Datos que no deben cambiar** (coordenadas, configuración)
- **Más eficientes** en memoria y velocidad que listas

```python
# Retornar múltiples valores
def obtener_coordenadas():
    return (10, 20)  # Tupla

x, y = obtener_coordenadas()

# Como clave de diccionario
posiciones = {
    (0, 0): 'origen',
    (1, 0): 'este',
    (0, 1): 'norte'
}
```

---

## Conjuntos (Set)

Los conjuntos son colecciones **no ordenadas** de elementos **únicos** (sin duplicados).

### ¿Por qué y cuándo usar Sets?

**Usa sets cuando necesites:**

1. **Eliminar duplicados** automáticamente
2. **Verificar pertenencia** rápidamente (más rápido que en listas)
3. **Operaciones matemáticas** de conjuntos (unión, intersección, diferencia)

### Ejemplos de Sets

```python
# Crear un set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'orange', 'banana', 'pear', 'apple'} - sin duplicados

# Set vacío (IMPORTANTE: NO uses {} porque eso crea un diccionario vacío)
vacio = set()

# Verificación de pertenencia (muy rápida)
'orange' in basket  # True

# Operaciones de conjuntos
a = set('abracadabra')  # {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam')     # {'a', 'l', 'c', 'z', 'm'}

a - b    # Diferencia: {'r', 'd', 'b'}
a | b    # Unión: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b    # Intersección: {'a', 'c'}
a ^ b    # Diferencia simétrica: {'r', 'd', 'b', 'm', 'z', 'l'}

# Comprensión de sets
vocales = {x for x in 'abracadabra' if x in 'aeiou'}
# {'a'}
```

### Casos de uso comunes

```python
# 1. Eliminar duplicados de una lista
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = list(set(numeros))  # [1, 2, 3, 4, 5]

# 2. Verificar si hay elementos comunes
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
hay_comunes = bool(set(lista1) & set(lista2))  # True

# 3. Encontrar elementos únicos en múltiples listas
todos_unicos = set(lista1) ^ set(lista2)  # {1, 2, 5, 6}
```

---

## Diccionarios

Los diccionarios almacenan pares **clave:valor** donde las claves son **únicas** e **inmutables**.

### Diferencias entre Set y Diccionario

| Característica | Set | Diccionario |
|---------------|-----|-------------|
| **Estructura** | Solo valores | Pares clave:valor |
| **Sintaxis vacío** | `set()` | `{}` |
| **Acceso** | Verificar pertenencia | Acceder por clave |
| **Uso** | Elementos únicos | Mapeo clave → valor |
| **Duplicados** | No permite | Claves únicas, valores pueden repetirse |

### Ejemplos de Diccionarios

```python
# Crear un diccionario
tel = {'jack': 4098, 'sape': 4139}

# Agregar/modificar
tel['guido'] = 4127

# Acceder (lanza KeyError si no existe)
tel['jack']  # 4098

# Acceso seguro (retorna None si no existe)
tel.get('irv')        # None
tel.get('irv', 0)     # 0 (valor por defecto)

# Eliminar
del tel['sape']

# Verificar existencia
'guido' in tel  # True

# Obtener claves, valores o ambos
list(tel.keys())    # ['jack', 'guido']
list(tel.values())  # [4098, 4127]
list(tel.items())   # [('jack', 4098), ('guido', 4127)]
```

### ¿Por qué usar diccionarios?

**Úsalos cuando necesites:**

1. **Asociar datos** (mapeo clave → valor)
2. **Búsquedas rápidas** por clave (O(1) en promedio)
3. **Estructurar datos** complejos
4. **Contar ocurrencias** fácilmente

```python
# Contar palabras
texto = "hola mundo hola python mundo mundo"
conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
# {'hola': 2, 'mundo': 3, 'python': 1}

# Comprensión de diccionarios
cuadrados = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Crear desde pares
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# Sintaxis con keywords (solo para claves tipo string)
dict(sape=4139, guido=4127, jack=4098)
```

---

## Técnicas de Iteración

### 1. Iterar sobre Diccionarios

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# Iterar sobre clave y valor
for clave, valor in knights.items():
    print(clave, valor)
```

### 2. Iterar con Índice (enumerate)

```python
for i, valor in enumerate(['tic', 'tac', 'toe']):
    print(i, valor)
# 0 tic
# 1 tac
# 2 toe
```

### 3. Iterar sobre Múltiples Secuencias (zip)

```python
preguntas = ['nombre', 'edad', 'ciudad']
respuestas = ['Ana', 25, 'Madrid']

for pregunta, respuesta in zip(preguntas, respuestas):
    print(f'{pregunta}: {respuesta}')
# nombre: Ana
# edad: 25
# ciudad: Madrid
```

### 4. Iterar en Orden Inverso (reversed)

```python
for i in reversed(range(1, 10, 2)):
    print(i)
# 9, 7, 5, 3, 1
```

### 5. Iterar Ordenado (sorted)

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for fruta in sorted(basket):
    print(fruta)
# apple, apple, banana, orange, orange, pear
```

### 6. Iterar sin Duplicados (sorted + set)

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for fruta in sorted(set(basket)):
    print(fruta)
# apple, banana, orange, pear (sin duplicados y ordenado)
```

---

## Resumen Rápido

| Estructura | Mutable | Ordenada | Duplicados | Sintaxis | Uso Principal |
|-----------|---------|----------|------------|----------|---------------|
| **Lista** | Sí | Sí | Sí | `[1, 2, 3]` | Colección general de elementos |
| **Tupla** | No | Sí | Sí | `(1, 2, 3)` | Datos fijos, claves dict |
| **Set** | Sí | No | No | `{1, 2, 3}` | Elementos únicos, operaciones matemáticas |
| **Diccionario** | Sí | Sí* | Claves: No<br>Valores: Sí | `{'a': 1, 'b': 2}` | Mapeo clave-valor |

*Desde Python 3.7+, los diccionarios mantienen el orden de inserción.

---

## Consejos Finales

1. **Lista**: Tu opción por defecto para colecciones
2. **Tupla**: Cuando los datos no deben cambiar o como claves de diccionario
3. **Set**: Para eliminar duplicados o verificar pertenencia rápidamente
4. **Diccionario**: Para asociar datos con claves únicas
6. `del` elimina, `pop()` elimina y retorna
7. `{}` crea un diccionario vacío, usa `set()` para sets vacíos