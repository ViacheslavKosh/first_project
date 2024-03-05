# Робота з випадковими величинами
# Для отримання випадкового цілого числа з рівномірного розподілу в інтервалі між a та b включно треба використати метод random.randint(a, b). Він повертає випадкове ціле число N таке, що a <= N <= b:
import random

random.randint(1, 1000)

import random

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

# генерує випадкове дійсне число між 0.0 (включно) та 1.0 (не включно):

num = random.random()
print(num)

# випадкове відсоткове заповнення

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

# Метод random.randrange(start, stop[, step]) повертає випадково вибране число з заданого діапазону

print(random.randrange(10))  # Верхня межа є 10, але не включається

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

# перемішати порядок елементів в цьому списку на випадковий, ми використовуємо метод random.shuffle(x)

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)
print(f"Перемішана колода: {cards}")

# потрібно вибрати випадковий елемент зі списку, нам потрібно використати метод random.choice(seq)
print(random.choice(cards))

# Щоб вибрати більше чим один випадковий елемент зі списку, нам необхідний метод random.choices()
# random.choices(population, weights=None, cum_weights=None, k=1)
items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item) 
numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)

# Вибір з вагами:
colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color) 

# вибрати N елементів зі списку і вони при цьому не повторювалися треба використати метод random.sample(population, k)
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

# random.uniform(a, b). Метод повертає випадкове дійсне число N, таке що a <= N <= b.

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")