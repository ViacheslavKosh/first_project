s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1 не знайдена

s = 'Some words'

print(s.find("o")) #1 пошук зліва направо
print(s.rfind('o')) #6 пошку з права на ліво

print(s.index("o")) #1 те саме що find але якщо не знайде ValueError
print(s.rindex('o')) #6


