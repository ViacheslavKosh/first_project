import time

current_time = time.time()
print(f"Поточний час: {current_time}") # повертає поточний час у секундах з 1 січня 1970 року

# Метод time.sleep(seconds) зупиняє виконання програми на вказану кількість секунд
print("Початок паузи")
time.sleep(5)
print("Кінець паузи")

# Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення

current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

# Метод time.localtime([seconds]) перетворює часову мітку в структуру struct_time у місцевій часовій зоні

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

