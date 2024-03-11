# Модуль pathlib в Python є сучасним інструментом для роботи з файловою системою

from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

# Path наслідує всі методи з PurePath і додає методи читання, запис файлів, перевірка існування 
from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 
