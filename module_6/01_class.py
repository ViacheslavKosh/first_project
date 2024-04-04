# пустий клас
class Person:
    pass  # Порожній блок для тіла класу
p = Person()

# один клас, два різних об'єкти
class User:
    name = 'Anonymous'
    age = 15
user1 = User()
print(user1.name)
print(user1.age)
user2 = User()
user2.name = "John"
user2.age = 90
print(user2.name)
print(user2.age)

# атрибути класу
class MyClass:
    class_attribute = "I am a class attribute" 

# Поля класу використовуються для зберігання даних
class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу
obj1 = MyClass(5)
obj2 = MyClass(10)
print(obj1)
print(obj2)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')
    def set_age(self, age: int) -> None:
        self.age = age
bob = Person('Boris', 34)
bob.say_name()
bob.set_age(25)
bob.say_name()
slava = Person('Slava', 38)
slava.say_name()