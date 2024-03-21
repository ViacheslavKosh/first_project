
def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            print(cache)
            return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(8))  
print(fib(16))  






# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))


# # Проста функція
# def add(a, b):
#     return a + b


# # Каррінг постої функції
# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b
# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)
