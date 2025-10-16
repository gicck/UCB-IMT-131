# Polimorfismo en Python

El polimorfismo es uno de los pilares fundamentales de la Programación Orientada a Objetos (OOP). Permite que objetos de diferentes clases sean tratados de manera uniforme a través de una interfaz común.

## ¿Qué es el Polimorfismo?

**Polimorfismo** significa "muchas formas". En programación, se refiere a la capacidad de diferentes clases de responder al mismo mensaje (método) de maneras diferentes.

### Concepto Clave
El polimorfismo permite escribir código más flexible y reutilizable, ya que puedes trabajar con objetos a través de sus interfaces comunes sin preocuparte por sus tipos específicos.

## Tipos de Polimorfismo en Python

### 1. Polimorfismo de Métodos (Method Overriding)

El polimorfismo más común en Python ocurre cuando clases hijas sobrescriben métodos de la clase padre.

```py
class Animal:
    def hacer_sonido(self):
        return "Algún sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"

# Polimorfismo en acción
def escuchar_animal(animal):
    print(animal.hacer_sonido())

# Mismo método funciona con diferentes tipos
perro = Perro()
gato = Gato()
vaca = Vaca()

escuchar_animal(perro)  # Output: Guau guau
escuchar_animal(gato)   # Output: Miau miau
escuchar_animal(vaca)   # Output: Muuu
```

### 2. Polimorfismo con Funciones

Python permite que una función trabaje con diferentes tipos de objetos siempre que implementen los métodos necesarios.

```py
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14159 * self.radio ** 2

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Función polimórfica
def imprimir_area(forma):
    print(f"El área es: {forma.calcular_area()}")

# Funciona con cualquier forma
rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)
triangulo = Triangulo(6, 8)

imprimir_area(rectangulo)  # El área es: 50
imprimir_area(circulo)     # El área es: 153.93804
imprimir_area(triangulo)   # El área es: 24.0
```

### 3. Polimorfismo con Clases Abstractas

Las clases abstractas definen una interfaz común que todas las clases hijas deben implementar.

```py
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def detener(self):
        pass

class Carro(Vehiculo):
    def mover(self):
        return "El carro se mueve por la carretera"
    
    def detener(self):
        return "El carro frena"

class Barco(Vehiculo):
    def mover(self):
        return "El barco navega por el agua"
    
    def detener(self):
        return "El barco echa el ancla"

class Avion(Vehiculo):
    def mover(self):
        return "El avión vuela por el aire"
    
    def detener(self):
        return "El avión aterriza"

# Función polimórfica
def operar_vehiculo(vehiculo):
    print(vehiculo.mover())
    print(vehiculo.detener())

# Funciona con todos los vehículos
carro = Carro()
barco = Barco()
avion = Avion()

operar_vehiculo(carro)
operar_vehiculo(barco)
operar_vehiculo(avion)
```

## Duck Typing

Python usa "duck typing": "Si camina como un pato y suena como un pato, entonces es un pato". No importa el tipo real del objeto, sino los métodos que implementa.

```py
class Pato:
    def volar(self):
        return "El pato vuela"
    
    def nadar(self):
        return "El pato nada"

class Avion:
    def volar(self):
        return "El avión vuela"

class Persona:
    def nadar(self):
        return "La persona nada"

# Función que acepta cualquier cosa que pueda volar
def hacer_volar(algo):
    try:
        print(algo.volar())
    except AttributeError:
        print("Este objeto no puede volar")

# Duck typing en acción
pato = Pato()
avion = Avion()
persona = Persona()

hacer_volar(pato)     # El pato vuela
hacer_volar(avion)    # El avión vuela
hacer_volar(persona)  # Este objeto no puede volar
```

## Polimorfismo con Operadores

Python permite sobrecargar operadores para crear comportamientos polimórficos.

```py
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

# El operador + funciona de manera diferente
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)

p1 = Punto(1, 2)
p2 = Punto(3, 4)
print(p1 + p2)  # Punto(4, 6)
```

## Ventajas del Polimorfismo

1. **Flexibilidad**: El código es más adaptable a cambios
2. **Reutilización**: Una función puede trabajar con múltiples tipos
3. **Mantenibilidad**: Código más limpio y fácil de mantener
4. **Extensibilidad**: Fácil agregar nuevos tipos sin modificar código existente

## Ejemplo Completo: Sistema de Pagos

```py
from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass
    
    @abstractmethod
    def validar(self):
        pass

class TarjetaCredito(MetodoPago):
    def __init__(self, numero, cvv):
        self.numero = numero
        self.cvv = cvv
    
    def procesar_pago(self, cantidad):
        if self.validar():
            return f"Procesando ${cantidad} con tarjeta de crédito {self.numero[-4:]}"
        return "Tarjeta inválida"
    
    def validar(self):
        return len(self.numero) == 16 and len(self.cvv) == 3

class PayPal(MetodoPago):
    def __init__(self, email):
        self.email = email
    
    def procesar_pago(self, cantidad):
        if self.validar():
            return f"Procesando ${cantidad} con PayPal ({self.email})"
        return "Email inválido"
    
    def validar(self):
        return "@" in self.email

class Bitcoin(MetodoPago):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def procesar_pago(self, cantidad):
        if self.validar():
            return f"Procesando ${cantidad} con Bitcoin a {self.wallet_address[:10]}..."
        return "Dirección de wallet inválida"
    
    def validar(self):
        return len(self.wallet_address) > 20

# Función polimórfica para procesar cualquier tipo de pago
def realizar_compra(metodo_pago, cantidad):
    print(metodo_pago.procesar_pago(cantidad))

# Uso del polimorfismo
tarjeta = TarjetaCredito("1234567890123456", "123")
paypal = PayPal("usuario@email.com")
bitcoin = Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

realizar_compra(tarjeta, 100)
realizar_compra(paypal, 50)
realizar_compra(bitcoin, 200)
```

## Polimorfismo vs Herencia

**Herencia** es el mecanismo que permite crear nuevas clases basadas en clases existentes.

**Polimorfismo** es la capacidad de tratar objetos de diferentes clases de manera uniforme.

Aunque están relacionados, son conceptos distintos:
- Puedes tener polimorfismo sin herencia (duck typing)
- La herencia facilita el polimorfismo pero no lo requiere
