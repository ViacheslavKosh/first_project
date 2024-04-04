# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
        
#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, color):
#         Animal.color = color

# first_animal = Animal('Dusya', 10)
# second_animal = Animal('Gav', 20)
# print(first_animal.color)
# print(second_animal.color)
# second_animal.change_color('red')
# print(first_animal.color)
# print(second_animal.color)

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Dog(Animal):
#     def __init__(self, nickname, weight, bread):
#         super().__init__(nickname, weight)
#         self.bread = bread
    
#     def say(self):
#         return "Woof"

# dog = Dog("Barbos", 23, "labrador")
# print(dog.bread)

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
    
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
        
#     def info(self):
#         return {'name': self.name, 'age': self.age, 'address': self.address}


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         super().__init__(nickname, weight)
#         self.breed = breed
#         self.owner = owner
        
#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()
    
# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# dog = Dog("Simon", 10, "british", owner)

# print(owner.info())
# print(dog.who_is_owner())



class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog (Cat, Dog):
    def say(self):
        return super().say()

class DogCat (Dog, Cat):
    def say(self):
        return super().say()
        
dog = DogCat("Simon", 10)
cat = CatDog("Mimon", 12)

print(dog.say())
print(cat.say())

    