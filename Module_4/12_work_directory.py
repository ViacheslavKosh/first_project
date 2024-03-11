# Метод iterdir() використовується для отримання переліку всіх файлів та піддиректорій у вказаній директорії
from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path("./Module_4")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)
