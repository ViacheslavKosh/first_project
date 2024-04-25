# print ("WTF")
# # Введення (отримання даних)
# ім_я = input("Введіть ваше ім'я: ")

# # Перетворення (обробка даних)
# вітання = f"Привіт, {ім_я}!"

# # Виведення (виведення даних)
# print(вітання)
# print(ім_я[2])
# int_number = 3
# float_number = 3.3
# complex_number = 3 + 3.5j

# is_active = True
# is_delete = False

# age = 18
# is_adult = age >= 18  # True
# print (is_adult)

# age = 15
# is_adult = age >= 18  # False
# print(is_adult)
# side_a = 10
# side_b = 5
# hipotenuse = (side_a**2 + side_b**2)**0.5
# print(hipotenuse)

# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60

# print(hours)
# print (minutes)
# print(seconds)

# ratio = -10
# result = 8 * (ratio + 5) - ratio ** 2
# print(result)
# print(f'{hours} годин, {minutes} хвилин, {seconds} секунд')
# age = input("How old are you? ")
# age = int(age)

# a = float(input("Введіть сторону квадрата a: "))
# P = 4 * a
# print(f"Периметр квадрата дорівнює {P}")

# Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# # Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# # Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant + \
#              num_glasses * price_per_glass + \
#              num_coffee_packs * price_per_coffee_pack

# # Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# # Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")

# СПИСКИ
# my_list = list()
# empty_list = [1, 2, 'hello', 3, 4, 5]
# empty_list.append(8)
# my_list.append(1)
# first = empty_list[0]
# second = empty_list[1]
# third = empty_list[2]
# empty_list[5] = 566
# vitannya = empty_list.pop(2)
# empty_list.extend(my_list)
# print(empty_list)
# empty_list.insert(3, vitannya)
# print(empty_list)
# vitannya_index = empty_list.index('hello')
# print(vitannya_index)
# count_1 = empty_list.count(1)
# print(count_1)
# print(len(empty_list))
# empty_list[3] = 7
# empty_list.sort()
# print(empty_list)
# empty_list.sort(reverse=True)
# print(empty_list)
# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)  # Виведе ['apple', 'banana', 'cherry']
# empty_list_copy = empty_list.copy()
# empty_list.reverse()
# print(empty_list)

# СЛОВНИКИ
# my_dict = {"name": "Slava", "age": 37, "city": "Zaporizhzhia"}
# print(my_dict['name'])
# my_dict['email'] = 'koshelevskiy.v@gmail.com'
# my_dict['street'] = 'Charivna'
# print(my_dict)
# street = my_dict.pop('street')
# print(street)
# print(my_dict)
# my_dict_copy = my_dict.copy()
# my_dict_copy.clear()
# print(my_dict_copy)
# name = my_dict.get('name')
# print(name)
# print(my_dict)

# МНОЖИНИ
# empty_set = set()
# a = {1, 2, 3, 4, 5, 6, 7, 8}
# print(a)
# lst = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8]
# d_lst = set(lst)
# lst = list(d_lst)
# a.add(9)
# print(a)
# a.remove(5)
# print(a)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))  # {3}
# print(a & b)  # {3}
# print(a.difference(b))
# print(a-b)
# print(a.symmetric_difference(b))
# print(a^b)
# print(a.union(b))  # {1, 2, 3, 4, 5}
# print(a | b)  # {1, 2, 3, 4, 5}
# my_frozenset = frozenset([1, 2, 3, 4, 5])

# КОРТЕЖІ
# my_tuple = (1, 2, 3)

# # РЯДКИ
# game_string = 'My favorit"Game"'

# s = "Hello world!"
# print(s[0])# H
# print(s[-1])# !
# game_string.upper()
# print(game_string)
# s = "Hello"
# d = s.upper()
# s.upper()
# print(s)
# print(s.upper()) # Виведе 'HELLO' перший варіант
# print(d)  # Виведе 'HELLO' другий варіант
# d.lower()
# print(d)
# print(d.lower())
# print(game_string.startswith("My"))
# s = "hello.jpg"
# print(s.endswith("jpg"))  # Виведе True
# s = "hello world".capitalize()  # Результат: "Hello world"
# print(s)
# s = "hello world".title()  # Результат: "Hello World"
# print(s)
# "123".isdigit()  # True
# "hello".isalpha()  # True
# " ".isspace()  # True

# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# # ЗРІЗИ

# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[::2]
# print(odd_numbers)
# rven_numbers = numbers[1::2]
# print(rven_numbers)
# tree_numbers = numbers[2::3]
# print(tree_numbers)
# reverse_numbers = numbers[::-1]
# print(reverse_numbers)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# copy_numbers = numbers[:]
# print(copy_numbers)

# length = 2.75
# width = 1.75
# area = length*width
# show = f"'With width {width} and length {length} of the room, its area is equal to {area}'"
# print(show)

# length = float("2.75")
# width = float("1.75")
# # length = float(length)
# # width = float(width)
# area = width * length
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"

# print(type(length))

# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# my_list.insert(1, 'Python')
# my_list.reverse
# print(my_list)

cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = "падлюка", "насцяв" 
print(cat)
age = cat.get("age")
cat.update({"status": "vaccinated", "breed": True})
print(cat)
print(age)