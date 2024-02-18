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
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")