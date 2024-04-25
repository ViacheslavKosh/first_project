# еретворення всіх символів рядка у нижній регістр за допомогою методу .lower(), або у верхній регістр за допомогою .upper()
string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

# casefold() призначений для видалення усіх відмінностей у регістрі
# Виведення буде 'python programming' таке саме як і для методу .lower().
text = "Python Programming"
print(text.casefold())

# наприклад, в німецькій мові
german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі
# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()
# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()
print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")
