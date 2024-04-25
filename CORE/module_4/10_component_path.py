# Метод with_name замінює ім'я файлу в шляху на нове
from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)

# Метод with_suffix замінює або додає розширення файлу в шляху
from pathlib import Path

# Початковий шлях до файлу
original_path = Path("Module_4/example.txt")

# Зміна імені файлу
new_path = original_path.with_suffix(".md")
print(new_path)

# with_name і with_suffix в класі Path модуля pathlib в Python не змінюють фізичне ім'я файлу на диску
from pathlib import Path

original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")

print(original_path)
print(new_path)

# Щоб фізично змінити ім'я файлу на диску, потрібно використовувати методи для роботи з файловою системою, наприклад, rename
from pathlib import Path

original_path = Path("Module_4/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)


