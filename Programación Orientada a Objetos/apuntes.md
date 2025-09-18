## Lunes 25/08
### Python Roadmap
**Core Python**
- Variables, data types, lists, dictionaries, tuples
- Operators
-  Conditional operators, arithmetic operators, type conversions
- Conditional statements
    -  if, like, elif
- for loops, while loops
- Mutability
- Fuctions
- Clases
- Objects
- Methods

**Small Projects / practice OOP**
- How to Split code into multiple files
    - Packages, modules
- How to Write reusable calsses and functions
- How to save and load data from files(basic data persistance)
- Quiza app, inventoriy tracker
    - Work on digestable topics

**Learn real developer tools**
- Git + github
- Virtual environments
    - VENV, Conda, UV
- Debugging tools
    - print, logging, pdb
- pip
    - install various different packages
    - how does this fit with virtual environments
- requirements.txt
- Python modules, imports, python ecosystem
- Terminal Fluency -> cd, rm, cp, etc 

**Pick a track and build something real**
- WEBDEV
    - Flask, FastAPI, Django
- Data analysis
    - Pandas, NumPy, Matplotlib
- Automation
    - Write basic scripts
    - Selenium
    - Playwright
    - Puppeteer
    - Web berowser automation
- APIs
    - Request, JSON, external services
- AI/LLMS
    - LangChain, LAngflow, Ollama, Transformers, HuggingFace

**Become Pythonic**
- List comprenhensions
- generator expressions
- with statemetns(context managers)
- Decorators
- *args, **kwargs
- type hints
- docstrings

**Advance Concepts**
- Threading/Multiprocessing
- AsyncIO
- Global Interpreter Lock
- Python Versions
- CPython vs PyPy vs MicroPython 


# Ejercicios de Práctica de Abstracción en Python (OOP)

## Ejercicio 1: Sistema Bancario

### Reto de Programación Secuencial
Crea un programa de consola que gestione cuentas bancarias usando variables y funciones básicas:

**Requisitos:**
- Usa listas para almacenar números de cuenta, nombres de titulares y saldos  
- Crea funciones para: `create_account()`, `deposit()`, `withdraw()`, `check_balance()`  
- Maneja múltiples cuentas usando bucles y condicionales  
- Muestra la información de las cuentas con `print` simples  

**Ejemplo de Enfoque Secuencial:**
```python
# Global lists
account_holders = []
balances = []
account_numbers = []

def create_account(name, initial_balance):
    # Add to lists
    pass

def deposit(account_number, amount):
    # Find account in list, update balance
    pass

def find_account_index(account_number):
    # Loop through list to find account
    pass
```

### Conversión a OOP (Aplicando Abstracción)


**Beneficios de la Abstracción:**
- El usuario no necesita saber cómo se generan los números de cuenta  
- La validación de saldo está oculta dentro de los métodos  
- Interfaz limpia: `deposit()`, `withdraw()`, `display_account_info()`  
- Los datos internos están protegidos contra manipulación directa  

---

## Ejercicio 2: Sistema de Gestión de Biblioteca

### Reto de Programación Secuencial
Construye un sistema de biblioteca usando estructuras básicas:

**Requisitos:**
- Usa listas para títulos de libros, autores, ISBN y estado de disponibilidad  
- Crea funciones: `add_book()`, `borrow_book()`, `return_book()`, `search_book()`  
- Usa bucles para buscar libros  
- Controla libros prestados/disponibles con listas booleanas  

**Ejemplo de Enfoque Secuencial:**
```python
book_titles = []
authors = []
isbns = []
is_available = []

def add_book(title, author, isbn):
    # Add to parallel lists
    pass
```

### Conversión a OOP (Aplicando Abstracción)


**Beneficios de la Abstracción:**
- El estado interno del libro está oculto y se gestiona internamente  
- Los usuarios interactúan con métodos simples: `borrow()`, `return_book()`, `display_info()`  
- La complejidad de búsqueda está abstraída en la clase `Library`  
- No es necesario manejar listas paralelas manualmente  

