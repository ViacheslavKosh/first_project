# Основна відмінність від байт-рядків — це змінність
# bytearray сприймається як послідовність чисел
byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)

# перетворити в рядок за допомогою методу decode()
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'
