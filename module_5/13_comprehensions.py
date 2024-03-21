# Колекція квадратів
sq = []
for i in range(1, 6):
    sq.append(i**2)
print(sq)


# спрощення по методу list comprehensions [new_item for item in iterable if condition]
sq = [x**2 for x in range(1, 6)]
print(sq)
# з використанням умови
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)


# для множин {new_item for item in iterable if condition}
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)
# множина з умовою
odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)


# Для словників {key: value for item in iterable if condition}
sq = {x: x**2 for x in range(1, 10)}
print(sq)
# з використанням умови
sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)