---

## Ejercicio 3: Sistema de Gestión de Calificaciones de Estudiantes

### Reto de Programación Secuencial
Crea un sistema de calificaciones estudiantiles usando programación procedural:

**Requisitos:**
- Usa listas para nombres de estudiantes, materias y calificaciones  
- Funciones: `add_student()`, `add_grade()`, `calculate_average()`, `display_report()`  
- Usa bucles anidados para manejar múltiples materias por estudiante  
- Calcula el GPA usando condicionales  

**Ejemplo de Enfoque Secuencial:**
```python
student_names = []
student_grades = []  # List of lists - each student has a list of (subject, grade) tuples

def add_student(name):
    # Add student and initialize empty grade list
    pass
```

### Conversión a OOP (Aplicando Abstracción)


**Beneficios de la Abstracción:**
- El cálculo del promedio está oculto dentro de los métodos  
- La conversión de nota numérica a letra está abstraída  
- Los estudiantes no necesitan saber cómo se almacenan las calificaciones  
- Interfaz limpia: `add_grade()`, `calculate_average()`, `display_report()`  

---

## Ejercicio 4: Sistema de Gestión de Inventario

### Reto de Programación Secuencial
Construye un sistema de inventario para una tienda pequeña:

**Requisitos:**
- Listas para nombres de productos, cantidades, precios y categorías  
- Funciones: `add_product()`, `update_quantity()`, `check_stock()`, `calculate_total()`  
- Usa bucles para buscar y actualizar inventario  
- Calcula el valor total del inventario con operaciones aritméticas  

**Ejemplo de Enfoque Secuencial:**
```python
product_names = []
quantities = []
prices = []
categories = []

def add_product(name, qty, price, category):
    # Add to parallel lists
    pass
```

### Conversión a OOP (Aplicando Abstracción)

**Beneficios de la Abstracción:**
- La validación de stock está oculta en los métodos  
- Los cálculos complejos de inventario están abstraídos  
- Los usuarios interactúan con métodos simples: `add_stock()`, `remove_stock()`, `display_info()`  
- El mecanismo interno de almacenamiento está completamente oculto  
- La lógica de negocio (como alertas de bajo stock) está encapsulada en las clases  

---

## Principios de Abstracción Demostrados

1. **Ocultar Detalles de Implementación**: el usuario no ve listas, bucles ni cálculos complejos  
2. **Proveer Interfaces Limpias**: métodos simples y con nombres significativos  
3. **Encapsular Datos y Comportamiento Relacionados**: todo lo relacionado a un concepto está en una clase  
4. **Proteger la Integridad de los Datos**: atributos privados con acceso controlado  
5. **Modelar Entidades del Mundo Real**: las clases representan cosas reales (Cuenta, Libro, Estudiante, Producto)  

---

## Consejos de Práctica para OOP en Python

1. Usa la convención de guion bajo para atributos "privados" (`self._name`)  
2. Aprovecha el decorador `@property` para acceso controlado  
3. Usa list comprehensions para filtrado y transformaciones  
4. Mantén los métodos enfocados: cada uno debe hacer una sola cosa bien  
5. Usa nombres descriptivos: Python enfatiza la legibilidad  
6. Sigue **PEP 8** para un código limpio  

---


## Lunes 01/09

### Resolucion Ejercicio 1

