import json

# Python об'єкт (словник)
data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Десеріалізація з файлу
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)
