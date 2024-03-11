# # Для копіювання файлів використовується функція shutil.copy() або shutil.copy2().
# import shutil
# from pathlib import Path
# # Вихідний і цільовий файли
# source = Path('/path/to/source/file.txt')
# destination = Path('/path/to/destination/file.txt')
# # Копіювання файла
# shutil.copy(source, destination)
# # Функція shutil.copy() копіює вміст файлу, але не копіює метадані, тоді як shutil.copy2() копіює і вміст, і метадані.

# # Для переміщення файлів використовується функція shutil.move().
# import shutil
# from pathlib import Path
# # Вихідний і цільовий шляхи
# source = Path('/path/to/source/file.txt')
# destination = Path('/path/to/destination/file.txt')
# # Переміщення файла
# shutil.move(source, destination)

# Метод stat() повертає інформацію про файл, включаючи його розмір.
from pathlib import Path
file_path = Path("./picture/1.png")
# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

# Метод stat() також надає час створення, атрибут st_ctime, та час останньої модифікації файлу, атрибут st_mtime.
from pathlib import Path
import time
file_path = Path("./picture/1.png")
# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")

# Для видалення файлу використовується метод unlink(). Він видаляє файл, на який вказує об'єкт Path.
from pathlib import Path
# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')
# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

# Можна також видалити файл без попередньої перевірки його існування, використовуючи параметр missing_ok.
from pathlib import Path
file_path = Path('/path/to/file.txt')
file_path.unlink(missing_ok=True)