#### Programacion Secuencial
```py
# Global lists
# "Gonzalo Account", "Bonny Account"
account_holders = []
# 100.2, 122.3, 100.2
balances = []
# 11222, 12223, 12224
account_numbers = []

def create_account(name, initial_balance, account_number):
    # Add to lists
    account_holders.append(name)
    balances.append(initial_balance)
    account_numbers.append(account_number)

def find_account_index(account_number):
    # Loop through list to find account
    for i in range(len(account_numbers)):
        if account_numbers[i] == account_number:
            return i
    return -1    

def deposit(account_number, amount):
    # Find account in list, update balance
    index = find_account_index(account_number)

    balances[index] += amount
    return True

def withdraw(account_number, amount):
    index = find_account_index(account_number)

    balances[index] -= amount
    return True

def check_balance(account_number):
    index = find_account_index(account_number)
    return balances[index] 

def main():
    create_account("GonzaloAccount", 20, 122)
    create_account("AlexAccount", 20, 123)

    deposit(122, 200.2)
    deposit(123, 200.2)

    print(f"El balance de 122 es: {check_balance(122)}")
    print(f"El balance de 123 es: {check_balance(123)}")

    withdraw(123, 100)

    print(f"El balance de 123 es: {check_balance(123)}")



if __name__ == "__main__":
    main()
```
#### Programacion Orientada Objetos

```py
class BankAccount:
    def __init__(self, id: int, name: str, initial_ammount: float) -> None:
        self._id = id
        self._name = name
        self._balance = initial_ammount

    def get_id(self)-> int:
        return self._id

    def get_balance(self)-> float:
        return self._balance
    
    def deposit(self, amount: float)-> bool:
        self._balance += amount
        return True
  
    def withdraw(self, amount: float)-> bool:
        self._balance -= amount
        return True

class BankSystem:
    def __init__(self) -> None:
        self._accounts: list[BankAccount] = []

    def create_account(self, bank_account: BankAccount) -> None:
        self._accounts.append(bank_account)

    def find_account(self, id: int) -> BankAccount | None:
        for account in self._accounts:
            if account.get_id() == id:
                return account
        return None

def main():

    gonzalo_account: BankAccount = BankAccount(122, "Gonzalo Account", 32.2)
    # print(f"El balance de 122 es: {gonzalo_account.get_balance()}")

    # gonzalo_account.deposit(233)
    ucb_bank: BankSystem = BankSystem()
    ucb_bank.create_account(gonzalo_account)

    found_account = ucb_bank.find_account(1220000)

    if  found_account == None:
        print("la cuenta no existe")
    else:
        print(found_account.get_balance())
    # create_account("GonzaloAccount", 20, 122)
    # create_account("AlexAccount", 20, 123)

    # deposit(122, 200.2)
    # deposit(123, 200.2)

    # print(f"El balance de 123 es: {check_balance(123)}")

    # withdraw(123, 100)

    # print(f"El balance de 123 es: {check_balance(123)}")

if __name__ == "__main__":
    main()
```

# Semana 6

## Encapsulamiento

- El encapsulamiento agrupa datos (atributos) y comportamiento (métodos) dentro de una clase y controla su acceso.
- Esto ayuda a separar la lógica de e.j. sensores/actuadores del control de alto nivel.

Objetivos

- Proteger estados internos de sensores y actuadores.
- Diseñar interfaces públicas (comandos seguros) y mantener invariantes (limites físicos).
- Crear propiedades con validación (por ejemplo límites de velocidad, rangos de sensor).

Caso de estudio `SensorIMU` que procese lecturas crudas de acelerómetro y giroscopio. Proponer métodos públicos para obtener ángulos filtrados y privados para aplicar calibración y filtrado. Especificar qué datos se almacenan internamente y cómo se valida la calibración.

- https://www.mathworks.com/help/nav/ug/introduction-to-simulating-imu-measurements.html
- https://github.com/niru-5/imusensor?tab=readme-ov-file

### Ejercicios

1. Diseñar una clase `MotorController` para un motor DC que exponga métodos públicos `set_speed(valor)` y `stop()`. Indicar qué atributos deben ser privados (p. ej. PWM, dirección, estado de emergencia) y las validaciones necesarias (velocidad dentro de rango, bloqueo por emergencia).

