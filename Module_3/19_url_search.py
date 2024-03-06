url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)


number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
