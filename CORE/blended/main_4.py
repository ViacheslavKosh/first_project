''' Привіт! Це я переплутав в яку сторону йде змішення і трохи потрібно поравити алгоритм)
    Тобто алфавіт йде в ліву сторону і виходить:
    Hello, world!
     a b c d e f g h i j k l m n o p q r s t u v w x y z
     k = 3
     d e f g h i j k l m n o p q r s t u v w x y z a b c
     Khoor, zruog! 
    Тобто спочатку потрібно з позицій компʼютера перетворити у позиції алфавіту:
    'a' це 97, тобто 0 елемент алфавіту:
    position = ord(symbol) - min_value_for_lower_case # 97 - 97 -> 0 | 98 - 97 -> 1
    А далі до цієї позицій додавати відступ і заокруглювати:
            new_position = (position + key) % 26
            new_symbol = chr(new_position + min_value_for_lower_case)
            
            cipher_text += new_symbol
    Виходить:
    min_value_for_lower_case = 97
    min_value_for_upper_case = 65
'''


min_value_for_lower_case = 97
min_value_for_upper_case = 65

def caesar(text: str, key):
    cipher_text = ""
    for symbol in text:
        if symbol.islower():
            position = ord(symbol) - min_value_for_lower_case # 97 - 97 -> 0 | 98 - 97 -> 1
            new_position = (position + key) % 26
            new_symbol = chr(new_position + min_value_for_lower_case)
            
            cipher_text += new_symbol
        elif symbol.isupper():
            position = ord(symbol) - min_value_for_upper_case
            new_position = (position + key) % 26
            new_symbol = chr(new_position + min_value_for_upper_case)
            
            cipher_text += new_symbol
        else:
            cipher_text += symbol
    return cipher_text

print(caesar("Hello, world!", 3))