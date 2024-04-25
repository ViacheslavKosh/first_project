# Звичайний код
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def greeting(self) -> str:
        return f"Hi {self.name}"
p = Person("Boris", 34)

# Protected позначаються нижнім підкрксленням _
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
    def greeting(self):
        return f"Hi {self.name}"
p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active)
print(p.greeting())

# додали метод is_active, щоб отримати доступ для читання захищеного атрибута _is_active
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())

# Privat
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
p = Person("Boris", 34, True, False)
# print(p.__is_admin)

# але доступно ззовни класу
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
p = Person("Boris", 34, True, False)
print(p._Person__is_admin)

# Захист від доступу
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
    def get_is_admin(self):
        return self.__is_admin
    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin
p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())

