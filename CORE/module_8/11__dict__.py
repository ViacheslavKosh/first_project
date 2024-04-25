class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age
obj = Example("Gupalo Vasyl", 30)
# obj.__dict__ --> {'name': 'Gupalo Vasyl', 'age': 30}

obj.__dict__['city'] = 'Poltava'  # Додавання нового атрибута
print(obj.city)  # Виведення: Poltava

del obj.__dict__['age']  # Видалення атрибута age
print(obj.__dict__)  # Виведення: {'name': 'Gupalo Vasyl', 'city': 'Poltava'}

