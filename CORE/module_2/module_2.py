# num = int(input("Enter number for 0 to 20: "))
# if num >= 10:
#     print("Number over 10")
# else: print("Number under 10")

# x = int(input("Enter number: "))
# if x % 2 == 0:
#     print("This is even number")
# else:
#     print("This is odd number")

# y = int(input("Enter number: "))
# if y > 0:
#     print("This is a positive number")
# elif y < 0:
#     print("This ss a negative number")
# else:
#     print("This is 0")

# money = 0
# if money:
#     print(f"You have {money} in your bank account.")
# else:
#     print(print("You have no money in your bank account."))              

# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# user_name = input("Enter your name: ")
# if user_name:
#     print(f"Hello {user_name}!!!")
# else:
#     print("Hello ANONIMNUS!")

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# has_driver_licence = True

# if user_name and user_age >=18 and has_driver_licence:
#     print(f"User {user_name} can rent a car")
# else:
#     print("Acess denied!")

# num = int(input("Enter number: "))
# lenght = len(str(num))
# if lenght == 2 and num % 2 == 0:
#     print("Two-digit even number")
# else: 
#     print("NO")

# num = int(input("Enter number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can't be equal zerro!")
#     x = int(input("X: "))
# result = y/x
# print(result)

# is_nice = False
# state = "nice" if is_nice else "not nice"
# print(state)  

# some_data = 123
# msg = some_data or "Не було повернено даних"
# print(msg)

# MATCH

# fruit = "apple"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

# x = int(input("X: "))
# y = int(input("Y: "))

# point = (x, y)
# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")

# FOR

# fruit = 'apple'
# for char in fruit:
#     print(char)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

# some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)

# text = input("Input some text with 5 words: ")
# number_symbols = len(text)
# space_count = 0
# for char in text:
#     if char == " ":
#         space_count += 1

# print(f"Number of symbols in text: {number_symbols}")
# print(f"Number of spaces in texp: {space_count}")

# WHILE

# k = 0
# while k < 1000:
#     k = k + 1
#     print(k)
# while k > 0:
#     k = k - 1
#     print(k)

# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2: # все равно, что "if a % 2 == 0:" т.е. нет остатка от деления
#         continue
#     print(a)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum += num
#     num = num - 1
#     print(sum)


# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"{i} є парним числом.")
#     else:
#         print(f"{i} є непарним числом.")


# while True:
#     number = input("number = ")
#     if number == "exit":
#         break
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break

# for i in range(5):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)

# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for number, letter in zip(list1, list2):
#     print(number, letter)

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

# for key in numbers:
#     print(key)

# for val in numbers.values():
#     print(val)

# for key, value in numbers.items():
#     print(key, value)

# ВИЙНЯТКИ

# val = input("enter number: ")
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
# #     print(f"{age} is not a number")

# hindi_text = "हेलो वर्ल्ड"  # Припустимо, це ваш рядок у кодуванні Unicode

# # Конвертація рядка у кодування UTF-8
# utf_text = hindi_text.encode('utf-8')

# print(utf_text)  # Виводить байти у кодуванні UTF-8

# ФУНКЦІЇ

# def say_hello():
#     print("Hello!")
# say_hello()

# def print_max(a: int, b: int):
#     if a > b:
#         print ("a MAX")
#     elif a == b:
#         print ("they are identical")
#     else:
#         print ("b MAX")
# print_max(6, 45)
# x = 43
# y = 42
# print_max(x, y)

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum
# result = add_numbers(4, 4)
# print(result)

# def greet(name: str) -> str:
#     return f"Hi {name}!"
# greetings = greet ("Alex")
# print(greetings)

# def is_even(num: int) -> bool:
#     return num % 2 == 0
# a = int(input("Enter even number: "))
# check_even = is_even(a)
# is_even(check_even)
# print(check_even)


