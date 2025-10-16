# Herencia en Python

La herencia en Python te permite construir nuevas clases reutilizando y ampliando la funcionalidad de las existentes. Aprende a diseñar relaciones entre clases padre-hijo, a implementar patrones de herencia y a aplicar técnicas como la sustitución de métodos.

## Conceptos Básicos

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

## Tipos de Herencia en Python

### 1. Herencia Única

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

### 2. Herencia Múltiple

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

### 3. Herencia Multinivel

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

### 4. Herencia Jerárquica

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

### 5. Herencia Híbrida

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

## Beneficios de la Herencia

**Reutilización:** Con la herencia puedes escribir código una vez en la clase padre y reutilizarlo en las clases hijas. Utilizando el ejemplo, tanto `FullTimeEmployee` como `Contractor` pueden heredar un método `get_details()` de la clase padre `Employee`.

**Simplicidad:** La herencia modela las relaciones con claridad. Un buen ejemplo es la clase `FullTimeEmployee` que "es-un" tipo de la clase padre `Employee`.

**Escalabilidad:** También añade nuevas funciones o clases hijo sin afectar al código existente. Por ejemplo, podemos añadir fácilmente una nueva clase Intern como clase hija.

## Técnicas Importantes

### Sobrescribir Métodos en Python

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

### Utilizar super() para la Inicialización de los Padres

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

### Clases Base Abstractas (ABC)

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
