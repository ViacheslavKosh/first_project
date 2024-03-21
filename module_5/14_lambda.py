# синтаксис lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8
# використовувати краще без змінної
print((lambda x, y: x + y)(5, 3))  # Виведе 8

# використання як аргумента у функції
nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)
