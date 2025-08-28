# Concepts
## Py files
## Variables

```py
name = 'Bob'
age = 20

print(name, age)
print('Hello my name is:', name)
```

## Basic Data Types 

```py
number: int = 10
decimal : float = 2.5
text: str = 'Hello, world!'
active: bool = False

names:list = ['Bob', 'Anna', 'Luigi']
coordinates: tuple = (1.5, 2.5)
unique: set = {1, 4, 2, 9}
data: dict = {'name': 'Bob', 'age': 21}

```

## Type Anotations

```py
name = 'Bob'
name: str = 'Bob'

age: int = 'Eleven'
# think of trafic lights
```

## Constants
```py
from typing import Final

VERSION: Final[str] = '1.0.13'
VERSION = '1.2'

```

## Functions

```py
from datetime import datetime

print('this is the current time:')
print(datetime.now())

print('this is the current time:')
print(datetime.now())

def show_date() -> None:
    print('this is the current time:')
    print(datetime.now())

show_date()
show_date()

def greet(name: str) -> None:
    print(f'Hello: {name}')

def add(a: float, b: float) -> float:
    return a + b

print(add(1,2))
```
## Class / Methods

```py
class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.brand} is driving')
    
    def get_info(self) -> None:
        print(f'{self.brand} with {self.horsepower} horsepower')


volvo: Car = Car('Volvo', 200)

print(volvo.brand)
print(volvo.horsepower)
volvo.drive()
volvo.get_info()

# bmw

```


## Dunder Methods

```py
class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower} hp'

    def __add__(self, other Self) -> str
        return f'{self.brand} & {other.brand}'

volvo: Car = Car('Volvo', 200)
print(volvo)

bmw: Car = Car('BMW', 200)
print(volvo + bmw)

```