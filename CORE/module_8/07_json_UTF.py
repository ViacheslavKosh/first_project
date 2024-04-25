import json

# Python об'єкт (словник)
data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json.1", "w", encoding="utf-8") as f:
    json.dump(data, f)


# Серіалізація у файл
with open("data.json.+6+9++2", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
