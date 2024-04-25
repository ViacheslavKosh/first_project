#str.split(separator=None, maxsplit=-1) # separator - роздільник (замовчення пробіл). maxsplit - кількість розділів (-1 необмеж)

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']


# string.join(iterable) string - рядок роздільник, iterable - послідовність

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

clean = '   spacious   '.strip()
print(clean) # spacious

# str.replace(old, new, count=-1) 
#old - підрядок, який потрібно замінити. 
#new - підрядок, на який потрібно замінити
#ount - лічильник максимальної кількості замін. Якщо не вказано або вказано -1, замінюються всі входження.

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  

text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

print('TestHook'.removesuffix('Test')) # TestHook
print('TestHook'.removesuffix('Hook')) # Hook

