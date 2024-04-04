# from dataclasses import dataclass
# @dataclass
# class ExampleClass:
#     attribute1: type
#     attribute2: type = default_value

# з ініціалізацією атрибутів
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# спрощеня через @dataclass
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int


from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int
    def area(self) -> int:
        return self.width * self.height
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)
print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")