2. Caso de estudio: `BateriaRobot` con monitoreo de voltaje y corriente. Plantear una interfaz pública para consultar estado y métodos privados para calcular carga restante. Definir reglas para evitar lecturas falsas o acciones peligrosas (por ejemplo, desactivar actuadores si el voltaje es crítico).

3. Mini-ejercicio de refactorización: Dado código donde múltiples módulos acceden y modifican directamente los límites de velocidad de los motores, describir los pasos para encapsular esa lógica dentro de `MotorController` y proporcionar una transición segura para el código cliente (adaptadores, métodos de compatibilidad).

```py
# Código inicial problemático - NO HACER ESTO
class Motor:
    def __init__(self, id_motor):
        self.id = id_motor
        self.velocidad_maxima = 100  # RPM
        self.velocidad_minima = -100  # RPM
        self.velocidad_actual = 0
        self.pwm_value = 0
        self.direccion = "forward"
        self.emergencia_activa = False

# Módulos que usan directamente los atributos del motor
class ModuloNavegacion:
    def mover_adelante(self, motor_izq, motor_der):
        # ¡PROBLEMA! Acceso directo sin validación
        motor_izq.velocidad_actual = 80
        motor_der.velocidad_actual = 80
        motor_izq.pwm_value = 80
        motor_der.pwm_value = 80

class ModuloEmergencia:
    def detener_todo(self, motores):
        for motor in motores:
            # ¡PROBLEMA! Modifica estado interno directamente
            motor.emergencia_activa = True
            motor.velocidad_actual = 0

class ModuloTeleoperacion:
    def controlar_manual(self, motor, velocidad_joystick):
        # ¡PROBLEMA! No valida límites
        motor.velocidad_actual = velocidad_joystick * 150  # Puede exceder límites!
        motor.pwm_value = abs(velocidad_joystick * 150)
```

# Semana 7

## Herencia

La herencia en Python te permite construir nuevas clases reutilizando y ampliando la funcionalidad de las existentes. Aprende a diseñar relaciones entre clases padre-hijo, a implementar patrones de herencia y a aplicar técnicas como la sustitución de métodos.

```py
class ParentClass:
    def __init__(self, attributes):
        # Initialize attributes
        pass

    def method(self):
        # Define behavior
        pass
```

```py
class ChildClass(ParentClass):
    def additional_method(self):
        # Define new behavior
        pass
```

### Tipos de herencia en Python

**Herencia Unica**
```py
class Person:
    """Represents a general person with basic details."""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    """Represents a student, extending the Person class to include academic details."""
    def __init__(self, name, id, grade, courses):
        super().__init__(name, id)
        self.grade = grade
        self.courses = courses

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Courses: {', '.join(self.courses)}"

# Example usage in a school system
student = Student("Samuel", 5678, "B+", ["Math", "Physics", "Computer Science"])
print(student.get_details())
```

**Herencia Multiple**
```py
class Person:
    def get_details(self):
        return "Details of a person."

class Athlete:
    def get_skill(self):
        return "Athletic skills."

class Student(Person, Athlete):
    pass

# Example usage
student = Student()
print(student.get_details())
print(student.get_skill())
```

**Herencia Multinivel**

```py
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

class GraduateStudent(Student):
    def __init__(self, name, id, grade, thesis_title):
        super().__init__(name, id, grade)
        self.thesis_title = thesis_title

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Thesis: {self.thesis_title}"

# Example usage
grad_student = GraduateStudent("Charlie", 91011, "A", "AI in Healthcare")
print(grad_student.get_details())
```

**Herencia jerárquica**

```py
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, id, subject):
        super().__init__(name, id)
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Subject: {self.subject}"

# Example usage
student = Student("Samuel", 5678, "B+")
teacher = Teacher("Dr. Smith", 1234, "Math")
print(student.get_details())  
print(teacher.get_details())
```

