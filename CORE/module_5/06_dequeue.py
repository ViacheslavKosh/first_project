from collections import deque

# Створення пустої двосторонньої черги
d = deque()
# Додаємо елементи в чергу
d.append('middle')  # Додаємо 'middle' в кінець черги
d.append('last')    # Додаємо 'last' в кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги
# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))
# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())
# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())
# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))

# можливість обмежити розмір Deque
d = deque(maxlen=5)
for i in range(10):
    d.append(i)
print(d)

# Приклади використання
from collections import deque
# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]
# Ініціалізація черги завдань
task_queue = deque()
# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")
# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")

