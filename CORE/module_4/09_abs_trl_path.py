# Абсолютний шлях - це повний шлях до файлу 
# Приклад на Unix/Linux: /home/user/documents/example.txt
# Приклад на Windows: C:\Users\user\documents\example.txt
# Відносний шлях - це шлях до файлу або директорії відносно поточного робочого каталогу
# робочий каталог - C:\Users\Username, то відносний шлях до файлу example.txt у директорії Documents буде просто Documents\example.txt.

from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

# Існує метод relative_to() який навпаки, використовується для отримання відносного шляху відносно заданої директорії