import copy

class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting

class ComplexObject:
    def __init__(self, value, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")
