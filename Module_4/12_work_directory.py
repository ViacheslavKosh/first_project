# Метод iterdir() використовується для отримання переліку всіх файлів та піддиректорій у вказаній директорії
from pathlib import Path
# Створення об'єкту Path для директорії
directory = Path("./picture")
# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)


# Для створення нової директорії використовується метод mkdir().
from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)

# Для видалення директорії використовується метод rmdir()
from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.rmdir()

# метод exists() перевіряє, чи існує файл або директорія.
# метод is_dir() перевіряє, чи є об'єкт директорією.
# метод is_file() перевіряє, чи є об'єкт файлом.
from pathlib import Path

path = Path("./picture")
# Перевірка існування
if path.exists():
    print(f"{path} існує")
# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")
# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

