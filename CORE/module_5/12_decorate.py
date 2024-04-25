# Дії для логування (декорування)
def complicated(x: int, y: int) -> int:
    return x + y
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner
complicated = logger(complicated)
print(complicated(2, 3))


# спрощення для дій декорування
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner
@logger
def complicated(x: int, y: int) -> int:
    return x + y
print(complicated(2, 3))


# Збереження інформації про основну функцію за допомогою функції functools.wraps
from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)
