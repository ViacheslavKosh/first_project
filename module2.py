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
