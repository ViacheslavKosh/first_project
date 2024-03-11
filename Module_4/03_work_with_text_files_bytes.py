# режим відкриття файлів як b, скорочено від bytes

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')
with open('raw_data.bin', "r") as fh:
    data = fh.read()
print(data)

s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

# Створення байт-рядока

byte_string = b'Hello world!'

# перетворення рядка у байт-рядок методом рядків encode 
#  str.encode(encoding="utf-8", errors="strict")

byte_str = 'some text'.encode()
print(byte_str)

# Перетворення чисел у байт-рядки

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел

for num in [127, 255, 156]:
  print(hex(num))

# в UTF-8 відповідає символ, є функція ord (від order).
ord('a')  # 97

# Зворотна операція, коли потрібно дізнатися, який символ закодований числом, наприклад 100, є функція chr
chr(128)  # 'd'

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

# неправильне декодування
print(b'Hello world!'.decode('utf-16'))

# завжди вказувати кодування UTF-8 під час відкриття файлів параметр encoding у функції open()
# Відкриття текстового файлу з явним вказівкам UTF-8 кодування

# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('example.txt', 'w') as file:
    file.write("hello everybody")
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
