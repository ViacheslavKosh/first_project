# fh = open('test.txt')
# # операції над файлом
# fh.close()
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


# fh = open('test.txt', 'w')
# symbols_written = fh.write('hello!\n')
# print(symbols_written) # 6
# fh.write("WTF!")
# fh.close()

# метод read, який дозволяє прочитати деяку кількість символів із файлу

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)
# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'
# fh.close()

# Щоб прочитати увесь вміст файлу за раз, можна викликати метод read без аргументів

# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()
# fh = open('test.txt', 'r')
# all_file = fh.read()
# print(all_file)  # 'hello!'
# fh.close()

# у циклі ми зчитували та виводили у консоль вміст файлу по одному символу за раз

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# читати файл порядково, по одному рядку за раз, для цього можна скористатися методом readline

# fh.close()
# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()
# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)
# fh.close()

# # метод readlines, який читає увесь файл повністю, але повертає список рядків, де елемент списку — це один рядок з файлу

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()
# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)
# fh.close()

# # для видалення символу переносу рядка \n використали метод strip() і тепер виведення в нас чисте

# fh = open("test.txt", "w")
# fh.write("first line\nsecond line\nthird line")
# fh.close()
# fh = open("test.txt", "r")
# lines = [el.strip() for el in fh.readlines()]
# print(lines)
# fh.close()

# Є можливість управляти положенням курсора (вказівника) у файлі та довільно переміщатися файлом за допомогою методу seek

# fh = open("test.txt", "w+")
# fh.write('hello!')
# fh.seek(1)
# second = fh.read(1)
# print(second)
# fh.close()

# Щоб дізнатися положення курсора в цей момент, можна скористатися методом tell

fh = open("test.txt", "w+")
fh.write("hello everybody!")
position = fh.tell()
print(position) # 16
fh.seek(1)
position = fh.tell()
print(position) # 1
fh.read(2)
position = fh.tell()
print(position)  # 3
fh.close()