**Herencia híbrida**
(herencia jerárquica + herencia múltiple)
```py
# Base class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

# Intermediate class inheriting from the base class
class Employee(Person):
    def __init__(self, name, id, position):
        super().__init__(name, id)
        self.position = position

    def get_position(self):
        return f"Position: {self.position}"

# Another independent base class
class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def get_sport(self):
        return f"Sport: {self.sport}"

# Derived class combining Employee and Athlete
class Student(Employee, Athlete):
    def __init__(self, name, id, position, grade, sport):
        Employee.__init__(self, name, id, position)
        Athlete.__init__(self, sport)
        self.grade = grade

    def get_grade(self):
        return f"Grade: {self.grade}"

# Example usage
student = Student("Samuel", 1234, "Intern", "A", "Soccer")
print(student.get_details())  # From Person
print(student.get_position())  # From Employee
print(student.get_grade())  # From Student
print(student.get_sport())  # From Athlete
```

### Beneficios de la herencia
**Reutilización:** Con la herencia puedes escribir código una vez en la clase padre y reutilizarlo en las clases hijas. Utilizando el ejemplo, tanto `FullTimeEmployee` como `Contractor` pueden heredar un método `get_details() `de la clase padre `Employee`.

**Simplicidad:** La herencia modela las relaciones con claridad. Un buen ejemplo es la clase `FullTimeEmployee` que "es-un" tipo de la clase padre `Employee`.

**Escalabilidad:** También añade nuevas funciones o clases hijo sin afectar al código existente. Por ejemplo, podemos añadir fácilmente una nueva clase Intern como clase hija.

### Tecnicas

#### Sobrescribir métodos en python

```py
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade
    
    # Overriding the get_details method
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

# Example usage
student = Student("Samuel", 1234, "A")
print(student.get_details())
```
### Utilizar super() para la inicialización de los padres

```py
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(Person):
    def __init__(self, name, id, grade):
        # Using super() to initialize the parent class
        super().__init__(name, id)
        self.grade = grade

# Example usage
student = Student("Samuel", 5678, "B+")
print(student.name)
print(student.id)
print(student.grade)
```

### Clases base abstractas (ABC)
Una clase base abstracta (ABC) es una clase que no puede utilizarse directamente para crear objetos. Su finalidad es definir un conjunto común de métodos que otras clases deben aplicar. Por tanto, los ABC son útiles cuando quieres asegurarte de que determinados métodos estén siempre presentes en las clases hijas.

```py
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Student(Person):
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
    
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

# Example usage
student = Student("Hamilton", 7890, "A-")
print(student.get_details())
```
### Polimorfismo
```py
class Person:
    def get_details(self):
        return "Details of a person."

class Student(Person):
    def get_details(self):
        return "Details of a student."

class Teacher(Person):
    def get_details(self):
        return "Details of a teacher."

# Example usage
def print_details(person):
    print(person.get_details())

student = Student()
teacher = Teacher()

print_details(student) 
print_details(teacher)
```

# Ejercicios de Herencia - Semana 7

## Ejercicio 1: Sistema de Control de Robots Industriales

### Enunciado:
Diseña un sistema de jerarquía de clases para robots industriales aplicando **herencia única y multinivel**.

**Requisitos:**

1. **Clase base `Robot`:**
   - Atributos: `modelo`, `año_fabricacion`, `estado` (activo/inactivo), `horas_operacion`
   - Métodos: `encender()`, `apagar()`, `obtener_estado()`, `registrar_horas(horas)`

2. **Clase `RobotIndustrial` (hereda de `Robot`):**
   - Atributos adicionales: `carga_maxima`, `precision_mm`, `area_trabajo`
   - Métodos adicionales: `validar_carga(peso)`, `mover_a_posicion(x, y, z)`
   - Sobrescribir: `obtener_estado()` para incluir información de carga