# def string_to_codes(string: str) -> dict:
#     codes = {}    
#     for ch in string:
#         if ch not in codes:
#             codes [ch] = ord (ch)
#     return codes
# surer_change = string_to_codes("avadakedabra")
# print(surer_change)

# ОБЛАСТІ ВИДИМОСТІ (LEGB)

# x = 50
# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2
# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# def outer_func():
#     enclosing_var = "Я змінна в функції, що охоплює"
#     def inner_func():
#         print("Всередині вкладеної функції:", enclosing_var)
#     inner_func()

# outer_func()
# def func_outer():
#     x = 2
#     def func_inner():
#         nonlocal x
#         x = 5
#     func_inner()
#     return x
# result = func_outer()  # 5

# x = 50
# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2
# func()
# print('Значення x складає', x)# Значення x складає 2

# КЛЮЧОВІ АРГУМЕНТИ ФУНКЦІЇ

# def greet (name, message = "Привіт "):
#     print (f"{message}, {name}")
# greet ("ALESHA")
# greet ("MARUSIA", message = "Vitayu")
# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)
# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)
# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)
# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)

# def say (message, times = 1):
#     print(message*times)
# say ("Rumba")
# say ("tumba ", 5)

# def real_cost(base: int, discount: int = 0) -> int:
#     return base * (1 - discount)
# price_bread = 15
# price_butter = 50
# price_sugar = 60
# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)
# print(f'Нова вартість хліба: {current_price_bread}')
# print(f'Нова вартість масла: {current_price_butter}')
# print(f'Нова вартість цукру: {current_price_sugar}')

# ЗМІННА КІЛЬКІСТЬ ПАРАМЕТРІВ

# def print_all_args(*args):
#     for arg in args:
#         print(arg)
# print_all_args(1, 'hello', True) 

# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result
# print(concatenate("Hello", " ", "world", "!"))

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# greet(name="Alice", age=25)

# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)
# example_function(1, 2, 3, name="Alice", age=25)

# Розпакування списків та словників

# my_list = [1, 2, 3]
# a, b, c = my_list
# print(my_list)
# a, *rest = my_list
# print(rest)

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")
# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)

# # РЕКУРСІЯ

# # факторіал

# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок
# print(factorial(20)) # виведе 120

# # фібаначі

# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок
# print(fibonacci(20)) # виведе 55

# Стек викликів рекурсії

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')


# def discount_price(price, discount):
  
#     def apply_discount():
       
#         nonlocal price    
#         price = price * (1-discount)
       
    
#     apply_discount()
    
#     return price
# a = discount_price (100, 0.1)  
# print(a)

# def get_fullname (first_name, last_name, middle_name = "") -> str:
#     if middle_name:
#         fullname = f"{first_name} {last_name} {middle_name}"
#     else:
#         fullname = f"{first_name} {last_name}"
#     return fullname
# a = get_fullname("Vasya", "Vasilkov", "Vasillevich")
# b = get_fullname("Vasya", "Vasilkov")
# print(a)
# print(b)

# def get_fullname (first_name, last_name, middle_name = ""):
#     fullname = f"{first_name} {last_name} {middle_name}"
#     return fullname
# a = get_fullname("Vasya", "Vasilkov", "Vasillevich")
# b = get_fullname("Vasya", "Vasilkov")
# print(a)
# print(b)

# def format_string(string, length):
#     if len(string) == length:
#         string = string
#     else:
#         len(string) < length
#         string = " " * ((length - len(string))//2)
#     return string

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
# def factorial(k):
#     if k < 2:
#         return 1
#     else:
#         return k * factorial(k - 1)
# def factorial(c):
#     if c < 2:
#         return 1
#     else:
#         return c * factorial(c - 1)
# def number_of_groups(n, k) -> int:
#     c = n - k
#     winner_list = factorial(n) // (factorial(c) * factorial(k))
#     print(winner_list)
#     return winner_list
# number_of_groups(50, 7)

s = "Hello" 
print(s.upper()) # Виведе 'HELLO'
