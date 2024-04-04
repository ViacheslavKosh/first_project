class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")

first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()
third = Person('Slava')
first.how_many_persons()

# змінна класу
class Person:
    count = 0
    def __init__(self):
        pass
person = Person()
print(person.count)  # 0

class Person:
    count = 0
    def __init__(self):
        self.count = 10
person = Person()
print(person.count)  # 10
print(Person.count)  # 0

# Приклад
class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health
    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")
    def dodge(self):
        print(f"{self.name} dodged the attack!")
    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form
# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)
# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")
