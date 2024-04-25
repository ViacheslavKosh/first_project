import json

class Name:
    def __init__(self, name):
        self.name = name


class Phone:
    def __init__(self, phone):
        self.phone = phone


class Person:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
    
    def __getstate__(self):
        return {
            "name": self.name.__getstate__(),
            "phone": self.phone.__getstate__()
        }

    
def save_to_file(data, filename='data.json'):
    with open(filename, 'w') as data_file:
        json.dump(data.__getstate__(), data_file)

if __name__ == '__main__':
    phone = Phone('1234567890')
    name = Name('John')

    john = Person('John', '1234567890')

    save_to_file(john)
    print('Hello, from main')


#
# (1, 2), (2, 3)
# 1---2-----3

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
    (3, 4): 3
}

# [1, 2, 3, 4]
# (1, 2), (2, 3), (3, 4)
# [1, 2, 3, 0, 1]

def calculate_distance(points_list):
    # [1, 2, 3, 4] -> [(1, 2), (2, 3), (3, 4)]
    # [0, 1, 2, 3]
    distance = 0
    for i in range(len(points_list) - 1):
        pair = (points_list[i], points_list[i + 1])
        alternative_pair = (points_list[i + 1], points_list[i])
        # distance += points.get(pair)
        if pair in points:
            distance += points.get(pair)
        elif alternative_pair in points:
            distance += points.get(alternative_pair)
        else:
            raise ValueError(f'Pair {pair} does not exist')
        print(pair)
    return distance

print(calculate_distance([1, 2, 3, 0, 4]))


# Створити клас, який буде себе поводити як звичайне число
# one = Number(1), two = Number(2)
# print(one * two), one + two, one - two, two / one, two // one

# __add__, __sub__, __mul__, __truediv___, __floordiv__

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value
    
#     def __sub__(self, other):
#         return self.value - other.value
    
#     def __mul__(self, other):
#         return self.value * other.value
    
#     def __truediv___(self, other):
#         return self.value / other.value


# three = Number(3)
# six = Number(6)
# print(three * six)

# Написати клас, який буде себе поводити як множина, але не використовувати множину
# my_set_one = {1, 2, 3}
# my_set_one = set({1, 2, 3})
# print(my_set_one)
# my_set_two = {4, 5, 6}

# my_set_one.add(2)
# print(my_set_one)

# my_set_one.add(4)
# my_set_one.add(0)
# print(my_set_one)

# Множина сортує елементи

# Множина підтримує унікальність елементів

class Set:
    def __init__(self, starting_set=[]):
        self.data = []
        for element in starting_set:
            if element in self.data:
                continue
            self.data.append(element)
        self.data.sort()

    def add(self, value):
        if value in self.data:
            return
        self.data.append(value)
        self.data.sort()

    def intersection(self, other_set):
        result_set = Set()
        for element in self.data:
            if element in other_set.data:
                result_set.add(element)
        return result_set


    def __str__(self):
        return f'{self.data}'
    
from collections import UserList

class MyList(UserList):
    def __init__(self, starting_set=[]):
        self.data = starting_set

    def intersection(self, other_set):
        result_list = MyList()
        for element in self.data:
            if element in other_set.data:
                result_list.append(element)
        return result_list
    


# my_set_one = set({1, 2, 3})
# my_set_one = Set({1, 1, 2, 3, 0})
# print(my_set_one)

# my_set_one.add(1)
# my_set_one.add(4)
# my_set_one.add(-1)
# print(my_set_one)

# my_set_one = {1, 2, 3, 4}
# my_set_two = {4, 5, 6, 7}

# print(my_set_one.intersection(my_set_two))

# my_class_set_one = Set({1, 2, 3, 4})
# my_class_set_two = Set({4, 5, 6, 7})

# print(my_class_set_one.intersection(my_class_set_two))

my_list_one = MyList([1, 1, 2, 3, 4, 5, 5])
my_list_two = MyList([4, 5, 5, 7, 8])

print(my_list_one.intersection(my_list_two))

# Потрібно написати клас, в який ми можемо записати пароль, але не можемо його звідти дістати
# Повертати невірний пароль, такої самої довжини

# Чи такий пароль вже був використаний

class Storage:
    def __init__(self, password):
        self.__password = None
        self.password = password

    @property
    def password(self):
        return "You can not have my password"
    
    @password.setter
    def password(self, new_password):
        if (len(new_password) < 8):
            raise ValueError('Password is too short')
        if new_password == self.__password:
            raise ValueError('Password is the same as previous one')
        self.__password = new_password


storage = Storage('password123')
print(dir(storage))
print(storage.password)

storage.password = 'password123'

storage.password = '12334'

# storage.password = '1234'
# storage._Storage__password += "543"
# print(storage._Storage__password)