3. **Clase `RobotSoldador` (hereda de `RobotIndustrial`):**
   - Atributos adicionales: `tipo_soldadura`, `temperatura_max`, `consumo_electrodo`
   - Métodos adicionales: `iniciar_soldadura()`, `ajustar_temperatura(temp)`, `cambiar_electrodo()`
   - Sobrescribir: `obtener_estado()` para incluir información de soldadura

**Tareas:**
- Implementar las tres clases con herencia apropiada
- Crear instancias y demostrar el uso de `super()`
- Mostrar cómo cada clase sobrescribe métodos del padre
- Crear un programa principal que maneje una lista de diferentes tipos de robots

---

## Ejercicios Herencia: Sistema de Sensores con Herencia Múltiple

### Enunciado:
Desarrolla un sistema de sensores que combine capacidades usando **herencia múltiple**.

**Requisitos:**

1. **Clases base independientes:**
   ```python
   class DispositivoElectronico:
       # Atributos: voltaje_operacion, consumo_energia, pin_conexion
       # Métodos: conectar(), desconectar(), verificar_alimentacion()

   class ComunicacionWireless:
       # Atributos: protocolo, frecuencia, alcance_metros
       # Métodos: conectar_red(), enviar_datos(datos), recibir_datos()

   class SensorAmbiental:
       # Atributos: rango_medicion, precision, unidad_medida
       # Métodos: calibrar(), tomar_lectura(), validar_rango(valor)
   ```

2. **Clases derivadas con herencia múltiple:**
   - `SensorTemperaturaIoT` (hereda de `DispositivoElectronico`, `ComunicacionWireless`, `SensorAmbiental`)
   - `SensorHumedadIoT` (hereda de `DispositivoElectronico`, `ComunicacionWireless`, `SensorAmbiental`)

**Tareas:**
- Implementar las clases base y las clases derivadas
- Resolver posibles conflictos en el Method Resolution Order (MRO)
- Demostrar cómo una instancia puede usar métodos de todas las clases padre
- Crear un sistema que gestione múltiples sensores IoT

---

## Ejercicio 3: Refactorización usando Clases Abstractas (ABC)

### Enunciado:
Refactoriza el siguiente código problemático usando **Abstract Base Classes** para crear una jerarquía limpia de actuadores.

**Código inicial problemático:**
```python
# Sistema actual sin estructura clara
class ActuadorLineal:
    def mover(self, distancia):
        print(f"Moviendo linealmente {distancia}mm")

class ActuadorRotativo:
    def girar(self, angulos):
        print(f"Girando {angulos} grados")

class ActuadorNeumatico:
    def activar_cilindro(self, presion):
        print(f"Activando cilindro a {presion} PSI")

# Uso inconsistente - cada actuador tiene interfaz diferente
actuadores = [ActuadorLineal(), ActuadorRotativo(), ActuadorNeumatico()]
# No se pueden tratar de forma uniforme
```

**Requisitos de refactorización:**

1. **Crear clase base abstracta `Actuador`:**
   - Métodos abstractos: `activar()`, `desactivar()`, `obtener_posicion_actual()`
   - Métodos concretos: `obtener_estado()`, `tiempo_operacion()`

2. **Refactorizar las clases existentes:**
   - Que hereden de `Actuador`
   - Implementen todos los métodos abstractos
   - Mantengan su funcionalidad específica

3. **Crear nuevas clases:**
   - `ActuadorHidraulico` (nueva implementación)
   - `SistemaActuadores` (clase gestora que maneje polimórficamente todos los actuadores)

**Tareas:**
- Implementar la clase abstracta usando `ABC` y `@abstractmethod`
- Refactorizar las clases existentes
- Demostrar polimorfismo: mismo código funciona con diferentes actuadores
- Mostrar cómo el sistema rechaza instanciar la clase abstracta directamente
- Crear un programa que demuestre el manejo uniforme de todos los actuadores

**Bonus:** Agregar validación de tipos usando `isinstance()` y manejo de excepciones para operaciones inválidas.