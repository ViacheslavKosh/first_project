# Створення шляхів за допомогою класу Path у модулі pathlib

from pathlib import Path

# Для Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")

# Додавання шляхів
from pathlib import Path

# Початковий шлях
base_path = Path("/usr/bin")

# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"

print(full_path)  # Виведе: /usr/bin/subdir/script.py


