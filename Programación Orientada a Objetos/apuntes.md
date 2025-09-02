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
